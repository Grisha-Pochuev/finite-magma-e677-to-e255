param(
    [string]$PythonPath = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$shadowChecker = Join-Path $repoRoot "tools\e677_idempotent_latin_order_scan.py"
$completionChecker = Join-Path $repoRoot "tools\e677_k5_block_tree_completion_sat.py"

function Resolve-Python {
    if ($PythonPath) {
        if (-not (Test-Path -LiteralPath $PythonPath -PathType Leaf)) {
            throw "Python executable not found: $PythonPath"
        }
        return (Resolve-Path -LiteralPath $PythonPath).Path
    }

    $bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    if (Test-Path -LiteralPath $bundled -PathType Leaf) {
        return $bundled
    }

    foreach ($name in @("python", "py")) {
        $command = Get-Command $name -ErrorAction SilentlyContinue
        if ($command) {
            return $command.Source
        }
    }
    throw "Python was not found. Pass -PythonPath with a Python 3 executable."
}

function Invoke-ExpectedCheck {
    param(
        [string]$Name,
        [string]$Checker,
        [string[]]$CheckArgs,
        [int]$ExpectedExitCode,
        [string[]]$ExpectedText
    )

    Write-Host "[$Name]"
    $output = & $script:PythonExe $Checker @CheckArgs 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $output.TrimEnd()
    if ($exitCode -ne $ExpectedExitCode) {
        throw "$Name returned exit code $exitCode; expected $ExpectedExitCode."
    }
    foreach ($marker in $ExpectedText) {
        if (-not $output.Contains($marker)) {
            throw "$Name did not print the expected marker: $marker"
        }
    }
}

$script:PythonExe = Resolve-Python
Write-Host "Python: $script:PythonExe"
Write-Host "Shadow checker SHA256: $((Get-FileHash -LiteralPath $shadowChecker -Algorithm SHA256).Hash)"
Write-Host "Completion checker SHA256: $((Get-FileHash -LiteralPath $completionChecker -Algorithm SHA256).Hash)"

try {
    Invoke-ExpectedCheck `
        -Name "shadow orders 2--8 / CaDiCaL" `
        -Checker $shadowChecker `
        -CheckArgs @(
            "--min-order", "2", "--max-order", "8",
            "--solver", "cadical195", "--per-cube-seconds", "10"
        ) `
        -ExpectedExitCode 0 `
        -ExpectedText @(
            "order=2: UNSAT", "order=5: SAT", "order=8: UNSAT",
            "order=5 VERIFIED MODEL"
        )

    Invoke-ExpectedCheck `
        -Name "unique order-five shadow / Glucose" `
        -Checker $shadowChecker `
        -CheckArgs @(
            "--min-order", "5", "--max-order", "5",
            "--solver", "glucose42", "--per-cube-seconds", "10",
            "--exclude-k5-orbit"
        ) `
        -ExpectedExitCode 0 `
        -ExpectedText @("excluded-K5-labelled-orbit=6", "order=5: UNSAT")

    $terminal = @(
        "--blocks", "1", "--extra", "4", "--terminal-k5", "--seconds", "30"
    )

    Invoke-ExpectedCheck `
        -Name "terminal order 9 / Glucose" `
        -Checker $completionChecker `
        -CheckArgs @($terminal + @("--solver", "glucose42")) `
        -ExpectedExitCode 2 `
        -ExpectedText @("order=9", "terminal-k5=True", "status: UNSAT")

    Invoke-ExpectedCheck `
        -Name "terminal order 9 / CaDiCaL" `
        -Checker $completionChecker `
        -CheckArgs @($terminal + @("--solver", "cadical195")) `
        -ExpectedExitCode 2 `
        -ExpectedText @("order=9", "terminal-k5=True", "status: UNSAT")
} catch {
    Write-Error $_
    Write-Host "If PySAT is missing, install the pinned package from tools/requirements-e677-sat.txt."
    exit 1
}

Write-Host "Order-9 terminal ZERO-shadow certificate checks passed."
exit 0

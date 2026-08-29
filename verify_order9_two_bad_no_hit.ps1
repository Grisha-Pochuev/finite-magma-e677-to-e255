param(
    [string]$PythonPath = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$checker = Join-Path $repoRoot "tools\e677_order9_no_hit_bad_count_sat.py"

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
        [string[]]$CheckArgs,
        [string]$ExpectedText
    )
    Write-Host "[$Name]"
    $output = & $script:PythonExe $checker @CheckArgs 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $output.TrimEnd()
    if ($exitCode -ne 2) {
        throw "$Name returned exit code $exitCode; expected 2."
    }
    if (-not $output.Contains($ExpectedText)) {
        throw "$Name did not print the expected marker: $ExpectedText"
    }
}

$script:PythonExe = Resolve-Python
$base = @(
    "--min-bad", "2", "--max-bad", "2", "--scan-bad2-structural"
)

Write-Host "Python: $script:PythonExe"
Write-Host "Checker SHA256: $((Get-FileHash -LiteralPath $checker -Algorithm SHA256).Hash)"

try {
    Invoke-ExpectedCheck `
        -Name "form I / CaDiCaL" `
        -CheckArgs @($base + @(
            "--bad2-case", "1", "--solver", "cadical195",
            "--conflict-budget", "50000"
        )) `
        -ExpectedText "bad2 summary: unsat=1/1"

    foreach ($solverSpec in @(
        @("cadical195", "--conflict-budget", "250000"),
        @("glucose42", "--per-count-seconds", "30")
    )) {
        Invoke-ExpectedCheck `
            -Name "form II / $($solverSpec[0])" `
            -CheckArgs @($base + @("--bad2-case", "2", "--solver") + $solverSpec) `
            -ExpectedText "bad2 summary: unsat=1/1"
    }

    foreach ($solver in @("cadical195", "glucose42")) {
        $limit = if ($solver -eq "cadical195") {
            @("--conflict-budget", "50000")
        } else {
            @("--per-count-seconds", "15")
        }
        Invoke-ExpectedCheck `
            -Name "form III renewal cores / $solver" `
            -CheckArgs @(
                $base + @(
                    "--bad2-case", "3", "--case3-term-cores", "--solver", $solver
                ) + $limit
            ) `
            -ExpectedText "bad2 summary: unsat=5/5"

        Invoke-ExpectedCheck `
            -Name "form IV product cores / $solver" `
            -CheckArgs @(
                $base + @(
                    "--bad2-case", "4", "--case4-product-cores", "--solver", $solver
                ) + $limit
            ) `
            -ExpectedText "bad2 summary: unsat=20/20"
    }
} catch {
    Write-Error $_
    Write-Host "If PySAT is missing, install the pinned package from tools/requirements-e677-sat.txt."
    exit 1
}

Write-Host "Order-9 two-Bad no-HIT certificate checks passed."
exit 0

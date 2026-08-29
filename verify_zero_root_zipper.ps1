param(
    [string]$PythonPath = "",
    [switch]$IncludeOrder10
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$checker = Join-Path $repoRoot "tools\e677_k5_block_tree_completion_sat.py"

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
        [int]$ExpectedExitCode,
        [string]$ExpectedText
    )

    Write-Host "[$Name]"
    $output = & $script:PythonExe $checker @CheckArgs 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $output.TrimEnd()
    if ($exitCode -ne $ExpectedExitCode) {
        throw "$Name returned exit code $exitCode; expected $ExpectedExitCode."
    }
    if (-not $output.Contains($ExpectedText)) {
        throw "$Name did not print the expected marker: $ExpectedText"
    }
}

$script:PythonExe = Resolve-Python
Write-Host "Python: $script:PythonExe"
Write-Host "Checker SHA256: $((Get-FileHash -LiteralPath $checker -Algorithm SHA256).Hash)"

$zipper = @(
    "--blocks", "1",
    "--extra", "10",
    "--terminal-k5",
    "--equivariant-three-layer-zipper",
    "--seconds", "30"
)

try {
    Invoke-ExpectedCheck `
        -Name "base shell / Glucose" `
        -CheckArgs @($zipper + @("--skip-e677", "--solver", "glucose42")) `
        -ExpectedExitCode 0 `
        -ExpectedText "status: BASE SHELL SAT VERIFIED"

    Invoke-ExpectedCheck `
        -Name "full E677 / Glucose" `
        -CheckArgs @($zipper + @("--solver", "glucose42")) `
        -ExpectedExitCode 2 `
        -ExpectedText "status: UNSAT"

    Invoke-ExpectedCheck `
        -Name "full E677 / CaDiCaL" `
        -CheckArgs @($zipper + @("--solver", "cadical195")) `
        -ExpectedExitCode 2 `
        -ExpectedText "status: UNSAT"

    if ($IncludeOrder10) {
        Invoke-ExpectedCheck `
            -Name "terminal K5 order 10 / CaDiCaL" `
            -CheckArgs @(
                "--blocks", "1",
                "--extra", "5",
                "--terminal-k5",
                "--solver", "cadical195",
                "--seconds", "300"
            ) `
            -ExpectedExitCode 2 `
            -ExpectedText "status: UNSAT"
    }
} catch {
    Write-Error $_
    Write-Host "If PySAT is missing, install the 'python-sat' package for this Python."
    exit 1
}

Write-Host "ZERO-root ZIPPER certificate checks passed."
exit 0

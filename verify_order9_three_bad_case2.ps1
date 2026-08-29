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
        [string[]]$CheckArgs
    )
    Write-Host "[$Name]"
    $output = & $script:PythonExe $checker @CheckArgs 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $output.TrimEnd()
    if ($exitCode -ne 2) {
        throw "$Name returned exit code $exitCode; expected 2."
    }
    $marker = "bad3 summary: unsat=8/8; unknown=[]"
    if (-not $output.Contains($marker)) {
        throw "$Name did not print the expected marker: $marker"
    }
}

$script:PythonExe = Resolve-Python
$base = @(
    "--min-bad", "3", "--max-bad", "3",
    "--scan-bad3-structural", "--bad3-frontier-only",
    "--bad3-case2-reduction"
)

Write-Host "Python: $script:PythonExe"
Write-Host "Checker SHA256: $((Get-FileHash -LiteralPath $checker -Algorithm SHA256).Hash)"

Invoke-ExpectedCheck `
    -Name "case 2 reduction / CaDiCaL195" `
    -CheckArgs @($base + @(
        "--solver", "cadical195", "--conflict-budget", "50000"
    ))

Invoke-ExpectedCheck `
    -Name "case 2 reduction / Glucose42" `
    -CheckArgs @($base + @(
        "--solver", "glucose42", "--per-count-seconds", "30"
    ))

Write-Host "PASS: order-9 three-Bad case-2 reduction is 8/8 UNSAT in both engines."

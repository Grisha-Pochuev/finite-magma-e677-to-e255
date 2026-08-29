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
        [string]$Marker
    )
    Write-Host "[$Name]"
    $output = & $script:PythonExe $checker @CheckArgs 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $output.TrimEnd()
    if ($exitCode -ne 2) {
        throw "$Name returned exit code $exitCode; expected 2."
    }
    if (-not $output.Contains($Marker)) {
        throw "$Name did not print the expected marker: $Marker"
    }
}

$script:PythonExe = Resolve-Python
$base = @(
    "--min-bad", "3", "--max-bad", "3",
    "--scan-bad3-structural", "--bad3-frontier-only",
    "--bad3-case", "3"
)

Write-Host "Python: $script:PythonExe"
Write-Host "Base checker SHA256: $((Get-FileHash -LiteralPath $checker -Algorithm SHA256).Hash)"

Invoke-ExpectedCheck `
    -Name "case 3 canonical root outcomes / CaDiCaL195" `
    -CheckArgs @($base + @(
        "--bad3-canonical-root-outcomes",
        "--solver", "cadical195",
        "--conflict-budget", "500000"
    )) `
    -Marker "bad3 summary: unsat=6/6; unknown=[]"

Invoke-ExpectedCheck `
    -Name "case 3 canonical root outcomes / Glucose42" `
    -CheckArgs @($base + @(
        "--bad3-canonical-root-outcomes",
        "--solver", "glucose42",
        "--per-count-seconds", "60"
    )) `
    -Marker "bad3 summary: unsat=6/6; unknown=[]"

Invoke-ExpectedCheck `
    -Name "case 3 Good-product representatives / CaDiCaL195" `
    -CheckArgs @($base + @(
        "--bad3-good-product-reps-only",
        "--solver", "cadical195",
        "--conflict-budget", "200000"
    )) `
    -Marker "bad3 summary: unsat=4/4; unknown=[]"

Invoke-ExpectedCheck `
    -Name "case 3 Good-product representatives / Glucose42" `
    -CheckArgs @($base + @(
        "--bad3-good-product-reps-only",
        "--solver", "glucose42",
        "--per-count-seconds", "60"
    )) `
    -Marker "bad3 summary: unsat=4/4; unknown=[]"

Write-Host "PASS: order-9 three-Bad top form 3 is fully excluded in both engines."

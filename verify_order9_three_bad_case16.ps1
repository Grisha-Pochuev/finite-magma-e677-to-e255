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

function Invoke-ExactCheck {
    param(
        [string]$Name,
        [string[]]$CheckArgs,
        [int[]]$ExpectedExitCodes,
        [string[]]$AcceptedMarkers
    )
    Write-Host "[$Name]"
    $output = & $script:PythonExe $checker @CheckArgs 2>&1 | Out-String
    $exitCode = $LASTEXITCODE
    Write-Host $output.TrimEnd()

    if ($ExpectedExitCodes -notcontains $exitCode) {
        throw "$Name returned exit code $exitCode; expected one of $($ExpectedExitCodes -join ', ')."
    }

    $matched = $false
    foreach ($marker in $AcceptedMarkers) {
        if ($output.Contains($marker)) {
            $matched = $true
            break
        }
    }
    if (-not $matched) {
        throw "$Name did not print any accepted marker: $($AcceptedMarkers -join ' OR ')"
    }
}

$script:PythonExe = Resolve-Python
$base = @(
    "--min-bad", "3", "--max-bad", "3",
    "--scan-bad3-structural", "--bad3-frontier-only",
    "--bad3-case", "16"
)

Write-Host "Python: $script:PythonExe"
Write-Host "Base checker SHA256: $((Get-FileHash -LiteralPath $checker -Algorithm SHA256).Hash)"

Invoke-ExactCheck `
    -Name "case 16 canonical root outcomes / CaDiCaL195" `
    -CheckArgs @($base + @(
        "--bad3-canonical-root-outcomes",
        "--solver", "cadical195",
        "--conflict-budget", "500000"
    )) `
    -ExpectedExitCodes @(2, 3) `
    -AcceptedMarkers @(
        "bad3 summary: unsat=6/6; unknown=[]",
        "bad3 summary: unsat=5/6; unknown=['C:square-Good,D0=2; D-3cycle; f1=2,f2=2; root=(0,2),product=Good']"
    )

Invoke-ExactCheck `
    -Name "case 16 canonical root outcomes / Glucose42" `
    -CheckArgs @($base + @(
        "--bad3-canonical-root-outcomes",
        "--solver", "glucose42",
        "--per-count-seconds", "60"
    )) `
    -ExpectedExitCodes @(2) `
    -AcceptedMarkers @("bad3 summary: unsat=6/6; unknown=[]")

Invoke-ExactCheck `
    -Name "case 16 Good-product representatives / CaDiCaL195" `
    -CheckArgs @($base + @(
        "--bad3-good-product-reps-only",
        "--solver", "cadical195",
        "--conflict-budget", "500000"
    )) `
    -ExpectedExitCodes @(2) `
    -AcceptedMarkers @("bad3 summary: unsat=2/2; unknown=[]")

Invoke-ExactCheck `
    -Name "case 16 Good-product representatives / Glucose42" `
    -CheckArgs @($base + @(
        "--bad3-good-product-reps-only",
        "--solver", "glucose42",
        "--per-count-seconds", "60"
    )) `
    -ExpectedExitCodes @(2) `
    -AcceptedMarkers @("bad3 summary: unsat=2/2; unknown=[]")

Write-Host "PASS: order-9 three-Bad top form 16 is fully excluded; any bounded aggregate Good UNKNOWN is discharged by the exact Good-product representatives."

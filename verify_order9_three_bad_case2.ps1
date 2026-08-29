param(
    [string]$PythonPath = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$checker = Join-Path $repoRoot "tools\e677_order9_no_hit_bad_count_sat.py"
$pausedChecker = Join-Path $repoRoot "Experiments\2026-08-29-order9-case2-paused\run_case2_paused.py"

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
        [string]$ScriptPath,
        [string[]]$CheckArgs,
        [string]$Marker
    )
    Write-Host "[$Name]"
    $output = & $script:PythonExe $ScriptPath @CheckArgs 2>&1 | Out-String
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
    "--bad3-case2-reduction"
)

Write-Host "Python: $script:PythonExe"
Write-Host "Base checker SHA256: $((Get-FileHash -LiteralPath $checker -Algorithm SHA256).Hash)"
Write-Host "Paused wrapper SHA256: $((Get-FileHash -LiteralPath $pausedChecker -Algorithm SHA256).Hash)"

Invoke-ExpectedCheck `
    -Name "case 2 root reduction / CaDiCaL195" `
    -ScriptPath $checker `
    -CheckArgs @($base + @(
        "--solver", "cadical195", "--conflict-budget", "50000"
    )) `
    -Marker "bad3 summary: unsat=8/8; unknown=[]"

Invoke-ExpectedCheck `
    -Name "case 2 root reduction / Glucose42" `
    -ScriptPath $checker `
    -CheckArgs @($base + @(
        "--solver", "glucose42", "--per-count-seconds", "30"
    )) `
    -Marker "bad3 summary: unsat=8/8; unknown=[]"

Invoke-ExpectedCheck `
    -Name "case 2 paused continuation / CaDiCaL195" `
    -ScriptPath $pausedChecker `
    -CheckArgs @(
        "--solver", "cadical195", "--conflict-budget", "100000"
    ) `
    -Marker "bad3 summary: unsat=6/6; unknown=[]"

Invoke-ExpectedCheck `
    -Name "case 2 paused continuation / Glucose42" `
    -ScriptPath $pausedChecker `
    -CheckArgs @(
        "--solver", "glucose42", "--per-leaf-seconds", "30"
    ) `
    -Marker "bad3 summary: unsat=6/6; unknown=[]"

Write-Host "PASS: order-9 three-Bad top form 2 is fully excluded in both engines."

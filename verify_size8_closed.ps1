$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$logDir = Join-Path $root "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$log = Join-Path $logDir "size8_rerun_$stamp.txt"
"E677 -> E255 size 8 verification with structural splits, started $(Get-Date)" | Set-Content -Path $log -Encoding UTF8

function Run-Case {
  param(
    [int]$CaseNumber,
    [int]$Index,
    [string]$Extra = "",
    [int]$Seconds = 90
  )

  $label = if ($Extra) { "case $CaseNumber, extra $Extra" } else { "case $CaseNumber" }
  Write-Host ""
  Write-Host "Checking $label"
  Add-Content -Path $log -Value ""
  Add-Content -Path $log -Value "=== $label ==="

  $args = @(".\tools\search_counterexample_strong.js", "8", "$Seconds", "$Index", "counterexample")
  if ($Extra) { $args += $Extra }
  $out = & node @args
  $out | Add-Content -Path $log

  $status = ($out | Select-String '^status:').Line
  Write-Host $status
  if ($status -ne "status: none") {
    Write-Host "Stopped: this subcase did not close cleanly. Inspect the rerun log:"
    Write-Host $log
    exit 1
  }
}

Write-Host "E677 -> E255: verifying no size-8 counterexample."
Write-Host "This uses the improved structural split by k*0 for cases 24-30."

foreach ($i in 0..22) {
  Run-Case -CaseNumber ($i + 1) -Index $i -Seconds 90
}

$splitCases = @(
  @{ Case = 24; Index = 23; Row = 4; Values = @(1, 2, 4, 5, 6, 7) },
  @{ Case = 25; Index = 24; Row = 4; Values = @(1, 2, 4, 5, 6, 7) },
  @{ Case = 26; Index = 25; Row = 4; Values = @(1, 2, 4, 5, 6, 7) },
  @{ Case = 27; Index = 26; Row = 5; Values = @(1, 2, 3, 5, 6, 7) },
  @{ Case = 28; Index = 27; Row = 5; Values = @(1, 2, 3, 5, 6, 7) },
  @{ Case = 29; Index = 28; Row = 6; Values = @(1, 2, 3, 4, 6, 7) },
  @{ Case = 30; Index = 29; Row = 7; Values = @(1, 2, 3, 4, 5, 7) }
)

foreach ($split in $splitCases) {
  foreach ($value in $split.Values) {
    Run-Case `
      -CaseNumber $split.Case `
      -Index $split.Index `
      -Extra "$($split.Row):0:$value" `
      -Seconds 90
  }
}

Write-Host ""
Write-Host "Done: all size-8 cases closed. Log: $log"
Add-Content -Path $log -Value ""
Add-Content -Path $log -Value "Done: all size-8 cases closed, finished $(Get-Date)"

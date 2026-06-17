$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

function Find-NodeExe {
  if ($env:NODE_EXE) {
    if (Test-Path -LiteralPath $env:NODE_EXE) {
      return $env:NODE_EXE
    }
    throw "NODE_EXE is set, but the file does not exist: $env:NODE_EXE"
  }

  $cmd = Get-Command node -ErrorAction SilentlyContinue
  if ($cmd) {
    return $cmd.Source
  }

  throw "Node.js was not found. Install Node.js or set NODE_EXE to node.exe."
}

$nodeExe = Find-NodeExe
$nodeVersion = & $nodeExe --version

$logDir = Join-Path $root "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$log = Join-Path $logDir "sizes_5_6_7_rerun_$stamp.txt"

"E677 -> E255 sizes 5, 6, 7 verification, started $(Get-Date)" | Set-Content -Path $log -Encoding UTF8
"Node.js: $nodeVersion" | Add-Content -Path $log

function Run-Case {
  param(
    [int]$Size,
    [int]$Index,
    [int]$Seconds
  )

  $caseNumber = $Index + 1
  $label = "size $Size, row-0 case $caseNumber"
  Write-Host ""
  Write-Host "Checking $label"
  Add-Content -Path $log -Value ""
  Add-Content -Path $log -Value "=== $label ==="

  $args = @(".\tools\search_counterexample_strong.js", "$Size", "$Seconds", "$Index", "counterexample")
  $out = & $nodeExe @args
  $out | Add-Content -Path $log

  $status = ($out | Select-String '^status:').Line
  Write-Host $status
  if ($status -ne "status: none") {
    Write-Host "Stopped: this case did not close cleanly. Inspect the rerun log:"
    Write-Host $log
    exit 1
  }

  $countLine = $out | Where-Object { $_ -match '^row-0 case\s+\d+/(\d+):' } | Select-Object -First 1
  if ($countLine -and ($countLine -match '^row-0 case\s+\d+/(\d+):')) {
    return [int]$Matches[1]
  }

  return $null
}

Write-Host "E677 -> E255: verifying no counterexample in sizes 5, 6, and 7."
Write-Host "Node.js: $nodeVersion"

$jobs = @(
  @{ Size = 5; Seconds = 30 },
  @{ Size = 6; Seconds = 30 },
  @{ Size = 7; Seconds = 60 }
)

$totalCases = 0

foreach ($job in $jobs) {
  $size = [int]$job.Size
  $seconds = [int]$job.Seconds

  $count = Run-Case -Size $size -Index 0 -Seconds $seconds
  if (-not $count) {
    throw "Could not read row-0 representative count for size $size."
  }

  for ($i = 1; $i -lt $count; $i++) {
    Run-Case -Size $size -Index $i -Seconds $seconds | Out-Null
  }

  $totalCases += $count
  Add-Content -Path $log -Value ""
  Add-Content -Path $log -Value "Size $size done: $count row-0 cases closed."
}

Write-Host ""
Write-Host "Done: all sizes 5, 6, and 7 closed. Total row-0 cases: $totalCases. Log: $log"
Add-Content -Path $log -Value ""
Add-Content -Path $log -Value "Done: all sizes 5, 6, and 7 closed."
Add-Content -Path $log -Value "Total row-0 cases: $totalCases."
Add-Content -Path $log -Value "Finished $(Get-Date)"

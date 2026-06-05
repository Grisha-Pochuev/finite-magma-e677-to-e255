$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

Write-Host "E677 -> E255 reproducibility smoke test"
Write-Host "This is a short environment check, not the full size-8 verification."
Write-Host ""

Write-Host "Checking Node.js..."
$nodeVersion = & node --version
Write-Host "Node.js: $nodeVersion"
Write-Host ""

function Run-Smoke {
  param(
    [string]$Label,
    [string[]]$Args
  )

  Write-Host "Running $Label"
  $out = & node @Args
  $out | ForEach-Object { Write-Host $_ }
  $status = ($out | Select-String '^status:').Line
  if ($status -ne "status: none") {
    throw "Smoke test failed for ${Label}: expected 'status: none', got '$status'"
  }
  Write-Host ""
}

Run-Smoke `
  -Label "size-5 one-case check" `
  -Args @(".\tools\search_counterexample_strong.js", "5", "10", "0", "counterexample")

Run-Smoke `
  -Label "size-8 base case 1 check" `
  -Args @(".\tools\search_counterexample_strong.js", "8", "10", "0", "counterexample")

Run-Smoke `
  -Label "size-8 split case check" `
  -Args @(".\tools\search_counterexample_strong.js", "8", "20", "23", "counterexample", "4:0:1")

Write-Host "Smoke test passed."


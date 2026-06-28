param(
  [string]$Major = "22"
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$tools = Join-Path $root "tools"
$installDir = Join-Path $tools "node-portable"
$tmp = Join-Path $tools "_node_download"

if (Test-Path -LiteralPath (Join-Path $installDir "node.exe")) {
  Write-Host "Portable Node.js already installed:"
  & (Join-Path $installDir "node.exe") --version
  exit 0
}

New-Item -ItemType Directory -Force -Path $tools | Out-Null
if (Test-Path -LiteralPath $tmp) {
  Remove-Item -LiteralPath $tmp -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

$base = "https://nodejs.org/dist/latest-v$Major.x"
$shaUrl = "$base/SHASUMS256.txt"
$shaFile = Join-Path $tmp "SHASUMS256.txt"

Write-Host "Downloading Node.js metadata from $shaUrl"
& curl.exe -L --fail --retry 3 --output $shaFile $shaUrl

$line = Get-Content -LiteralPath $shaFile | Where-Object { $_ -match " node-v.*-win-x64\.zip$" } | Select-Object -First 1
if (-not $line) {
  throw "Cannot find win-x64 zip in SHASUMS256.txt"
}

$parts = $line -split "\s+"
$expectedHash = $parts[0].ToUpperInvariant()
$zipName = $parts[1]
$zipUrl = "$base/$zipName"
$zipFile = Join-Path $tmp $zipName

Write-Host "Downloading $zipName"
if (Test-Path -LiteralPath $zipFile) {
  Remove-Item -LiteralPath $zipFile -Force
}
& curl.exe -L --fail --retry 3 --output $zipFile $zipUrl

$actualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $zipFile).Hash.ToUpperInvariant()
if ($actualHash -ne $expectedHash) {
  throw "SHA256 mismatch for $zipName"
}

Write-Host "Extracting portable Node.js"
Expand-Archive -LiteralPath $zipFile -DestinationPath $tmp -Force
$extracted = Get-ChildItem -LiteralPath $tmp -Directory | Where-Object { $_.Name -like "node-v*-win-x64" } | Select-Object -First 1
if (-not $extracted) {
  throw "Cannot find extracted Node.js directory"
}

if (Test-Path -LiteralPath $installDir) {
  Remove-Item -LiteralPath $installDir -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $installDir | Out-Null
Copy-Item -Path (Join-Path $extracted.FullName "*") -Destination $installDir -Recurse -Force

Remove-Item -LiteralPath $tmp -Recurse -Force

Write-Host "Portable Node.js installed:"
& (Join-Path $installDir "node.exe") --version

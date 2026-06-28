param(
  [string]$NodePath = ""
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$script = Join-Path $root "tools\directed_two_edge_witness_diagnostics.js"

if (-not (Test-Path -LiteralPath $script)) {
  throw "Не найден скрипт диагностики: $script"
}

if ($NodePath -and (Test-Path -LiteralPath $NodePath)) {
  $node = $NodePath
} else {
  $portable = Join-Path $root "tools\node-portable\node.exe"
  if (Test-Path -LiteralPath $portable) {
    $node = $portable
  } else {
    $cmd = Get-Command node.exe -ErrorAction SilentlyContinue
    if ($cmd -and $cmd.Source -and ($cmd.Source -notmatch "WindowsApps")) {
      $node = $cmd.Source
    } else {
      Write-Host "Node.js не найден вне WindowsApps."
      Write-Host "Сначала запустите: .\install_portable_node.ps1"
      exit 2
    }
  }
}

Write-Host "Node: $node"
& $node $script
exit $LASTEXITCODE

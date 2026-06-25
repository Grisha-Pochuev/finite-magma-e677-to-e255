$ErrorActionPreference = "Stop"

$template = Join-Path $PSScriptRoot "anchored_x3_m7_self_repeat.p"
$provers = @("eprover", "vampire", "twee", "iprover", "prover9")

Write-Host "ATP environment check"
Write-Host "Template: $template"

if (-not (Test-Path -LiteralPath $template)) {
    Write-Host "Template file is missing."
    exit 1
}

$found = @()
foreach ($name in $provers) {
    $cmd = Get-Command $name -ErrorAction SilentlyContinue
    if ($null -ne $cmd) {
        $found += [pscustomobject]@{
            Name = $name
            Path = $cmd.Source
        }
    }
}

if ($found.Count -eq 0) {
    Write-Host "No ATP prover found in PATH."
    Write-Host "This is not a proof failure; install or expose one prover before running the template."
    exit 0
}

Write-Host "Found ATP prover(s):"
$found | Format-Table -AutoSize

Write-Host ""
Write-Host "Next step: edit only the conjecture block in anchored_x3_m7_self_repeat.p,"
Write-Host "then run the chosen prover on that file."

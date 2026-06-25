$ErrorActionPreference = "Stop"

# Diagnostic for the shared-step anchored triangle in the known M496 model.
# This is only a model diagnostic, not a proof.

$Prime = 31
$F = 16
$N = $Prime * $F

function ModP([int]$a, [int]$p) {
    $r = $a % $p
    if ($r -lt 0) { return $r + $p }
    return $r
}

function GfMul([int]$a, [int]$b) {
    $out = 0
    $aa = $a
    $bb = $b
    while ($bb -ne 0) {
        if (($bb -band 1) -ne 0) { $out = $out -bxor $aa }
        $bb = $bb -shr 1
        $aa = $aa -shl 1
        if (($aa -band 0x10) -ne 0) { $aa = $aa -bxor 0x13 }
    }
    return ($out -band 0x0f)
}

function GfPow([int]$a, [int]$e) {
    $out = 1
    $base = $a
    while ($e -ne 0) {
        if (($e -band 1) -ne 0) { $out = GfMul $out $base }
        $base = GfMul $base $base
        $e = $e -shr 1
    }
    return $out
}

$zeta = GfPow 2 3
$omega = GfPow 2 5
$residues = New-Object 'bool[]' $Prime
for ($x = 1; $x -lt $Prime; $x++) {
    $residues[(ModP ($x * $x) $Prime)] = $true
}

function Op([int]$a, [int]$b) {
    $x = [math]::Floor($a / $F)
    $s = $a -band 15
    $y = [math]::Floor($b / $F)
    $t = $b -band 15
    $z = ModP ($x - 2 * ($y - $x)) $script:Prime
    $d = ModP ($y - $x) $script:Prime
    if ($d -eq 0) {
        $u = $s -bxor (GfMul $script:zeta ($t -bxor $s))
    } elseif ($script:residues[$d]) {
        $u = $t
    } else {
        $u = $s -bxor (GfMul $script:omega ($t -bxor $s))
    }
    return ($z * $F + $u)
}

$table = New-Object 'int[][]' $N
$inverse = New-Object 'int[][]' $N
for ($row = 0; $row -lt $N; $row++) {
    $tableRow = New-Object 'int[]' $N
    $inv = New-Object 'int[]' $N
    for ($col = 0; $col -lt $N; $col++) {
        $value = Op $row $col
        $tableRow[$col] = $value
        $inv[$value] = $col
    }
    $table[$row] = $tableRow
    $inverse[$row] = $inv
}

$groups = @{}
for ($p = 0; $p -lt $N; $p++) {
    for ($b = 0; $b -lt $N; $b++) {
        $z = $table[$p][$b]
        $key = $b * $N + $z
        if (-not $groups.ContainsKey($key)) {
            $groups[$key] = [System.Collections.Generic.List[int]]::new()
        }
        $groups[$key].Add($p)
    }
}

$pairs = 0
$hMismatch = 0
$zhMismatch = 0
$uWHMismatch = 0
$triangleMismatch = 0
$sameOutput = 0
$valueRelations = [ordered]@{
    T_eq_b = 0
    T_eq_z = 0
    T_eq_h = 0
    T_eq_U = 0
    T_eq_W = 0
    T_eq_p = 0
    T_eq_q = 0
    other = 0
}
$examples = @()

foreach ($entry in $groups.GetEnumerator()) {
    $rows = $entry.Value
    if ($rows.Count -lt 2) { continue }
    $b = [int][math]::Floor($entry.Key / $N)
    $z = [int]($entry.Key % $N)

    for ($i = 0; $i -lt $rows.Count; $i++) {
        for ($j = $i + 1; $j -lt $rows.Count; $j++) {
            $p = $rows[$i]
            $q = $rows[$j]
            $U = $table[$p][$z]
            $W = $table[$q][$z]
            $h1 = $table[$U][$p]
            $h2 = $table[$W][$q]
            $pairs++

            if ($h1 -ne $h2) {
                $hMismatch++
                if ($examples.Count -lt 5) {
                    $examples += @{ kind = "hMismatch"; b = $b; z = $z; p = $p; q = $q; U = $U; W = $W; h1 = $h1; h2 = $h2 }
                }
                continue
            }

            $h = $h1
            if ($table[$z][$h] -ne $b) { $zhMismatch++ }
            $alpha = $inverse[$z][$h]

            $T1 = $table[$U][$h]
            $T2 = $table[$W][$h]
            if ($T1 -ne $T2) {
                $uWHMismatch++
                if ($examples.Count -lt 5) {
                    $examples += @{ kind = "uWHMismatch"; b = $b; z = $z; p = $p; q = $q; U = $U; W = $W; h = $h; T1 = $T1; T2 = $T2 }
                }
            } else {
                $sameOutput++
            }

            if ($table[$U][$p] -ne $h -or $table[$W][$q] -ne $h -or $table[$z][$alpha] -ne $h -or $table[$z][$h] -ne $b) {
                $triangleMismatch++
            }

            if ($T1 -eq $b) { $valueRelations.T_eq_b++ }
            elseif ($T1 -eq $z) { $valueRelations.T_eq_z++ }
            elseif ($T1 -eq $h) { $valueRelations.T_eq_h++ }
            elseif ($T1 -eq $U) { $valueRelations.T_eq_U++ }
            elseif ($T1 -eq $W) { $valueRelations.T_eq_W++ }
            elseif ($T1 -eq $p) { $valueRelations.T_eq_p++ }
            elseif ($T1 -eq $q) { $valueRelations.T_eq_q++ }
            else { $valueRelations.other++ }
        }
    }
}

[pscustomobject]@{
    N = $N
    zeta = $zeta
    omega = $omega
    sharedStepPairs = $pairs
    hMismatch = $hMismatch
    zhMismatch = $zhMismatch
    uWHMismatch = $uWHMismatch
    triangleMismatch = $triangleMismatch
    sameOutput = $sameOutput
    valueRelations = $valueRelations
    examples = $examples
} | ConvertTo-Json -Depth 6

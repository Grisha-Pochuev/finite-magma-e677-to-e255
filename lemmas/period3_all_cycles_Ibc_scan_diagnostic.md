# Period-3 All-Cycles `Ib*c` Scan Diagnostic

Date: 2026-06-28.

Status:

```text
diagnostic / `Ib*c=z` is G12-specific evidence, not a general period-3 law
```

## Purpose

The current G12 period-3 branch strongly suggests:

```text
Ib*c=z.
```

This scan checks whether the same identity holds for all right-`h` period-3
cycles in the cached public `eq677` database, not only for the strict
shared-step/G12 representatives used by:

```text
period3_db_identity_scan.js
period3_core_hook_scan.js
```

## Script

```text
tools/period3_all_cycles_identity_scan.js
```

It scans every cached model and every triple:

```text
z*h=b,
b*h=c,
c*h=z,
z,b,c distinct.
```

For each cycle it defines:

```text
Ib=pred_b(h),
Ic=pred_c(h),
BC=b*c,
A=Ib*c,
K=A*Ib=(Ib*c)*Ib,
L=c*K.
```

It then records whether:

```text
A=z,
K=Ic,
L=h,
K=c,
L=c*c,
```

and other named hits occur.

## Result

Run:

```text
tools\node-portable\node.exe tools\period3_all_cycles_identity_scan.js
```

Summary:

```text
totalPeriod3Cycles:        343512
strictPeriod3Cycles:       201500
cleanAdvancePeriod3Cycles: 201500
```

For all strict/clean-advance period-3 cycles, the dominant profile is:

```text
A=Ib*c=z: 179254
```

But it is not universal.  The scan found strict clean-advance cycles without
`A=z`, including:

```text
fresh:                  1500
K=(Ib*c)*Ib=c; L=c*c:   1248
K=(Ib*c)*Ib=A; L=Ib:     312
```

The stored misses begin in model:

```text
49/18
```

and the first twenty strict misses all have:

```text
K=(Ib*c)*Ib=c,
L=c*c.
```

## Interpretation

Therefore:

```text
Ib*c=z
```

should not be promoted to a general period-3 E677 lemma.

It remains highly relevant for the current strict shared-step/G12 residual,
where the previous scan found it in all:

```text
6240
```

cached representatives.  But the all-cycles scan shows why an attempted proof
must use the extra G12/shared-step/minimality assumptions, not only the bare
period-3 zipper.

## New Structural Warning

The fresh all-cycle branch is not arbitrary.  A common fresh profile is:

```text
A=Ib*c fresh,
K=A*Ib=c,
L=c*c.
```

Equivalently, in `H_c` the row-`Ib` lifted edge becomes:

```text
c*c -> A.
```

This suggests a fallback split for any future attempt to prove `Ib*c=z`:

```text
either A hits watched data,
or A*Ib=c and the row-Ib edge is anchored at c*c,
or the fully clean V3/fixed-target orbit branch remains.
```

Do not use this diagnostic as a proof.  It is only model evidence and a
warning against overgeneralizing the db-supported G12 identity.

## Shared-Step Filter Check

The size-49 family contains the first recorded strict fresh all-cycle misses,
for example:

```text
49/18
```

A focused shared-step scan on size 49 gives:

```text
period3AdvancePairs: 0
firstOrbitCleanSelfRepeat: 0
firstOrbitRouted: 2520
```

For `49/18` specifically:

```text
anchoredX3CleanTriple: 630
firstOrbitCleanSelfRepeat: 0
firstOrbitRouted: 630
```

The first events route at depths 1 or 2.  Therefore the fresh all-cycle
period-3 profiles in size 49 are not examples of the current M7/G12
period-3 residual.  They are eliminated before the clean period-3 self-repeat
stage.

This strengthens the current interpretation:

```text
bare period-3 does not imply Ib*c=z,
but the shared-step/M7 clean-self-repeat filter may force it.
```

The next proof attempt should therefore use the first-event minimality
conditions from:

```text
anchored_m7_first_event_routing_lemma.md
period3_named_fan_v3_dichotomy_lemma.md
```

not only the three equations:

```text
z*h=b,
b*h=c,
c*h=z.
```

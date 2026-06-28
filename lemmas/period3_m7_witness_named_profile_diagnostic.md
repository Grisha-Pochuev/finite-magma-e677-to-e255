# Period-3 M7 Witness Named Profile Diagnostic

Date: 2026-06-28.

Status:

```text
diagnostic / M7 witness filter forces the named period-3 profile in cached db
```

## Purpose

This continues:

```text
period3_all_cycles_Ibc_scan_diagnostic.md
```

The all-cycles scan showed that:

```text
Ib*c=z
```

is not a law of a bare period-3 right-`h` cycle.  This diagnostic checks the
sharper question:

```text
what happens after adding the shared-step/M7 witness condition?
```

## Script

```text
tools/period3_m7_witness_cycle_scan.js
```

It scans cached db models for every period-3 cycle:

```text
z*h=b,
b*h=c,
c*h=z.
```

Then it marks whether that cycle is actually the `z` orbit of a clean
shared-step/M7 first-event self-repeat:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
U*h!=W*h,
clean anchored-X3 triple,
first source-orbit event is a clean self-repeat with z:3->0.
```

The scan counts cycles, not only pair-level witnesses.

## Result

Run:

```text
tools\node-portable\node.exe tools\period3_m7_witness_cycle_scan.js
```

Summary:

```text
cycles:                     343512
strictCycles:               201500
cyclesWithM7Witness:           240
strictCyclesWithM7Witness:      240
m7WitnessPairs:              6240
```

All `240` strict cycles with an M7 witness have the same named profile:

```text
A=Ib*c=z;
Ib*h=c;
K=(Ib*c)*Ib=Ic;
L=h;
z*Ib=Ic.
```

The scan found:

```text
examplesM7WithoutAIbcz: []
```

So every cached M7-witness period-3 cycle has the watched output hit:

```text
Ib*c=z.
```

and in fact the full named fan profile.

## Contrast With Non-M7 Cycles

Strict cycles without M7 witnesses still show many other profiles:

```text
A=Ib*c=z:       191073
fresh:             1500
K=c; L=c*c:        1248
K=A:                312
```

Thus the M7 witness is the meaningful extra condition.  It is not enough to
argue from:

```text
z*h=b,
b*h=c,
c*h=z.
```

alone.

## Interpretation

The next proof target should be stated as:

```text
M7-witness named-profile lemma:
in a clean shared-step/M7 period-3 residual, the cycle must satisfy

    Ib*c=z,
    z*Ib=Ic,
    (Ib*c)*Ib=Ic,
    Ib*h=c.
```

Proving only `Ib*c=z` may be the first useful subgoal, since it is a watched
output hit of the `c`-input V3 bridge.  But the db evidence says the whole
named profile arrives together once the M7 witness condition is present.

## Next Structural Question

Find which part of the M7 witness eliminates the non-M7 alternatives:

```text
K=(Ib*c)*Ib=c,
L=c*c,
or fresh A=Ib*c.
```

The candidate source is first-event minimality: in the non-M7 db examples,
the corresponding shared-step scan routes before the clean period-3
self-repeat stage.  Therefore the proof should try to show:

```text
if a period-3 cycle has A!=z or K=c/L=c*c, then any shared-step witness routes
by an earlier first event, so it cannot be the minimal clean M7 residual.
```

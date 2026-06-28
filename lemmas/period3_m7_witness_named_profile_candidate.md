# Period-3 M7 Witness Named Profile Candidate

Date: 2026-06-28.

Status:

```text
candidate / exact theorem target suggested by db and reductions
```

## Purpose

The current period-3 work should no longer aim at a bare period-3 identity.
The exact candidate is a theorem about a period-3 cycle that comes from a
clean shared-step/M7 witness.

This file states the target cleanly, separate from the diagnostics.

## Setup

Assume the shared-step anchored-X3/M7 residual:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
U*h=T,
W*h=S,
T!=S.
```

The anchored-X3 triple in `H_h` is clean:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b,
alpha=pred_z(h).
```

The first source-orbit event is a clean same-orbit self-repeat of the `z`
orbit at depth 3:

```text
z*h=b,
b*h=c,
c*h=z.
```

No earlier source hit, output merge, input repeat, input-output cross hit, or
watched/core hit occurs before this period-3 return.

Use the period-3 zipper inputs:

```text
b*Ib=h,
c*Ic=h.
```

Define:

```text
A=Ib*c,
K=A*Ib=(Ib*c)*Ib,
L=c*K.
```

## Candidate Statement

In the clean shared-step/M7 period-3 residual:

```text
A=z.
```

Equivalently:

```text
Ib*c=z.
```

The db evidence suggests the stronger named profile:

```text
Ib*c=z,
z*Ib=Ic,
(Ib*c)*Ib=Ic,
Ib*h=c.
```

## Why This Is The Right Target

The implication:

```text
(Ib*c)*Ib=Ic -> Ib*h=c
```

is already proved in:

```text
period3_shifted_hook_pair_implies_named_fan_lemma.md
```

and then:

```text
Ib*h=c
```

gives the named outgoing fan in `H_c` by:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
```

The `c`-input V3 split shows that if:

```text
Ib*c=z,
```

then the output of the row-`Ib` branch is a watched period-3 vertex, so the
branch routes before the fully clean generic V3 residual.

## What Must Not Be Proved

Do not try to prove:

```text
bare period-3 zipper -> Ib*c=z.
```

This is false in the cached db evidence.  See:

```text
period3_all_cycles_Ibc_scan_diagnostic.md
```

The additional assumptions needed are exactly the shared-step/M7 origin and
the first-event minimality.

## Db Evidence

The cycle-level witness scan:

```text
period3_m7_witness_named_profile_diagnostic.md
tools/period3_m7_witness_cycle_scan.js
```

found:

```text
strict period-3 cycles:              201500
strict cycles with M7 witness:          240
pair-level M7 witnesses:              6240
M7 cycles without Ib*c=z:                0
```

All M7-witness cycles have:

```text
Ib*c=z,
z*Ib=Ic,
(Ib*c)*Ib=Ic,
Ib*h=c.
```

## Possible Proof Route

Assume the contrary:

```text
A=Ib*c != z.
```

Then by:

```text
period3_c_input_v3_second_layer_boundary.md
period3_c_input_v3_fixed_target_orbit_boundary.md
```

either:

```text
1. A or L hits another watched/core value and routes;
2. L=h and the named fan already appears;
3. or rows b and Ib create a clean generic V3 in H_c.
```

In case 3, the two right-`c` source orbits are:

```text
b  -> b*c  -> (b*c)*c  -> ...
Ib -> Ib*c -> (Ib*c)*c -> ...
```

The proof should show that this object is born before the terminal M7 return
`c*h=z`, or that its first event is an earlier routed event.  Either outcome
contradicts minimality of the clean M7 period-3 residual.

## Next Use

Attack this candidate directly:

```text
clean shared-step/M7 period-3 + A!=z
```

and try to derive one of the routed first-event roles excluded by the M7
normal form.

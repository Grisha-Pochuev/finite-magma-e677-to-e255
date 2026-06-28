# Period-3 c-Input V3 Second-Layer Boundary

Date: 2026-06-28.

Status:

```text
boundary/diagnostic / c-input V3 is generic clean V3 unless it hits watched data
```

## Purpose

This continues:

```text
period3_row_b_Ib_c_input_v3_lemma.md
```

The clean period-3 residual exposes the same-input split:

```text
row b:  c -> BC,
row Ib: c -> A,
```

where:

```text
BC=b*c,
A=Ib*c.
```

This file records the exact second-layer expansion and the clean residual.

## Setup

Use:

```text
z*h=b,
b*h=c,
c*h=z,
b*Ib=h.
```

Define:

```text
BC=b*c,
A=Ib*c,
K=A*Ib=(Ib*c)*Ib,
L=c*K.
```

E677 with `x=c,y=Ib` gives:

```text
Ib*L=c.
```

So the target-lift of the `c`-input split in `H_c` is:

```text
row b:  h -> BC,
row Ib: L -> A.
```

## Immediate Routes

The split is not fully clean if any of the following happens:

```text
A=BC                     -> same output / incoming merge in H_c;
L=h                      -> named H_c fan at h;
A or L hits watched data -> old/core attachment;
L=BC or A=h              -> input-output path in H_c;
same full interval       -> source-row reconstruction.
```

The db-supported identity:

```text
Ib*c=z
```

is in this list.  It is a watched hit of the output `A`, so it routes before
one reaches the fully clean `c`-input V3 residual.  Thus the public db
examples support the idea that the new V3 should close by watched/core
attachment, not only by the named fan equality.

## Second-Layer Expansion

For the generic V3:

```text
p=b,
q=Ib,
common input c,
s=BC,
r=A,
```

the general second-layer lemma gives two more edges in `H_c`.

The row-`BC` edge is:

```text
(b*BC)*b -> BC*c.
```

The row-`A` edge is:

```text
(Ib*A)*Ib -> A*c.
```

Therefore the fully clean second-layer object in `H_c` is:

```text
row b:  h             -> BC
row Ib: L             -> A
row BC: (b*BC)*b      -> BC*c
row A:  (Ib*A)*Ib     -> A*c.
```

This is a generic four-edge V3 matching, not a zipper-born shifted window:
unlike the adjacent right-`h` zipper bridge, the source/output overlap
`q=s` is not forced here.

## Local Saturation Diagnostic

The script:

```text
tools/period3_zipper_saturation.js
```

now watches:

```text
A=Ib*c,
L=c*((Ib*c)*Ib),
(b*BC)*b,
(Ib*A)*Ib,
BC*c,
A*c.
```

Runs:

```text
tools\node-portable\node.exe tools\period3_zipper_saturation.js 4 12 250000
tools\node-portable\node.exe tools\period3_zipper_saturation.js 5 16 1200000
```

Both remain clean-consistent.  At depth 5 the checker does not derive:

```text
A=BC,
A in {z,b,c,h},
L in {h,alpha,Ib,Ic,z,b,c,BC,A},
(Ib*c)*Ib=Ic,
BC*c=A*c,
or second-layer input/output hits against the displayed watched set.
```

So the bare local period-3 equations do not close the `c`-input V3 by a short
second-layer collision.

The depth-4 class output is also informative:

```text
A=Ib*c class: ["(Ib*c)"]
L=c*((Ib*c)*Ib) class: ["(c*((Ib*c)*Ib))"]
```

So at this bounded local level neither `A` nor `L` even rewrites to another
short named expression.  The db relation `Ib*c=z` is therefore not a hidden
form of the already proved zipper input identities; it needs a global/core
argument or a stronger hypothesis.

A small raw-label model diagnostic for the fresh case is recorded in:

```text
period3_c_input_fresh_A_rawmodel_diagnostic.md
```

It exhausts size 7 with no arbitrary E677 model for the weak fresh-A template;
size 8 times out at 60 seconds without a model.

The broader all-cycle db scan is recorded in:

```text
period3_all_cycles_Ibc_scan_diagnostic.md
period3_m7_witness_named_profile_diagnostic.md
```

It shows that `Ib*c=z` is not a general period-3 law.  Strict db period-3
cycles outside the G12/shared-step filter can have fresh `A=Ib*c`, often with:

```text
(Ib*c)*Ib=c,
L=c*c.
```

So any proof of `Ib*c=z` must use the extra current residual hypotheses, not
only the bare right-`h` period-3 cycle.

The M7 witness scan sharpens this: all cached strict period-3 cycles with a
clean shared-step/M7 witness have:

```text
Ib*c=z,
z*Ib=Ic,
(Ib*c)*Ib=Ic,
Ib*h=c.
```

Thus the live target is the M7-witness named-profile lemma, not a general
period-3 identity.

## Consequence

The period-3 residual now has a cleaner split:

```text
1. A=Ib*c hits watched/old data, especially A=z in the public db;
2. L=h, equivalently (Ib*c)*Ib=Ic, giving the named H_c fan;
3. or the branch is a generic ungenerated clean V3 four-edge matching in H_c.
```

Case 3 is no longer a special period-3 equality hunt.  It belongs to:

```text
clean_same_input_v3_admissibility_frontier.md
clean_same_input_v3_second_layer_expansion_lemma.md
clean_v3_fixed_target_source_orbit_reduction.md
period3_c_input_v3_fixed_target_orbit_boundary.md
```

with fixed target:

```text
c.
```

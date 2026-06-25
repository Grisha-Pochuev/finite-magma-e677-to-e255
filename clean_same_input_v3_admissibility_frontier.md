# Clean Same-Input V3 Admissibility Frontier

Date: 2026-06-25.

Status:

```text
active frontier / unified admissibility target for clean V3 bridges
```

## Purpose

This unifies the two remaining appearances of the same object:

```text
clean same-input two-target bridge.
```

It is the common obstruction behind:

```text
general_v3_bridge_descent_boundary.md
anchored_m7_reduces_to_general_v3_admissibility.md
```

## General V3 Object

Rows `p,q` share an input:

```text
p*z=s,
q*z=r,
s!=r.
```

The bridge is:

```text
H_s: z -> p*s,
H_r: z -> q*r.
```

Equivalently, the target-lift in `H_z` is:

```text
P_z -> s,
Q_z -> r,
P_z=z*(s*p),
Q_z=z*(r*q).
```

If the lifted pair has same input, same output, full interval repetition, or
input-output cross hit, it is routed by:

```text
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
same_target_pair_collision_trichotomy_lemma.md
```

So the hard case is the clean-disjoint lift/advance square.

## Two Sources Of V3

### 1. First-Extra V3

From:

```text
general_v3_bridge_descent_boundary.md
```

The common input is the first extra row-orbit intersection:

```text
z=w.
```

This V3 is born before the terminal same-row recurrence event.  The existing
measure names it by:

```text
M5/M6.
```

### 2. Anchored-M7 V3 Necklace

From:

```text
anchored_m7_clean_v3_necklace_obstruction.md
```

The common input is the anchor:

```text
z=h.
```

The bridge is adjacent inside the first clean right-`h` self-repeat cycle:

```text
H_{r_i}:     h -> A_i,
H_{r_{i+1}}: h -> A_{i+1}.
```

The proposed measure names it by:

```text
M8.
```

## Generated-Input Subcase

When the common input is a generated input:

```text
z=A_j,
```

the bridge has extra structure.  Use:

```text
generated_input_three_source_bridge_expansion_lemma.md
row_b_generated_input_bridge_lemma.md
clean_external_bridge_fifth_stage_reduction_lemma.md
```

Then the V3 bridge is not isolated: row `x_j` and row `b` provide the base
generated edges, and the residual expands to a three-source same-target
configuration or a three-target same-input bridge.

This generated-input subcase is better than the general V3 problem.

## Ungenerated Clean V3 Gap

The remaining hard case is:

```text
clean same-input two-target bridge
whose common input is not known to be a generated input A_j
and whose lifted H_z pair is clean-disjoint.
```

This includes:

```text
first-extra V3 at z=w,
anchored-M7 V3 at z=h,
```

unless `w` or `h` is later shown to be generated/watched/core.

## Second-Layer Expansion

The ungenerated clean V3 gap now has a sharper internal form.

Use:

```text
clean_same_input_v3_second_layer_expansion_lemma.md
```

For:

```text
p*z=s,
q*z=r,
A=p*s,
B=q*r,
```

the usual lift in `H_z`:

```text
P=z*(s*p) -> s,
Q=z*(r*q) -> r
```

forces a second layer in the same graph:

```text
A*p -> s*z,
B*q -> r*z.
```

Any input repeat, output repeat, input-output hit, full ported interval
repeat, or watched/core hit between these two layers routes locally.  For a
generic V3 bridge, the fully clean residual is therefore a clean four-edge
matching in `H_z`, not only a two-edge target-lift pair.

This four-edge matching is itself the first two layers of two fixed-target
source-successor orbits in `H_z`.  Use:

```text
clean_v3_fixed_target_source_orbit_reduction.md
```

The two orbits are:

```text
p -> s -> s*z -> ...
q -> r -> r*z -> ...
```

First source-orbit events route by fixed-target first-merge and same-target
collision roles.  The only clean finite residual is a same-orbit right-`z`
self-repeat, which has the same zipper form as the anchored-M7 self-repeat.

The common fixed-target zipper/V3 necklace transport is recorded in:

```text
fixed_target_zipper_bridge_necklace_lemma.md
fixed_target_zipper_reduces_to_v3_admissibility.md
zipper_born_v3_second_layer_shift_lemma.md
```

It covers both the anchored-M7 case (`t=h`) and the V3-born case (`t=z`).

Important distinction:

```text
generic ungenerated V3 -> possible clean four-edge matching;
zipper-born adjacent V3 -> shifted zipper window, not fresh four-edge clean.
```

## Unified Admissibility Principle

The needed statement is:

```text
In a minimal G12 loop, an ungenerated clean same-input two-target bridge born
before the current terminal event is admissible as a smaller measured relay
object, unless it hits watched/core data or repeats a full ported interval in
an independent role.
```

If true:

```text
first-extra V3 closes by M5/M6;
anchored-M7 V3 necklace closes by M8.
```

## Exact Next Target

Prove one of:

```text
1. any ungenerated clean V3 bridge has a second-layer hit in H_z;
2. any clean four-edge V3 matching has a routed fixed-target first event;
3. any zipper-born clean adjacent V3 bridge is admissible under the same
   global measure as first-extra V3 bridges;
4. the common input z must be generated/watched/core in both current sources;
5. a fully clean fixed-target zipper/V3 necklace is the true final obstruction.
```

Do not continue treating first-extra V3 and anchored-M7 V3 as separate
local problems unless a source-specific extra structure is being used.

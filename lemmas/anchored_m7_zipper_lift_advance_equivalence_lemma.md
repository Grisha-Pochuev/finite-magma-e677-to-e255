# Anchored-M7 Zipper Lift-Advance Equivalence Lemma

Date: 2026-06-25.

Status:

```text
proved transport / adjacent zipper edges are exactly lifted same-input splits
```

## Purpose

This refines:

```text
anchored_m7_coupled_zipper_bridge_residual.md
```

The coupled zipper-bridge residual is not a new kind of bridge.  Each adjacent
pair of zipper edges is exactly the same-input target-lift construction, and
target advance returns it to the same-input bridge necklace.

## Local Setup

Take three consecutive source rows in the clean right-`h` source cycle:

```text
r_{i-1}*h = r_i,
r_i*h     = r_{i+1}.
```

This is a same-input split at the common input:

```text
h.
```

Apply:

```text
same_input_split_target_lift_lemma.md
```

with:

```text
p=r_{i-1},
q=r_i,
z=h,
s=r_i,
r=r_{i+1}.
```

The lifted feet are:

```text
P_h = h*(r_i*r_{i-1}),
Q_h = h*(r_{i+1}*r_i).
```

But these are exactly the zipper inputs:

```text
P_h=I_{i-1},
Q_h=I_i.
```

Therefore the target-lift of the same-input split:

```text
r_{i-1}*h=r_i,
r_i*h=r_{i+1}
```

is precisely the adjacent pair of `H_h` edges:

```text
I_{i-1} -> r_i,
I_i     -> r_{i+1}.
```

## Advance Back

Now apply:

```text
same_input_lift_target_advance_lemma.md
```

to this adjacent `H_h` pair.

Target advance returns to the same-input two-target bridge:

```text
H_{r_i}:     h -> r_{i-1}*r_i,
H_{r_{i+1}}: h -> r_i*r_{i+1}.
```

In the notation:

```text
A_i=r_{i-1}*r_i,
A_{i+1}=r_i*r_{i+1},
```

this is:

```text
H_{r_i}:     h -> A_i,
H_{r_{i+1}}: h -> A_{i+1}.
```

Thus the coupled zipper-bridge residual is a closed necklace of the standard
same-input split:

```text
same-input split at h
  -> target-lift to adjacent H_h zipper pair
  -> target-advance back to same-input bridge at h.
```

## Consequence

The fully clean residual can be described without new primitives:

```text
a cyclic chain of clean same-input splits at h,
whose target-lifts form a clean matching in H_h,
and whose target-advances form a clean same-input bridge necklace.
```

So the remaining issue is not local classification.  It is admissibility:

```text
Can a minimal G12 loop contain a closed clean necklace of V3-type
same-input bridges all sharing the anchor h?
```

## Routed Cases

Any failure of cleanness routes by existing lemmas:

```text
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
same_target_pair_collision_trichotomy_lemma.md
general_v3_bridge_descent_boundary.md
anchored_m7_zipper_first_collision_target.md
```

The only live case is therefore:

```text
fully clean lift/advance necklace at common input h.
```

## Next Target

Prove that the fully clean necklace is a smaller measured V3/M7 object.

If this descent cannot be shown directly, the next exact obstruction is:

```text
a closed clean V3 necklace at one common input h,
with no target/output/input/cross-layer collisions and no watched/core hit.
```

This is narrower than the previous "clean cyclic zipper" statement because it
places every adjacent pair inside the already-established same-input
lift/advance transport.

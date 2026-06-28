# Anchored-M7 Zipper Target-Advance Lemma

Date: 2026-06-25.

Status:

```text
proved transport / clean zipper advances to same-input multi-target bridge
```

## Purpose

This sharpens the live residual from:

```text
anchored_m7_cycle_zipper_lemma.md
anchored_m7_zipper_first_collision_target.md
```

The clean cyclic zipper is not only a matching in `H_h`.  Target advance turns
it into a family of same-input bridge edges with common input `h`.

This connects the anchored-M7 residual back to the general V3/same-input
bridge machinery.

## Setup

Use the clean right-`h` source cycle:

```text
r_i*h=r_{i+1}
```

with indices taken cyclically on the first clean self-repeat segment.

Let:

```text
I_i=pred_{r_i}(h).
```

So row `r_i` gives an edge in `H_h`:

```text
I_i -> r_{i+1}.
```

The zipper lemma gives:

```text
I_i=h*(r_{i+1}*r_i)=(r_{i-1}*r_i)*r_{i-1}.
```

## Target Advance

The full ported interval carried by row `r_i` is:

```text
(target,input,output)=(h,I_i,r_{i+1}).
```

Target advance by the same row gives:

```text
(target,input,output)
  =
(r_{i+1}, h, r_i*r_{i+1}).
```

Thus in the target graph `H_{r_{i+1}}`:

```text
h -> r_i*r_{i+1}
```

carried by row `r_i`.

Equivalently, if:

```text
A_{i+1}=r_i*r_{i+1},
```

then the whole clean zipper gives:

```text
H_{r_{i+1}}: h -> A_{i+1}
```

for every position `i`.

## Consequence

Every pair of positions gives a same-input two-target bridge:

```text
H_{r_{i+1}}: h -> A_{i+1},
H_{r_{j+1}}: h -> A_{j+1}.
```

Since the source cycle is a first clean self-repeat:

```text
r_{i+1} != r_{j+1}
```

for distinct positions before the chosen return.  Therefore the targets of
these bridge edges are distinct.

## Immediate Hit Roles

The advanced bridge is not clean if any displayed term hits a watched/core
layer, or if it produces an already routed same-input bridge collision:

```text
A_{i+1}=A_{j+1},
A_{i+1}=r_{j+1},
A_{j+1}=r_{i+1},
A_{i+1}=h,
A_{j+1}=h.
```

These roles route by the already existing same-input / target-advance
machinery:

```text
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
general_v3_bridge_descent_boundary.md
```

If no such hit occurs, the advanced object is a clean same-input
multi-target bridge necklace with common input:

```text
h.
```

## Relation To The Zipper Inputs

The advanced output:

```text
A_i=r_{i-1}*r_i
```

is also the left factor in the zipper input:

```text
I_i=A_i*r_{i-1}.
```

So the two views are coupled:

```text
H_h:     I_i -> r_{i+1}      carried by row r_i,
H_{r_i}: h   -> A_i          carried by row r_{i-1},
I_i=A_i*r_{i-1}.
```

This is stronger than an arbitrary V3 bridge: each bridge output `A_i` feeds
back into the next `H_h` input.

## Remaining Clean Residual

After routing first collisions in the zipper matching and in the advanced
same-input bridges, the live object is:

```text
a clean cyclic zipper matching in H_h,
coupled to a clean same-input multi-target bridge necklace at common input h.
```

The next proof target is to show that this coupled object is either:

```text
1. a smaller admissible V3/M7 bridge;
2. a strict clean theta in H_h;
3. an independent full ported-interval repeat;
4. a watched/core attachment.
```

In a minimal G12 loop, option 1 should be the expected descent route.

# Fixed-Target Zipper Reduces To V3 Admissibility

Date: 2026-06-26.

Status:

```text
conditional reduction / unified measure gap for zipper-born V3 necklaces
```

## Purpose

This replaces the anchored-only measure statement:

```text
anchored_m7_v3_necklace_measure_extension.md
```

with a target-independent version using:

```text
fixed_target_zipper_bridge_necklace_lemma.md
```

The goal is to state the remaining admissibility gap once, for both:

```text
anchored-M7 self-repeat, where t=h;
V3-born fixed-target self-repeat, where t=z.
```

## Generic Zipper Data

Fix a target:

```text
t.
```

Let a clean right-`t` source self-repeat have first return rank:

```text
r_0*t=r_1,
...
r_{n-1}*t=r_0.
```

For each position define:

```text
A_i=r_{i-1}*r_i.
```

By:

```text
fixed_target_zipper_bridge_necklace_lemma.md
```

the self-repeat gives a same-input V3 bridge necklace:

```text
H_{r_i}: t -> A_i.
```

Every adjacent pair is a V3 bridge:

```text
H_{r_i}:     t -> A_i,
H_{r_{i+1}}: t -> A_{i+1}.
```

Its target-lift is exactly the adjacent zipper pair in `H_t`.

## Routed Cases

If any adjacent V3 bridge is not clean, it routes by:

```text
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
same_target_pair_collision_trichotomy_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
ported_interval_state_lemma.md
```

If any displayed source/input/output hits watched/core data, it routes by the
ordinary relay/core attachment machinery.

So the only relevant residual is:

```text
a fully clean fixed-target zipper/V3 necklace.
```

## Generic Necklace Rank

Add a target-independent subrank:

```text
MZ. fixed-target zipper-born V3 bridge rank:
    the first position i<n at which the clean right-t self-repeat produces
    a locally clean adjacent V3 bridge

        H_{r_i}:     t -> A_i,
        H_{r_{i+1}}: t -> A_{i+1}.
```

This specializes to the old anchored rank:

```text
MZ = M8 when t=h and the self-repeat is the anchored-M7 cycle.
```

For a V3-born self-repeat, the same rank measures the first clean bridge born
inside the right-`z` source orbit created by the V3 four-edge matching.

## Why It Is Smaller

The terminal event is the first return:

```text
r_n=r_0.
```

Every adjacent V3 bridge in the necklace is born at a position:

```text
i<n.
```

Therefore, if such a bridge is admissible as a relay object of the same global
kind, it is smaller than the terminal self-repeat that generated it:

```text
MZ < n.
```

This is the common descent:

```text
clean fixed-target self-repeat
-> zipper/V3 necklace
-> earliest clean adjacent V3 bridge
-> smaller measured relay object.
```

## Conditional Reduction

Assume the unified V3 admissibility principle:

```text
Every clean same-input V3 bridge born before the current terminal event is
either locally routed, or admissible as a smaller measured relay object.
```

Then a fully clean fixed-target zipper/V3 necklace cannot be terminal in a
minimal G12 loop.

Proof:

```text
1. choose the earliest locally clean adjacent V3 bridge in the necklace;
2. it is born at position i<n before the terminal self-repeat return;
3. by unified V3 admissibility it is a smaller measured relay object;
4. this contradicts minimality of the terminal clean self-repeat.
```

Thus any terminal zipper/V3 necklace must violate unified V3 admissibility or
one of the routed assumptions.

## Exact Remaining Gap

The remaining proof obligation is now a single sentence:

```text
A zipper-born clean adjacent V3 bridge is admissible under the same global
minimality measure as first-extra V3 bridges.
```

Use the clarification:

```text
zipper_born_v3_second_layer_shift_lemma.md
```

A zipper-born adjacent V3 bridge is not a generic clean four-edge V3 object.
Its second V3 layer overlaps the existing zipper:

```text
I_a -> b,
I_b -> c,
I_b -> c,
I_c -> c*t.
```

So the admissibility sentence is really about a clean shifted zipper window,
not about a fresh four-edge matching.

If this sentence is true, then both currently live clean residuals close:

```text
anchored-M7 clean necklace;
V3-born clean self-repeat zipper.
```

If it is false, the exact obstruction is:

```text
a fully clean fixed-target zipper/V3 necklace whose adjacent V3 bridges are
locally standard shifted zipper windows but cannot be inserted into the
global relay measure.
```

This is narrower than the previous obstruction because it is no longer tied
to the anchor `h`; it is the target-independent final V3 admissibility gap.

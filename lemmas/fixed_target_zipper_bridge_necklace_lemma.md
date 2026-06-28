# Fixed-Target Zipper Bridge-Necklace Lemma

Date: 2026-06-26.

Status:

```text
proved transport / any clean fixed-target self-repeat gives a V3 necklace
```

## Purpose

This extracts the target-independent part of:

```text
anchored_m7_cycle_zipper_lemma.md
anchored_m7_zipper_target_advance_lemma.md
anchored_m7_zipper_lift_advance_equivalence_lemma.md
clean_v3_fixed_target_source_orbit_reduction.md
```

The same mechanism works for every fixed target.  The anchored-M7 case is the
specialization `t=h`; the V3-born case is the specialization `t=z`.

## Setup

Fix a target:

```text
t.
```

Let a clean same-orbit source-successor self-repeat under right multiplication
by `t` be:

```text
r_i*t=r_{i+1}
```

with indices taken cyclically on the first clean self-repeat segment.

For each source row `r_i`, define the `H_t` input:

```text
I_i=pred_{r_i}(t).
```

Thus row `r_i` gives the `H_t` interval:

```text
r_i*I_i=t,
r_i*t=r_{i+1},
I_i -> r_{i+1}.
```

## Zipper Formula

The predecessor formula gives:

```text
I_i=t*(r_{i+1}*r_i).
```

The previous source row `r_{i-1}` gives:

```text
r_{i-1}*t=r_i.
```

Apply the fixed-target source-successor formula to row `r_{i-1}`.  The next
`H_t` input for row `r_i` is:

```text
(r_{i-1}*r_i)*r_{i-1}.
```

Since row `r_i` has a unique input mapping to `t`, we get:

```text
I_i=(r_{i-1}*r_i)*r_{i-1}.
```

Therefore every internal position satisfies the zipper equation:

```text
t*(r_{i+1}*r_i)=(r_{i-1}*r_i)*r_{i-1}.
```

## Target Advance To A Same-Input Necklace

The full ported interval carried by row `r_i` is:

```text
(target,input,output)=(t,I_i,r_{i+1}).
```

Target advance by the same row gives:

```text
(r_{i+1}, t, r_i*r_{i+1}).
```

So in `H_{r_{i+1}}`:

```text
t -> A_{i+1},
A_{i+1}=r_i*r_{i+1}.
```

Thus the self-repeat zipper produces a same-input bridge necklace:

```text
H_{r_i}: t -> A_i,
A_i=r_{i-1}*r_i.
```

Every adjacent pair is a V3-type same-input bridge:

```text
H_{r_i}:     t -> A_i,
H_{r_{i+1}}: t -> A_{i+1}.
```

## Lift/Advance Equivalence

Take two adjacent source steps:

```text
r_{i-1}*t=r_i,
r_i*t=r_{i+1}.
```

This is a same-input split at common input `t`.  Apply the standard target-lift:

```text
P_t=t*(r_i*r_{i-1}),
Q_t=t*(r_{i+1}*r_i).
```

By the zipper input formula:

```text
P_t=I_{i-1},
Q_t=I_i.
```

Therefore the target-lift of the adjacent same-input split is exactly the
adjacent pair of zipper edges in `H_t`:

```text
I_{i-1} -> r_i,
I_i     -> r_{i+1}.
```

Target-advance returns exactly to the adjacent same-input bridge:

```text
H_{r_i}:     t -> A_i,
H_{r_{i+1}}: t -> A_{i+1}.
```

So the clean self-repeat zipper and the clean V3 necklace are two views of
the same fixed-target object.

For the adjacent V3 bridge, the generic V3 second-layer expansion is not a
fresh four-edge layer.  It is a shifted zipper window:

```text
zipper_born_v3_second_layer_shift_lemma.md
```

The overlap is forced because in the adjacent split:

```text
r_{i-1}*t=r_i,
r_i*t=r_{i+1},
```

the second row is also the first output.

## Routed Hits

If any of the following occurs:

```text
I_i=I_j,
r_i=r_j before the chosen self-repeat,
I_i=r_j,
A_i=A_j,
A_i=r_j,
A_i=I_j,
A_i=t,
watched/core hit,
full ported interval repetition in an independent role,
```

then the object is not the fully clean residual.  It routes by:

```text
same_target_pair_collision_trichotomy_lemma.md
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
ported_interval_state_lemma.md
```

## Clean Residual

The exact clean residual is:

```text
a clean cyclic zipper matching in H_t
coupled to a clean same-input V3 bridge necklace at common input t.
```

This single residual covers both:

```text
anchored-M7 clean self-repeat, with t=h;
V3-born clean self-repeat, with t=z.
```

## Consequence

The remaining admissibility problem is now target-independent:

```text
Can a minimal G12 loop contain a clean fixed-target zipper/V3 necklace?
```

A successful descent proof only needs to show:

```text
some adjacent V3 bridge in the necklace is admissible as a smaller measured
relay object,
```

unless one of the routed hits above occurs.

# Anchored-M7 Coupled Zipper-Bridge Residual

Date: 2026-06-25.

Status:

```text
residual / exact live object after zipper target advance
```

## Starting Point

Use:

```text
anchored_m7_cycle_zipper_lemma.md
anchored_m7_zipper_first_collision_target.md
anchored_m7_zipper_target_advance_lemma.md
```

The live branch is no longer just a source cycle.  It is two coupled layers.

## Layer 1: Matching In `H_h`

The clean right-`h` source cycle has:

```text
r_i*h=r_{i+1}.
```

For each position, row `r_i` gives an edge in `H_h`:

```text
I_i -> r_{i+1},
r_i*I_i=h.
```

The fully clean matching assumptions are:

```text
all r_i distinct before return,
all I_i distinct,
no I_i equals any r_j,
no watched/core hit.
```

## Layer 2: Same-Input Bridge Necklace

Target advance of the same interval gives:

```text
H_{r_{i+1}}: h -> A_{i+1},
A_{i+1}=r_i*r_{i+1}.
```

Thus all advanced edges share the same input:

```text
h.
```

For every two positions, this is a V3-type same-input two-target bridge.

## Coupling

The two layers are tied by the zipper equation:

```text
I_i=h*(r_{i+1}*r_i)=A_i*r_{i-1},
A_i=r_{i-1}*r_i.
```

So:

```text
H_{r_i}: h -> A_i      carried by row r_{i-1},
H_h:     I_i -> r_{i+1} carried by row r_i,
I_i=A_i*r_{i-1}.
```

The advanced bridge output `A_i` is not a free endpoint; it immediately
generates the next `H_h` input through row `r_{i-1}`.

## Routed Hits

Route immediately if any of the following occurs:

```text
I_i=I_j                  -> outgoing fan in H_h;
r_{i+1}=r_{j+1}          -> earlier source repeat;
I_i=r_{j+1}              -> path in H_h;
A_i=A_j                  -> same-input bridge collision / V3 route;
A_i=r_j or A_i=I_j       -> layer hit / path/fan route;
A_i=h                   -> loop/fixed target hit;
any displayed term watched/core -> old relay/core attachment.
```

These are not new cases.  Use:

```text
same_target_pair_collision_trichotomy_lemma.md
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
general_v3_bridge_descent_boundary.md
anchored_m7_first_event_routing_lemma.md
```

## Exact Clean Residual

The only live residual is:

```text
clean cyclic zipper matching
+
clean same-input bridge necklace at common input h
+
no cross-layer hits among r_i, I_i, A_i, h, or watched/core terms.
```

## Next Target

Prove one of:

```text
1. the clean same-input bridge necklace is a smaller admissible V3/M7 object;
2. the coupled matching creates strict clean theta in H_h;
3. some full ported interval repeats in an independent role;
4. the chain hits watched/core data.
```

The most promising route is to show descent:

```text
anchored false branch
  -> clean cyclic zipper
  -> same-input bridge necklace with smaller M7 rank.
```

The obstacle is to formalize "smaller": the new bridge targets `r_i` lie
inside the first self-repeat cycle, not after it.

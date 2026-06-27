# Clean First-Extra Matching Bridge Alignment

Date: 2026-06-20.

Status:

```text
proved reduction / identifies clean first-extra matching as V3-type bridge
```

## Purpose

This records the exact status of the only open branch in:

```text
two_row_first_extra_intersection_routing_lemma.md
```

The point is to avoid treating clean first-extra matching as a new same-row
recurrence.  It is the same structural object as the V3 clean same-input
two-target bridge frontier, but with a general common input rather than a
generated input `A_j`.

## Setup

Use the notation from:

```text
two_row_first_extra_intersection_routing_lemma.md
```

Rows `p,q` share:

```text
p*b=z,
q*b=z,
p!=q.
```

Their row cycles have a first extra intersection:

```text
w=x_i=y_j
```

outside `{b,z}`.

The two `H_w` edges are:

```text
x_{i-1} -> x_{i+1}   carried by row p,
y_{j-1} -> y_{j+1}   carried by row q.
```

Assume this pair is clean-disjoint under:

```text
same_target_pair_collision_trichotomy_lemma.md
```

so none of:

```text
x_{i-1}=y_{j-1},
x_{i+1}=y_{j+1},
x_{i-1}=y_{j+1},
y_{j-1}=x_{i+1}
```

holds.

## Target-Advance Image

Target advance sends the two intervals:

```text
(w,x_{i-1},x_{i+1}),
(w,y_{j-1},y_{j+1})
```

to:

```text
(x_{i+1},w,x_{i+2}),
(y_{j+1},w,y_{j+2}).
```

Equivalently, it gives a same-input two-target bridge with common input `w`:

```text
H_{x_{i+1}}:  w -> x_{i+2}   carried by row p,
H_{y_{j+1}}:  w -> y_{j+2}   carried by row q.
```

This is exactly the general transport mechanism from:

```text
same_input_lift_target_advance_lemma.md
clean_external_bridge_fourth_stage_reduction_lemma.md
```

## Relation To V3/W3

The clean external bridge route already removed clean disjoint same-target
matching as an independent residual:

```text
clean_external_bridge_fourth_stage_reduction_lemma.md
```

It becomes:

```text
V3. clean same-input two-target bridge.
```

Then, in the generated-input clean bridge setting, this specializes to W3:

```text
clean_external_bridge_fifth_stage_reduction_lemma.md
```

The present first-extra branch is the same V3-type bridge, but the common
input is the first extra row-orbit intersection `w`, not necessarily a
generated input `A_j`.

## Consequence For G12

Therefore the clean first-extra matching branch is not a new G12 recurrence.
It has exactly two possible roles:

```text
1. if the bridge hits the old visible/core footprint or repeats an independent
   full ported interval, it routes by the existing relay reductions;

2. if it remains clean, it is a general V3-type same-input two-target bridge
   whose descent/admissibility must be measured by the global M0-M4 relay
   measure.
```

The next proof target should not reopen same-target matching.  It should prove
that this general V3-type bridge either:

```text
forces the same-output fan pattern seen in M496,
hits a watched/core layer,
or is admissible as a smaller measured relay object.
```

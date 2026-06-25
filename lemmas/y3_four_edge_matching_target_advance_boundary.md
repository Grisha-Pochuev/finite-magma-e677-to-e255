# Y3 Four-Edge Matching Target-Advance Boundary

Date: 2026-06-19.

Status:

```text
boundary / target-advance form of the clean four-edge Z3 matching
```

## Purpose

This continues:

```text
y3_clean_square_four_edge_matching_boundary.md
```

When the shared-successor square stays clean, Z3 contains a four-edge matching
in the single target graph `H_{A_j}`:

```text
P      -> S,
U*p    -> V,
Beta_j -> b,
H_j    -> D_j.
```

This file records its target-advance form.

## Setup

Use:

```text
p*A_j=S,
p*S=U,
S*A_j=V,
S*(U*p)=A_j,

x_j*Beta_j=A_j,
x_j*A_j=b,
x_j*b=x_{j+1},

b*H_j=A_j,
b*A_j=D_j.
```

The clean four-edge matching in `H_{A_j}` is:

```text
row p:   P      -> S,
row S:   U*p    -> V,
row x_j: Beta_j -> b,
row b:   H_j    -> D_j.
```

## Target Advance

Advance each edge along its source row.

Row `p` gives:

```text
H_S: A_j -> U.
```

Row `S` gives:

```text
H_V: A_j -> S*V.
```

Row `x_j` gives:

```text
H_b: A_j -> x_{j+1}.
```

Row `b` gives:

```text
H_{D_j}: A_j -> b*D_j.
```

Thus the clean square produces a four-target same-input bridge:

```text
target S:   A_j -> U,
target V:   A_j -> S*V,
target b:   A_j -> x_{j+1},
target D_j: A_j -> b*D_j.
```

## Collision Split

Any equality among the four advanced outputs:

```text
U,
S*V,
x_{j+1},
b*D_j
```

or any hit of these values to the watched footprint routes by:

```text
same_input_lift_target_advance_lemma.md
same_target_pair_collision_trichotomy_lemma.md
row_b_generated_input_bridge_lemma.md
y3_shared_successor_watched_hit_routing_lemma.md
```

In particular:

```text
U=x_{j+1}
```

means the left row-`p` cycle has hit the generated `X` successor layer.

```text
U=b*D_j
```

compares the left row-`p` second step with the row-`b` second successor from
`D_j`.

```text
S*V=x_{j+1}
or
S*V=b*D_j
```

means the next source row `S` has collided with a generated target-advance
output.

All of these are routed hit/bridge cases, not fresh Z3 square cases.

## Clean Advanced Residual

If all four advanced outputs are fresh and distinct, the remaining object is a
paired four-edge/four-target shell:

```text
H_{A_j} matching:
  P      -> S,
  U*p    -> V,
  Beta_j -> b,
  H_j    -> D_j;

common-input target advance:
  H_S:     A_j -> U,
  H_V:     A_j -> S*V,
  H_b:     A_j -> x_{j+1},
  H_{D_j}: A_j -> b*D_j.
```

The next useful structural question is whether this clean paired shell can
survive the first merge of the two fixed-target source-successor orbits:

```text
p -> S -> V -> ...
x_j -> b -> D_j -> ...
```

without producing a same-target collision in `H_{A_j}`.

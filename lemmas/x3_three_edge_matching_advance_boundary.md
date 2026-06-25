# X3 Three-Edge Matching Advance Boundary

Date: 2026-06-18.

Status:

```text
boundary / target-advance form of the X3 residual
```

## Purpose

This records the target-advance form of the current X3 residual from:

```text
clean_external_bridge_sixth_stage_reduction_lemma.md
```

X3 is a clean extra-source three-edge matching in:

```text
H_{A_j}.
```

Target advance turns it into a clean three-target same-input bridge at the
generated input `A_j`.

## Setup

The X3 same-target matching is:

```text
P      -> S       carried by row p,
Beta_j -> b       carried by row x_j,
H_j    -> D_j     carried by row b,
```

inside:

```text
H_{A_j},
```

with:

```text
p notin {b,x_j},
D_j=b*A_j.
```

Equivalently:

```text
p*P=A_j,
p*A_j=S,

x_j*Beta_j=A_j,
x_j*A_j=b,

b*H_j=A_j,
b*A_j=D_j.
```

Assume the three edges are clean:

```text
inputs P, Beta_j, H_j are pairwise distinct;
outputs S, b, D_j are pairwise distinct;
no input-output cross hit among these six endpoints;
no endpoint hits the watched footprint.
```

## Target Advance

Advance each edge along its own source row.

Row `p` gives:

```text
(A_j, P, S)
  -> (S, A_j, p*S).
```

Row `x_j` gives:

```text
(A_j, Beta_j, b)
  -> (b, A_j, x_{j+1}).
```

Row `b` gives:

```text
(A_j, H_j, D_j)
  -> (D_j, A_j, b*D_j).
```

So the advanced form is the three-target same-input bridge:

```text
H_S:     A_j -> p*S,
H_b:     A_j -> x_{j+1},
H_{D_j}: A_j -> b*D_j.
```

## First Collision Split

The next meaningful split is among the advanced outputs:

```text
p*S,
x_{j+1},
b*D_j.
```

If two advanced outputs coincide, then two source rows share the full edge:

```text
A_j -> common output
```

in their respective operation rows.  This gives a common-edge fan over input
`A_j`, unless the corresponding source rows also coincide.

If one advanced output hits a watched layer, route by that layer.

If all three advanced outputs are clean and distinct, the X3 residual becomes
a clean three-target same-input bridge:

```text
same input A_j,
three source rows p, x_j, b,
three distinct targets S, b, D_j,
three distinct forward outputs p*S, x_{j+1}, b*D_j.
```

## Exact Remaining Residual

The remaining X3 obstruction is therefore not the original matching in
`H_{A_j}`.  It is the paired object:

```text
1. clean three-edge matching in H_{A_j};
2. clean three-target same-input bridge after target advance.
```

The next useful step is to use edge-predecessor triangles on the three
advanced edges, or to compare the common input `A_j` with the row-`b`
predecessor/successor cycle through:

```text
H_j -> A_j -> D_j.
```

The triangle expansion is recorded in:

```text
x3_advanced_edge_triangle_pressure_lemma.md
```

It produces second-triangle edges back into the same target `A_j`, carried by
rows:

```text
p*S,
x_{j+1},
b*D_j.
```

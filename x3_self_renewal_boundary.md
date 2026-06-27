# X3 Self-Renewal Boundary

Date: 2026-06-19.

Status:

```text
corrected boundary / X3 creates a second triangle layer at A_j
```

## Purpose

This packages the result of:

```text
x3_three_edge_matching_advance_boundary.md
x3_advanced_edge_triangle_pressure_lemma.md
```

If X3 remains clean after target advance and triangle expansion, it does not
simply renew with source rows `p*S,x_{j+1},b*D_j`.  The correct triangle layer
uses rows:

```text
S,
b,
D_j.
```

The row `b` part is the already tracked row-b edge.

## Starting X3

The original X3 matching in `H_{A_j}` is:

```text
P      -> S       carried by row p,
Beta_j -> b       carried by row x_j,
H_j    -> D_j     carried by row b.
```

It is clean:

```text
no pairwise input/output/cross collision,
no watched-layer hit.
```

## Advanced Outputs

Target advance gives the three outputs:

```text
U=p*S,
X=x_{j+1},
W=b*D_j.
```

If any two of:

```text
U, X, W
```

coincide, or if any hits a watched layer, route by that collision/hit.

Assume they remain clean and distinct.

## Triangle Layer

The edge-predecessor triangles for:

```text
p*A_j=S,
x_j*A_j=b,
b*A_j=D_j
```

give three row-predecessor edges into `A_j`:

```text
S  * C_p = A_j,
b  * H_j = A_j,
D_j* C_b = A_j,
```

where:

```text
C_p=(p*S)*p,
C_b=(b*D_j)*b.
```

Equivalently, the triangle layer involves rows:

```text
S,
b,
D_j.
```

## Exact Boundary

If the triangle layer has any local collision, use:

```text
same_target_pair_collision_trichotomy_lemma.md
```

If the triangle layer hits the visible/generated watched layers, route by
that hit.

If it is clean, X3 has produced a second triangle layer at the same target
`A_j`:

```text
(p, x_j, b)
  -> triangle rows (S, b, D_j).
```

The middle row `b` is the old row-b bridge, so this is a coupled triangle
layer, not a free source-triple successor.

## Consequence

The remaining X3 obstruction is now exactly:

```text
a clean X3 matching at A_j together with a clean second triangle layer
coupled through the old row-b edge H_j -> D_j.
```

Continuing from here should not assume a simple source-triple successor map.
The next useful split is:

```text
1. a collision/hit involving rows S or D_j;
2. a return to the row-b A-layer cycle through H_j -> A_j -> D_j;
3. or a clean coupled triangle-layer residual.
```

The forward-return mechanism for the extra source row is recorded in:

```text
source_successor_eventual_predecessor_hit_lemma.md
```

Applied to:

```text
p*P=A_j,
p*A_j=S,
```

it says that the row-`p` successor chain from `A_j` eventually hits `P`.

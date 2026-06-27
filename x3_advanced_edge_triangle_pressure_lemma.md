# X3 Advanced Edge Triangle Pressure Lemma

Date: 2026-06-19.

Status:

```text
proved pressure expansion / triangles on the X3 advanced edges
```

## Purpose

This applies the edge-predecessor triangle to the three target-advanced X3
edges from:

```text
x3_three_edge_matching_advance_boundary.md
```

The goal is to expose the next forced predecessor layer after X3 becomes a
clean three-target same-input bridge.

## Setup

The clean advanced X3 bridge has:

```text
H_S:     A_j -> U,
H_b:     A_j -> x_{j+1},
H_{D_j}: A_j -> W,
```

where:

```text
U=p*S,
W=b*D_j,
D_j=b*A_j.
```

These are the target-advanced ported intervals:

```text
S, b, D_j.
```

```text
(S,   A_j, U),
(b,   A_j, x_{j+1}),
(D_j, A_j, W).
```

## Triangle Expansion

Apply the edge-predecessor triangle to each edge:

```text
p*A_j=S,
x_j*A_j=b,
b*A_j=D_j.
```

For row `p`:

```text
p*(A_j*(U*p))=A_j,
S*((p*S)*p)=A_j.
```

For row `x_j`:

```text
x_j*(A_j*(b*x_j))=A_j,
b*((x_j*b)*x_j)=A_j.
```

But:

```text
A_j*(b*x_j)=Beta_j,
x_j*b=x_{j+1},
x_{j+1}*x_j=H_j,
```

by the generated beta/H definitions.  Therefore:

```text
x_j*Beta_j=A_j.
b*H_j=A_j.
```

For row `b`:

```text
b*(A_j*(D_j*b))=A_j,
D_j*((b*D_j)*b)=A_j.
```

Since:

```text
H_j=pred_b(A_j),
```

the first row-`b` predecessor is:

```text
A_j*(D_j*b)=H_j.
```

## New Pressure Pair

The advanced X3 bridge therefore forces a three-way predecessor comparison at
the same input `A_j`:

```text
pred_p(A_j)   = A_j*(U*p),
pred_{x_j}(A_j)= Beta_j,
pred_b(A_j)   = H_j.
```

The clean X3 matching already named:

```text
P=pred_p(A_j),
Beta_j=pred_{x_j}(A_j),
H_j=pred_b(A_j).
```

So the triangle expansion is consistent with the original three-edge matching
in `H_{A_j}`:

```text
P -> S,
Beta_j -> b,
H_j -> D_j.
```

The second triangle edges add:

```text
S*((p*S)*p)=A_j,
b*H_j=A_j,
D_j*((b*D_j)*b)=A_j.
```

## Consequence

If any of the second-triangle columns:

```text
(p*S)*p,
H_j,
(b*D_j)*b
```

or the second-triangle source rows:

```text
S,
b,
D_j
```

hit the watched footprint, route by that hit.

If two second-triangle edges share a full ported interval with target `A_j`,
ported interval reconstruction gives a source-row collision.

If they remain clean, X3 has produced a second triangle layer into the same
target `A_j`, now involving rows:

```text
S,
b,
D_j.
```

The middle row `b` is not new: it is the already tracked row-b predecessor
edge:

```text
H_j -> D_j
```

in `H_{A_j}`.  Thus the next exact residual is not an unstructured new layer;
it is a triangle layer coupled back to the row-b/generated bridge.

# X-Layer Hit Target-Swap Edge Lemma

Date: 2026-06-18.

Status:

```text
proved routing lemma for G / target-swap edge
```

## Purpose

This is the first routing step for the X-layer two-target bridge boundary:

```text
H_i=x_j.
```

It shows that the G-branch always produces an ordinary target-swapped
`H_{x_j}` edge.

Reference:

```text
row_b_x_layer_hit_target_bridge_boundary.md
target_swap_fan_duality_lemma.md
```

## Setup

In the clean ported-matching residual:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i).
```

Assume the X-layer hit:

```text
H_i=x_j.
```

Then:

```text
b*x_j=A_i.
```

Define:

```text
D_i=b*A_i.
```

So row `b` carries the target-`A_i` edge:

```text
b*x_j=A_i,
b*A_i=D_i.
```

In `H_{A_i}`, this is:

```text
x_j -> D_i
```

with source row `b`.

## Target Swap

Apply the target-swap lemma to the edge:

```text
source row p=b,
input x_j,
target A_i,
output D_i.
```

Define:

```text
alpha=x_j*(A_i*b).
```

Then:

```text
b*alpha=x_j.
```

Therefore, after changing target from `A_i` to `x_j`, the same row `b`
contributes the edge in `H_{x_j}`:

```text
alpha -> A_i.
```

Equivalently:

```text
b*alpha=x_j,
b*x_j=A_i.
```

## Boundary Conditions

This is not yet a contradiction.  It becomes useful if:

```text
alpha
```

hits one of:

```text
the generated A-layer,
the generated X-layer,
the visible crossed-fan/core footprint,
or a previously transported target-swap foot.
```

If `alpha` is fresh, the G-branch has been converted from a two-target corner
into a fresh target-swapped edge:

```text
alpha -> A_i in H_{x_j}.
```

The next proof should compare this edge with the original target-`b` edge
carried by row `x_j`:

```text
A_j -> x_{j+1} in H_b.
```

## Consequence

The X-layer hit is routed one step:

```text
H_i=x_j
=> target-A_i edge x_j -> D_i carried by row b
=> target-swapped edge alpha -> A_i in H_{x_j}.
```

Thus G is no longer just an informal two-target bridge; it has a canonical
target-swapped edge with explicit input:

```text
alpha=x_j*(A_i*b).
```


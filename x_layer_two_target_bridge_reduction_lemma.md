# X-Layer Two-Target Bridge Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / G routed to hits or fresh reversible square residual
```

## Purpose

This file packages the G-branch routing:

```text
H_i=x_j.
```

It reduces the X-layer two-target bridge boundary to explicit hit cases or a
fresh reversible two-target square.

## Starting Data

In the clean ported-matching residual, assume:

```text
H_i=x_j.
```

Then:

```text
b*x_j=A_i,
x_j*A_j=b,
x_j*b=x_{j+1}.
```

Define:

```text
D_i=b*A_i,
alpha=x_j*(A_i*b),
gamma=A_j*A_i.
```

## Target-Swap Pair

The X-layer hit creates the target-swapped pair:

```text
H_{x_j}:  alpha -> A_i    carried by row b,
H_{A_j}:  gamma -> b      carried by row x_j.
```

Equivalently:

```text
b*alpha=x_j,
b*x_j=A_i,

x_j*gamma=A_j,
x_j*A_j=b.
```

References:

```text
x_layer_hit_target_swap_edge_lemma.md
x_layer_hit_target_swap_pair_lemma.md
```

## Hit Routing

The immediate hit split is recorded in:

```text
x_layer_target_swap_pair_hit_boundary.md
```

Key local roles:

```text
alpha=x_j  -> routed A-X hit A_i=x_j;
alpha=A_i  -> row-b swaps x_j and A_i;
alpha=A_j  -> same-input two-target split at A_j;

gamma=b    -> routed adjacent recurrence A_j=x_{j+1};
gamma=A_j  -> impossible because A_j!=b.
```

Any other hit of:

```text
alpha or gamma
```

against:

```text
visible footprint,
generated A-layer,
generated X-layer
```

is a concrete attachment to an already tracked layer and should be routed by
the hit target.

## Fresh Reversible Square Residual

If both `alpha` and `gamma` are fresh relative to the watched layers, then G
does not continue as a new target-swap tower.

By:

```text
x_layer_bridge_pair_reversible_square_lemma.md
```

the four intervals:

```text
P =(A_i, x_j, D_i)        source row b,
P'=(x_j, alpha, A_i)     source row b,

Q =(b, A_j, x_{j+1})     source row x_j,
Q'=(A_j, gamma, b)       source row x_j
```

form a reversible two-target square:

```text
P <-> P',
Q <-> Q'.
```

Target advance of `P'` returns to `P`, and target advance of `Q'` returns to
`Q`.

## Final G Reduction

The same-input subcase:

```text
alpha=A_j
```

is further routed by:

```text
same_input_split_target_lift_lemma.md
```

It couples to the beta foot at index `j`:

```text
gamma=Beta_j,
```

and in `H_{A_j}` gives:

```text
H_j    -> x_j,
Beta_j -> b.
```

Therefore it is not an independent residual.

Thus the X-layer two-target bridge boundary is reduced to:

```text
1. visible/generated-layer hit by alpha or gamma;
2. row-b swap x_j <-> A_i;
3. beta-coupled same-input lift at A_j;
4. adjacent same-row recurrence;
5. fresh reversible two-target square residual.
```

This is strictly narrower than the previous G formulation.  The next work
should compare the fresh reversible square with the existing row-b A-layer
cycle / independent-cycle boundaries, not repeat the basic target-swap
calculation.

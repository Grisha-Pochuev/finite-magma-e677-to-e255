# X-Layer Target-Swap Pair Hit Boundary

Date: 2026-06-18.

Status:

```text
boundary / hit split for G target-swap pair
```

## Purpose

After the X-layer hit target-swap pair lemma, G is controlled by two new
target-swap feet:

```text
alpha=x_j*(A_i*b),
gamma=A_j*A_i.
```

This file records the immediate hit split for those feet.

Reference:

```text
x_layer_hit_target_swap_pair_lemma.md
```

## Setup

Assume:

```text
H_i=x_j,
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

Then:

```text
b*alpha=x_j,
b*x_j=A_i,
```

so in `H_{x_j}` row `b` gives:

```text
alpha -> A_i.
```

Also:

```text
x_j*gamma=A_j,
x_j*A_j=b,
```

so in `H_{A_j}` row `x_j` gives:

```text
gamma -> b.
```

## Immediate Alpha Roles

### `alpha=x_j`

Then:

```text
b*alpha=b*x_j=A_i
```

but also:

```text
b*alpha=x_j.
```

Thus:

```text
A_i=x_j.
```

This is an `A-X` hit and is routed out of the clean matching residual.

### `alpha=A_i`

Then:

```text
b*A_i=x_j,
b*x_j=A_i.
```

So row `b` swaps:

```text
x_j <-> A_i.
```

This is a row-`b` same-row target-swap recurrence boundary, not a
bad-target contradiction.

### `alpha=A_j`

Then:

```text
b*A_j=x_j,
x_j*A_j=b.
```

Rows `b` and `x_j` share the input `A_j`, but have outputs `x_j` and `b`.
This is the same-input two-target split form, parallel to:

```text
beta_a_hit_same_input_split_boundary.md
```

It is not a common-edge fan unless an additional equality makes the outputs
coincide.

### Other alpha hits

If:

```text
alpha in visible footprint or alpha in {A_r,x_r}
```

then the target-swapped edge in `H_{x_j}` attaches to an already tracked
layer.  It should be routed by the hit target.

## Immediate Gamma Roles

### `gamma=b`

Then:

```text
x_j*gamma=x_j*b=x_{j+1}
```

but also:

```text
x_j*gamma=A_j.
```

So:

```text
A_j=x_{j+1}.
```

This is the adjacent same-row swap recurrence role already routed in:

```text
right_b_orbit_local_repeat_roles.md
```

### `gamma=A_j`

Then:

```text
x_j*A_j=b
```

and:

```text
x_j*gamma=A_j.
```

Thus:

```text
A_j=b,
```

which is impossible in the bad-target right-`b` orbit setup because
`A_j!=b`.

### Other gamma hits

If:

```text
gamma in visible footprint or gamma in {A_r,x_r}
```

then the target-swapped edge in `H_{A_j}` attaches to an already tracked
layer.  It should be routed by the hit target.

## Fresh Pair Residual

If both:

```text
alpha,
gamma
```

avoid:

```text
visible footprint,
generated A-layer,
generated X-layer,
and the immediate recurrence/impossibility roles above,
```

then G reduces to a fresh two-target bridge-pair residual:

```text
H_{x_j}:  alpha -> A_i    carried by row b,
H_{A_j}:  gamma -> b      carried by row x_j.
```

This residual is narrower than the original X-layer hit.  It should be
attacked by iterating target-swap/ported-interval transport, not by treating G
as an `H_b` path.

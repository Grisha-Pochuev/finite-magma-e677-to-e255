# Beta-X Hit Target-Bridge Boundary

Date: 2026-06-18.

Status:

```text
boundary / beta-layer X hit, target-bridge role
```

## Purpose

This records the beta-layer hit:

```text
Beta_i=x_j.
```

It is the beta-layer analogue of the X-layer bridge, but the active source row
is `x_i`, not row `b`.

Reference:

```text
beta_layer_first_hit_boundary.md
```

## Setup

Use:

```text
Beta_i=pred_{x_i}(A_i),
x_i*Beta_i=A_i,
x_i*A_i=b,
x_i*b=x_{i+1}.
```

Assume:

```text
Beta_i=x_j.
```

Then:

```text
x_i*x_j=A_i.
```

The same row `x_j` in the generated ported cycle satisfies:

```text
x_j*A_j=b,
x_j*b=x_{j+1}.
```

## Target-A_i Edge Carried By Row x_i

Row `x_i` carries the target-`A_i` interval:

```text
x_i*x_j=A_i,
x_i*A_i=b.
```

So in `H_{A_i}`:

```text
x_j -> b
```

is carried by source row `x_i`.

This is not an `H_b` edge.  It is a two-target bridge between:

```text
A_i and b.
```

## Target Swap

Swap target:

```text
A_i -> x_j.
```

Define:

```text
delta=x_j*(A_i*x_i).
```

Then:

```text
x_i*delta=x_j,
x_i*x_j=A_i.
```

Therefore in `H_{x_j}`, row `x_i` contributes:

```text
delta -> A_i.
```

## Immediate Roles

If:

```text
delta=x_j,
```

then:

```text
x_i*x_j=A_i
```

and:

```text
x_i*delta=x_j
```

force:

```text
A_i=x_j,
```

which is a routed generated `A-X` hit.

If:

```text
delta=A_i,
```

then row `x_i` swaps:

```text
x_j <-> A_i.
```

This is a same-row recurrence boundary for row `x_i`.

Other hits of `delta` against the generated A/X layers or visible footprint
should be routed by the hit target.

## Fresh Residual

If `delta` is fresh, the `Beta_i=x_j` branch becomes a fresh target-swapped
edge:

```text
delta -> A_i
```

in `H_{x_j}`, carried by row `x_i`.

This is a precise two-target bridge residual, not a common-edge fan and not
an immediate contradiction.

The sharper package is recorded in:

```text
beta_x_bridge_pair_reversible_square_lemma.md
```

Together with the row `x_j` generated interval and its beta foot `Beta_j`,
the branch forms the reversible pair:

```text
(A_i, x_j, b)      <-> (x_j, delta, A_i),
(b, A_j, x_{j+1}) <-> (A_j, Beta_j, b).
```

Thus a fresh `delta` should be treated as part of a fresh reversible square,
not as the start of an unbounded target-swap tower.

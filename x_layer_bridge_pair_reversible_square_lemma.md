# X-Layer Bridge-Pair Reversible Square Lemma

Date: 2026-06-18.

Status:

```text
proved / G is a reversible two-target square, not a new tower
```

## Purpose

The fresh residual of the X-layer target-swap pair might look like a new
target tower.  It is not.  The two target-swapped intervals are exactly the
target-swap inverses of the original G-corner intervals.

Thus G produces a reversible two-target square.

References:

```text
x_layer_hit_target_swap_pair_lemma.md
x_layer_target_swap_pair_hit_boundary.md
target_advance_row_orbit_lemma.md
```

## Setup

Assume the X-layer hit:

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

Then the original intervals are:

```text
P=(A_i, x_j, D_i)        carried by row b,
Q=(b, A_j, x_{j+1})      carried by row x_j.
```

The target-swapped intervals are:

```text
P'=(x_j, alpha, A_i)     carried by row b,
Q'=(A_j, gamma, b)       carried by row x_j.
```

## Reversibility

Target advance of `P'` along row `b` gives:

```text
(x_j, alpha, A_i)
  -> (A_i, x_j, b*A_i)
  =  (A_i, x_j, D_i)
  =  P.
```

Target advance of `Q'` along row `x_j` gives:

```text
(A_j, gamma, b)
  -> (b, A_j, x_j*b)
  =  (b, A_j, x_{j+1})
  =  Q.
```

Conversely, target-swapping `P` at its input `x_j` recovers `P'`, and
target-swapping `Q` at its input `A_j` recovers `Q'`.

## Consequence

The G-branch:

```text
H_i=x_j
```

does not by itself generate an unbounded sequence of new target states.

After immediate `alpha/gamma` hits are routed, the fresh G residual is the
closed reversible square:

```text
P  <-> P'
Q  <-> Q'
```

with two source rows:

```text
b and x_j.
```

Therefore the remaining work in G is not "continue target-swapping".  It is to
show that a fresh reversible square cannot remain disjoint from the visible
crossed-fan footprint and the generated A/X layers, or else to record it as a
new exact residual.


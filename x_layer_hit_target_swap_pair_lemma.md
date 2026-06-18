# X-Layer Hit Target-Swap Pair Lemma

Date: 2026-06-18.

Status:

```text
proved routing lemma / two target-swapped edges for G
```

## Purpose

The X-layer hit:

```text
H_i=x_j
```

does not only give one target-swapped edge.  It gives a canonical pair of
target-swapped edges from the two rows involved:

```text
row b,
row x_j.
```

This is the natural two-target replacement for the original G-corner.

## Setup

Assume the X-layer hit:

```text
H_i=x_j.
```

Then:

```text
b*x_j=A_i.
```

The generated target-`b` edge at index `j` is:

```text
x_j*A_j=b,
x_j*b=x_{j+1}.
```

Also define:

```text
D_i=b*A_i.
```

So row `b` carries:

```text
b*x_j=A_i,
b*A_i=D_i.
```

## First Target-Swapped Edge: Row b

For the target-`A_i` edge:

```text
b*x_j=A_i,
b*A_i=D_i,
```

swap target `A_i -> x_j`.

Define:

```text
alpha=x_j*(A_i*b).
```

Then:

```text
b*alpha=x_j,
b*x_j=A_i.
```

So in `H_{x_j}`, row `b` gives:

```text
alpha -> A_i.
```

This is:

```text
x_layer_hit_target_swap_edge_lemma.md
```

## Second Target-Swapped Edge: Row x_j

For the original target-`b` edge:

```text
x_j*A_j=b,
x_j*b=x_{j+1},
```

swap target `b -> A_j`.

The target-swap foot is:

```text
gamma=A_j*(b*x_j).
```

Using the X-layer hit:

```text
b*x_j=A_i,
```

this becomes:

```text
gamma=A_j*A_i.
```

Then:

```text
x_j*gamma=A_j,
x_j*A_j=b.
```

So in `H_{A_j}`, row `x_j` gives:

```text
gamma -> b.
```

## The Pair

The X-layer hit therefore creates the target-swapped pair:

```text
H_{x_j}:  alpha -> A_i    carried by row b,
H_{A_j}:  gamma -> b      carried by row x_j,
```

where:

```text
alpha=x_j*(A_i*b),
gamma=A_j*A_i.
```

## Consequence

The G-branch is not an ordinary one-target `H_b` path.  It is a two-target
bridge pair on the targets:

```text
x_j and A_j,
```

with outputs:

```text
A_i and b.
```

The next routing split should test whether:

```text
alpha or gamma
```

hits the generated `A`/`X` layers or the visible crossed-fan footprint.

If both are fresh, G becomes a fresh two-target bridge-pair residual rather
than a local contradiction.


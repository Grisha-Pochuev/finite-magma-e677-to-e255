# Row-b A-Layer Cycle Boundary

Date: 2026-06-18.

Status:

```text
proved finite boundary / A-layer tower closure
```

## Purpose

This records what happens if the row-`b` predecessor tower of the clean
ported-matching residual keeps hitting only the generated `A`-layer.

It refines Type 1 of:

```text
row_b_tower_first_hit_role_map.md
```

## Setup

Use the clean ported-matching residual:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i).
```

Thus:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

The generated `H_b` footprint is a matching:

```text
A_i -> x_{i+1}.
```

Assume the generated `A_i` are pairwise distinct and disjoint from the orbit
labels `x_j` and from the visible crossed-fan footprint.

## A-Layer Hit

An A-layer hit is:

```text
H_i=A_j.
```

Then:

```text
b*A_j=A_i.
```

So row `b` maps one generated input to another generated input:

```text
A_j -> A_i
```

inside row `b`.

Because row `b` is a function, each generated `A_j` has at most one forward
image in the generated `A`-layer.  Because row `b` is injective, each
generated `A_i` has at most one generated predecessor.

## Finite A-Layer Closure

Suppose a row-`b` predecessor tower starting from some `A_i` never hits:

```text
the orbit layer {x_j},
the visible crossed-fan/core footprint,
or a row-b fixed point boundary,
```

and every nonfresh tower hit is an `A`-layer hit.

Then, since the generated `A`-layer on the chosen finite right-`b` orbit cycle
is finite, the row-`b` predecessor tower eventually repeats inside the
`A`-layer.

Equivalently, row `b` contains a directed cycle entirely on generated
`A`-vertices:

```text
A_{i_0} -> A_{i_1} -> ... -> A_{i_m} -> A_{i_0}
```

where each arrow is a row-`b` edge:

```text
b*A_{i_r}=A_{i_{r+1}}.
```

This cycle is disjoint from:

```text
the orbit labels x_j,
the visible crossed-fan footprint,
and the generated H_b outputs x_{j+1}.
```

under the clean residual assumptions.

## Relation To Generated H_b Edges

Each cycle vertex `A_i` also carries an `H_b` edge:

```text
A_i -> x_{i+1}
```

with source row `x_i`.

Thus the A-layer cycle is not an `H_b` cycle.  It is a row-`b` cycle on the
inputs of the generated `H_b` matching:

```text
row b cycle on A_i
plus matching edges A_i -> x_{i+1}.
```

This distinction matters: it does not by itself contradict badness of `b`,
because badness forbids `q*b=b`, not row-`b` cycles away from `b`.

## Consequence

The Type-1 first-hit branch is now reduced to:

```text
1. exits the A-layer to X / visible / fixed-point boundary;
2. or closes as a row-b A-layer cycle disjoint from the visible crossed-fan
   footprint.
```

The second case is a genuine remaining boundary.  It must be attacked using
cross-source predecessor pressure between the row-`b` A-cycle and the source
rows `x_i`, or by a target-swap argument.  It should not be treated as an
immediate `H_b` core attachment.

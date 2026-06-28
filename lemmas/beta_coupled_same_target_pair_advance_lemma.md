# Beta-Coupled Same-Target Pair Advance Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / U3 target-advance returns to known layers
```

## Purpose

This sharpens the U3 residual:

```text
beta-coupled same-target pair.
```

The pair is not an anonymous two-edge matching in a new target graph.  It is
the target-lift of a same-input split, and target advance sends it back to two
known layer edges.

## Setup

Assume the beta-A hit:

```text
Beta_i=A_j.
```

Then:

```text
x_i*A_j=A_i,
x_j*A_j=b.
```

By the same-input target-lift lemma, define:

```text
E_{i,j}=A_j*(A_i*x_i),
Beta_j=A_j*(b*x_j).
```

The lifted pair in `H_{A_j}` is:

```text
E_{i,j} -> A_i      carried by row x_i,
Beta_j  -> b        carried by row x_j.
```

Equivalently:

```text
x_i*E_{i,j}=A_j,
x_i*A_j=A_i,

x_j*Beta_j=A_j,
x_j*A_j=b.
```

## Target Advance

Advance the first lifted interval along row `x_i`:

```text
(A_j, E_{i,j}, A_i)
  -> (A_i, A_j, x_i*A_i)
  =  (A_i, A_j, b).
```

So in `H_{A_i}`:

```text
A_j -> b
```

is carried by row `x_i`.

Advance the second lifted interval along row `x_j`:

```text
(A_j, Beta_j, b)
  -> (b, A_j, x_j*b)
  =  (b, A_j, x_{j+1}).
```

So in `H_b`:

```text
A_j -> x_{j+1}
```

is exactly the generated matching edge carried by row `x_j`.

## Consequence

The U3 clean-disjoint same-target pair has only two roles:

```text
1. local collision in H_{A_j}, routed by
   same_target_pair_collision_trichotomy_lemma.md;

2. if clean-disjoint, target advance returns it to:
   H_{A_i}: A_j -> b,
   H_b:    A_j -> x_{j+1}.
```

Thus U3 is not an independent growth mechanism.  Its clean residual is a
two-target bridge between:

```text
target A_i
and
target b,
```

sharing the input `A_j`.

The next useful treatment of U3 should compare:

```text
H_{A_i}: A_j -> b
```

with the already known row-`x_i` chain:

```text
A_i -> b -> x_{i+1},
```

and the generated `H_b` matching:

```text
A_j -> x_{j+1}.
```

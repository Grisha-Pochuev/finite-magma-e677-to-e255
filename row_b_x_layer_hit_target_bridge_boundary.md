# Row-b X-Layer Hit Target-Bridge Boundary

Date: 2026-06-18.

Status:

```text
boundary / target-bridge role, not contradiction
```

## Purpose

This records Type 2 of the row-`b` predecessor-tower first-hit role map:

```text
H_i=x_j.
```

It is the case where the row-`b` predecessor tower hits an orbit/source label
rather than a generated `A` input.

Reference:

```text
row_b_tower_first_hit_role_map.md
```

## Setup

In the clean ported-matching residual:

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

Assume:

```text
H_i=x_j.
```

Then:

```text
b*x_j=A_i.
```

The same label `x_j`, as a source row in the generated ported cycle, carries:

```text
x_j*A_j=b,
x_j*b=x_{j+1}.
```

## Two-Row Corner

The X-layer hit creates the two-row corner:

```text
row b:   x_j -> A_i
row x_j: b   -> x_{j+1}
```

and row `x_j` also has:

```text
row x_j: A_j -> b.
```

So the local picture is:

```text
A_j --row x_j--> b --row x_j--> x_{j+1}
              ^
              |
            row b from x_j to A_i
```

This is not an `H_b` path.  It is a target-bridge event between the two
targets:

```text
b and A_i.
```

## Target-A_i Edge Carried By Row b

Let:

```text
D_i=b*A_i.
```

Then row `b` carries the full ported interval for target `A_i`:

```text
b*x_j=A_i,
b*A_i=D_i.
```

Equivalently:

```text
(A_i, x_j, D_i)
```

is a full ported interval with source row `b`.

The complete edge certificate for this target-`A_i` edge gives:

```text
D_i*b=pred_{A_i}(x_j),
A_i*(D_i*b)=x_j.
```

It also gives:

```text
(b*D_i)*b = A_{A_i}(D_i),
D_i*((b*D_i)*b)=A_i.
```

These are target-`A_i` bridge labels.  They are not the same as the original
target-`b` labels unless an additional hit occurs.

## Clean Residual Consequence

Under the clean matching assumptions:

```text
A_i != x_j,
A_i != x_{j+1},
A_i not in visible footprint.
```

Therefore the X-layer hit is not already one of:

```text
generated A-X hit,
right-b fixed point,
or visible attachment.
```

It must be routed by comparing two full intervals involving the same row label
`x_j` and the row `b`:

```text
row x_j at target b:    (b, A_j, x_{j+1});
row b   at target A_i:  (A_i, x_j, D_i).
```

## Consequence

The X-layer hit branch is now reduced to a two-target bridge problem:

```text
target b, source x_j
target A_i, source b
```

The next useful step is to apply target-swap / bridge-pair transport to this
two-target corner.  It should not be treated as a direct contradiction or as
ordinary `H_b` core attachment.

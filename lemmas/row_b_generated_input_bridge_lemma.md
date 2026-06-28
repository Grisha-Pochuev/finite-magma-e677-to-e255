# Row-b Generated-Input Bridge Lemma

Date: 2026-06-18.

Status:

```text
proved structural bridge / unavoidable at every generated input A_j
```

## Purpose

This isolates the unavoidable bridge at every generated input:

```text
A_j=pred_{x_j}(b).
```

It is the row-`b` / generated-row version of the W3 bridge and is the base
case of the V4-folded residual.

## Setup

Use:

```text
x_j*A_j=b,
x_j*b=x_{j+1},
H_j=pred_b(A_j),
Beta_j=pred_{x_j}(A_j).
```

Define:

```text
D_j=b*A_j.
```

Then:

```text
b*H_j=A_j,
x_j*Beta_j=A_j.
```

## Same-Input Bridge At A_j

Rows `b` and `x_j` share the input:

```text
A_j.
```

Their outputs are:

```text
row b:   A_j -> D_j,
row x_j: A_j -> b.
```

If:

```text
D_j=b,
```

then rows `b` and `x_j` share the edge:

```text
A_j -> b.
```

Otherwise this is a proper same-input two-target bridge at the generated input
`A_j`.

## Lift To H_{A_j}

The same-input lift gives exactly the beta-anchor pair:

```text
H_j    -> D_j     carried by row b,
Beta_j -> b       carried by row x_j
```

inside:

```text
H_{A_j}.
```

This is the pair used in:

```text
beta_anchor_row_b_partner_reduction_lemma.md
```

## Target Advance

If the lifted pair is clean-disjoint, target advance gives:

```text
H_{D_j}: A_j -> b*D_j,
H_b:     A_j -> x_{j+1}.
```

So the bridge is tied directly to the generated `H_b` matching edge:

```text
A_j -> x_{j+1}.
```

## Consequence

The row-b/generated bridge is unavoidable at every generated input `A_j`.

Therefore the W3 residual should be viewed as:

```text
the unavoidable bridge between rows b and x_j,
possibly plus an extra source row p through the same input A_j.
```

The next useful split is:

```text
1. D_j hits visible/A/X/H/beta layers -> route by the hit;
2. D_j=b -> common-edge fan over A_j -> b;
3. D_j fresh -> row-b successor layer from A_j must be compared with the
   generated H_b edge A_j -> x_{j+1}.
```

The fresh successor branch is reduced further by:

```text
row_b_successor_eventual_h_hit_lemma.md
```

Since row `b` is a finite permutation, the forward row-`b` orbit from `A_j`
eventually hits:

```text
H_j=pred_b(A_j).
```

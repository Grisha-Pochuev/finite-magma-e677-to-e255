# Row-b Successor H-Hit Role Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / first H-hit immediately returns to generated A-layer
```

## Purpose

This routes the first generated H-hit from:

```text
row_b_successor_eventual_h_hit_lemma.md
```

If the forward row-`b` successor chain from `A_j` hits any generated
predecessor `H_k`, then the very next row-`b` step hits `A_k`.

## Setup

Use:

```text
C_j^0=A_j,
C_j^{m+1}=b*C_j^m,
H_k=pred_b(A_k),
b*H_k=A_k.
```

Suppose the first generated H-layer hit is:

```text
C_j^m=H_k.
```

## Statement

Then:

```text
C_j^{m+1}=A_k.
```

So the row-`b` successor chain gives a row-`b` path:

```text
A_j=C_j^0 -> C_j^1 -> ... -> C_j^m=H_k -> C_j^{m+1}=A_k.
```

## Roles

### 1. `k=j`

Then the chain closes the row-`b` cycle through:

```text
H_j -> A_j.
```

This is a same-row row-`b` recurrence boundary.

### 2. `k!=j`

Then row `b` connects two generated A-layer vertices:

```text
A_j -> ... -> H_k -> A_k.
```

This is an A-layer return/cross-hit for the row-`b` successor chain.  It is
the forward analogue of the row-`b` predecessor tower A-layer hit and should
be routed with:

```text
row_b_a_layer_cycle_boundary.md
row_b_tower_first_hit_role_map.md
```

## Consequence

The W3 base split:

```text
D_j fresh
```

does not produce a new infinite successor layer.  It either hits another
watched layer earlier or returns to:

```text
generated H-layer -> generated A-layer.
```

Thus the row-b/generated bridge frontier folds back into row-b A-layer
cycle/cross-hit analysis.

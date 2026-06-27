# Row-b Successor Eventual H-Hit Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / fresh row-b successor layer must hit H-layer
```

## Purpose

This attacks the fresh case in:

```text
row_b_generated_input_bridge_lemma.md
```

where:

```text
D_j=b*A_j
```

does not immediately hit a watched layer.

The point is that `D_j` is not an independent fresh direction.  It lies on the
finite row-`b` cycle through `A_j`, whose predecessor is:

```text
H_j=pred_b(A_j).
```

## Setup

Fix a generated input:

```text
A_j=pred_{x_j}(b).
```

Define the forward row-`b` successor chain:

```text
C_j^0=A_j,
C_j^1=D_j=b*A_j,
C_j^{m+1}=b*C_j^m.
```

The predecessor of `A_j` in row `b` is:

```text
H_j=pred_b(A_j),
b*H_j=A_j.
```

## Statement

Because row `b` is a finite permutation, the row-`b` orbit of `A_j` is a
finite cycle.  Hence there is a least `L>0` such that:

```text
C_j^L=A_j.
```

Then:

```text
C_j^{L-1}=H_j.
```

Therefore any fresh row-`b` successor extension from `D_j` must eventually hit
the generated H-layer.

## Proof

By definition:

```text
b*C_j^{L-1}=C_j^L=A_j.
```

The unique predecessor of `A_j` in row `b` is `H_j`, so:

```text
C_j^{L-1}=H_j.
```

If `D_j=A_j`, this is a row-`b` fixed point boundary.  If `D_j=H_j`, the hit
is immediate.  Otherwise the first return to the watched cycle still reaches
`H_j` before returning to `A_j`.

## Consequence

The third branch in the W3 split:

```text
D_j fresh
```

is not an unbounded residual.  It becomes:

```text
row-b successor chain from A_j hits H_j,
```

unless it hits another watched layer earlier.

Thus the base row-b/generated bridge at `A_j` reduces to:

```text
1. D_j=b:
   common-edge fan over A_j -> b;

2. D_j hits watched layer:
   route by that layer;

3. D_j fresh:
   finite row-b successor chain eventually hits H_j.
```

The next useful treatment is to route the first generated H-hit of the
row-`b` successor chain.

That role is recorded in:

```text
row_b_successor_h_hit_role_lemma.md
```

If the first H-hit is `H_k`, the next row-`b` step is `A_k`.

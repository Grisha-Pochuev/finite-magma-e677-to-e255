# Source Successor Eventual Predecessor-Hit Lemma

Date: 2026-06-19.

Status:

```text
general proved / forward source orbit returns through its predecessor
```

## Purpose

This generalizes the row-`b` successor hit:

```text
row_b_successor_eventual_h_hit_lemma.md
```

to any source row.

In X3, it applies to the extra source row `p`:

```text
p*P=A_j,
p*A_j=S.
```

If `S` is fresh, the forward row-`p` orbit from `A_j` cannot remain fresh
forever.  It eventually hits `P=pred_p(A_j)`.

## General Statement

Fix any row `r` and any target/input `a`.  Let:

```text
P=pred_r(a),
r*P=a.
```

Define the forward row-`r` successor chain:

```text
C^0=a,
C^{m+1}=r*C^m.
```

Since row `r` is a finite permutation, the orbit of `a` is a finite cycle.
Let `L>0` be the least return:

```text
C^L=a.
```

Then:

```text
C^{L-1}=P.
```

## Proof

By definition:

```text
r*C^{L-1}=C^L=a.
```

The unique predecessor of `a` in row `r` is `P`, so:

```text
C^{L-1}=P.
```

## X3 Application

In X3:

```text
p*P=A_j,
p*A_j=S.
```

If the forward row-`p` chain from `A_j` is:

```text
C_p^0=A_j,
C_p^1=S,
C_p^{m+1}=p*C_p^m,
```

then it eventually hits:

```text
P=pred_p(A_j).
```

So the extra-source branch:

```text
p*A_j=S
```

is not an independent fresh successor direction.  It either hits a watched
layer earlier, or it returns to the original X3 input `P`.

## Consequence For X3

For each of the three X3 source rows:

```text
p,
x_j,
b,
```

the forward successor chain from `A_j` eventually hits the corresponding
predecessor:

```text
P,
Beta_j,
H_j.
```

Thus a clean X3 residual is really a synchronized comparison of three finite
row cycles through the same input `A_j`, not an open-ended expansion.

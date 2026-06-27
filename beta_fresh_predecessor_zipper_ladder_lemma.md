# Beta Fresh Predecessor Zipper-Ladder Lemma

Date: 2026-06-18.

Status:

```text
general proved / structure of a fresh beta-layer extension
```

## Purpose

The fresh beta-layer residual should not be treated as an anonymous new
predecessor.

Once:

```text
Beta_i=pred_{x_i}(A_i)
```

is fresh, extending backward in row `x_i` creates a whole zipper ladder.  Each
new predecessor in row `x_i` also forces a shifted edge in the preceding row
of the chain.

## Setup

Fix an index `i` in the clean right-`b` orbit:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
Beta_i=pred_{x_i}(A_i).
```

Define a backward row-`x_i` chain:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m) for m>=1.
```

Then for all `m>=-1` where the expression is defined:

```text
x_i*Z_i^m=Z_i^{m-1}.
```

The known start is:

```text
x_i*A_i=b,
x_i*Beta_i=A_i.
```

## Zipper Recursion

For every `m>=0`, apply the edge predecessor triangle to:

```text
x_i*Z_i^m=Z_i^{m-1}.
```

The predecessor of `Z_i^m` in row `x_i` is:

```text
Z_i^{m+1}=Z_i^m*(Z_i^{m-1}*x_i).
```

The same edge also gives the shifted row edge:

```text
Z_i^{m-1}*(Z_i^{m-2}*x_i)=Z_i^m.
```

So each step of the row-`x_i` predecessor chain forces:

```text
row x_i:       Z_i^{m+1} -> Z_i^m -> Z_i^{m-1},
row Z_i^{m-1}: (Z_i^{m-2}*x_i) -> Z_i^m.
```

## First Instances

For `m=0`:

```text
Z_i^1=A_i*(b*x_i)=Beta_i,
row b: (x_{i+1}*x_i)=H_i -> A_i.
```

For `m=1`:

```text
Z_i^2=Beta_i*(A_i*x_i),
row A_i: (b*x_i) -> Beta_i.
```

For `m=2`:

```text
Z_i^3=Z_i^2*(Beta_i*x_i),
row Beta_i: (A_i*x_i) -> Z_i^2.
```

Thus the fresh beta extension starts with:

```text
row x_i: Beta_i -> A_i -> b -> x_{i+1},
row A_i: b*x_i -> Beta_i,
row Beta_i: A_i*x_i -> Z_i^2.
```

## Consequence

A fresh beta-layer extension is not one-dimensional.  It carries two linked
families:

```text
1. the backward row-x_i chain Z_i^m;
2. the shifted columns Z_i^{m-2}*x_i feeding the rows Z_i^{m-1}.
```

Therefore the next boundary should track first hits of both:

```text
Z_i^m
and
Z_i^{m-2}*x_i.
```

If both families stay fresh, finiteness can only close a same-row cycle in
row `x_i`, together with its zipper-ladder side edges.

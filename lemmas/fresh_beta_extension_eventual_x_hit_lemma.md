# Fresh Beta Extension Eventual X-Hit Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / fresh beta extension must hit generated X layer
```

## Purpose

This corrects the apparent residual:

```text
fresh beta-layer extension.
```

For a fixed row `x_i`, the predecessor chain is not an independent infinite
or disjoint finite object.  Since row `x_i` is a permutation, the backward
chain from `A_i` lies on the same row cycle as:

```text
A_i -> b -> x_{i+1}.
```

Therefore a completely fresh beta extension must eventually hit the generated
X-layer.

## Setup

Use:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m).
```

Then:

```text
x_i*Z_i^m=Z_i^{m-1}
```

for all displayed `m>=-1`.

## Statement

Because row `x_i` is a finite permutation, the backward orbit of `A_i` under
row `x_i` is periodic.  Hence there is a least `L>0` such that:

```text
Z_i^L=A_i.
```

If `Beta_i` is fresh relative to the watched set:

```text
visible footprint,
generated A-layer,
generated X-layer,
generated H-layer,
known beta feet,
```

then:

```text
L>=3,
Z_i^{L-2}=x_{i+1},
Z_i^{L-1}=b,
Z_i^L=A_i.
```

So before the chain returns to `b` or `A_i`, it hits:

```text
x_{i+1},
```

which is a generated X-layer vertex.

## Proof

Finiteness and bijectivity of row `x_i` put `A_i` on a finite row cycle.
The sequence:

```text
Z_i^1, Z_i^2, ...
```

is exactly the backward traversal of that same cycle from `A_i`.

Let `L>0` be the first return:

```text
Z_i^L=A_i.
```

Applying row `x_i` gives:

```text
Z_i^{L-1}=x_i*Z_i^L=x_i*A_i=b.
```

If `L>=2`, applying row `x_i` once more gives:

```text
Z_i^{L-2}=x_i*b=x_{i+1}.
```

If `L=1`, then:

```text
Beta_i=A_i,
```

a generated A-hit.  If `L=2`, then:

```text
Beta_i=b,
```

a visible target hit.  In the fresh beta residual both are excluded, so
`L>=3` and the displayed X-hit occurs.

## Consequence

There is no clean beta extension that stays forever disjoint from the watched
layers.  The exact remaining case is:

```text
the first watched hit of the beta zipper is a deeper generated X-hit
Z_i^m=x_j,
```

with the guaranteed terminal possibility:

```text
Z_i^{L-2}=x_{i+1}.
```

The next useful target is therefore a generalized beta-X hit lemma for:

```text
Z_i^m=x_j
```

not another attempt to extend the beta chain.

That route is recorded in:

```text
deep_beta_x_hit_reduction_lemma.md
```

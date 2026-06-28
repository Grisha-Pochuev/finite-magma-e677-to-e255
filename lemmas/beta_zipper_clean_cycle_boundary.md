# Beta Zipper Clean Cycle Boundary

Date: 2026-06-18.

Status:

```text
corrected boundary / pure disjoint Z-cycle is replaced by eventual X-hit
```

## Purpose

This file originally recorded the apparent residual when a fresh beta zipper
does not first create a shifted-column split.

The sharper correction is:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

Because row `x_i` is a finite permutation, the backward chain from `A_i`
eventually returns to the already known row cycle segment:

```text
A_i -> b -> x_{i+1}.
```

So a clean beta zipper cannot remain disjoint from the watched layers; it
must eventually hit the generated X-layer.

## Setup

Use:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m),
T_i^m=Z_i^{m-2}*x_i.
```

Assume no watched hit occurs in:

```text
Z_i^m
or
T_i^m
```

before the first main-chain repeat:

```text
Z_i^r=Z_i^s,
r>s>=1.
```

Assume also that no shifted-column repeat occurs before this `Z` repeat.

## Cycle

Let:

```text
L=r-s.
```

Then row `x_i` contains the cycle:

```text
Z_i^s <- Z_i^{s+1} <- ... <- Z_i^{r-1} <- Z_i^r=Z_i^s.
```

Equivalently:

```text
x_i*Z_i^{m+1}=Z_i^m
```

cyclically on the `L` displayed vertices.

## Side Zipper Edges

For each cycle index, the zipper side edge is:

```text
row Z_i^{m-1}: T_i^m -> Z_i^m.
```

Because:

```text
Z_i^{m+L}=Z_i^m,
```

the shifted side columns have the same period:

```text
T_i^{m+L}=T_i^m.
```

If no shifted-column repeat occurred before the first `Z` repeat, then the
side columns:

```text
T_i^s, T_i^{s+1}, ..., T_i^{r-1}
```

are pairwise distinct during the first cycle.

## Corrected Residual

The clean pure beta zipper cycle should now be read as:

```text
the predecessor chain follows the row-x_i cycle until its first watched hit,
and if no earlier hit occurs that hit is x_{i+1}.
```

Thus the next active branch is a deeper beta-X hit:

```text
Z_i^m=x_j.
```

## Next Use

Do not use this file as a final residual that is independent of the generated
X-layer.

# Row-b Predecessor-Tower Dichotomy Boundary

Date: 2026-06-18.

Status:

```text
proved finite dichotomy / boundary, not contradiction
```

## Purpose

After the clean ported-matching residual, the remaining coupling is through
row `b`:

```text
b*H_i=A_i.
```

This file records the finite predecessor-tower dichotomy for that row-`b`
layer.  It does not prove contradiction; it narrows the remaining hard branch.

References:

```text
clean_ported_matching_predecessor_layer_boundary.md
edge_predecessor_triangle_lemma.md
```

## Setup

Fix a bad target `b`.  In the clean ported-matching residual, we have:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i),
```

so:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

The generated `H_b` footprint is a matching:

```text
A_i -> x_{i+1},
```

and the row-`b` predecessor layer is:

```text
H_i -> A_i.
```

## Canonical Tower

For each `i`, define the row-`b` predecessor tower:

```text
B_i^{0}=A_i,
B_i^{1}=H_i=pred_b(A_i),
B_i^{m+1}=pred_b(B_i^m).
```

Equivalently:

```text
b*B_i^{m+1}=B_i^m.
```

The first nontrivial step can be written using the edge predecessor triangle:

```text
B_i^{2}=H_i*(A_i*b),
b*B_i^{2}=H_i.
```

This is just the usual predecessor operation in row `b`, but the formula is
useful because it is an explicit E677 term.

## Injectivity Consequence

Because row `b` is a permutation:

```text
B_i^m=B_j^m  <=>  A_i=A_j
```

for every fixed tower depth `m`.

Thus, if the `A_i` are pairwise distinct on the clean matching footprint, then
every equal-depth predecessor layer:

```text
{B_i^m}
```

is also pairwise distinct.

## First-Hit Dichotomy

Let the watched set be:

```text
W = visible footprint ∪ {x_j} ∪ {A_j}.
```

Here the visible footprint includes the selected crossed-fan data:

```text
a,b,c,d,u,v,h,k,t,ell
```

or any explicitly retained core/corridor footprint in the current application.

Then exactly one of the following holds.

### 1. First Hit

There are minimal indices:

```text
m>=1, i
```

such that:

```text
B_i^m in W.
```

This is a real predecessor-layer event.  It should be split by the hit target:

```text
B_i^m in {x_j}       -> row-b tower hits an orbit/source-output label;
B_i^m in {A_j}       -> row-b tower hits a generated H_b input;
B_i^m in visible     -> row-b tower attaches to crossed-fan/core footprint.
```

The local case:

```text
B_i^1=A_i
```

is the row-`b` fixed point boundary already listed as `H_i=A_i`.

### 2. No Hit Before Closure

For every `i`, the row-`b` predecessor tower starting at `A_i` closes inside a
row-`b` permutation cycle before hitting `W`.

In this case the clean residual has separated row-`b` cycles:

```text
... -> B_i^2 -> B_i^1=H_i -> B_i^0=A_i -> ...
```

disjoint from the generated orbit labels, the generated `H_b` inputs of other
branches, and the visible crossed-fan footprint.

This is not a contradiction by itself.  It is the exact row-`b` independent
cycle boundary.

## Cross-Tower Hit

If:

```text
B_i^m=B_j^n
```

with possibly different depths `m,n`, then the two `A`-inputs lie in the same
row-`b` cycle with offset:

```text
B_i^{m-n}=A_j
```

or the symmetric relation after applying row `b` enough times.

So unequal-depth tower collisions are not neutral: they are exactly hits of
one generated `A_j` by another row-`b` predecessor tower, hence belong to
case 1.

## Consequence

The clean external bridge has now been reduced further:

```text
right-b ported cycle
=> generated H_b footprint trichotomy
=> clean two-layer matching residual
=> row-b predecessor-tower first-hit dichotomy.
```

The next proof should classify the first-hit cases.  If all first hits are
routed away, the only remaining object is a family of row-`b` cycles disjoint
from the visible crossed-fan footprint and from the generated ported-cycle
labels.  That independent-cycle boundary must then be attacked with a
cross-source predecessor fan or target-swap argument, not by another local
one-step hit.

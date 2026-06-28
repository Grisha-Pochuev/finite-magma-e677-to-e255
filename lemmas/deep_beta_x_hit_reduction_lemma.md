# Deep Beta-X Hit Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / deeper beta zipper X-hit routes to reversible square
```

## Purpose

This generalizes:

```text
beta_x_bridge_pair_reversible_square_lemma.md
```

from the first beta foot:

```text
Beta_i=x_j
```

to any deeper beta zipper hit:

```text
Z_i^m=x_j.
```

This is the hit guaranteed by:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

if no earlier watched hit occurs.

## Setup

Use the beta zipper:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m).
```

Assume for some `m>=1`:

```text
Z_i^m=x_j.
```

Define:

```text
U=Z_i^{m-1},
V=Z_i^{m-2}.
```

Then row `x_i` has:

```text
x_i*x_j=U,
x_i*U=V.
```

Row `x_j` has the generated interval:

```text
x_j*A_j=b,
x_j*b=x_{j+1}.
```

## Target Swap

For the row `x_i` interval:

```text
(U, x_j, V),
```

swap target:

```text
U -> x_j.
```

Define:

```text
Delta=x_j*(U*x_i).
```

Then:

```text
x_i*Delta=x_j,
x_i*x_j=U.
```

So in `H_{x_j}`:

```text
Delta -> U
```

is carried by row `x_i`.

For row `x_j`, use:

```text
Beta_j=pred_{x_j}(A_j)=A_j*(b*x_j)=A_j*x_{j+1}.
```

Then the generated target-swap interval is:

```text
(A_j, Beta_j, b).
```

## Reversible Square

The two original intervals are:

```text
P=(U, x_j, V)             carried by row x_i,
Q=(b, A_j, x_{j+1})       carried by row x_j.
```

The target-swapped intervals are:

```text
P'=(x_j, Delta, U)        carried by row x_i,
Q'=(A_j, Beta_j, b)       carried by row x_j.
```

Target advance of `P'` along row `x_i` gives:

```text
(x_j, Delta, U)
  -> (U, x_j, x_i*U)
  =  (U, x_j, V)
  =  P.
```

Target advance of `Q'` along row `x_j` gives:

```text
(A_j, Beta_j, b)
  -> (b, A_j, x_j*b)
  =  (b, A_j, x_{j+1})
  =  Q.
```

Therefore:

```text
P  <-> P',
Q  <-> Q'.
```

## Immediate Roles

If `Delta` hits a watched layer, route by that hit.

If:

```text
Delta=x_j,
```

then:

```text
x_i*Delta=x_j
and
x_i*x_j=U
```

force:

```text
U=x_j,
```

which is a main `Z` repeat / generated X hit one level earlier.

If:

```text
Delta=U,
```

then row `x_i` swaps:

```text
x_j <-> U.
```

This is a same-row recurrence boundary for row `x_i`.

If `Beta_j` routes by the beta first-hit split, use:

```text
beta_layer_reduction_lemma.md
```

If both `Delta` and `Beta_j` are fresh, the result is a fresh reversible
square anchored at `Beta_j`, hence part of the beta-anchored square residual:

```text
fresh_reversible_square_beta_anchor_lemma.md
```

## Consequence

The guaranteed deeper X-hit in a fresh beta zipper does not create a new kind
of obstruction.  It reduces to:

```text
1. watched-layer hit;
2. row-x_i recurrence;
3. beta first-hit routing at Beta_j;
4. beta-anchored reversible square.
```

Thus the fresh beta extension has been converted back into the already known
second-stage residual types.

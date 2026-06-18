# Generated-Input Cross-Source Pressure Lemma

Date: 2026-06-18.

Status:

```text
general proved / pressure tool for clean matching residual
```

## Purpose

The clean two-layer matching residual still has one local pressure source at
each generated input `A_i`.

At the same pivot `A_i`, compare:

```text
source row b
source row x_i
```

using the cross-source predecessor fan.

References:

```text
cross_source_predecessor_fan_lemma.md
clean_ported_matching_predecessor_layer_boundary.md
```

## Setup

Fix a bad target `b`.  In the right-`b` ported-transition chain:

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

Define the predecessor of `A_i` in row `x_i`:

```text
Beta_i=pred_{x_i}(A_i).
```

By the edge predecessor triangle applied to:

```text
x_i*A_i=b,
```

we have:

```text
Beta_i=A_i*(b*x_i),
x_i*Beta_i=A_i.
```

## Statement

At the pivot `A_i`, the two source rows `b` and `x_i` give a cross-source
predecessor fan in row `A_i`:

```text
A_i*((b*A_i)*b)=H_i,
A_i*((x_i*A_i)*x_i)=Beta_i.
```

Since:

```text
x_i*A_i=b,
```

the second column simplifies to:

```text
(x_i*A_i)*x_i=b*x_i,
```

so:

```text
A_i*(b*x_i)=Beta_i.
```

Thus row `A_i` contains the pressure pair:

```text
A_i*((b*A_i)*b)=H_i,
A_i*(b*x_i)=Beta_i.
```

## Equality Criterion

Because row `A_i` is injective:

```text
H_i=Beta_i
<=>
(b*A_i)*b = b*x_i.
```

If:

```text
H_i!=Beta_i,
```

then row `A_i` has two distinct occupied outputs:

```text
H_i,
Beta_i.
```

## Use In The Clean Matching Residual

The row-`b` predecessor layer tracks:

```text
H_i -> A_i
```

in row `b`.

This lemma adds a second predecessor comparison at the same generated input:

```text
Beta_i -> A_i
```

in row `x_i`.

So an apparently independent row-`b` A-layer cycle is not isolated.  Every
vertex `A_i` on that cycle also carries a row-`A_i` pressure pair comparing:

```text
the row-b predecessor H_i
with the row-x_i predecessor Beta_i.
```

The next useful split for the independent row-`b` cycle boundary is:

```text
1. Beta_i hits the generated A/X/visible footprint;
2. Beta_i=H_i, giving the column coupling (b*A_i)*b=b*x_i;
3. Beta_i is fresh, extending a second predecessor layer.
```


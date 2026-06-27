# Cross-Source Predecessor Fan Lemma

Date: 2026-06-07.

Status:

```text
general proved E677 consequence / new coupling tool
```

Purpose:

```text
Couple the predecessor cycles of different left rows at the same element.
This is the missing kind of relation after the paired-chain audit.
```

## General Statement

For any elements `x` and `a` in a finite E677 magma:

```text
pred_a(x)=x*((a*x)*a),
```

where:

```text
pred_a(x)=L_a^{-1}(x).
```

Proof: E677 with variables `x,a` gives:

```text
x=a*(x*((a*x)*a)).
```

Since row `a` is a permutation, its unique preimage of `x` is:

```text
x*((a*x)*a).
```

Thus every source row `a` contributes one forced edge in the same row `x`:

```text
x*((a*x)*a)=pred_a(x).
```

For two source rows `a` and `b`, row `x` therefore contains the predecessor
fan:

```text
x*((a*x)*a)=pred_a(x)
x*((b*x)*b)=pred_b(x).
```

Because row `x` is injective:

```text
pred_a(x)=pred_b(x)
<=>
(a*x)*a=(b*x)*b.
```

This is a genuine coupling between the cycles of rows `a` and `b`.

## Application At The Offset Pivot

Use:

```text
t=r_2
b_2*0=t
b_3*t=b_4.
```

The predecessor of `t` in row `b_2` is:

```text
pred_{b_2}(t)=0.
```

The predecessor of `t` in row `b_3` is:

```text
pred_{b_3}(t)=c_{-1}.
```

Therefore row `t` contains:

```text
t*((b_2*t)*b_2)=0
t*((b_3*t)*b_3)=c_{-1}.
```

Using `b_3*t=b_4`, this is:

```text
t*z_t=0
t*(b_4*b_3)=c_{-1},
```

the known row-`t` pressure pair.

The fan formulation explains its meaning:

```text
the two columns encode the predecessors of the same pivot t
in the two source-row cycles.
```

In particular:

```text
c_{-1}=0
<=>
(b_2*t)*b_2=b_4*b_3.
```

So the backward-zero trap is exactly equality of the two predecessor columns
at the pivot.

## Application At Any Cross-Hit

If an element `x` belongs to both source-row cycles, then:

```text
pred_{b_2}(x)=A_{i-1}
pred_{b_3}(x)=B_{m-1}
```

for suitable positions `i,m`, and the fan gives:

```text
x*((b_2*x)*b_2)=A_{i-1}
x*((b_3*x)*b_3)=B_{m-1}.
```

Thus:

```text
A_{i-1}=B_{m-1}
<=>
(b_2*x)*b_2=(b_3*x)*b_3.
```

This replaces the vague "column coupling" role by a precise equality of
cross-source predecessor columns.

## Remaining Target

The paired-cycle problem is now:

```text
Can the row-b_2 cycle containing 0 -> t and the row-b_3 cycle containing
t -> b_4 close while the predecessor fan at every common point remains
nondegenerate?
```

The next useful step is to propagate the fan equality/inequality through one
source-row step and test whether the special initial fan at `t` can return
consistently after both cycles close.

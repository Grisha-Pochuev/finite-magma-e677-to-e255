# Right-b Orbit First-Repeat Fan Lemma

Date: 2026-06-18.

Status:

```text
general proved / finite-repeat pressure lemma
```

## Setup

Fix a bad target `b`.  Let:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
x_i*A_i=b.
```

So row `x_i` carries the `H_b` edge:

```text
A_i -> x_{i+1}.
```

Assume the right-`b` orbit has a first repeat:

```text
x_i=x_j=v,
0<=i<j.
```

## Case 1: Internal Repeat, `i>0`

Let:

```text
y=x_{i-1},
z=x_{j-1}.
```

Then:

```text
y*b=v,
z*b=v.
```

The rows `y` and `z` are distinct.  Otherwise `x_{i-1}=x_{j-1}` would be an
earlier repeat than `x_i=x_j`.

Thus the repeat creates an incoming common-edge fan:

```text
y*b=v,
z*b=v,
y!=z.
```

Their `H_b` inputs are:

```text
A_{i-1}=pred_y(b),
A_{j-1}=pred_z(b).
```

These are distinct.  If:

```text
A_{i-1}=A_{j-1},
```

then rows `y` and `z` contain the same ordered two-step interval:

```text
A_{i-1} -> b -> v,
```

so two-step source reconstruction forces `y=z`, contradiction.

Therefore, in `H_b`, the first repeat gives two distinct incoming edges:

```text
A_{i-1} -> v,
A_{j-1} -> v.
```

The common-edge fan over the shared edge `b -> v` has common hub:

```text
pred_v(b)=A_i,
```

and the canonical transport edge indexed by row `v` is:

```text
A_i -> x_{i+1}.
```

## Case 2: Return To The Start, `i=0`

Then:

```text
x_j=x_0=a,
z=x_{j-1},
z*b=a.
```

In the proper crossed-fan setup, the selected incoming rows already satisfy:

```text
r*b=a,
s*b=a.
```

If `z` is distinct from `r,s`, the repeat enlarges the incoming side to at
least a triple incoming fan:

```text
r*b=a,
s*b=a,
z*b=a.
```

If `z` equals one of `r,s`, the orbit has hit the visible selected source
footprint and is routed as a visible-hit case.

## Consequence

A first repeat of the right-`b` orbit is not a harmless isolated closure.

It gives one of:

```text
1. a fresh incoming common-edge fan at the repeated vertex v;
2. a triple incoming fan at the original crossed vertex a;
3. a visible-source hit already routed out of the clean residual.
```

In the internal case, the new fan also carries the standard transport edge:

```text
pred_v(b)=A_i -> v*b=x_{i+1}.
```

This is exactly the incoming-branch transport form used in the bad-target core
fan reduction.

## Use In The Clean External-Bridge Residual

The clean external bridge can now be reduced further:

```text
right-b orbit first repeat
=> new incoming branch fan or enlarged original incoming fan.
```

The remaining proof obligation is to show that this newly created fan cannot
close independently without producing a routed visible hit, repeated full
ported interval, or side attachment.

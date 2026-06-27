# Fixed-Source Zero Descent Lemma

Date: 2026-06-08.

Status:

```text
general proved
```

Purpose:

```text
Explain the common forced zero cell behind the two far tips in the u=b_3 fan.
```

## Statement

Assume:

```text
x*0=x
x*x=c.
```

Then:

```text
c*x=0*c
x*(0*c)=0.
```

## Proof

The two consecutive row-`x` edges:

```text
0 -> x -> c
```

give the source-orbit ladder:

```text
x*(c*x)=0.
```

Write:

```text
h=c*x.
```

Thus:

```text
x*h=0.
```

Apply the inverse edge chain to this zero edge.  Since:

```text
x*0=x,
```

it gives:

```text
x*x=pred_0(h).
```

Using `x*x=c`:

```text
c=pred_0(h).
```

Equivalently:

```text
h=0*c.
```

Therefore:

```text
c*x=0*c
x*(0*c)=0.
```

## Bad-Cycle Form

If:

```text
c=b_j,
```

then:

```text
0*c=b_{j-1}.
```

Hence:

```text
b_j*x=b_{j-1}
x*b_{j-1}=0.
```

So any occupied tip `x*x=b_j` descends one step along the bad row-`0` cycle
and creates a zero edge in row `x`.

## Application To The u=b_3 Fan

In:

```text
bad_tail_u_equals_s_fan_lemma.md
```

we have:

```text
P*0=P
P*P=C.
```

Therefore:

```text
C*P=0*C
P*(0*C)=0.
```

For the two remaining size-9 tips:

```text
C=b_7 -> b_7*P=b_6 and P*b_6=0;
C=b_6 -> b_6*P=b_5 and P*b_5=0.
```

These are exactly the common forced zero cells observed in the branch
diagnostics.

## Significance

The far-tip closures are not isolated numeric events.  Every occupied
self-tip:

```text
x*0=x
x*x=b_j
```

creates the two-edge descent:

```text
b_j*x=b_{j-1}
x*b_{j-1}=0.
```

The remaining work is to combine this zero descent with the other active row
segments, rather than split `x*x` numerically.

That combination is packaged in:

```text
self_containing_fan_spine_lemma.md
```

It extends the zero descent to the row-`x` spine:

```text
e -> h -> 0 -> x -> c.
```

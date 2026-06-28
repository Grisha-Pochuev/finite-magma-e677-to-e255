# Two-Step Source Reconstruction Lemma

Date: 2026-06-07.

Status:

```text
general proved
```

Purpose:

```text
Extract the missing cross-source coupling behind the double-interval method.
```

## Statement

Let a row `p` contain two consecutive edges:

```text
p*a=b
p*b=c.
```

Then the source `p` is determined by the ordered interval:

```text
a -> b -> c.
```

More precisely:

```text
p=pred_c(pred_b(a)),
```

where:

```text
pred_y(x)=x*((y*x)*y)
```

is the unique predecessor of `x` in row `y`.

Consequently, two distinct rows cannot contain the same ordered two-step
interval:

```text
p*a=b, p*b=c,
q*a=b, q*b=c
=> p=q.
```

## Proof

Apply E677 with:

```text
x=b
y=p.
```

It gives:

```text
b=p*(b*((p*b)*p)).
```

Since:

```text
p*a=b
p*b=c,
```

and row `p` is injective, we obtain:

```text
a=b*(c*p).
```

Therefore:

```text
c*p=pred_b(a),
```

and then:

```text
p=pred_c(pred_b(a)).
```

The right side depends only on `a,b,c`, so the source row is unique.

## Interval-Fan Form

Fix `a` and `b`.  Among all rows satisfying:

```text
p*a=b,
```

the values:

```text
p*b
```

are pairwise distinct.

Equivalently:

```text
p*a=q*a=b
and
p*b=q*b
=> p=q.
```

Thus a common first edge creates an injective fan at the next input.

## Zero-Triangle Form

Fix `s` and define:

```text
B=pred_0(s).
```

If:

```text
x*s=0
r=x*0,
```

then the source reconstruction formula gives:

```text
x=pred_r(B).
```

Equivalently, the inverse edge chain gives:

```text
r*x=B.
```

Hence, for fixed `s`, the map:

```text
x -> x*0
```

is injective on the set of zero sources:

```text
{x : x*s=0}.
```

In particular:

```text
x*s=y*s=0
x*0=y*0
=> x=y.
```

## Relevance To The Main Frontier

This is an explicit reconstruction upgrade of the earlier collision-separation
identity recorded from Lemma 13.1(iii).  The older form said that a common edge
forces distinct next outputs and a twisted equality.  The present form shows
why: the complete ordered two-step interval reconstructs its source row.

It does not by itself prove the No-Free-Tail Lemma, because two closed source
cycles may meet at one point while using different neighboring points.
However, it rules out every attempted closure in which two active rows acquire
the same complete adjacent interval.

It also turns every zero triangle:

```text
x*s=0
r=x*0
r*x=B
```

from a three-edge picture into a uniqueness statement:

```text
the return value r uniquely determines the zero source x.
```

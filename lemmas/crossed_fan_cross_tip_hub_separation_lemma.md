# Crossed-Fan Cross-Tip Hub Separation Lemma

Date: 2026-06-18.

Status:

```text
general proved
```

## Setup

Fix distinct `a,b`.  Suppose there is a crossed fan:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

The common-edge fan lemma gives the two common hubs:

```text
h=c*p=d*q=pred_b(a),   b*h=a,
k=u*r=v*s=pred_a(b),   a*k=b.
```

## Statement

If the two hubs coincide:

```text
h=k,
```

then no outgoing forward tip can coincide with an incoming forward tip:

```text
{c,d} ∩ {u,v} = empty.
```

Equivalently, any cross-tip collision forces:

```text
h != k.
```

## Proof

It is enough to prove one representative case; the others are the same by
renaming rows.

Assume:

```text
c=u,
h=k.
```

From the fan certificates:

```text
c*p=h,
u*r=k.
```

Since `c=u` and `h=k`, this becomes:

```text
c*p=c*r.
```

Row `c` is injective, so:

```text
p=r.
```

But then the same row would satisfy both:

```text
p*a=b,
r*b=a,
```

and, because `p=r`,

```text
p*b=a.
```

Together with `p*b=c` this gives `c=a`.  Also `r*a=u` and `p*a=b` give
`u=b`.  Since `c=u`, we get:

```text
a=b,
```

contradicting the assumption that `a` and `b` are distinct.

Thus `c=u` is impossible when `h=k`.  The cases `c=v`, `d=u`, and `d=v` are
identical:

```text
c=v and h=k -> c*p=v*s -> p=s;
d=u and h=k -> d*q=u*r -> q=r;
d=v and h=k -> d*q=v*s -> q=s.
```

Each gives the same contradiction.

## Use In The Proper Bad-Target Crossed-Fan Frontier

In the proper bad-target crossed-fan case, the swap-row degeneracy has already
been separated.  This lemma gives the next split:

```text
1. h=k:
   the four tips c,d,u,v are cross-disjoint;

2. some cross-tip collision:
   necessarily h!=k.
```

So the difficult proper case cannot mix hub equality with cross-tip collision.

## Diagnostic Check

The saturation diagnostic agrees with the proof.  With extra assumptions
`c=u` and `h=k`, the bounded closure collapses all selected rows and tips:

```text
tools/crossed_double_fan_saturation.js 4 c=u h=k

p == q: true
p == r: true
p == s: true
c == d: true
u == v: true
h == k: true
```

This computation is only a check; the proof above uses just the already proved
fan certificates and row injectivity.

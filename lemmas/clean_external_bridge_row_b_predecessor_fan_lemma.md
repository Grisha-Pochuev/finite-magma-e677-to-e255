# Clean External-Bridge Row-b Predecessor-Fan Lemma

Date: 2026-06-18.

Status:

```text
general proved / clean residual routing lemma
```

## Setup

Work in the clean external-bridge residual of a bad-target proper crossed fan.

Use:

```text
h=pred_b(a),   b*h=a,
k=pred_a(b),   a*k=b,
t=a*b,
ell=t*a=pred_b(k).
```

The row-a bridge edge is:

```text
a*k=b,
a*b=t.
```

The second certificate gives:

```text
b*ell=k.
```

## Statement

In the clean residual, row `b` contains two distinct predecessor arrows:

```text
b*h=a,
b*ell=k,
```

with:

```text
h!=ell,
a!=k.
```

Thus the clean external bridge creates a genuine row-`b` predecessor fan
between the old crossed vertex `a` and the new bridge source `k`.

## Proof

The first arrow:

```text
b*h=a
```

is part of the original crossed-fan certificate, where:

```text
h=pred_b(a).
```

The row-a bridge edge certificate gives:

```text
ell=t*a=pred_b(k),
b*ell=k.
```

In the clean residual:

```text
k!=a.
```

Since row `b` is injective, `b*h=a` and `b*ell=k` with `a!=k` imply:

```text
h!=ell.
```

Equivalently, if `h=ell`, row `b` injectivity would force `a=k`, which is a
routed attachment case and not part of the clean residual.

## Relation To Cross-Source Predecessor Fan

This is the row-`b` instance of the cross-source predecessor fan:

```text
pred_p(b)=a,
pred_a(b)=k.
```

For source rows `p` and `a`, row `b` contains:

```text
b*((p*b)*p)=a,
b*((a*b)*a)=k.
```

Since:

```text
p*b=c,
a*b=t,
```

the two columns are:

```text
c*p=h,
t*a=ell.
```

So the clean residual forces the predecessor columns:

```text
h != ell.
```

The three-source version using `p,q,a` is recorded in:

```text
clean_external_bridge_three_source_predecessor_fan_lemma.md
```

## Use

The next proof step should compare this row-`b` predecessor fan:

```text
h -> a,
ell -> k
```

with the original crossed-fan hubs:

```text
h=pred_b(a),
k=pred_a(b).
```

If the pair `(h,ell)` later repeats or collides with the visible two-target
footprint, two-step reconstruction or one of the routed attachment cases
should close the branch.

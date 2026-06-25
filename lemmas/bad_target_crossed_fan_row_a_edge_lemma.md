# Bad-Target Crossed-Fan Row-a Edge Lemma

Date: 2026-06-18.

Status:

```text
general proved / bridge-edge routing lemma
```

## Setup

Fix a bad target `b`.  In a crossed-fan configuration, suppose:

```text
r*b=a,
r*a=u,
s*b=a,
s*a=v.
```

The common-edge fan for the pair `(b,a)` gives the common hub:

```text
k=u*r=v*s=pred_a(b),
a*k=b.
```

## Statement

Row `a` always gives a genuine edge in `H_b`:

```text
a*k=b,
a*b=t,
```

so:

```text
k -> t
```

is an `H_b` edge carried by row `a`.

Moreover:

```text
k != b,
t != b.
```

## Proof

The equality:

```text
a*k=b
```

is exactly the statement that, for target `b`, row `a` has input:

```text
A_b(a)=k.
```

Its output is:

```text
R_b(a)=a*b=t.
```

Since `b` is bad, no row sends `b` to `b`.  In particular:

```text
a*b!=b,
```

so:

```text
t!=b.
```

If `k=b`, then `a*k=a*b=b`, contradicting the same badness condition.
Therefore:

```text
k!=b.
```

Thus row `a` contributes a real `H_b` edge:

```text
k -> t.
```

## Important Boundary

This edge is not automatically a side attachment to the original crossed-fan
component at `a`.  The hub `k=pred_a(b)` is a bridge vertex for the target pair
`{a,b}`; it need not already be an endpoint of one of the selected `H_b` edges
at `a`.

So the correct use is:

```text
if k lies on the active H_b corridor/core, row a supplies a side incidence;
otherwise it supplies an external bridge edge that must be tracked by the
two-target relay state.
```

## Equal-Hub Specialization

If the two hubs coincide:

```text
h=k,
```

then the same edge is:

```text
h -> a*b
```

in `H_b`.  This is the precise content behind the equal-hub routing lemma.  It
should not be described as a side attachment unless `h` is known to lie in the
active `H_b` corridor.

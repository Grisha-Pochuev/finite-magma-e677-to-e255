# Bicyclic Core Junction Lemma

Date: 2026-06-09.

Status:

```text
general proved / refinement of the core-fan reduction
```

## Statement

Use the bicyclic core forced by:

```text
bad_target_core_fan_lemma.md
```

Choose a core vertex `v` of degree at least `3`. Then one of two structural
types occurs.

### Type A: triple core fan

At least three core incidences have the same orientation at `v`.

Outgoing form:

```text
p_i*v=b
p_i*b=c_i
```

for three distinct sources `p_i`, with pairwise distinct tips `c_i`.

Incoming form:

```text
p_i*a_i=b
p_i*b=v
```

for three distinct sources `p_i`, with pairwise distinct backward feet
`a_i`.

### Type B: mixed `2+1` core junction

There are two core incidences in one direction and at least one in the
opposite direction.

Outgoing-majority form:

```text
p*v=b, p*b=c
q*v=b, q*b=d
r*a=b, r*b=v
```

where:

```text
p!=q
c!=d.
```

Incoming-majority form:

```text
p*a=b, p*b=v
q*e=b, q*b=v
r*v=b, r*b=c
```

where:

```text
p!=q
a!=e.
```

All displayed graph edges lie in the same cycle core.

## Proof

At `v`, classify every core incidence as incoming or outgoing.

If one orientation occurs at least three times, Type A holds.

Otherwise, because the total degree is at least three, one orientation occurs
exactly twice among a selected set of three incidences and the other occurs
at least once. This is Type B.

The distinct-tip and distinct-foot conclusions follow from the common-edge
fan and two-step source reconstruction lemmas.

## Forced Pressure In Type B

For the outgoing-majority junction define:

```text
h=pred_b(v)
k=pred_b(a).
```

Then:

```text
c*p=d*q=h
b*h=v
v*r=k
b*k=a.
```

Thus the junction contains:

```text
rows p,q: v -> b -> c,d, both returning to h;
row r:    a -> b -> v, with v*r=k.
```

The incoming edge also forces the same-target bridge:

```text
A_b(v)=pred_v(b)
A_b(v) -> b -> v*b
```

in row `v`.

For the incoming-majority junction define:

```text
k=pred_v(b)
h=pred_b(v).
```

Then:

```text
(p*v)*p=(q*v)*q=k=A_b(v)
v*k=b
c*r=h
b*h=v.
```

Thus:

```text
rows p,q: a,e -> b -> v, with a common return to k;
row r:    v -> b -> c, with c*r=h.
```

The outgoing edge also starts the target-changing transport from `b` to `v`.

## Significance

A bicyclic obstruction is not merely a pair of free branches. At the first
branch vertex, the second-cycle information is already present as either:

```text
three core branches in one common-edge fan;
or
a two-branch fan crossed by a core interval in the opposite direction.
```

Therefore the next No-Free-Tail proof should split only into:

```text
triple-fan closure;
mixed 2+1 junction closure.
```

It should not discard the third core edge and then try to reconstruct the
second cycle later.

## Boundary

The lemma classifies the forced junction but does not yet exclude either
closure type.

The exact behavior under the target change `b -> v` is proved in:

```text
target_swap_fan_duality_lemma.md
```

It sends a triple or mixed fan at `v` in `H_b` to the orientation-reversed
fan at `b` in `H_v`, preserving all source rows.

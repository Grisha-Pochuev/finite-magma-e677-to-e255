# Mixed Junction Target-Swap Bridge Square

Date: 2026-06-17.

Status:

```text
general proved / structural map for the mixed 2+1 frontier
```

## Setup

Fix a target `b`. Consider an outgoing-majority mixed `2+1` core junction in
`H_b`:

```text
p*v=b, p*b=c
q*v=b, q*b=d
r*a=b, r*b=v
```

with:

```text
p!=q,
c!=d.
```

Thus rows `p,q` give two outgoing core edges from `v`, while row `r` gives
one incoming core edge into `v`.

Define:

```text
h=c*p=d*q=pred_b(v),
k=v*r=pred_b(a),
s=r*v,
alpha=v*(b*p),
gamma=v*(b*q),
eta=b*(v*r).
```

The known mixed-junction lemma already gives:

```text
b*h=v,
b*k=a.
```

## Target Swap To `H_v`

After changing the target from `b` to `v`, the same three source rows become
an incoming-majority mixed junction at the vertex `b` in `H_v`:

```text
p*alpha=v, p*v=b
q*gamma=v, q*v=b
r*b=v,     r*v=s.
```

In graph language:

```text
alpha -> b
gamma -> b
b     -> s
```

inside `H_v`.

The two majority rows keep the common bridge:

```text
(p*b)*p=c*p=h,
(q*b)*q=d*q=h,
b*h=v.
```

The minority row gives the opposite bridge:

```text
s*r=pred_v(b),
v*(s*r)=b.
```

Hence the target-swapped mixed junction contains the bridge square:

```text
row b:  h       -> v
row v:  s*r     -> b
```

where:

```text
h=pred_b(v),
s*r=pred_v(b).
```

## Proof

For the two outgoing rows in `H_b`, apply the edge certificate to:

```text
p*v=b, p*b=c,
q*v=b, q*b=d.
```

It gives:

```text
c*p=pred_b(v),
d*q=pred_b(v),
b*(c*p)=v,
b*(d*q)=v.
```

Thus both values are the same element:

```text
h=pred_b(v).
```

The target-swap lemma applied to the same two edges gives:

```text
p*(v*(b*p))=v,
q*(v*(b*q))=v,
```

and therefore in `H_v`:

```text
alpha -> b,
gamma -> b.
```

For the incoming row `r`, in `H_b` we have:

```text
r*a=b,
r*b=v.
```

Changing the target to `v`, the same row has:

```text
r*b=v,
r*v=s,
```

so it is the outgoing edge:

```text
b -> s
```

in `H_v`.

Applying the edge certificate in `H_v` to:

```text
r*b=v,
r*v=s
```

gives:

```text
s*r=pred_v(b),
v*(s*r)=b.
```

All displayed formulas follow.

## Significance

The mixed `2+1` junction is stable under target swap, but it carries more
than orientation reversal. It produces an explicit two-target bridge square:

```text
b --h--> v
v --(s*r)--> b.
```

This is the next object to compare when the two majority branches close or
when the minority branch re-enters the same cyclic core. The comparison must
use the full last edge certificates, not only the endpoint labels.

## Boundary

This lemma does not prove that the relayed edge `b -> s` remains inside a
bicyclic core of `H_v`; the target-swap lemma already warns about this.

It also does not prove that:

```text
h=s*r
```

or that either bridge is a right fixer. Those would be additional structural
claims and must not be assumed.

## Model Diagnostic Boundary

A targeted diagnostic on `300` outgoing-majority mixed junctions in the known
size-496 model checked the simplest possible bridge shortcuts:

```text
h = s*r
h*b = b
(s*r)*b = b
h -> s*r in H_b
s*r -> h in H_b
```

All five counts were zero in the sample.

This is not a proof, but it is a useful warning: the next proof should not
try to identify the two bridge labels directly. The promising comparison is
still the full branch certificate up to first merge or cyclic closure.

The reproducible script is:

```text
tools/mixed_junction_bridge_square_diagnostics.js
```

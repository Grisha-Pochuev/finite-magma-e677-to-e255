# Double-Outgoing Mixed Witness Candidate

Date: 2026-06-17.

Status:

```text
candidate / algebraic target inside mixed 2+1
```

## Purpose

The relay-termination frontier says that the remaining No-Free-Tail work is
not a purely local graph classification problem.  We need an algebraic
identity that stops the recursive relay.

The best local algebraic target now appears to be stronger than the old
single directed two-edge witness.  In an outgoing-majority mixed `2+1`
junction, there are two directed two-edge paths sharing the same incoming
minority edge:

```text
a -> v -> c,
a -> v -> d.
```

This gives more pressure than an isolated path.

## Setup

Fix target `b`.  Let:

```text
p*v=b, p*b=c,
q*v=b, q*b=d,
r*a=b, r*b=v,
c!=d.
```

Rows `p,q` are the outgoing majority rows.  Row `r` is the incoming minority
row.

Define the mixed bridge-square labels:

```text
h=c*p=d*q=pred_b(v),
s=r*v,
j=s*r=pred_v(b).
```

Then:

```text
b*h=v,
v*j=b.
```

The two directed two-edge paths are:

```text
r: a -> b -> v,
p: v -> b -> c,

r: a -> b -> v,
q: v -> b -> d.
```

## Candidate Right Fixers

For the first path, the old Directed Two-Edge Witness candidate gives:

```text
Y_c=(b*c)*(s*j).
```

For the second path:

```text
Y_d=(b*d)*(s*j).
```

The desired mixed-junction strengthening is:

```text
Y_c*b=b
or
Y_d*b=b.
```

An even stronger possible statement is:

```text
Y_c*b=b and Y_d*b=b.
```

If either equality is proved, then `right_fixer_to_balanced_witness_lemma.md`
gives E255 for `b`.

## Why This Is Stronger Than The Old Single-Path Candidate

The old candidate for one path `a -> v -> c` only used:

```text
r*a=b, r*b=v,
p*v=b, p*b=c,
s=r*v,
j=s*r=pred_v(b).
```

The mixed setting adds a second outgoing row `q` with:

```text
q*v=b,
q*b=d,
d*q=h=c*p.
```

So both outgoing rows share the same backward bridge:

```text
pred_b(v)=h.
```

This common bridge is absent from the single-path formulation and is exactly
the extra double-interval pressure that should be used.

## Plausible Intermediate Identity

The right-fixer proof should probably not try to identify:

```text
h=j.
```

Diagnostics already warn that this shortcut is false in the known model.

Instead, the useful intermediate target is a paired identity involving both
outgoing tips:

```text
((b*c)*(s*j))*b = ((b*d)*(s*j))*b.
```

If this common value is then shown to be `b`, both candidates are right
fixers.

If the common value is not `b`, the equality alone is not a contradiction:
right columns are not known to be injective.  In that case one would still
need an additional argument turning the common image into either a right
fixer or a repeated ordered two-step interval.

## Relation To Relay Termination

A recursive relay chain can keep moving only while every local mixed junction
fails to produce a right fixer.

Thus this candidate is a direct stopping mechanism:

```text
mixed 2+1
=> paired two-edge witness
=> right fixer
=> E255 for b.
```

If the paired witness is too strong, the weaker useful result would be:

```text
failure of both Y_c*b=b and Y_d*b=b forces the next relay state to have a
strictly repeated ported interval.
```

That would also terminate the relay by two-step source reconstruction.

## Reproducible Diagnostic

The script:

```text
tools/mixed_junction_bridge_square_diagnostics.js
```

now checks this paired witness on outgoing-majority mixed junctions in the
known size-496 model.

On a sample of `300` mixed junctions it reported:

```text
yCRightFixesB: 300
yDRightFixesB: 300
bothYRightFixB: 300
pairedImagesEqual: 300
yCEqualsYD: 300
yCEqualsCanonical: 300
yDEqualsCanonical: 300
```

The same run still reported:

```text
hEqualsJ: 0
hRightFixesB: 0
jRightFixesB: 0
edgeHtoJ: 0
edgeJtoH: 0
```

Interpretation:

```text
the paired witness remains compatible with all tested structure,
but the proof should not try bridge-identification shortcuts.
```

The canonical equalities mean:

```text
Y_c=Y_d=(b*b)*b
```

This last canonical equality is not a safe universal target.  A later lifted
diagnostic on `F7 x M496` showed that the sampled mixed junctions still satisfy:

```text
Y_c*b=b,
Y_d*b=b,
Y_c=Y_d,
```

but usually do not satisfy:

```text
Y_c=b.
```

So the proof should keep the weaker, invariant target:

```text
Y_c=Y_d and Y_c*b=b.
```

The discarded stronger route is recorded in:

```text
mixed_row_lift_sufficient_candidate.md
```

on the tested model sample.  This is useful guidance, but it is not by itself
a proof of E255.  The real target remains:

```text
Y_c*b=b
```

or equivalently, after identifying `Y_c` with `(b*b)*b`, the E255 equality for
`b`.

Do not use the old `rawmodeldiagnose` search to test a fully labelled negation
of this witness at size `14`.  A first attempt with explicit labels for
`Y_c*b!=b` exhausted the JavaScript heap before producing mathematical
information.  This was a tooling limit, not evidence for or against the
candidate.

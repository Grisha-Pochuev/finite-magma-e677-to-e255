# Mixed Row-Lift Sufficient Candidate

Date: 2026-06-17.

Status:

```text
rejected as a universal proof target / useful only as M496 pattern
```

## Purpose

The paired mixed witness candidate asks to prove:

```text
Y_c*b=b,
Y_c=(b*c)*(s*j),
```

inside an outgoing-majority mixed `2+1` junction.

This file records a sharper sufficient route that looked promising in M496.
The route is now known to be too strong as a universal lemma.

The surviving target is the weaker right-fixer identity:

```text
((b*c)*(s*j))*b=b.
```

The stronger row-lift equalities below can still be useful as model guidance,
but they must not be treated as the next proof target.

## Setup

Fix a target `b` and an outgoing-majority mixed `2+1` junction:

```text
p*v=b, p*b=c,
q*v=b, q*b=d,
r*a=b, r*b=v.
```

Define:

```text
h=c*p=d*q=pred_b(v),
s=r*v,
j=s*r=pred_v(b),
B_c=b*c,
B_d=b*d.
```

Then:

```text
b*h=v,
v*j=b.
```

The paired witness candidates are:

```text
Y_c=B_c*(s*j),
Y_d=B_d*(s*j).
```

## Sufficient Row-Lift Identities

It is enough to prove:

```text
B_c*s=r,
B_c*j=a,
s*j = b*((B_c*b)*B_c).
```

The last equality says exactly that `s*j` is the inverse image of `b` in row
`B_c`.

Then:

```text
B_c*(s*j)=b,
```

so:

```text
Y_c=b,
```

and therefore:

```text
Y_c*b=b
```

holds trivially.

The analogous sufficient identities for `B_d` are:

```text
B_d*s=r,
B_d*j=a,
s*j = b*((B_d*b)*B_d).
```

## Why This Looked Better

The earlier bridge shortcuts:

```text
h=j,
h*b=b,
j*b=b
```

are false in the known model sample.

In M496, the row-lift identities instead use the full mixed structure:

```text
two outgoing majority rows sharing pred_b(v),
one incoming minority row giving pred_v(b).
```

There they explain the paired witness through a concrete row action:

```text
B_c maps s -> r and j -> a,
then maps s*j -> b.
```

## Diagnostic Evidence

The reproducible script:

```text
tools/mixed_junction_bridge_square_diagnostics.js
```

checks these identities on the known size-496 model.

On `300` sampled mixed junctions, split evenly across targets:

```text
bcTimesJEqualsA: 300
bdTimesJEqualsA: 300
bcTimesSEqualsR: 300
bdTimesSEqualsR: 300
suffixEqualsBInverseOfB: 300
```

The same sample also has:

```text
yCRightFixesB: 300
yDRightFixesB: 300
yCEqualsYD: 300
yCEqualsCanonical: 300
yDEqualsCanonical: 300
```

This is model evidence only, not a proof.

## Product Counter-Diagnostic

The same script now also lifts the sampled mixed junctions to the direct
product `F7 x M496`, where:

```text
u*v = 4u+v mod 7
```

This direct product is still an E677 model and the lifted samples are genuine
mixed `2+1` junctions.

On `300` lifted mixed junctions:

```text
validSetup: 300
yCRightFixesB: 300
yDRightFixesB: 300
yCEqualsYD: 300
```

but the stronger row-lift/equality pattern mostly fails:

```text
yCEqualsB: 43
yDEqualsB: 43
bcTimesSEqualsR: 0
bdTimesSEqualsR: 0
bcTimesJEqualsA: 43
bdTimesJEqualsA: 43
suffixEqualsBInverseOfB: 43
```

Interpretation:

```text
Y*b=b is stable in the lifted mixed samples;
Y=b and the row-lift identities are not stable.
```

Therefore the row-lift candidate is too strong for a general proof.  It should
not be used as the main lemma unless additional hypotheses are added.

## Negative Boundary

The abstract zigzag alone is too weak.

The following equations by themselves:

```text
B*s=r,
s*r=j,
B*j=a,
r*a=b
```

do not force `B*(s*j)=b` under the current small diagnostic closure.  A size-8
`rawmodeldiagnose` check with an explicit labelled negation remained
consistent at the initial propagation level.

Therefore the proof must use that:

```text
B=b*c
```

comes from the outgoing majority edge of the same mixed junction.  The
corrected sufficient lemma is not a generic zigzag lemma; it is a mixed
row-lift lemma.

## Corrected Proof Target

Do not try to prove the row-lift identities as a universal statement:

```text
(b*c)*(r*v)=r,
(b*c)*((r*v)*r)=a,
(r*v)*((r*v)*r)=b*(((b*c)*b)*(b*c)).
```

The first two identities lift the minority row through `B_c=b*c`.  The third
identity identifies `s*j` as the `B_c`-predecessor of `b`.

The corrected target is the weaker paired right-fixer statement:

```text
Y_c=(b*c)*(s*j),
Y_d=(b*d)*(s*j),

Y_c*b=b
or
Y_d*b=b.
```

The lifted product diagnostic suggests an even cleaner intermediate target:

```text
Y_c=Y_d
and
Y_c*b=b.
```

This target remains compatible with both M496 and `F7 x M496`, while avoiding
the false stronger claim `Y_c=b`.

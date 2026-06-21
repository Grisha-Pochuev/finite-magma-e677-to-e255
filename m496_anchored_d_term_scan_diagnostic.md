# M496 Anchored d-Term Scan Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / idempotent-model warning for d-term scans
```

## Purpose

This applies the useful idea from the external `eq677` repository
`src/analysis.rs`: include the unary term

```text
d(x)=((x*x)*x)
```

when mining short identities in M496.

The scan is narrow: it only checks the current shared-step anchored triangle
frontier.

## Script

```text
tools/m496_anchored_d_term_scan.js
```

It scans all shared-step row pairs in M496:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
T=U*h=W*h.
```

## Result

The scan covered:

```text
shared-step pairs: 892800
anchored pairs:    892800
M496 satisfies E255 on all elements: true
```

Universal d-term relations found:

```text
d(h)=h
d(z)=z
h*h=h
z*z=z
d(z)*h=b
z*d(h)=b
d(U)*h=d(W)*h
U*d(h)=W*d(h)
d(T)*T=T
```

Universal E255 checks on named terms:

```text
d(b)*b=b
d(z)*z=z
d(h)*h=h
d(T)*T=T
d(U)*U=U
d(W)*W=W
```

Relations that never held in the scan:

```text
d(U)=d(W)
d(p)=d(q)
T=d(h)
T=d(z)
T=d(b)
b=d(h)
z=d(h)
h*d(T)=b
T*d(h)=b
h*d(U)=h*d(W)
```

## Correction: M496 Is Idempotent

M496 satisfies:

```text
x*x=x
```

for all `496` elements.  Therefore:

```text
d(x)=((x*x)*x)=x
```

throughout M496.

So the relations:

```text
d(h)=h,
d(z)=z,
h*h=h,
z*z=z,
z*d(h)=b,
d(z)*h=b,
d(U)*h=d(W)*h,
U*d(h)=W*d(h)
```

are not anchored-specific evidence by themselves.  They reduce to:

```text
z*h=b,
U*h=W*h,
x*x=x.
```

## Interpretation

The useful new pattern is not:

```text
d(U)=d(W).
```

The useful lesson is methodological: d-term scans on an idempotent model can
produce strong-looking but misleading patterns.  They should not be promoted
to proof targets unless a non-idempotent model also supports them, or unless
they are derived from non-idempotent structural assumptions.

In M496 the shared-step anchor appears to have an extra pair of
right-`h`/right-`d(h)` routes to the old target:

```text
z*h=b,
d(z)*h=b,
z*d(h)=b.
```

But this is explained by:

```text
x*x=x
```

rather than by a new anchored mechanism.

## Follow-Up Diagnostic

The local strong-branch raw check is recorded in:

```text
anchored_d_term_strong_branch_raw_diagnostic.md
```

It shows that the visible strong anchored branch alone does not close:

```text
h*h!=h,
d(h)!=h.
```

by short raw closure.

## Current Use

Do not use this file as evidence that `h` or `z` must be idempotent in the
general anchored triangle.  Its value is negative: it prevents overfitting to
M496 and sends the main proof back to the clean M7 self-repeat cycle-end
template.

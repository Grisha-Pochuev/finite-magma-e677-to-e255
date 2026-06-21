# M496 Anchored d-Term Scan Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / external eq677 analysis.rs idea applied to anchored triangle
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

## Interpretation

The useful new pattern is not:

```text
d(U)=d(W).
```

Instead M496 suggests that the shared-step anchor has an extra pair of
right-`h`/right-`d(h)` routes to the old target:

```text
z*h=b,
d(z)*h=b,
z*d(h)=b.
```

Since row `z` is cancellative, the pair:

```text
z*h=b,
z*d(h)=b
```

would imply:

```text
d(h)=h.
```

M496 also has:

```text
h*h=h.
```

So the observed pattern is stronger than a neighboring product coincidence:
it says that the shared-step anchor `h` behaves like an idempotent fixed point
of `d`.  The same is observed for `z`.

## Next Proof Target

Try to prove, from E677 plus the shared-step anchored triangle, one of:

```text
d(z)*h=b,
z*d(h)=b,
d(U)*h=d(W)*h,
U*d(h)=W*d(h).
```

The strongest immediately useful target is:

```text
z*d(h)=b.
```

Together with the already known:

```text
z*h=b
```

left cancellation in row `z` would give:

```text
d(h)=h.
```

Then E255 for `h` is much closer, and the anchored false branch may collapse
through the old target `b`.  A still stronger target, also supported by M496,
is:

```text
h*h=h.
```

Together with `d(h)=h`, this gives the E255 equation for `h` immediately.

This is only a model diagnostic.  It must be proved or rejected by a local
symbolic/ATP check before being used as a lemma.

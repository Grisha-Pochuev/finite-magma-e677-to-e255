# Directed Two-Edge Canonical Collapse Boundary

Date: 2026-06-17.

Status:

```text
diagnostic boundary / not a proof
```

## Setup

For a directed two-edge path in `H_b`:

```text
p*a=b, p*b=v,
r*v=b, r*b=c,
u=p*v,
k=u*p,
v*k=b,
Y=(b*c)*(u*k).
```

The old hoped-for stopping identity was:

```text
Y*b=b.
```

## New Diagnostic Result

The persistent diagnostic:

```text
tools/directed_two_edge_witness_diagnostics.js
```

now checks whether `Y` is merely the canonical E255 term:

```text
canonical=(b*b)*b.
```

On the sampled `M496` paths:

```text
YEqualsCanonical: 144/144
YEqualsB: 144/144
```

On the lifted direct-product paths in `F7 x M496`:

```text
YEqualsCanonical: 144/144
YEqualsB: 0/144
canonicalRightFixesB: 144/144
```

Thus the equality `Y*b=b` seen in the tested models may be explained by the
fact that those models already satisfy E255.  The path candidate can collapse
to the canonical term `((b*b)*b)`, and then `Y*b=b` is exactly the desired
E255 identity for `b`, not an independent stopping mechanism.

## Consequence For No-Free-Tail

Do not use a single directed two-edge path as the main relay stopper unless an
independent proof of `Y*b=b` is found.

The safer No-Free-Tail target is:

```text
recursive relay
=> repeated full ported interval
=> same source row by two-step reconstruction
=> branch contradiction.
```

A right-fixer route remains useful only if it produces either:

```text
1. a noncanonical right fixer, or
2. a proof of Y*b=b that does not merely restate E255 through
   Y=((b*b)*b).
```

## Shallow Symbolic Check

The bounded script:

```text
tools/two_edge_canonical_saturation.js
```

tries a small ground-congruence closure using:

```text
the directed two-edge cells,
the explicit edge-certificate consequences,
E677 instances on a bounded term basis,
congruence,
left cancellation.
```

With depth `3` it reports:

```text
terms: 93496
Y == canonical: false
Y == b: false
Y*b == b: false
```

This is not a refutation.  It only says that the canonical collapse is not a
short shallow consequence of the currently supplied local certificates.  Do
not repeat this by simply increasing depth; the earlier broad version already
hit the Node memory limit.

Interpretation:

```text
The two-edge witness remains diagnostically suspicious, but the current proof
work should stay on No-Free-Tail / ported-interval recurrence rather than
local term saturation.
```

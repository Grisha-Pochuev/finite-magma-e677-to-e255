# Figure-Eight Closure Crossed-Fan Boundary

Date: 2026-06-17.

Status:

```text
general reduction / depends on crossed double-fan exclusion
```

## Setup

Fix target `b`.  Suppose a core vertex `v` has an outgoing fan:

```text
p*v=b, p*b=c,
q*v=b, q*b=d,
c!=d.
```

Assume the two selected branches do not first merge at a distinct sink.
Instead they close back to the original split vertex `v`, forming a
figure-eight type closure.

That means there are two incoming return incidences into `v`:

```text
r*x=b, r*b=v,
s*y=b, s*b=v.
```

If the two returns are genuinely different:

```text
r!=s
```

then `v` has:

```text
two outgoing incidences: p,q
two incoming incidences: r,s.
```

## Consequence

The figure-eight closure is exactly a crossed double fan at `v`:

```text
outgoing fiber F(v,b) has size at least 2,
incoming fiber into v has size at least 2.
```

Equivalently, after switching notation to the crossed-fan candidate:

```text
F(v,b) has p,q,
F(b,v) has r,s.
```

This boundary is therefore not a new relay type.  It is reduced to:

```text
crossed_double_fan_pressure_candidate.md
```

## Degenerate Return

If the two apparent returns use the same source row, then they are not two
independent return incidences.  The case is a same-row recurrence and must be
handled through:

```text
target_advance_row_orbit_lemma.md
ported_interval_recurrence_boundary.md
```

## Use In No-Free-Tail

A minimal closed relay cycle can now be split more sharply:

```text
distinct branch returns to the old split -> crossed double fan;
same-row return to the old split         -> row-orbit recurrence boundary.
```

Thus one possible route to finish No-Free-Tail is:

```text
prove crossed double-fan exclusion,
then handle the remaining same-row recurrence separately.
```

For the actual E677 -> E255 proof, the needed crossed-fan exclusion can be
weaker:

```text
bad_target_crossed_fan_boundary.md
```

It is enough to exclude crossed double fans where the target `b` is the
hypothetical bad element.

One degenerate crossed-fan subcase is now separated:

```text
crossed_fan_swap_row_degeneracy_lemma.md
swap_row_target_advance_loop_lemma.md
```

If a branch row swaps `a` and `b`, then the row is uniquely determined by the
two-step interval `a -> b -> a`.  Hence two short returns through different
rows are impossible.  A crossed-fan with a shared swap row should be treated as
same-row/loop recurrence, not as two independent branch returns.

## Shallow Diagnostic

The bounded script:

```text
tools/crossed_double_fan_saturation.js
```

tests whether the crossed double-fan equations immediately force one of:

```text
p=q,
c=d,
r=s,
u=v,
h=k.
```

With explicit fan certificates and E677 ground closure on a bounded basis, the
depth `3` and `4` runs give:

```text
p == q: false
c == d: false
r == s: false
u == v: false
h == k: false
```

This is not evidence that crossed double fans exist.  It only says that the
candidate does not close by the very shortest symbolic congruence check.
Do not treat crossed-fan exclusion as proved.

## Size-8 Raw-Label Boundary

A valid raw-label arbitrary-model search for crossed double fan at size `8`
was run with:

```text
2*0=1,
3*0=1,
4*1=0,
5*1=0.
```

The 10-minute run did not find a model, but also did not complete:

```text
status: timeout
time: 600.03s
nodes: 93290
dead ends: 91862
forced cells: 704888
domain checks: 876744396
```

The corresponding raw initial diagnostic is consistent:

```text
status: ok
row 2 domain=4272 with 0->1
row 3 domain=4272 with 0->1
row 4 domain=4272 with 1->0
row 5 domain=4272 with 1->0
```

Interpretation:

```text
crossed double fan is strongly constrained but not locally contradictory
under the current search/closure tools.
```

## M496 Scan

The diagnostic:

```text
tools/core_orientation_diagnostics.js all
```

now scans all targets of the known size-496 E677 model. It reports:

```text
targets: 496
crossedTargets in 2-core: 0
crossedVertices in 2-core: 0
allCrossedTargets: 0
allCrossedVertices: 0
maxCoreEdges: 45
```

Thus the known large non-right-cancellative model has no crossed double-fan
vertex at any target, even outside the 2-core. This supports crossed-fan
exclusion as a structural target, but still does not prove it.

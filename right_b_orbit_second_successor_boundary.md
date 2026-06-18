# Right-b Orbit Second-Successor Boundary

Date: 2026-06-18.

Status:

```text
boundary clarification / diagnostic support / not a contradiction lemma
```

## Setup

Work in the clean external-bridge residual of a proper bad-target crossed fan.

Use:

```text
x_0=a,
x_1=t=a*b,
x_2=t*b.
```

The first bridge has:

```text
a*k=b,
a*b=t,
ell=t*a=pred_b(k),
b*ell=k.
```

## Immediate Second-Successor Routes

The second successor `x_2=t*b` should be treated as a right-`b` orbit hit,
not as a new independent local case.

The useful first split is:

```text
x_2=b
```

This is impossible for a bad target `b`, because it says:

```text
t*b=b.
```

The already routed first-successor return is:

```text
x_2=a.
```

Then row `t` joins the incoming crossed-fan side:

```text
t*b=a,
```

so this is an enlarged `F(b,a)` / right-`b` two-cycle boundary, as recorded in:

```text
first_right_b_successor_fan_attachment_lemma.md
```

The fixed second-successor case:

```text
x_2=t
```

is only a right-`b` fixed orbit boundary:

```text
t*b=t.
```

It is not a right fixer for the bad target `b`.

Hits:

```text
x_2 in {c,d,u,v,h,k}
```

are visible-footprint or bridge-hub hits of the right-`b` orbit.  They should
be routed through the first-visible-hit branch of:

```text
right_b_orbit_first_repeat_boundary.md
right_b_orbit_local_repeat_roles.md
```

not treated as immediate contradictions.

## Shallow Diagnostic

The permanent diagnostic:

```text
tools/crossed_double_fan_saturation.js
```

now supports flags:

```text
tb=a, tb=b, tb=c, tb=d, tb=u, tb=v, tb=h, tb=k, tb=ab, tb=ta
```

where:

```text
tb=(a*b)*b=t*b.
```

Depth-3 bounded closure gives:

```text
tb=b   -> short right-fixers of b include ab=t, as expected;
tb=a   -> no short contradiction beyond the routed incoming-side hit;
tb=ab  -> no short contradiction; this is the right-b fixed orbit boundary;
tb=h   -> no short contradiction; visible bridge-hub output hit;
tb=k   -> no short contradiction; visible bridge-hub output hit.
```

Earlier depth-3 checks for:

```text
ta=a, ta=k, ta=ab
```

also did not produce a short bad-target right fixer.  The exception remains:

```text
ta=h -> k=a
```

which is already routed out of the clean residual.

## Consequence

The clean external-bridge residual should not be attacked by expecting one of
the first two right-`b` orbit successors to force an immediate local
contradiction.

After routing visible hits, the genuine remaining object is:

```text
a closed right-b orbit segment disjoint from the visible crossed-fan footprint,
plus the attached predecessor chain A_i=pred_{x_i}(b).
```

Thus the next proof target remains the first-repeat fan step:

```text
right-b orbit first repeat
=> fresh incoming fan in H_b
=> branch-relay / No-Free-Tail termination.
```


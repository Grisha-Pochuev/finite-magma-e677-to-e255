# Right-b Orbit First-Repeat Boundary

Date: 2026-06-18.

Status:

```text
boundary / finite reduction / strengthened by right_b_orbit_first_repeat_fan_lemma.md
```

## Setup

Fix a bad target `b` and start the right-`b` orbit at:

```text
x_0=a,
x_{i+1}=x_i*b.
```

For each `i`, define:

```text
A_i=pred_{x_i}(b),
H_i=x_{i+1}*x_i=pred_b(A_i).
```

Then:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

## Finite First Repeat

Because the magma is finite and the sequence `x_i` is deterministic, there
exist indices:

```text
0 <= i < j
```

with:

```text
x_i=x_j.
```

Let `j` be the first repeat time after all routed visible-hit cases are
excluded.

Then the orbit segment:

```text
x_i -> x_{i+1} -> ... -> x_{j-1} -> x_j=x_i
```

is a closed right-`b` cycle.

## What This Gives

For every point on the closed cycle, the predecessor recursion gives a row-`b`
arrow:

```text
b*H_m=A_m,
H_m=pred_b(A_m).
```

The full ported interval carried by row `x_m` is:

```text
(b,A_m,x_{m+1}).
```

When `x_m` repeats, the corresponding source row repeats too.  Therefore a
same-source recurrence is expected, not an immediate contradiction.

However, the repeat is not graphically neutral.  It creates an incoming fan in
`H_b`; see:

```text
right_b_orbit_first_repeat_fan_lemma.md
```

If the first repeat is internal, the two predecessor rows entering the
repeated value give two distinct incoming `H_b` edges.  If the orbit returns
to `a`, it enlarges the original incoming side unless it hits a selected
source row.

## Routed First-Hit Conditions

Before treating the first repeat as a clean cycle, the following hits should
already be routed:

```text
x_m in visible fan footprint;
A_m in visible fan footprint;
H_m in visible fan footprint;
A_m=x_{m+1}        -> same-row swap recurrence;
A_m=x_m           -> self-source fan boundary;
x_{m+1}=x_m       -> right-b fixed orbit boundary;
H_m=A_m           -> row-b fixed point boundary.
```

The local repeat roles are recorded in:

```text
right_b_orbit_local_repeat_roles.md
```

## Remaining Boundary

If none of the routed hits occurs, the clean first-repeat case is:

```text
a closed right-b cycle disjoint from the visible crossed-fan footprint,
with a new incoming common-edge fan at the first repeated vertex and a
parallel row-b predecessor-arrow cycle attached through A_m,H_m.
```

This is not yet proved impossible.

The next proof must use extra pressure from the original crossed-fan rows
`p,q,r,s`, or from the row-`b` predecessor fan, to show that such a closed
cycle cannot remain independent.

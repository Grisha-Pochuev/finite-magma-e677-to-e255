# Anchored-X3 Clean Self-Repeat Normal Form

Date: 2026-06-21.

Status:

```text
boundary / exact normal form for the remaining M7 self-repeat
```

## Purpose

This records what remains after:

```text
anchored_x3_source_orbit_boundary.md
anchored_x3_visible_short_repeat_lemma.md
```

The visible period-1 and period-2 cases are routed.  The remaining clean
self-repeat is a closed source-successor cycle under right multiplication by
the fixed anchor `h`.

This file names that object without pretending it is already a directed path
or a left-row orbit.

## General Fixed-Target Source Orbit

Fix the target:

```text
h.
```

Let one of the anchored starting rows be:

```text
r_0 in {U,W,z}.
```

Define the right-`h` source-successor sequence:

```text
r_{n+1}=r_n*h.
```

For each `n`, row `r_n` gives an edge in `H_h`:

```text
I_n -> r_{n+1},
```

where:

```text
r_n*I_n=h.
```

Equivalently, by the standard predecessor formula:

```text
I_n=h*(r_{n+1}*r_n).
```

And by the fixed-target source-successor lemma:

```text
I_{n+1}=(r_n*r_{n+1})*r_n.
```

## Clean Self-Repeat

A clean self-repeat has:

```text
r_m=r_n,
0 <= m < n,
```

with no earlier event among:

```text
cross-orbit source hit,
next-output merge,
input-output cross hit,
watched/core hit,
self-repeat.
```

Then the segment:

```text
r_m -> r_{m+1} -> ... -> r_{n-1} -> r_m
```

is a closed right-`h` source cycle.

Since the same source row appears again in the same fixed target graph,
the corresponding ported interval repeats:

```text
(h,I_m,r_{m+1})=(h,I_n,r_{n+1}).
```

If the two occurrences are in independent branch roles, this is already an
independent full ported-interval collision.  The clean residual is therefore
only the same-orbit, same-role recurrence.

## What It Is Not

This normal form is not automatically an `H_h` directed cycle, because the
next edge starts at:

```text
I_{n+1},
```

not necessarily at:

```text
r_{n+1}.
```

It is also not the same as:

```text
target_advance_same_row_period_lemma.md
```

because that lemma follows a left row:

```text
x_{i+1}=p*x_i.
```

Here we follow right multiplication by the fixed anchor:

```text
r_{n+1}=r_n*h.
```

## Remaining Clean Residual

After visible short repeats are removed, the live self-repeat must satisfy:

```text
cycle length >= 3 if it returns to the initial anchored row;
or it is a later fresh cycle disjoint from the displayed anchored layer.
```

The displayed anchored layer is:

```text
U,W,z,T,S,b,p,q,alpha.
```

No endpoint of the source cycle or its `H_h` edges may hit this displayed
layer without routing as a watched hit.

## Next Target

The next proof step should show one of:

```text
1. the clean right-h source cycle creates strict clean theta;
2. it repeats a full ported interval in an independent role;
3. it regenerates a smaller anchored-X3 source-orbit object under M7;
4. it hits the old/core footprint.
```

Until one of these is proved, this normal form is the exact remaining M7
self-repeat residual.

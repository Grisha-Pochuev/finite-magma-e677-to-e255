# Anchored-X3 Rank Measure Candidate

Date: 2026-06-21.

Status:

```text
candidate / measure extension for clean anchored-X3 source-orbit residual
```

## Purpose

This records the measure needed after:

```text
anchored_x3_source_orbit_boundary.md
```

The clean anchored-X3 false branch is now a fixed-target source-orbit residual
inside:

```text
H_h.
```

The remaining proof should not return to broad search.  It should compare the
first repeat/merge of the three source orbits with the global relay measure.

## Clean Anchored-X3 Source-Orbit Data

The three initial rows and first successors are:

```text
U -> T,
W -> S,
z -> b
```

under right multiplication by the fixed target `h`:

```text
r_{n+1}=r_n*h.
```

Their corresponding `H_h` edges are:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

and the next layer begins:

```text
row T: (U*T)*U -> T*h,
row S: (W*S)*W -> S*h,
row b: (z*b)*z -> b*h.
```

## Proposed Rank

Extend the global measure from:

```text
relay_minimality_measure_candidate.md
```

by adding:

```text
M7. anchored-X3 source-orbit first-event rank:
    the earliest source-orbit event among the three right-h orbits starting
    from U,W,z.
```

An event is one of:

```text
1. a source-row hit between two different orbits;
2. a next-output merge between two different orbits;
3. an input-output cross hit between two active H_h edges;
4. a watched/core hit;
5. a self-repeat inside one orbit.
```

The first four event types route locally:

```text
source hit       -> repeated full ported interval or same-source recurrence;
output merge     -> incoming fan in H_h;
input-output hit -> directed path in H_h;
watched/core hit -> ordinary relay/core attachment.
```

The only event that can remain as a clean residual is:

```text
self-repeat inside one source orbit before any cross-orbit hit.
```

The visible short part of this residual is routed in:

```text
anchored_x3_visible_short_repeat_lemma.md
```

So the live clean self-repeat is only a later/fresh right-`h` repeat, or a
return to the initial source after at least three right-`h` steps.

The exact normal form for that remaining case is:

```text
anchored_x3_clean_self_repeat_normal_form.md
```

It is a clean right-`h` source-successor cycle, not automatically a directed
cycle in `H_h` and not a left-row period.

## Desired Descent Sentence

The next proof target is:

```text
In a minimal G12 loop, a clean anchored-X3 source-orbit self-repeat is either
one of the already routed same-row recurrence types, or it regenerates an
anchored-X3 object with smaller M7.
```

Equivalently:

```text
the false branch U*h!=W*h cannot be a terminal clean residual unless it
creates a strictly descending anchored-X3 source-orbit rank.
```

## Why This Is Smaller Than The Previous Residual

The old open branch was:

```text
clean same-input two-target bridge after first extra intersection
```

measured by:

```text
M5/M6
```

The anchored-X3 false branch is born earlier from the shared-step certificate
itself and carries the old row `b` in its third source orbit:

```text
z -> b -> b*h -> ...
```

So it should be measured before treating the first-extra V3 bridge as an
independent residual.  If the anchored rank descends, both:

```text
clean first-extra V3
clean orbit-theta
```

are bypassed by the shared-step anchored route.

## Current Boundary

This file does not prove the descent sentence.

It names the exact missing measure component:

```text
M7 anchored-X3 source-orbit first-event rank.
```

The next work should prove the M7 descent or find the exact clean self-repeat
subcase that fails it.

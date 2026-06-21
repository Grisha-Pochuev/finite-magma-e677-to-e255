# Anchored-M7 Cycle-End Template

Date: 2026-06-21.

Status:

```text
template / next concrete working surface for clean self-repeat
```

## Purpose

After:

```text
anchored_m7_first_event_routing_lemma.md
```

the only live anchored-M7 event is:

```text
clean same-orbit right-h self-repeat.
```

This file records the useful cycle-end encoding suggested by the external
`eq677` `cycle-sen.p` pattern.

## Cycle-End Notation

Fix the target:

```text
h.
```

Choose one clean right-`h` source orbit and name:

```text
r0   = chosen start row,
r1   = r0*h,
rm2  = next-to-last row before return,
rm1  = last row before return.
```

So:

```text
r0*h  = r1,
rm2*h = rm1,
rm1*h = r0.
```

Each source row carries an edge in `H_h`:

```text
i0  -> r1   carried by row r0,
im2 -> rm1  carried by row rm2,
im1 -> r0   carried by row rm1.
```

The attached inputs are:

```text
i0  = h*(r1*r0),
im2 = h*(rm1*rm2),
im1 = h*(r0*rm1).
```

## Clean Conditions

The current residual excludes:

```text
cross-orbit source hit,
output merge,
input-output cross hit,
watched/core hit,
earlier self-repeat.
```

For the displayed cycle-end triple, that means the three `H_h` edges must not
already have:

```text
same input,
same output,
full ported interval,
input-output concatenation,
visible/core endpoint.
```

If any of these occurs, it routes by:

```text
same_target_pair_collision_trichotomy_lemma.md
anchored_m7_first_event_routing_lemma.md
```

## ATP Template

The formal template is:

```text
atp/anchored_m7_cycle_end.p
```

It includes:

```text
E677,
left cancellation,
edge predecessor formula,
fixed-target source successor formula,
anchored-X3 false branch,
clean visible short-repeat exclusions,
cycle start/end equations.
```

It does not prove the theorem by itself.  Its purpose is to make the next
candidate consequence precise.

## Next Candidate Consequences

Useful first conjectures are:

```text
im1 = r1
```

which would concatenate the last cycle-end edge to the start successor, or:

```text
f(r0,r1) = f(rm1,r0)
```

which compares the two row/source certificates at the return point.

Another direct target is to prove that the cycle-end triple creates a clean
theta in `H_h`.  If it does, strict clean theta is already excluded by:

```text
strict_clean_theta_exclusion_lemma.md
```

## Do Not Overclaim

The cycle:

```text
r0 -> r1 -> ... -> rm1 -> r0
```

is a right-`h` source-successor cycle.  It is not automatically a directed
cycle in `H_h`, because the `H_h` edge starts at the predecessor input `i`,
not at the source successor row.

The proof must use the attached inputs:

```text
i0, im2, im1
```

rather than treating the source orbit itself as an `H_h` path.

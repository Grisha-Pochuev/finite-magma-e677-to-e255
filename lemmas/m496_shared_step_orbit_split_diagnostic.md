# M496 Shared-Step Orbit Split Diagnostic

Date: 2026-06-20.

Status:

```text
diagnostic / supports first-extra-intersection focus
```

## Purpose

This checks the split isolated in:

```text
two_row_orbit_theta_boundary.md
```

For every pair of distinct rows in the known M496 model that share one step:

```text
p*b=z,
q*b=z,
p!=q,
```

the diagnostic asks whether the row cycles through `b -> z` meet again outside
the shared pair `{b,z}`.

## Script

The permanent script is:

```text
tools/m496_shared_step_orbit_split.js
```

It precomputes row-cycle bitsets, so it checks all shared-step row pairs
quickly.

## Result

The scan found:

```text
groups with shared-step fiber size:
  size 16: 7440 groups

max fiber size: 16
shared-step row pairs: 892800
extra-intersection pairs: 892800
clean orbit-theta pairs: 0
```

Example extra-intersection rows all occur in the expected period `>= 3`
range, such as periods `10` and `30`.

## Interpretation

In M496, every pair of distinct rows sharing a step `b -> z` has another
cycle intersection beyond `{b,z}`.

So the clean orbit-theta branch from:

```text
two_row_orbit_theta_boundary.md
```

does not appear in the known model.  This does not prove the branch impossible
in all finite E677 magmas, but it strongly suggests the next proof effort
should prioritize the first-extra-intersection route:

```text
two_row_first_extra_intersection_routing_lemma.md
```

and especially the clean same-input two-target bridge left by that route.

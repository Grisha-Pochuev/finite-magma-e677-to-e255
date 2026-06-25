# Anchored-X3 Visible Short Repeat Lemma

Date: 2026-06-21.

Status:

```text
proved local routing / visible short repeats in anchored-X3 source orbits
```

## Purpose

This records the part of the `M7` self-repeat problem that is genuinely local.

The clean anchored-X3 false branch has three right-`h` source orbits:

```text
U -> T -> T*h -> ...
W -> S -> S*h -> ...
z -> b -> b*h -> ...
```

from:

```text
anchored_x3_source_orbit_boundary.md
```

Because right multiplication by `h` is not known to be a permutation, a
general later self-repeat in a fresh source row is not automatically the same
as the left-row period classification.  This file only closes the visible
short repeats that hit the already named anchored layer.

## Period 1 At The Initial Source

If:

```text
U*h=U,
```

then:

```text
T=U.
```

But `T` is an output of the original `H_h` edge:

```text
row U: p -> T.
```

So the output hits the visible source row `U`.  This is not a clean anchored
matching; route it as a watched/visible hit.

Similarly:

```text
W*h=W  => S=W,
z*h=z  => b=z.
```

The last case also contradicts the bad-target setting when `b` is the watched
bad target, because a row would send `b` to `b`.

Thus no initial period-1 source orbit belongs to the clean false branch.

## Period 2 Returning To The Initial Source

If:

```text
T*h=U,
```

then the second triangle layer has:

```text
row T: (U*T)*U -> U
```

inside `H_h`.

Its output hits the original visible source row `U`, so this is a cross-layer
visible hit, not a clean residual.

Similarly:

```text
S*h=W
```

routes by a visible hit to `W`, and:

```text
b*h=z
```

routes by a visible hit to the original source row `z`.

Thus no initial period-2 return belongs to the clean false branch.

## Remaining Self-Repeat Residual

After removing the visible short repeats, a clean `M7` self-repeat must be one
of:

```text
1. a later repeat wholly inside fresh source rows;
2. a return to the initial source after at least three right-h steps.
```

In either case the repeat does not immediately hit the displayed anchored
layer:

```text
U,W,z,T,S,b.
```

This is the exact remaining self-repeat problem.  It should not be confused
with:

```text
target_advance_same_row_period_lemma.md
```

because that lemma concerns a left-row orbit under a fixed source row, while
`M7` uses the right-`h` source-successor map.

## Current Boundary

The next proof target is:

```text
clean later right-h self-repeat
=> smaller anchored-X3 rank, watched/core hit, or independent full interval.
```

The visible period-1 and period-2 cases are no longer live.

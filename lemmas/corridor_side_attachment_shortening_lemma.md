# Corridor Side-Attachment Shortening Lemma

Date: 2026-06-17.

Status:

```text
candidate / graph pruning observation, measure still needed
```

## Setup

Work in the undirected cycle core of some `H_b`.

Let `C` be a clean two-branch corridor: two internally disjoint simple paths
from a split vertex `s` to a first merge vertex `z`.

Suppose an extra core incidence attaches at an internal corridor vertex `w`.
This means the extra edge is not one of the two corridor edges incident with
`w`.

## Claim

The extra incidence creates a new two-branch corridor whose footprint on the
old corridor is a proper subpath of the old `s`-to-`z` corridor.

More precisely, follow the extra core edge away from `w` along a simple core
path until it first hits the old corridor again, at a vertex `t`.

Then:

```text
1. the extra path from w to t is internally disjoint from the old corridor;
2. the old corridor contains a simple subpath from w to t;
3. these two paths form a new clean corridor between w and t.
```

The old-corridor part of this new corridor is strictly smaller than the whole
old corridor because `w` is internal.  However, the extra outside path from
`w` to `t` may be long.  Therefore this lemma does not by itself prove
descent for the total number of vertices.  The relay proof still needs the
right well-founded measure.

## Proof

Because the extra incidence is a core incidence, it lies on an undirected
cycle.  Starting from `w` along the extra edge, follow that cycle until the
first time it meets the old corridor again.  Call that first meeting point
`t`.

By first-return choice, the path from `w` to `t` has no internal vertex on the
old corridor.

The old corridor is the union of two simple `s`-to-`z` paths.  Between any two
vertices on this union there is at least one simple subpath lying entirely in
the old corridor.  Choose such a subpath from `w` to `t`.

Together with the extra return path, this gives two internally disjoint paths
between `w` and `t`.

Since `w` is internal to the old corridor, any old-corridor subpath from `w`
to `t` omits at least one nonempty part of the original selected corridor
unless `t` is chosen so that the subpath deliberately goes the long way around.
For the relay argument, one should choose the shorter old-corridor arc from
`w` to `t` and measure descent by the old-corridor footprint, not by the
uncontrolled length of the outside return path.

## Use In No-Free-Tail

In a minimal relay-cycle argument, an internal side attachment cannot be
ignored:

```text
it gives a new corridor on a proper subarc of the old corridor.
```

To turn this into a proof, the minimal relay cycle must be chosen with a
measure that decreases when the old-corridor footprint shrinks.  With such a
measure, internal side attachments are incompatible with minimality, leaving
the strict clean-theta boundary already excluded by:

```text
strict_clean_theta_exclusion_lemma.md
```

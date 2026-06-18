# Strict Clean-Theta Exclusion Lemma

Date: 2026-06-17.

Status:

```text
graph proved / excludes the strict clean mixed-theta boundary
```

## Setup

Fix a target `b`.  Suppose an outgoing-majority mixed `2+1` junction at `v`
has exactly the three displayed core incidences:

```text
p*v=b, p*b=c,
q*v=b, q*b=d,
r*a=b, r*b=v.
```

Rows `p,q` start two outgoing branches from `v`.  Assume:

```text
1. the two outgoing branches first meet at z;
2. z is a binary pure incoming sink;
3. the interiors of the two branches have no side attachment;
4. v has no fourth core incidence.
```

This is the strict clean mixed-theta boundary.

## Claim

The strict clean mixed-theta boundary is impossible in a cycle core.

## Proof

The two outgoing branches from `v` to `z` form one simple undirected cycle.

The minority edge:

```text
a -> v
```

is assumed to be a core edge.  Therefore it lies on some undirected cycle.
Equivalently, after using the minority edge away from `v`, there must be a
core path from `a` back to the selected outgoing corridor without reusing the
minority edge itself.

Let `w` be the first vertex of the outgoing corridor hit by such a return
path.

There are only three possibilities.

### `w` Is Internal To One Outgoing Branch

Then the final edge of the return path is a side attachment to the interior of
one outgoing branch, contradicting assumption 3.

### `w=z`

Then `z` has an additional core incidence beyond the two incoming branch
edges, or an outgoing/loop continuation.  This contradicts assumption 2 that
`z` is a binary pure incoming sink.

### `w=v`

Then the return path supplies an additional core incidence at `v`, distinct
from the original minority edge.  This contradicts assumption 4 that `v` has
exactly the three displayed core incidences.

All possible first return positions are impossible.  Hence the strict clean
mixed-theta boundary cannot occur in a cycle core.

## Consequence

After the previous relays, the only possible mixed-theta residue must have at
least one of the following non-strict features:

```text
an internal side attachment;
an extra incidence at the sink z;
an extra incidence at the split v.
```

But each of those is already classified by the existing relay lemmas:

```text
side_attachment_orientation_reduction_lemma.md
pure_incoming_merge_target_swap_fan_lemma.md
first_merge_target_swap_junction_dichotomy.md
minority_core_return_relay_lemma.md
```

Thus the branch-closure problem has been reduced from a passive clean theta to
a recursive relay among already classified junctions.  The remaining work is
to make that recursion well-founded, not to analyze the strict clean theta
itself.


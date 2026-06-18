# Binary Sink Core-Escape Lemma

Date: 2026-06-17.

Status:

```text
graph proved / boundary reduction for branch closure
```

## Setup

Work inside the cycle core of a connected component of `H_b` with at least two
independent cycles.

Suppose two directed branch paths start at a common split vertex `s` and first
merge at a vertex `z`.  Assume this first merge is the remaining binary pure
incoming sink:

```text
exactly two incoming core incidences at z,
no outgoing continuation from z,
no loop at z,
no third incoming incidence at z.
```

So, inside the selected two-branch corridor, the two paths form:

```text
s ... -> z
s ... -> z
```

and there is no extra core incidence at `z`.

## Graph Observation

The union of the two branch paths from `s` to `z` is one simple undirected
cycle, provided the paths have no earlier common vertex.

Therefore this corridor accounts for only one independent cycle.

But the ambient core component has at least two independent cycles. Hence
there must be some additional core edge or core path not contained in this
two-branch corridor.

Because the ambient core is connected, this additional core material must
attach to the corridor somewhere.

It cannot attach only at `z`, because that would give one of:

```text
a third incoming incidence at z,
an outgoing continuation from z,
a loop at z,
```

all excluded by the binary pure incoming sink assumption.

Therefore the additional core material attaches before `z`:

```text
at the initial split s,
or at an internal vertex of one of the two branch paths.
```

## Consequence

The binary pure incoming sink is not a standalone terminal obstruction inside
the forced bicyclic core.

If the extra attachment is at `s`, then it is exactly the already retained
third core incidence from the original triple fan or mixed `2+1` junction.

If the extra attachment is at an internal branch vertex, then the correct next
frontier is not the sink `z` itself.  It is the first side attachment before
`z`.

Thus the branch-closure problem is reduced from:

```text
an isolated binary sink at the first merge
```

to:

```text
the earliest side attachment to the two-branch corridor before that sink.
```

The next algebraic task is to classify this earliest side attachment by
orientation.  It must become one of:

```text
outgoing continuation / mixed relay,
incoming fan / target-swap fan,
or an ordered two-step overlap with one of the active branch rows.
```

## Boundary

This is a graph-theoretic reduction.  It does not yet prove the algebraic
No-Free-Tail Lemma.

It shows that the binary pure incoming sink should not be analyzed as an
isolated endpoint.  The missing pressure must come from the first extra core
attachment to the two-branch corridor.

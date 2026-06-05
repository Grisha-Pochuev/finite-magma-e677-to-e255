# Far-Row Killer Lemma

Status:

```text
historical candidate / branch-closing mechanism
```

This note records the public English summary of the far-row killer mechanism
found in the case45 branch analysis.

## Context

The mechanism appeared in branches where a forced value moved pressure away
from the immediate low rows.  The useful discovery was that a far row could
still force a return, zero hit, or collision through the same `E677`
predecessor pattern.

## Structural content

The branch pattern can be summarized as:

```text
forced edge in a far row
  -> predecessor edge by E677
  -> relay into an occupied row or zero-pressure row
  -> branch closure
```

The point is not the numeric labels themselves.  The point is that a far row is
not free: `E677` forces it to interact with the occupied bad-cycle structure.

## Current role

This is a historical source for the current no-free-tail strategy.  The modern
version is expressed more generally in:

```text
edge_predecessor_triangle_lemma.md
offset_pressure_diamond_lemma.md
double_interval_pressure_lemma.md
```


# Row-6 Compact Residual Lemma

Status:

```text
historical branch-closure lemma
```

This file summarizes a compact residual mechanism found in row-6 case45
branches.

## Idea

After several forced row-6 edges, the remaining residual cases were not
independent.  They shared a compact pattern:

```text
forced row edge
  -> predecessor edge
  -> relay through a low row
  -> zero hit or occupied-row collision
```

## Why it mattered

This reduced several apparently different subcases to the same structural
explanation.  It was an important step away from mechanical case-by-case
closure.

## Current role

The compact-residual pattern is now viewed as an example of the broader
no-free-tail principle.

Related current files:

```text
main_bad_cycle_no_free_tail_lemma.md
source_orbit_zipper_lemma.md
double_interval_pressure_lemma.md
```


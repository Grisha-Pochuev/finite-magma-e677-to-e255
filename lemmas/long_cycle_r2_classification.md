# Long-Cycle `r_2` Classification

Status:

```text
historical classification note
```

This file records the public summary of an earlier classification attempt for
the value

```text
r_2 = b_2*0.
```

## Purpose

The classification was used to understand what happens when `r_2` lies inside
or outside the occupied bad-cycle block.

The useful distinction was:

```text
r_2 = 0       -> E255 holds for the chosen element
r_2 = b_j     -> occupied-block return or descent pressure
r_2 fresh     -> source-orbit / free-tail pressure
```

## Current role

The modern version of this idea is the no-free-tail candidate:

```text
main_bad_cycle_no_free_tail_lemma.md
double_interval_pressure_lemma.md
```

This older classification is kept as background for how the current split was
found.


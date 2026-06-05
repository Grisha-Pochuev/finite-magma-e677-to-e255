# Top-Branch Row-6 Transfer Plan

Status:

```text
historical plan / superseded by later structural files
```

This file records the public summary of an older row-6 transfer plan.

## Purpose

The plan was to use row-6 transfers to close top branches without continuing
blind enumeration.

The intended method was:

```text
identify a forced row-6 edge
derive its E677 predecessor edge
check whether the predecessor hits 0, an occupied row, or a known relay
record the resulting structural closure
```

## Current role

This plan was an intermediate step.  The current strategy is more general and
is recorded in:

```text
main_bad_cycle_no_free_tail_lemma.md
offset_pressure_diamond_lemma.md
double_interval_pressure_lemma.md
```


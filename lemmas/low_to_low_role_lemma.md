# Low-to-Low Role Lemma

Status:

```text
historical role split
```

This file records a role split used in the low-row part of the case45 branch
analysis.

## Role split

Low-row transfers were separated into:

```text
immediate zero-hit
eventual zero-hit
return to an occupied low row
fresh low-row prefix
self-swap or short-cycle boundary
```

The useful lesson was that a fresh prefix is the only dangerous case.  All
other roles tend to close by zero pressure, descent, or collision.

## Current role

This older role split is an ancestor of the current frontier split:

```text
u_2=t
u_2=b_j
u_2 fresh
```

See:

```text
docs/CURRENT_FRONTIER.md
lemmas/double_interval_pressure_lemma.md
```


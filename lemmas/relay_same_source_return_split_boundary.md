# Relay Same-Source Return Split Boundary

Date: 2026-06-20.

Status:

```text
boundary / separates independent return from same-source row-orbit return
```

## Purpose

This sharpens the remaining G12 obstruction from:

```text
relay_minimality_measure_candidate.md
minimal_relay_cycle_dichotomy_candidate.md
figure_eight_closure_crossed_fan_boundary.md
```

The goal is to avoid treating every closed relay return as the same kind of
recurrence.  There are two sharply different return roles.

## Setup

Fix a relay state in `H_b` with active split vertex `v`.

Suppose a relay branch returns to `v`:

```text
r*x=b,
r*b=v.
```

If there are two return incidences into `v`, compare their source rows.

## Independent Return

If the returns use distinct rows:

```text
r*x=b, r*b=v,
s*y=b, s*b=v,
r!=s,
```

then together with the two outgoing branch rows at `v` this is a crossed
double fan:

```text
two outgoing incidences from v,
two incoming incidences into v.
```

This is the nondegenerate figure-eight branch from:

```text
figure_eight_closure_crossed_fan_boundary.md
```

For a bad target, the crossed-fan route has now been reduced through:

```text
clean_external_bridge_twelfth_stage_reduction_lemma.md
```

to the global minimal relay-cycle descent G12.

So an independent return does not create a new local recurrence type.  It
re-enters the crossed-fan/clean-bridge reduction already completed locally.

## Same-Source Return

If the apparent return is through the same source row as an earlier occurrence,
then the full ported interval recurrence is in one row-orbit:

```text
(target,input,output)
  --same source row-->
...
  --same source row-->
(same target,input,output).
```

This is the degenerate return from:

```text
fixed_target_same_source_return_collapse_lemma.md
ported_interval_recurrence_boundary.md
target_advance_row_orbit_lemma.md
```

Inside one fixed target graph `H_b`, this cannot be a new second return to the
same split vertex: the fixed-target same-source collapse lemma says it is the
same incidence again.

Thus the same-source residue is only the target-advance row-orbit phenomenon:
the relay has moved the target along the same row and later repeats the same
full ported interval in the same branch role.

## Consequence

In a minimal relay-cycle proof, every return to an old split has the exact
split:

```text
1. independent return:
   crossed fan -> clean external bridge reductions -> G12;

2. same-source return:
   fixed-target duplicate edge, or pure target-advance row-orbit recurrence.
```

Thus the remaining G12 obstruction can be stated more narrowly:

```text
exclude a minimal closed relay cycle whose only returns are same-source
target-advance row-orbit returns and whose independent returns all reduce
back to the same minimal G12 state.
```

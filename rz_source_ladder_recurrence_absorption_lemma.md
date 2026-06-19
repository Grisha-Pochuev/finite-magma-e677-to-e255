# R-Z Source-Ladder Recurrence Absorption Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / R-Z is exactly the Z3 contribution to E11
```

## Purpose

This removes `R-Z` from:

```text
same_row_recurrence_inventory.md
```

as an independent recurrence branch.

`R-Z` is a same-ladder source recurrence in the fixed-target source-successor
orbit:

```text
r_{n+1}=r_n*A_j.
```

## Setup

In the Z3 paired shell, the two source ladders are:

```text
r_0=p,     r_{n+1}=r_n*A_j,
s_0=x_j,   s_{n+1}=s_n*A_j.
```

Each source row gives an edge in:

```text
H_{A_j}.
```

The ladder predecessor formula is:

```text
pred_{r_{n+1}}(A_j)=(r_n*r_{n+1})*r_n.
```

## Existing Reduction

The whole paired source-ladder analysis is recorded in:

```text
z3_paired_source_ladder_eventual_merge_lemma.md
clean_external_bridge_tenth_stage_reduction_lemma.md
```

Every first event in the paired ladders is one of:

```text
same input/output/cross-hit in H_{A_j},
full ported interval collision,
cross-ladder source hit,
same-ladder source repeat,
watched visible/generated hit.
```

All but same-ladder source repeat are routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
ported_interval_state_lemma.md
```

or by watched-hit routing.

## Consequence

The same-ladder source repeat is exactly the Z3 contribution to:

```text
E11. global same-row recurrence / minimal relay descent.
```

It is not an additional clean local branch.  Any attempt to expand it locally
just recreates the fixed-target ladder already handled by the tenth-stage
reduction.

So R-Z should be treated only through the global minimal relay-cycle measure:

```text
relay_minimality_measure_candidate.md
minimal_relay_cycle_dichotomy_candidate.md
```


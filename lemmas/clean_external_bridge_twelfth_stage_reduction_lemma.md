# Clean External-Bridge Twelfth-Stage Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / local recurrence inventory exhausted
```

## Purpose

This updates:

```text
clean_external_bridge_eleventh_stage_reduction_lemma.md
same_row_recurrence_inventory.md
```

using:

```text
rb5_beta_necklace_first_hit_reduction_lemma.md
rx_beta_chain_recurrence_absorption_lemma.md
rz_source_ladder_recurrence_absorption_lemma.md
local_swap_fixed_recurrence_classification.md
```

## Local Recurrence Exhaustion

The recurrence inventory contained:

```text
R-a, R-b1, R-b2, R-b3, R-b4, R-b5, R-x, R-Z.
```

The row-b cycle cases:

```text
R-b4, R-b5
```

are standard relay/base-bridge forms with local footprint descent or beta/Z3
coverage.

The beta-chain case:

```text
R-x
```

is absorbed by the beta-X route and existing recurrence reductions.

The source-ladder case:

```text
R-Z
```

is exactly the Z3 contribution to E11 and is handled only through the global
minimal relay-cycle measure.

The small local swap/fixed cases:

```text
R-a, R-b1, R-b2, R-b3
```

are visible/generated target-swap loops, generated A-X hits, or base-bridge
fixed-point boundaries.

## Twelfth-Stage Residual

After these reductions, the clean external bridge has no independent local
same-row recurrence branch left.

The remaining obstruction is exactly:

```text
G12. global minimal relay-cycle descent.
```

In other words, any hypothetical bad target now forces the existing global
No-Free-Tail problem:

```text
prove that a minimal closed relay cycle cannot consist only of same-source
ported recurrences without visible/core attachment, independent full
ported-interval collision, right fixer, or strict clean theta.
```

The local clean external bridge case tree is exhausted.

## Next Useful Target

Work directly on:

```text
relay_minimality_measure_candidate.md
minimal_relay_cycle_dichotomy_candidate.md
relay_termination_frontier.md
```

The next proof obligation is no longer a clean external bridge subcase.  It is
the global admissibility/descent sentence:

```text
Every regenerated relay object produced by a same-source recurrence is
admissible for the lexicographic measure M0-M4, unless it already creates
visible/core attachment, independent full ported-interval collision, or a
right fixer.
```

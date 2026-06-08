# Lemma Status

Date: 2026-06-08.

The project is active research.  This file distinguishes proved general
lemmas, bounded computational closures, and unproved candidates.

## Latest general proved lemmas

```text
lemmas/fan_tip_bridge_expansion_lemma.md
lemmas/fan_bridge_zipper_extension_lemma.md
lemmas/terminal_source_anchored_fan_lemma.md
```

They prove:

```text
each common-edge source produces a bridge;
each bridge produces a zipper return;
bridge collisions produce a new common-edge fan;
the terminal source is anchored to the old bad tail r_{m-2}.
```

## Fan-spine proved layer

```text
lemmas/two_sided_common_edge_fan_lemma.md
lemmas/fixed_source_zero_descent_lemma.md
lemmas/self_containing_fan_spine_lemma.md
lemmas/fan_spine_four_cycle_descent_lemma.md
lemmas/tip_source_collision_zero_tooth_lemma.md
lemmas/fan_tip_bad_cycle_alignment_lemma.md
lemmas/zero_tooth_bad_cycle_return_lemma.md
lemmas/fan_source_tip_graph_lemma.md
lemmas/minimal_bad_short_cycle_reduction.md
lemmas/fan_spine_fourth_predecessor_test.md
lemmas/fan_spine_length_five_badness_lemma.md
lemmas/good_p_occupied_tip_pressure_lemma.md
```

This layer proves two-sided fan pressure, several explicit descents, exclusion
of short harmless closures, and the exact boundary before a good six-cycle.

## Reconstruction and overlap layer

```text
lemmas/two_step_source_reconstruction_lemma.md
lemmas/paired_chain_aligned_overlap_lemma.md
lemmas/shared_edge_divergence_lemma.md
lemmas/common_edge_fan_lemma.md
lemmas/bad_cycle_shared_edge_descent_lemma.md
```

Important consequence:

```text
an ordered two-step interval determines its source row;
distinct source rows cannot share two aligned consecutive edges.
```

## Bounded computational closure

The normalized size-9 role

```text
u=b_3
```

is recorded as closed.  Its final two occupied tip roles closed in the recorded
diagnostics:

```text
C=b_7 -> status none, 46.31s, 640 nodes
C=b_6 -> status none, 28.37s, 410 nodes
```

This is finite evidence and must not be promoted to a general theorem.

## Current candidates, not proved

```text
lemmas/three_source_good_six_pressure_candidate.md
lemmas/fan_spine_termination_candidate.md
lemmas/main_bad_cycle_no_free_tail_lemma.md
```

The full statement `E677 => E255` remains unproved.

## Next valid step

Classify the first intersection of the three bridge paths with sources, fan
tips, the good six-cycle, and the terminal bad-cycle anchor.


# Lemma Status

Date: 2026-06-17.

The project is active research.  This file distinguishes proved general
lemmas, bounded computational closures, finite evidence, withdrawn claims, and
unproved candidates.

## Latest general proved lemmas

```text
lemmas/double_interval_edge_certificate_lemma.md
lemmas/general_target_bridge_orbit_lemma.md
lemmas/labeled_right_translation_graph_lemma.md
lemmas/right_p_orbit_bridge_recursion_lemma.md
lemmas/right_p_orbit_collision_duality_lemma.md
lemmas/cycle_entry_two_sided_fan_lemma.md
lemmas/cycle_entry_hub_transport_lemma.md
lemmas/good_p_unique_reverse_edge_lemma.md
lemmas/target_swap_fan_duality_lemma.md
lemmas/right_fixed_point_uniqueness_lemma.md
lemmas/right_fixer_to_balanced_witness_lemma.md
lemmas/bicyclic_component_branch_fan_lemma.md
lemmas/bad_target_core_fan_lemma.md
lemmas/bicyclic_core_junction_lemma.md
```

They prove the current bridge-recursion layer:

```text
every target edge q*a=b, q*b=c has a full local certificate;
right-target orbits create bridge labels;
first orbit repetition creates a new two-sided fan;
target swap converts outgoing and incoming fan pressure;
bicyclic target cores reduce to triple-fan or mixed 2+1 junction pressure.
```

## Previous proved fan and zipper layer

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

## Bounded computational closures

Sizes `5`, `6`, and `7` are now reproducible from this repository:

```text
verify_sizes_5_6_7_closed.ps1
logs/sizes_5_6_7_rerun_20260617_143540.txt
```

The script checks `38` normalized row-0 cases.

Size `8` remains reproducible from:

```text
verify_size8_closed.ps1
logs/size8_verified_split_log.txt
```

The normalized size-9 role

```text
u=b_3
```

is recorded as closed.  Its final two occupied tip roles closed in recorded
diagnostics:

```text
C=b_7 -> status none, 46.31s, 640 nodes
C=b_6 -> status none, 28.37s, 410 nodes
```

This size-9 material is finite evidence and must not be promoted to a general
theorem.

## Current candidates, not proved

```text
lemmas/branch_closure_no_free_tail_candidate.md
lemmas/crossed_double_fan_pressure_candidate.md
lemmas/main_bad_cycle_no_free_tail_lemma.md
```

The exact open symbolic task is to close the remaining branch configurations:

```text
triple core fan;
mixed 2+1 core junction.
```

## Finite evidence, not a lemma

Raw-label arbitrary E677 searches in sizes `6` and `7` did not produce a
crossed double-fan counterexample.  This is useful evidence, but it is not a
general proof.

## Withdrawn claims

The earlier size-8/9 crossed-fan and size-9 directed-diamond claims used an
invalid double normalization and are withdrawn.  They should not be counted as
closed cases.

The full statement `E677 => E255` remains unproved.

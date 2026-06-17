# Research Update: 2026-06-17

This update records two public-facing changes:

1. the finite closures for sizes `5`, `6`, and `7` are now packaged as a
   reproducible rerun script;
2. the current proof frontier has moved from the three-source good-six pressure
   picture to the branch-closure No-Free-Tail candidate.

## New reproducibility checkpoint

The repository now includes:

```text
verify_sizes_5_6_7_closed.ps1
verify_sizes_5_6_7_closed.cmd
logs/sizes_5_6_7_rerun_20260617_143540.txt
```

The recorded rerun checks every normalized row-0 representative for sizes
`5`, `6`, and `7`:

```text
size 5: 7 cases
size 6: 12 cases
size 7: 19 cases
total: 38 cases
```

Every case ended with:

```text
status: none
```

This upgrades the public status of sizes `5`, `6`, and `7` from recorded
closures to directly rerunnable computational checkpoints.

## Updated search tool

The public `tools/search_counterexample_strong.js` file has been updated to
the current working version.  It still supports the size-8 verification script
and now also supports the packaged sizes `5`-`7` verification.

## Structural update

The latest proof layer generalizes the old common-edge bridge mechanism to an
arbitrary target edge.

For fixed target `b`, define:

```text
A_b(q) = the unique a such that q*a=b
R_b(q) = q*b.
```

For every edge:

```text
q*a=b
q*b=c,
```

the project now records a complete local certificate:

```text
row q: beta -> a -> b -> c
row c: q -> pred_b(a), A_b(c) -> b
row b: pred_b(a) -> a.
```

This is the basis of the branch-closure reduction.

## New proved layer

The new public lemma files include:

```text
double_interval_edge_certificate_lemma.md
general_target_bridge_orbit_lemma.md
labeled_right_translation_graph_lemma.md
right_p_orbit_bridge_recursion_lemma.md
right_p_orbit_collision_duality_lemma.md
cycle_entry_two_sided_fan_lemma.md
cycle_entry_hub_transport_lemma.md
good_p_unique_reverse_edge_lemma.md
target_swap_fan_duality_lemma.md
right_fixed_point_uniqueness_lemma.md
right_fixer_to_balanced_witness_lemma.md
bicyclic_component_branch_fan_lemma.md
bad_target_core_fan_lemma.md
bicyclic_core_junction_lemma.md
```

## Current open candidate

The remaining candidate is:

```text
branch_closure_no_free_tail_candidate.md
```

with the related pressure candidate:

```text
crossed_double_fan_pressure_candidate.md
```

The exact open task is to rule out the remaining branch-closure configurations:

```text
triple core fan;
mixed 2+1 core junction.
```

## Audit correction

The earlier size-8/9 crossed-fan and size-9 directed-diamond claims used an
invalid double normalization and are withdrawn.  They should not be cited as
closed cases.

## Boundary

The No-Free-Tail Lemma and the full implication `E677 => E255` remain unproved.

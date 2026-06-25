# Lemma Status

Date: 2026-06-25.

This file is a compact public map.  It separates proved reductions,
boundaries, candidates, diagnostics, and experimental templates.

## Current Active Frontier

```text
shared-step anchored triangle / anchored-X3 / M7
clean same-orbit right-h self-repeat
```

Start from:

```text
NEXT_ACTION.md
docs/CURRENT_FRONTIER.md
docs/RESULTS_INDEX.md
```

## Proved or Routed Reductions in the Current Layer

The following files are recorded as proved reductions or routing lemmas in the
current public layer:

```text
lemmas/anchored_m7_first_event_routing_lemma.md
lemmas/anchored_x3_second_triangle_pressure_lemma.md
lemmas/anchored_x3_visible_short_repeat_lemma.md
lemmas/beta_coupled_same_target_pair_advance_lemma.md
lemmas/beta_equals_h_shared_edge_divergence_lemma.md
lemmas/beta_layer_reduction_lemma.md
lemmas/beta_x_bridge_pair_reversible_square_lemma.md
lemmas/beta_zipper_shifted_repeat_split_lemma.md
lemmas/clean_external_bridge_first_hit_reduction_lemma.md
lemmas/clean_external_bridge_second_stage_reduction_lemma.md
lemmas/clean_external_bridge_third_stage_reduction_lemma.md
lemmas/clean_external_bridge_fourth_stage_reduction_lemma.md
lemmas/clean_external_bridge_fifth_stage_reduction_lemma.md
lemmas/clean_external_bridge_sixth_stage_reduction_lemma.md
lemmas/clean_external_bridge_seventh_stage_reduction_lemma.md
lemmas/clean_external_bridge_eighth_stage_reduction_lemma.md
lemmas/clean_external_bridge_ninth_stage_reduction_lemma.md
lemmas/clean_external_bridge_tenth_stage_reduction_lemma.md
lemmas/clean_external_bridge_eleventh_stage_reduction_lemma.md
lemmas/clean_external_bridge_twelfth_stage_reduction_lemma.md
lemmas/cross_tip_collision_target_advance_lemma.md
lemmas/fixed_target_source_orbit_ladder_lemma.md
lemmas/fixed_target_source_successor_lemma.md
lemmas/fresh_beta_extension_eventual_x_hit_lemma.md
lemmas/generated_input_three_source_bridge_expansion_lemma.md
lemmas/rb5_beta_necklace_first_hit_reduction_lemma.md
lemmas/source_successor_eventual_predecessor_hit_lemma.md
lemmas/two_row_first_extra_intersection_routing_lemma.md
lemmas/x3_advanced_edge_triangle_pressure_lemma.md
lemmas/y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
lemmas/y3_commuting_second_step_reduction_lemma.md
lemmas/y3_shared_successor_watched_hit_routing_lemma.md
lemmas/z3_paired_source_ladder_eventual_merge_lemma.md
```

This list is intentionally not a substitute for the files themselves.  Each
file states its own assumptions and boundary.

## Boundary and Normal-Form Files

Boundary files record exact residual shapes.  They should not be cited as
contradictions by themselves:

```text
lemmas/anchored_m7_cycle_end_template.md
lemmas/anchored_m7_first_merge_target.md
lemmas/anchored_x3_clean_self_repeat_normal_form.md
lemmas/anchored_x3_source_orbit_boundary.md
lemmas/anchored_x3_three_target_bridge_boundary.md
lemmas/beta_layer_first_hit_boundary.md
lemmas/clean_ported_matching_predecessor_layer_boundary.md
lemmas/general_v3_bridge_descent_boundary.md
lemmas/minimal_g12_loop_normal_form_boundary.md
lemmas/ported_interval_recurrence_boundary.md
lemmas/proper_crossed_fan_clean_external_bridge_boundary.md
lemmas/relay_same_source_return_split_boundary.md
lemmas/row_b_predecessor_tower_dichotomy_boundary.md
lemmas/shared_step_anchored_triangle_boundary.md
lemmas/two_row_orbit_theta_boundary.md
lemmas/y3_fixed_target_source_orbit_boundary.md
lemmas/y3_three_cycle_first_intersection_boundary.md
```

## Candidates

The following are active or supporting candidates, not proved theorems:

```text
lemmas/anchored_x3_rank_measure_candidate.md
lemmas/clean_external_bridge_predecessor_chain_candidate.md
lemmas/crossed_double_fan_pressure_candidate.md
lemmas/minimal_relay_cycle_dichotomy_candidate.md
lemmas/rb5_beta_necklace_reduction_candidate.md
lemmas/relay_minimality_measure_candidate.md
lemmas/relay_termination_frontier.md
```

## Diagnostics

Diagnostics are bounded evidence or model-pattern checks.  They are useful but
do not prove the full theorem:

```text
lemmas/anchored_identity_negation_raw_diagnostic.md
lemmas/anchored_m7_saturation_diagnostic.md
lemmas/anchored_d_term_strong_branch_raw_diagnostic.md
lemmas/clean_first_extra_pattern_raw_diagnostic.md
lemmas/m496_anchored_d_term_scan_diagnostic.md
lemmas/m496_first_extra_intersection_roles_diagnostic.md
lemmas/m496_shared_step_anchored_triangle_diagnostic.md
lemmas/m496_shared_step_orbit_split_diagnostic.md
lemmas/m496_shared_step_relation_scan_diagnostic.md
lemmas/m496_target_advance_period_diagnostic.md
lemmas/y3_shell_saturation_diagnostic.md
```

## ATP Templates

The ATP files are experimental templates:

```text
atp/anchored_x3_m7_self_repeat.p
atp/anchored_m7_cycle_end.p
atp/check_atp_environment.ps1
```

They provide a concrete local working surface for theorem provers.  They are
not formal verification of `E677 => E255`.

## Still Open

```text
anchored identity U*h=W*h in full generality;
clean same-orbit right-h self-repeat closure;
global No-Free-Tail Lemma;
E677 => E255 for all finite magmas.
```

# Next Action

Date: 2026-06-18.

Read this file first.  Then read `CURRENT_FRONTIER.md` only if more context is
needed.

## Current Goal

Continue the E677 -> E255 proof through the bad-target crossed-fan route.

Do not restart broad case search.

## Current Narrow Frontier

The clean proper bad-target crossed-fan residual has:

```text
h!=k,
{c,d} ∩ {u,v}=empty,
t=a*b,
k -> t in H_b,
ell=t*a=pred_b(k),
b*ell=k.
```

The right-`b` orbit is:

```text
x_0=a,
x_1=t,
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b).
```

Each row `x_i` gives:

```text
A_i -> x_{i+1}
```

in `H_b`.

## Important Correction

The right-`b` orbit is not itself an `H_b` path.  Consecutive generated
`H_b` edges do not automatically concatenate.

Use the stronger full ported states:

```text
E_i=(b,A_i,x_{i+1}).
```

## Next Proof Target

Prove a connector lemma:

```text
A closed ported-transition cycle from the clean external bridge must either
hit the visible crossed-fan footprint, create an independent full-interval
collision, become core-attached, or reduce to same-row recurrence.
```

Start from:

```text
clean_external_bridge_first_hit_reduction_lemma.md
generated_input_cross_source_pressure_lemma.md
beta_layer_first_hit_boundary.md
beta_equals_h_shared_edge_divergence_lemma.md
beta_a_hit_same_input_split_boundary.md
beta_x_hit_target_bridge_boundary.md
beta_x_bridge_pair_reversible_square_lemma.md
beta_layer_reduction_lemma.md
x_layer_two_target_bridge_reduction_lemma.md
same_input_split_target_lift_lemma.md
clean_external_bridge_second_stage_reduction_lemma.md
fresh_reversible_square_beta_anchor_lemma.md
beta_fresh_predecessor_zipper_ladder_lemma.md
beta_fresh_extension_first_hit_boundary.md
beta_zipper_shifted_repeat_split_lemma.md
beta_zipper_clean_cycle_boundary.md
fresh_beta_extension_eventual_x_hit_lemma.md
deep_beta_x_hit_reduction_lemma.md
clean_external_bridge_third_stage_reduction_lemma.md
same_target_pair_collision_trichotomy_lemma.md
beta_coupled_same_target_pair_advance_lemma.md
same_input_lift_target_advance_lemma.md
clean_external_bridge_fourth_stage_reduction_lemma.md
beta_anchor_row_b_partner_reduction_lemma.md
clean_external_bridge_fifth_stage_reduction_lemma.md
generated_input_three_source_bridge_expansion_lemma.md
row_b_generated_input_bridge_lemma.md
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
clean_external_bridge_sixth_stage_reduction_lemma.md
x3_three_edge_matching_advance_boundary.md
x3_advanced_edge_triangle_pressure_lemma.md
x3_self_renewal_boundary.md
source_successor_eventual_predecessor_hit_lemma.md
clean_external_bridge_seventh_stage_reduction_lemma.md
clean_ported_matching_predecessor_layer_boundary.md
row_b_predecessor_tower_dichotomy_boundary.md
row_b_tower_first_hit_role_map.md
ported_cycle_hb_footprint_trichotomy_lemma.md
right_b_orbit_repeat_core_attachment_gap.md
right_b_orbit_ported_transition_lemma.md
proper_crossed_fan_clean_external_bridge_boundary.md
```

New split to use:

```text
A-repeat    -> outgoing fan in H_b;
X-repeat    -> incoming fan in H_b;
A-X hit     -> actual H_b path concatenation;
no such hit -> clean two-layer matching residual.
```

In the clean residual, use:

```text
H_i --row b--> A_i --H_b edge/source x_i--> x_{i+1}.
```

Next split:

```text
H_i hits X, A, visible footprint, or H_i=A_i;
otherwise the row-b predecessor layer extends backward.
```

First-hit role map:

```text
H_i=A_j -> row-b tower cross-hit H_j -> A_j -> A_i;
H_i=x_j -> two-target bridge with rows b and x_j;
H_i visible -> core attachment;
H_i=A_i -> row-b fixed point boundary.
```

Current exact residual split:

```text
clean_external_bridge_eleventh_stage_reduction_lemma.md
```

After routing G, beta-X, fresh beta extension, clean same-target matchings,
V4 beta anchors, base row-b/generated bridge, and X3 target-advance layers,
then removing the Y2 shared-edge branch and routing the Z3 paired source
ladder to its first finite merge/repeat, then routing R-b4/R-b5 row-b
recurrence to standard relay forms, the current residual is:

```text
E11. global same-row recurrence / minimal relay descent.
```

The old Y2 branch:

```text
Beta_i=H_i
```

folds into the already routed base row-b/generated bridge by:

```text
y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
```

The old Y3 branch is sharpened and routed by:

```text
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_successor_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
fixed_target_source_orbit_ladder_lemma.md
y3_fixed_target_source_orbit_boundary.md
y3_shared_successor_square_boundary.md
y3_shared_successor_watched_hit_routing_lemma.md
y3_commuting_second_step_reduction_lemma.md
y3_clean_square_four_edge_matching_boundary.md
y3_four_edge_matching_target_advance_boundary.md
clean_external_bridge_ninth_stage_reduction_lemma.md
z3_paired_source_ladder_eventual_merge_lemma.md
clean_external_bridge_tenth_stage_reduction_lemma.md
y3_shell_saturation_diagnostic.md
```

Next target: attack the unified same-row recurrence inventory.

Use:

```text
same_row_recurrence_inventory.md
clean_external_bridge_to_relay_recurrence_frontier.md
rb4_first_repeat_target_swap_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb5_a_layer_footprint_descent_boundary.md
clean_external_bridge_eleventh_stage_reduction_lemma.md
```

The row-b target has been sharpened:

```text
R-b4/R-b5: closed right-b and row-b A/predecessor cycles.
```

R-b4 is a first-merge target-swap relay.  R-b5 is a closed chain of base
row-b/generated bridge A-hits.

R-b4 internal repeats have smaller right-`b` footprint; R-b5 internal repeats
have smaller A-layer footprint.  Next target: integrate these local footprint
measures with the global minimal relay-cycle measure.  The remaining hard
cases are start-return minimal cycles, visible core hit, or repeated full
ported interval in an independent branch role.

Use the global relay framing:

```text
clean_external_bridge_to_relay_recurrence_frontier.md
minimal_relay_cycle_dichotomy_candidate.md
relay_termination_frontier.md
```

Do not restart X3/Z3 from the old three-edge matching or shared-successor
square.

Use:

```text
same_input_lift_target_advance_lemma.md
same_target_pair_collision_trichotomy_lemma.md
beta_coupled_same_target_pair_advance_lemma.md
beta_anchor_row_b_partner_reduction_lemma.md
clean_external_bridge_fifth_stage_reduction_lemma.md
generated_input_three_source_bridge_expansion_lemma.md
row_b_generated_input_bridge_lemma.md
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
clean_external_bridge_sixth_stage_reduction_lemma.md
x3_three_edge_matching_advance_boundary.md
x3_advanced_edge_triangle_pressure_lemma.md
x3_self_renewal_boundary.md
source_successor_eventual_predecessor_hit_lemma.md
clean_external_bridge_seventh_stage_reduction_lemma.md
y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_successor_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
fixed_target_source_orbit_ladder_lemma.md
y3_fixed_target_source_orbit_boundary.md
y3_shared_successor_square_boundary.md
y3_shared_successor_watched_hit_routing_lemma.md
y3_commuting_second_step_reduction_lemma.md
y3_clean_square_four_edge_matching_boundary.md
y3_four_edge_matching_target_advance_boundary.md
clean_external_bridge_ninth_stage_reduction_lemma.md
z3_paired_source_ladder_eventual_merge_lemma.md
clean_external_bridge_eighth_stage_reduction_lemma.md
clean_external_bridge_tenth_stage_reduction_lemma.md
same_row_recurrence_inventory.md
clean_external_bridge_to_relay_recurrence_frontier.md
rb4_first_repeat_target_swap_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb5_a_layer_footprint_descent_boundary.md
clean_external_bridge_eleventh_stage_reduction_lemma.md
```

only as already-proved transports.  Do not route G, beta-X, fresh beta
extension, or clean same-target matching from scratch again.

Additional beta-layer progress:

```text
Beta_i=H_i -> shared-edge divergence of rows b and x_i at H_i -> A_i,
              then folds into the base row-b/generated bridge.
Beta_i=A_j -> same-input split lifted into H_{A_j}: E_{i,j}->A_i and Beta_j->b.
Beta_i=x_j -> reversible square: (A_i,x_j,b)<->(x_j,delta,A_i) and (b,A_j,x_{j+1})<->(A_j,Beta_j,b).
alpha=A_j -> G same-input split couples to Beta_j in H_{A_j}.
```

## Do Not Repeat

Do not rerun broad size-8 crossed-fan timeouts.

Do not expect `t*b=a`, `t*b=t`, `t*b=h`, or `t*b=k` to close locally; these
were checked and routed in:

```text
right_b_orbit_second_successor_boundary.md
```

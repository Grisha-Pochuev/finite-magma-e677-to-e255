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
clean_external_bridge_twelfth_stage_reduction_lemma.md
```

After routing G, beta-X, fresh beta extension, clean same-target matchings,
V4 beta anchors, base row-b/generated bridge, and X3 target-advance layers,
then removing the Y2 shared-edge branch and routing the Z3 paired source
ladder to its first finite merge/repeat, then routing R-b4/R-b5 row-b
recurrence to standard relay forms and exhausting the local recurrence
inventory, the current residual is:

```text
G12. global minimal relay-cycle descent.
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

Next target: attack the remaining global same-row recurrence / minimal relay
descent.

Use:

```text
same_row_recurrence_inventory.md
clean_external_bridge_to_relay_recurrence_frontier.md
rb4_first_repeat_target_swap_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb5_a_layer_footprint_descent_boundary.md
rb5_start_return_a_cycle_beta_pair_boundary.md
rb5_beta_necklace_reduction_candidate.md
rb5_beta_necklace_first_hit_reduction_lemma.md
rx_beta_chain_recurrence_absorption_lemma.md
rz_source_ladder_recurrence_absorption_lemma.md
local_swap_fixed_recurrence_classification.md
clean_external_bridge_eleventh_stage_reduction_lemma.md
clean_external_bridge_twelfth_stage_reduction_lemma.md
```

The row-b target has been sharpened:

```text
R-b4/R-b5: closed right-b and row-b A/predecessor cycles.
```

R-b4 is a first-merge target-swap relay.  R-b5 is a closed chain of base
row-b/generated bridge A-hits.

R-b4 internal repeats have smaller right-`b` footprint; R-b5 internal repeats
have smaller A-layer footprint; the R-b5 start-return beta necklace is routed.
Next target: integrate these local footprint measures with the global minimal
relay-cycle measure.  The remaining hard cases are visible core hit, repeated
full ported interval in an independent branch role, or same-source recurrence
outside the row-b R-b4/R-b5 subtypes.

Latest narrow result:

```text
rb5_beta_necklace_first_hit_reduction_lemma.md
```

The finite first-hit coverage around a minimal R-b5 A-cycle is routed to
existing beta/Z3 reductions, visible hit, independent full interval collision,
or same-row recurrence.

Next target: return to the global minimal relay descent for the surviving
same-row recurrence cases outside row-b R-b4/R-b5.

After R-x and R-Z are absorbed, the small swap/fixed list is classified by:

```text
local_swap_fixed_recurrence_classification.md
```

The local recurrence inventory now has no independent fresh branch.  The
remaining target is purely global: prove the minimal relay-cycle descent or
force an independent full ported-interval collision/right fixer.

Current exact target:

```text
relay_minimality_measure_candidate.md
minimal_relay_cycle_dichotomy_candidate.md
relay_termination_frontier.md
relay_same_source_return_split_boundary.md
fixed_target_same_source_return_collapse_lemma.md
target_advance_same_row_period_lemma.md
m496_target_advance_period_diagnostic.md
two_row_target_advance_window_separation_lemma.md
two_row_orbit_theta_boundary.md
two_row_first_extra_intersection_routing_lemma.md
clean_first_extra_matching_bridge_alignment.md
general_v3_bridge_descent_boundary.md
shared_step_anchored_triangle_boundary.md
m496_shared_step_anchored_triangle_diagnostic.md
anchored_identity_negation_raw_diagnostic.md
anchored_identity_partial_reduction.md
m496_shared_step_relation_scan_diagnostic.md
anchored_x3_three_target_bridge_boundary.md
anchored_x3_second_triangle_pressure_lemma.md
anchored_x3_source_orbit_boundary.md
anchored_x3_rank_measure_candidate.md
anchored_x3_visible_short_repeat_lemma.md
anchored_x3_clean_self_repeat_normal_form.md
m496_shared_step_orbit_split_diagnostic.md
m496_first_extra_intersection_roles_diagnostic.md
clean_first_extra_pattern_raw_diagnostic.md
minimal_g12_loop_normal_form_boundary.md
```

The global admissibility/descent sentence is now sharpened to the G12 normal
form:

```text
minimal_g12_loop_normal_form_boundary.md
```

Next target: show that a closed relay loop made only of same-source
target-advance recurrences is either strict clean theta or contains an
independent repeated full ported interval.

The fixed-target ambiguity is now removed by:

```text
fixed_target_same_source_return_collapse_lemma.md
```

so the remaining same-source case is only the moving target-advance row-orbit
case, not a new second return inside one fixed `H_b`.

The moving same-source case is narrowed further by:

```text
target_advance_same_row_period_lemma.md
```

Periods 1 and 2 are local fixed/swap recurrences; the real remaining G12 loop
must use coupled same-row target-advance cycles of period at least 3.

The M496 diagnostic:

```text
m496_target_advance_period_diagnostic.md
```

shows that known E677 behavior has row periods `1,5,10,30`, so the period
`>= 3` residue is not a merely formal leftover.

The local two-row window inside this residue is separated by:

```text
two_row_target_advance_window_separation_lemma.md
```

Thus the next obstruction is global: a loop assembled only from separated
period `>= 3` two-row windows, with no independent full interval collision and
no strict clean theta.

This global obstruction is now split in:

```text
two_row_orbit_theta_boundary.md
```

Next target: route the first extra intersection of the two row cycles, or
translate the clean orbit-theta branch to strict clean theta.

The first extra intersection is now routed by:

```text
two_row_first_extra_intersection_routing_lemma.md
```

The remaining live branch from that route is the clean same-input two-target
bridge after target advance.

That branch is aligned with the V3-type bridge frontier in:

```text
clean_first_extra_matching_bridge_alignment.md
```

The M496 shared-step diagnostic:

```text
m496_shared_step_orbit_split_diagnostic.md
```

found no clean orbit-theta pairs and found an extra cycle intersection for
every shared-step row pair.  This suggests prioritizing the clean same-input
two-target bridge left by the first-extra-intersection route.

The first-extra role diagnostic:

```text
m496_first_extra_intersection_roles_diagnostic.md
```

found that M496 first extra intersections are always same-output fans; clean
matching is absent.  The next structural target is to prove this
clean-disjoint first-extra matching impossible in a minimal G12 loop, ideally
by proving the same-output fan pattern, or to route it to an already measured
two-target bridge descent.

After the bridge-alignment file, the clean-disjoint branch should be treated
as a general V3-type bridge descent/admissibility problem, not as a new
same-row recurrence.

The exact descent obligation is now isolated in:

```text
general_v3_bridge_descent_boundary.md
```

It extends the measure candidate by `M5` first-extra offset and `M6` clean V3
bridge rank.

New stronger route to try first:

```text
shared_step_anchored_triangle_boundary.md
m496_shared_step_anchored_triangle_diagnostic.md
```

For a shared step `p*b=q*b=z`, define `U=p*z`, `W=q*z`, and
`h=U*p=W*q=pred_z(b)`.  M496 satisfies `U*h=W*h` for all `892800`
shared-step pairs.  If this identity is proved generally, it gives an
incoming fan in `H_h` and bypasses both clean first-extra V3 and clean
orbit-theta branches.

Immediate algebraic proof target:

```text
p*b=q*b,
U=p*(p*b),
W=q*(p*b),
h=U*p=W*q
=> U*h=W*h.
```

The negation diagnostic:

```text
anchored_identity_negation_raw_diagnostic.md
```

shows short closure `ok`; both 60-second and 300-second size-9 rawmodel
searches timed out without finding a model.  Treat this as support only, not
proof.

The partial reduction:

```text
anchored_identity_partial_reduction.md
```

shows that with `T=U*h` and `S=W*h`, the negated branch satisfies:

```text
h*(T*U)=p,
h*(S*W)=q,
(h*(T*U))*b=(h*(S*W))*b=z.
```

So the next proof target is to rule out this anchored back-projected shared
step, or route it as a new measured residual.

The M496 neighboring-relation scan:

```text
m496_shared_step_relation_scan_diagnostic.md
```

found no additional universal short equality among `p*U`, `q*W`, `U*T`,
`W*T`, `z*T`, `T*b`, `T*h`, `h*p`, and `h*q`.  So the next route should be
structural, not another guessed one-step equality.

The false branch is classified in:

```text
anchored_x3_three_target_bridge_boundary.md
```

If `T=U*h` and `S=W*h` are distinct, then the clean local case target-advances
to:

```text
H_T: h -> U*T,
H_S: h -> W*S,
H_b: h -> z*b.
```

This is the exact anchored-X3 residual.  Next prove `T=S`, or show this
three-target same-input bridge is a smaller measured relay object.

The anchored-X3 false branch has additional pressure:

```text
anchored_x3_second_triangle_pressure_lemma.md
```

It forces a second triangle layer back in `H_h`:

```text
row T: (U*T)*U -> T*h,
row S: (W*S)*W -> S*h,
row b: (z*b)*z -> b*h.
```

Next target: prove this second layer hits the original anchored layer, old
visible/core footprint, or a full ported interval; otherwise introduce a
measured anchored-X3 rank.

The correct clean continuation is now:

```text
anchored_x3_source_orbit_boundary.md
```

It converts the anchored-X3 false branch into three fixed-target source
orbits in `H_h`:

```text
U -> T -> T*h -> ...
W -> S -> S*h -> ...
z -> b -> b*h -> ...
```

Next exact target: classify the first repeat/merge of these three orbits, or
define the anchored-X3 rank needed for the clean self-return case.

The measure candidate is:

```text
anchored_x3_rank_measure_candidate.md
```

It adds `M7`: the first-event rank of the three right-`h` source orbits
starting from `U,W,z`.  Next prove M7 descent for a clean self-repeat, or
isolate the exact clean self-repeat subcase that fails descent.

Short visible self-repeats are removed by:

```text
anchored_x3_visible_short_repeat_lemma.md
```

Initial period 1 or 2 in:

```text
U -> T -> ...
W -> S -> ...
z -> b -> ...
```

hits the displayed anchored layer and is not clean.  The live M7 self-repeat
is only a later/fresh right-`h` repeat or a return to the initial source after
at least three steps.

The exact remaining self-repeat normal form is:

```text
anchored_x3_clean_self_repeat_normal_form.md
```

It is a closed right-`h` source-successor cycle in `H_h`.  It is not
automatically an `H_h` directed path and not a left-row period.  Next prove it
creates strict clean theta, an independent full interval, a smaller M7 object,
or a core hit.

The raw diagnostic:

```text
clean_first_extra_pattern_raw_diagnostic.md
```

shows that the clean first-extra pattern is not killed by short closure, and a
60-second size-9 rawmodel search timed out without finding a model.  Do not
claim this branch impossible from computation alone.

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
rb5_start_return_a_cycle_beta_pair_boundary.md
rb5_beta_necklace_reduction_candidate.md
rb5_beta_necklace_first_hit_reduction_lemma.md
rx_beta_chain_recurrence_absorption_lemma.md
rz_source_ladder_recurrence_absorption_lemma.md
local_swap_fixed_recurrence_classification.md
clean_external_bridge_eleventh_stage_reduction_lemma.md
clean_external_bridge_twelfth_stage_reduction_lemma.md
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

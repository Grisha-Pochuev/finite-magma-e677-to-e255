# Current Frontier: E677 -> E255

Date: 2026-06-18.

Read this file first at the start of a new run.  Do not start from
`research_log.md`, `PROJECT_STATUS.md`, or old stop checkpoints unless a
specific derivation needs auditing.

## Problem

For a finite magma satisfying:

```text
E677: x = y*(x*((y*x)*y))
```

prove:

```text
E255: x = ((x*x)*x)*x.
```

No associativity is assumed.

## Standing Core Facts

In every finite E677 magma, each left row:

```text
L_y(x)=y*x
```

is a permutation.  Thus left cancellation and row-predecessors are available.

For a fixed target `b`, define:

```text
A_b(q)=the unique a with q*a=b,
R_b(q)=q*b.
```

Row `q` gives an oriented edge in `H_b`:

```text
A_b(q) -> R_b(q)
```

and a full ported interval:

```text
(target,input,output) = (b,A_b(q),R_b(q)).
```

The full ported interval determines the source row.  Bridge pairs alone are
too weak.  Use:

```text
ported_interval_state_lemma.md
ported_interval_recurrence_boundary.md
target_advance_row_orbit_lemma.md
```

## Bad Target Reduction

If `b` is a bad E255 target, then:

```text
q*b != b
```

for every row `q`.  Therefore no edge of `H_b` uses `b` as output, and the
usual bad-target core argument gives:

```text
bad target
=> bicyclic component of H_b
=> core junction
=> triple fan or mixed 2+1 junction.
```

Reference files:

```text
bicyclic_component_branch_fan_lemma.md
bad_target_core_fan_lemma.md
bicyclic_core_junction_lemma.md
```

## Local Relay Reductions Already Proved

The local branch-closure shapes are no longer independent terminal cases.
They relay back to triple fan / mixed `2+1`, except for the global termination
problem.

Use:

```text
target_swap_fan_duality_lemma.md
mixed_junction_target_swap_bridge_square.md
first_merge_certificate_separation_lemma.md
first_merge_target_swap_junction_dichotomy.md
pure_incoming_merge_target_swap_fan_lemma.md
binary_sink_core_escape_lemma.md
earliest_side_attachment_mixed_junction_lemma.md
side_attachment_orientation_reduction_lemma.md
minority_core_return_relay_lemma.md
strict_clean_theta_exclusion_lemma.md
```

Current global relay frontier:

```text
relay_termination_frontier.md
minimal_relay_cycle_dichotomy_candidate.md
```

Important: strict clean theta is excluded.  The remaining issue is not local
classification; it is recurrence/termination of the relay chain.

## Warning: Avoid The Circular Witness Route

Do not rely on the old directed two-edge right-fixer candidate:

```text
Y=(b*c)*(u*k)
```

Diagnostics show this candidate collapses to the canonical E255 term
`((b*b)*b)` in known samples.  Proving `Y*b=b` after that is just the original
target again.

Reference:

```text
directed_two_edge_canonical_collapse_boundary.md
```

## Active Crossed-Fan Frontier

For a bad target `b`, a figure-eight closure would create a crossed fan:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

with:

```text
c*p=d*q=h=pred_b(a),
u*r=v*s=k=pred_a(b),
b*h=a,
a*k=b.
```

The broad crossed-fan target is:

```text
bad_target_crossed_fan_boundary.md
crossed_double_fan_pressure_candidate.md
figure_eight_closure_crossed_fan_boundary.md
```

Do not restart from the broad statement unless needed.  The useful current
object is the proper bad-target clean residual.

## Routed Crossed-Fan Cases

Already routed:

```text
crossed_fan_swap_row_degeneracy_lemma.md
swap_row_target_advance_loop_lemma.md
crossed_fan_cross_tip_hub_separation_lemma.md
crossed_fan_equal_hub_side_incidence_lemma.md
cross_tip_collision_target_advance_lemma.md
proper_crossed_fan_target_swap_self_duality_lemma.md
bad_target_crossed_fan_row_a_edge_lemma.md
bad_target_no_predecessor_output_lemma.md
bad_target_row_a_output_avoids_b_hub_lemma.md
row_a_bridge_edge_attachment_cases.md
row_a_bridge_loop_recurrence_boundary.md
row_a_bridge_second_certificate_lemma.md
row_a_second_bridge_visible_hit_cases.md
clean_external_bridge_row_b_predecessor_fan_lemma.md
clean_external_bridge_three_source_predecessor_fan_lemma.md
clean_external_bridge_new_source_row_lemma.md
```

Important routed facts:

```text
h=k       -> cross tips are disjoint, plus row-a bridge edge;
{c,d}∩{u,v} != empty -> target-advance relay;
t=a*b=h   -> impossible for bad b;
t=a*b=k   -> same-row recurrence loop;
k or t hitting visible footprints -> routed attachment.
```

## Clean External-Bridge Residual

After routing, the clean crossed-fan residual may assume:

```text
h!=k,
{c,d} ∩ {u,v}=empty,
t=a*b,
k -> t is a real H_b edge,
k,t not in {a,c,d,u,v},
t not in {b,h,k}.
```

The second certificate gives:

```text
ell=t*a=pred_b(k),
b*ell=k,
ell!=h.
```

So row `b` contains a predecessor fan:

```text
b*h=a,
b*ell=k,
h!=ell,
a!=k.
```

Active files:

```text
proper_crossed_fan_clean_external_bridge_boundary.md
clean_external_bridge_predecessor_chain_candidate.md
bad_target_right_b_orbit_predecessor_recursion_lemma.md
right_b_orbit_local_repeat_roles.md
right_b_orbit_second_successor_boundary.md
right_b_orbit_first_repeat_boundary.md
right_b_orbit_first_repeat_fan_lemma.md
right_b_orbit_repeat_core_attachment_gap.md
right_b_orbit_ported_transition_lemma.md
ported_cycle_hb_footprint_trichotomy_lemma.md
clean_ported_matching_predecessor_layer_boundary.md
row_b_predecessor_tower_dichotomy_boundary.md
row_b_tower_first_hit_role_map.md
row_b_a_layer_cycle_boundary.md
row_b_x_layer_hit_target_bridge_boundary.md
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
y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_successor_lemma.md
y3_fixed_target_source_orbit_boundary.md
clean_external_bridge_eighth_stage_reduction_lemma.md
y3_shell_saturation_diagnostic.md
y3_shared_successor_square_boundary.md
y3_shared_successor_watched_hit_routing_lemma.md
y3_commuting_second_step_reduction_lemma.md
y3_clean_square_four_edge_matching_boundary.md
y3_four_edge_matching_target_advance_boundary.md
clean_external_bridge_ninth_stage_reduction_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
fixed_target_source_orbit_ladder_lemma.md
z3_paired_source_ladder_eventual_merge_lemma.md
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

## Right-b Orbit Status

Start:

```text
x_0=a,
x_1=t=a*b,
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
x_i*A_i=b.
```

Each row `x_i` gives an `H_b` edge:

```text
A_i -> x_{i+1}.
```

But the right-`b` orbit itself is not an `H_b` path: the next edge starts at
`A_{i+1}`, not at `x_{i+1}`.  This is the connector gap:

```text
right_b_orbit_repeat_core_attachment_gap.md
```

The stronger correct state is the ported interval:

```text
E_i=(b,A_i,x_{i+1})
```

and these states have a canonical transition because the output/source row
advances:

```text
right_b_orbit_ported_transition_lemma.md
```

First repeat of the right-`b` orbit creates an incoming fan in `H_b`, but it
is not yet proved to be attached to the original cyclic core.

The generated `H_b` footprint now has a proved trichotomy:

```text
A_i=A_j          -> outgoing fan in H_b;
x_{i+1}=x_{j+1}  -> incoming fan in H_b;
A_i=x_{j+1}      -> actual H_b path concatenation.
```

Reference:

```text
ported_cycle_hb_footprint_trichotomy_lemma.md
```

If none of these routed/generated incidences occurs, the remaining footprint
is a clean matching:

```text
A_i -> x_{i+1}
```

plus the row-`b` predecessor arrows:

```text
b*H_i=A_i.
```

This clean two-layer residual is recorded in:

```text
clean_ported_matching_predecessor_layer_boundary.md
```

It gives:

```text
H_i=H_j <=> A_i=A_j.
```

So once the `A_i` are pairwise distinct, the predecessor labels `H_i` are
pairwise distinct too.  The next hit to classify is:

```text
H_i in X, H_i in A, H_i in visible footprint, or H_i=A_i.
```

The first-hit role map is:

```text
H_i=A_j       -> row-b tower cross-hit H_j -> A_j -> A_i;
H_i=x_j       -> two-target bridge involving rows b and x_j;
H_i visible   -> core attachment;
H_i=A_i       -> row-b fixed point boundary;
no hit        -> extend the row-b predecessor tower backward.
```

References:

```text
row_b_predecessor_tower_dichotomy_boundary.md
row_b_tower_first_hit_role_map.md
row_b_a_layer_cycle_boundary.md
row_b_x_layer_hit_target_bridge_boundary.md
clean_external_bridge_first_hit_reduction_lemma.md
```

The clean external bridge first-hit reduction left exact alternatives:

```text
A-D: generated H_b fan/path or visible core attachment;
E: row-b fixed point boundary;
F: row-b A-layer cycle boundary;
G: X-layer two-target bridge boundary;
H: independent row-b predecessor cycle disjoint from the watched set.
```

The old active target was to route G.

G has now been routed by:

```text
x_layer_two_target_bridge_reduction_lemma.md
same_input_split_target_lift_lemma.md
```

The sharper second-stage split is:

```text
clean_external_bridge_second_stage_reduction_lemma.md
```

After visible/generated hits are routed, the remaining exact residuals are:

```text
R1. same-row recurrence: row-b fixed point or row-b swap boundary;
R2. row-b independent predecessor cycle, now with beta pressure at every A_i;
R3. beta-coupled fresh same-target pair in H_{A_j};
R4. fresh reversible two-target square from G or Beta_i=x_j;
R5. genuinely fresh beta-layer extension in row x_i.
```

The reversible-square residual is not independent:

```text
fresh_reversible_square_beta_anchor_lemma.md
```

shows that every fresh square contains the beta interval:

```text
(A_j,Beta_j,b).
```

So, after beta first-hit routing, a fresh square is a structured subcase of a
fresh beta-layer extension.

The fresh beta-layer extension itself is now sharpened by:

```text
beta_fresh_predecessor_zipper_ladder_lemma.md
beta_fresh_extension_first_hit_boundary.md
```

Use:

```text
Z_i^{-2}=x_{i+1}, Z_i^{-1}=b, Z_i^0=A_i, Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m)=Z_i^m*(Z_i^{m-1}*x_i).
```

Every step also forces the side edge:

```text
row Z_i^{m-1}: (Z_i^{m-2}*x_i) -> Z_i^m.
```

So the next exact target is not just the first repeat of `Z_i^m`; it is the
comparison between the first repeat of `Z_i^m` and the first repeat of the
shifted side columns:

```text
T_i^m=Z_i^{m-2}*x_i.
```

If the first shifted-column repeat happens before the first `Z` repeat, then:

```text
beta_zipper_shifted_repeat_split_lemma.md
```

turns it into a proper same-input split and lifts it to `H_T`.

If instead the first event is the main `Z` repeat, then:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

shows the beta chain cannot stay disjoint.  It must return through the known
row-`x_i` segment and hit the generated X-layer, at worst `x_{i+1}`.

The next exact target is therefore:

```text
route a deeper beta-X hit Z_i^m=x_j.
```

This route is recorded in:

```text
deep_beta_x_hit_reduction_lemma.md
```

So the fresh beta extension is no longer independent: it returns to watched
hits, row-`x_i` recurrence, beta first-hit routing, or beta-anchored reversible
square.

After routing the U/V/W/X/Y/Z bridge layers, the current clean external bridge
frontier is summarized in:

```text
clean_external_bridge_twelfth_stage_reduction_lemma.md
```

Current residuals:

```text
G12. global minimal relay-cycle descent.
```

Removed:

```text
Y2. Beta_i=H_i shared-edge divergence.
```

It folds into the base row-b/generated bridge by:

```text
y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
```

Sharpened:

```text
Y3 -> Z3 coupled clean cycle shell -> paired ladder first merge/repeat.
```

The old three-row comparison at `A_j` is now:

```text
left-row cycles through A_j:
  row p, row x_j, row b;

fixed-target source-successor orbits in H_{A_j}:
  p -> S -> S*A_j -> ...
  x_j -> b -> D_j -> D_j*A_j -> ...
```

Important correction: right multiplication by `A_j` is not known to be a
permutation.  These are forward source orbits tracked to first merge/repeat,
not automatically cycles.  Use:

```text
fixed_target_source_orbit_first_merge_boundary.md
```

The next exact target is the shared-successor square:

```text
p*A_j=S,
U=p*S,
V=S*A_j,
S*(U*p)=A_j.
```

The branch `U=V` has been reduced to a same-target pair in `H_U` by:

```text
y3_commuting_second_step_reduction_lemma.md
```

The shallow local diagnostic:

```text
y3_shell_saturation_diagnostic.md
```

found no forced named collapse at the tested bounded level.

The paired Z3 ladder is no longer an independent fresh residual:

```text
z3_paired_source_ladder_eventual_merge_lemma.md
```

shows that finite source-successor ladders in `H_{A_j}` must hit a first
fan/path/full-interval/source-repeat event.  The only non-routed outcome is a
same-row/source recurrence boundary, now collected in:

```text
same_row_recurrence_inventory.md
```

This aligns the clean external bridge route with the global No-Free-Tail
frontier:

```text
clean_external_bridge_to_relay_recurrence_frontier.md
```

The next target is a minimality/descent statement for `R-b4/R-b5` row-b
recurrence: a regenerated fan must have a smaller old-corridor footprint,
unless it hits the visible core or repeats a full ported interval in an
independent branch role.

R-b4 and R-b5 are now locally reduced:

```text
rb4_first_repeat_target_swap_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb5_a_layer_footprint_descent_boundary.md
```

So the local footprint descent is identified.  The remaining work is the
global minimality/descent step: start-return minimal cycles and regenerated
relay objects must either shrink the global relay measure, hit the visible
core, or repeat a full ported interval in an independent role.

Latest narrow result:

```text
rb5_beta_necklace_first_hit_reduction_lemma.md
```

The start-return R-b5 A-cycle carries a cyclic necklace of lifted beta-anchor
pairs, and its first beta/X/Z hit is covered by existing beta/Z3 reductions or
by the global same-row recurrence inventory.

Next target: global minimal relay descent for the remaining same-row
recurrence cases outside row-b R-b4/R-b5.

R-x and R-Z are absorbed by:

```text
rx_beta_chain_recurrence_absorption_lemma.md
rz_source_ladder_recurrence_absorption_lemma.md
```

The small local swap/fixed cases:

```text
R-a, R-b1, R-b2, R-b3
```

are classified by:

```text
local_swap_fixed_recurrence_classification.md
```

So the local recurrence inventory has no independent fresh branch left.  The
remaining target is the global minimal relay-cycle descent.

The clean external bridge case tree is now exhausted locally:

```text
clean_external_bridge_twelfth_stage_reduction_lemma.md
```

Continue with:

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
m496_shared_step_orbit_split_diagnostic.md
m496_first_extra_intersection_roles_diagnostic.md
clean_first_extra_pattern_raw_diagnostic.md
minimal_g12_loop_normal_form_boundary.md
```

The remaining loop is now normalized in:

```text
minimal_g12_loop_normal_form_boundary.md
```

Only period `>= 3` same-source target-advance row-orbit recurrences remain.
The next target is to show that this normal form is strict clean theta or
forces an independent full ported-interval repeat.

The fixed-target ambiguity is removed by:

```text
fixed_target_same_source_return_collapse_lemma.md
```

A same-source return to the same old split in one fixed `H_b` is the same edge
again, so it is not a new core return.

The moving same-source case is narrowed by:

```text
target_advance_same_row_period_lemma.md
```

Periods 1 and 2 are fixed/swap local recurrences.  The remaining same-source
target-advance cycles have period at least 3.

The diagnostic:

```text
m496_target_advance_period_diagnostic.md
```

confirms that the known M496 model has periods `1,5,10,30`; the period
`>= 3` residue is structurally real.

The local two-row window is separated by:

```text
two_row_target_advance_window_separation_lemma.md
```

So neighboring-port equality is not the next target; it would already be a
full-interval collision.  The next target is the global loop assembled from
separated period `>= 3` windows.

The global split is:

```text
two_row_orbit_theta_boundary.md
```

Either the two row cycles have a first extra intersection, or their union is a
clean two-row orbit theta in the target-advance state space.

The first extra intersection is routed by:

```text
two_row_first_extra_intersection_routing_lemma.md
```

leaving only its clean same-input two-target bridge subcase.

That clean subcase is aligned with the general V3-type bridge frontier in:

```text
clean_first_extra_matching_bridge_alignment.md
```

The diagnostic:

```text
m496_shared_step_orbit_split_diagnostic.md
```

found no clean orbit-theta pairs in M496; every shared-step row pair had an
extra cycle intersection.  Prioritize the clean same-input two-target bridge
left by that route.

The diagnostic:

```text
m496_first_extra_intersection_roles_diagnostic.md
```

also found no clean first-extra matching in M496: after rotating cycles to the
shared step `b -> z`, the first extra intersection is always a same-output
fan.  Next target: prove or route away the clean-disjoint first-extra matching
subcase, preferably by proving the same-output pattern.

If the same-output pattern is not proved directly, treat the clean branch as a
general V3-type bridge descent/admissibility problem.

The exact bridge descent boundary is:

```text
general_v3_bridge_descent_boundary.md
```

It adds `M5` first-extra offset and `M6` clean V3 bridge rank to the measure
candidate.

The raw diagnostic:

```text
clean_first_extra_pattern_raw_diagnostic.md
```

found short closure `ok` for the clean pattern and a 60-second size-9 rawmodel
timeout without a model.

For independent row-b cycle boundaries, each generated input `A_i` also has
cross-source pressure between rows `b` and `x_i`:

```text
generated_input_cross_source_pressure_lemma.md
beta_layer_first_hit_boundary.md
```

The important equality branch is routed:

```text
Beta_i=H_i
```

becomes a shared-edge divergence of rows `b` and `x_i` at:

```text
H_i -> A_i.
```

Reference:

```text
beta_equals_h_shared_edge_divergence_lemma.md
y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
```

It is no longer an independent residual: after the shared edge, the next step
is the already routed base row-b/generated bridge at `A_i`.

The `Beta_i=A_j` branch is separated as:

```text
beta_a_hit_same_input_split_boundary.md
```

It is not a common-edge fan; it is a same-input split across targets:

```text
row x_i: A_j -> A_i
row x_j: A_j -> b
```

and then lifted by:

```text
same_input_split_target_lift_lemma.md
```

to:

```text
H_{A_j}: E_{i,j}->A_i and Beta_j->b.
```

The `Beta_i=x_j` branch is routed by:

```text
beta_x_bridge_pair_reversible_square_lemma.md
```

to a reversible two-target square, not an unbounded target-swap tower.

## Second-Successor Boundary

For `t=a*b`, the following are routed:

```text
t*b=b                  -> impossible by badness of b;
t*b=a                  -> t joins F(b,a), right-b two-cycle a->t->a;
t*b=t                  -> right-b fixed orbit boundary;
t*b in {c,d,u,v,h,k}   -> visible footprint / bridge-hub hit.
```

Depth-3 bounded closure in `tools/crossed_double_fan_saturation.js` did not
turn `t*b=a`, `t*b=t`, `t*b=h`, or `t*b=k` into a short bad-target
contradiction.  So do not waste a run expecting a one-step local hit to close
the clean residual.

The script now supports flags:

```text
tb=a, tb=b, tb=c, tb=d, tb=u, tb=v, tb=h, tb=k, tb=ab, tb=ta
```

where `tb=(a*b)*b`.

## Exact Next Mathematical Target

Prove the connector:

```text
A closed ported-transition cycle born from the clean external bridge must
either:

1. hit the visible crossed-fan/core footprint;
2. produce a full ported interval collision in independent branch roles;
3. become core-attached and hence return to ordinary branch relay;
4. produce an A-repeat / X-repeat / A-X hit as classified above;
5. or reduce to the clean two-layer matching residual and then classify the
   first nonfresh row-b predecessor-layer hit;
6. attack the fresh beta-layer extension; fresh reversible squares are
   beta-anchored subcases.
```

This is narrower and safer than saying “the right-b orbit repeat returns to
branch relay”.  Fan regeneration is proved; core attachment is not yet proved.

## Computation Rules For The Next Run

Use computation only for targeted checks with clear interpretation.  The user
approved assistant-run local CPU checks up to 10 minutes when sharply bounded.

Avoid:

```text
old size-8 crossed-fan broad timeouts;
old invalid row-0 normalized diagnostics;
searches that only ask "what happens".
```

Prefer:

```text
tools/crossed_double_fan_saturation.js
tools/search_counterexample_strong.js raw* modes
```

only after formulating one precise connector hypothesis.

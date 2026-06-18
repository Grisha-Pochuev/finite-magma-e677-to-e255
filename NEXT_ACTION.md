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
A-D: generated H_b fan/path or visible core attachment;
E: row-b fixed point boundary;
F/H: row-b independent cycle boundary;
G: X-layer two-target bridge boundary.
```

Next target: attack the fresh beta-layer extension directly.  Fresh reversible
squares are beta-anchored, so do not treat R4 as an independent tower and do
not route G from scratch again.

Additional beta-layer progress:

```text
Beta_i=H_i -> shared-edge divergence of rows b and x_i at H_i -> A_i.
Beta_i=A_j -> same-input split lifted into H_{A_j}: E_{i,j}->A_i and Beta_j->b.
Beta_i=x_j -> reversible square: (A_i,x_j,b)<->(x_j,delta,A_i) and (b,A_j,x_{j+1})<->(A_j,Beta_j,b).
alpha=A_j -> G same-input split couples to Beta_j in H_{A_j}.
```

Second-stage exact residuals:

```text
R1. same-row recurrence: row-b fixed point or row-b swap boundary;
R2. row-b independent predecessor cycle with beta pressure at every A_i;
R3. beta-coupled fresh same-target pair in H_{A_j};
R4. fresh reversible two-target square from G or Beta_i=x_j;
R5. genuinely fresh beta-layer extension in row x_i.
```

Compression:

```text
R4 is beta-anchored: every fresh reversible square contains (A_j,Beta_j,b).
So after beta first-hit routing, R4 is a structured subcase of R5.
```

## Do Not Repeat

Do not rerun broad size-8 crossed-fan timeouts.

Do not expect `t*b=a`, `t*b=t`, `t*b=h`, or `t*b=k` to close locally; these
were checked and routed in:

```text
right_b_orbit_second_successor_boundary.md
```

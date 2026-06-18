# Bad-Target Crossed-Fan Boundary

Date: 2026-06-17.

Status:

```text
active subproblem / proper case not proved / swap-row split proved
```

## Purpose

The general crossed double-fan question asks whether two opposite common-edge
fibers can both have size at least two:

```text
F(a,b)={p:p*a=b},
F(b,a)={r:r*b=a}.
```

For the main theorem we need a narrower statement.  The target `b` is a bad
element, so:

```text
q*b!=b
```

for every row `q`.

Thus the useful subproblem is:

```text
Bad-target crossed-fan exclusion:
if b is bad, then there is no a!=b such that
|F(a,b)|>=2 and |F(b,a)|>=2.
```

This is the exact crossed-fan form needed for a figure-eight closure in
`H_b`.

## Diagnostics

The normalized but invalid diagnostic:

```text
mode diagnose
2*1=0, 3*1=0, 4*0=1, 5*0=1
```

gave a contradiction, but it used row-0 canonical normalization together with
fixed role labels.  This must not be used as evidence.

The valid raw diagnostic:

```text
mode rawdiagnose
2*1=0, 3*1=0, 4*0=1, 5*0=1
```

reported:

```text
status: ok
row 0 domain=9624
row 1 domain=10488
rows 2,3,4,5 domain=4272 each
```

So the bad-target crossed fan is not an immediate propagation contradiction.

A raw-label size-8 counterexample search with the same four cells ran for 10
minutes:

```text
status: timeout
time: 600.02s
nodes: 101900
dead ends: 100428
forced cells: 769317
domain checks: 939612140
```

No model was found, but the search did not finish.

Size `7` with the bad-target crossed-fan cells is completely closed in raw
mode:

```text
status: none
time: 16.79s
nodes: 18584
dead ends: 18226
```

This is finite evidence only, not a proof.

## Swap-Row Split

A new proved reduction is recorded in:

```text
crossed_fan_swap_row_degeneracy_lemma.md
swap_row_target_advance_loop_lemma.md
```

If a row swaps the two crossed-fan vertices:

```text
x*a=b,
x*b=a,
```

then that row is unique by the two-step source reconstruction lemma applied to
the interval `a -> b -> a`.

Therefore two short returns cannot be independent:

```text
p*a=b, p*b=a,
r*b=a, r*a=b
=> p=r.
```

If the same row is shared, the target-advance state is just:

```text
(b,a,a) -> (a,b,b) -> (b,a,a).
```

So the shared swap-row case belongs to the same-row recurrence boundary, not
to the proper crossed-fan case.

The crossed-fan frontier should now be split as:

```text
1. swap-row degenerate case:
   one shared row swaps a and b;

2. proper crossed-fan case:
   no selected source row swaps a and b.
```

The distinct-row double-swap size-8 raw check closes quickly:

```text
2*1=0, 3*1=0, 4*0=1, 5*0=1,
2*0=1, 4*1=0

status: none
time: 64.54s
nodes: 721
dead ends: 720
```

The shared-swap residual is not computationally closed at size `8` under the
current search:

```text
2*1=0, 2*0=1, 3*1=0, 4*0=1

status: timeout
time: 180.01s
nodes: 21710
dead ends: 21414
```

This timeout should not be interpreted as a proper crossed-fan obstruction.
Mathematically, the shared swap row is already a same-row target-advance loop;
the remaining proof obligation is the same-row recurrence boundary, not the
proper crossed-fan boundary.

The proper no-swap version is also still open at size `8`:

```text
forbid each selected row from having both a->b and b->a

status: timeout
time: 180.28s
nodes: 75176
dead ends: 74662
```

## Interpretation

Bad-target crossed-fan exclusion remains a serious candidate lemma.  It is
stronger than the currently proved local relay reductions and weaker than the
fully general crossed double-fan exclusion.

The next useful target is sharper than the original statement:

```text
proper bad-target crossed-fan exclusion
```

The shared swap-row case has now been routed to the already separated
same-row recurrence boundary.

The next proved split is:

```text
crossed_fan_cross_tip_hub_separation_lemma.md
crossed_fan_equal_hub_side_incidence_lemma.md
bad_target_crossed_fan_row_a_edge_lemma.md
bad_target_no_predecessor_output_lemma.md
bad_target_self_labeled_edge_recursion_lemma.md
bad_target_row_a_output_avoids_b_hub_lemma.md
row_a_bridge_loop_recurrence_boundary.md
row_a_bridge_edge_attachment_cases.md
row_a_bridge_second_certificate_lemma.md
clean_external_bridge_row_b_predecessor_fan_lemma.md
clean_external_bridge_three_source_predecessor_fan_lemma.md
clean_external_bridge_new_source_row_lemma.md
row_a_second_bridge_visible_hit_cases.md
bad_target_right_b_orbit_predecessor_recursion_lemma.md
right_b_orbit_local_repeat_roles.md
right_b_orbit_second_successor_boundary.md
right_b_orbit_first_repeat_boundary.md
right_b_orbit_first_repeat_fan_lemma.md
right_b_orbit_repeat_core_attachment_gap.md
clean_external_bridge_returns_to_branch_relay_lemma.md
first_right_b_successor_fan_attachment_lemma.md
cross_tip_collision_target_advance_lemma.md
proper_crossed_fan_target_swap_self_duality_lemma.md
proper_crossed_fan_clean_external_bridge_boundary.md
clean_external_bridge_predecessor_chain_candidate.md
```

In any crossed fan, if the two common hubs coincide:

```text
h=pred_b(a)=pred_a(b)=k,
```

then the outgoing tips and incoming tips are cross-disjoint:

```text
{c,d} ∩ {u,v} = empty.
```

Equivalently, every cross-tip collision forces `h!=k`.

Thus the proper bad-target frontier is now divided into:

```text
1. h=k with four cross-disjoint tips and an added row-a bridge edge
   h -> a*b in H_b;
2. h!=k with possible cross-tip collisions, each of which advances to a
   common new target.
```

In fact, in every bad-target crossed fan, badness of `b` gives a real row-`a`
edge in `H_b`:

```text
a*k=b,
a*b=t,
k -> t,
k!=b,
t!=b.
```

In addition:

```text
t!=h=pred_b(a).
```

Indeed, this is the `x=a` instance of
`bad_target_no_predecessor_output_lemma.md`: `t=h` would imply `(b*a)*b=b`,
contradicting badness of `b`.

If:

```text
t=k,
```

then row `a` swaps `b` and `k`, giving the same-row recurrence loop:

```text
(b,k,k) -> (k,b,b) -> (b,k,k).
```

So this equality is routed to the same-row recurrence boundary, not to the
clean external bridge branch.

In the equal-hub branch this specializes to:

```text
a*h=b,
a*b=t,
h -> t.
```

If `h!=a`, this is a bridge edge based at the common hub.  It is a side
attachment only when `h` is known to lie in the active `H_b` corridor/core.  If
`h=a`, row `a` belongs to the outgoing fiber `F(a,b)`, giving an enlarged
outgoing fan unless row `a` was already one of the selected branch rows.

The immediate attachment cases of the general row-`a` edge are classified in:

```text
row_a_bridge_edge_attachment_cases.md
```

In particular, `k=a` or `a*b=a` enlarges one of the two fibers unless row `a`
is already selected, while `k` or `a*b` hitting `{c,d}` attaches the edge to
the visible outgoing fan footprint in `H_b`.

The next certificate of the row-a edge is:

```text
bad_target_self_labeled_edge_recursion_lemma.md
row_a_bridge_second_certificate_lemma.md
```

For `t=a*b`, it defines:

```text
ell=t*a=pred_b(k),
b*ell=k.
```

In the clean residual, `ell!=h=pred_b(a)`, because otherwise row `b`
injectivity gives `k=a`.

Thus row `b` contains the genuine predecessor fan:

```text
b*h=a,
b*ell=k,
h!=ell.
```

This is recorded in:

```text
clean_external_bridge_row_b_predecessor_fan_lemma.md
clean_external_bridge_three_source_predecessor_fan_lemma.md
```

Visible-hit cases for `ell` are classified in:

```text
row_a_second_bridge_visible_hit_cases.md
```

Only `ell=h` is immediately impossible in the clean residual.  Other visible
hits are routed rather than closed.

For a cross-tip collision, for example `c=u`, the two rows advance to the same
new target:

```text
(b,a,c) -> (c,b,p*c),
(a,b,c) -> (c,a,r*c).
```

So cross-tip collision is a relay-routing event, not a local right-fixer
event.

The clean residual proper case is target-swap self-dual on the unordered pair
`{a,b}`:

```text
proper_crossed_fan_target_swap_self_duality_lemma.md
```

Under `a <-> b`, the outgoing and incoming fans exchange and the hubs exchange:

```text
(p,q,c,d,h) <-> (r,s,u,v,k).
```

So the final clean case must be handled as a two-target relay object, not as a
one-sided local fan.

After all routing splits, the active residual is recorded in:

```text
proper_crossed_fan_clean_external_bridge_boundary.md
clean_external_bridge_predecessor_chain_candidate.md
```

It assumes:

```text
h!=k,
{c,d} ∩ {u,v}=empty,
t=a*b,
k -> t in H_b,
k,t not in {a,c,d,u,v},
t not in {b,h,k}.
```

This is now the narrowest crossed-fan frontier.

The current candidate mechanism is to turn the clean external bridge into a
finite row-`b` predecessor-chain argument.  This is not proved yet; the missing
successor label has now been identified as the next point of the right-`b`
orbit:

```text
x_{i+1}=x_i*b.
```

The remaining missing step is classifying the first repeat or visible hit of
that orbit-predecessor chain.

The first two successors of this right-`b` orbit are now separated in:

```text
right_b_orbit_second_successor_boundary.md
```

They do not give a new short local contradiction beyond the already routed
cases:

```text
t*b=b    -> impossible by badness;
t*b=a    -> incoming-side fan attachment;
t*b=t    -> right-b fixed orbit boundary;
t*b in {c,d,u,v,h,k} -> visible footprint / bridge-hub hit.
```

The local repeat roles and first-successor fan attachments are recorded in:

```text
right_b_orbit_local_repeat_roles.md
right_b_orbit_first_repeat_boundary.md
right_b_orbit_first_repeat_fan_lemma.md
clean_external_bridge_returns_to_branch_relay_lemma.md
first_right_b_successor_fan_attachment_lemma.md
```

The clean external bridge is therefore routed back to branch relay, not left
as a one-step local obstruction.  More precisely, the right-`b` orbit first
repeat regenerates an incoming fan, but `right_b_orbit_repeat_core_attachment_gap.md`
records the remaining connector: this fan is not automatically in the original
cyclic core component because the right-`b` orbit is not itself an `H_b` path.

For No-Free-Tail, the desired route is now:

```text
figure-eight closure at bad target
=> bad-target crossed fan
=> contradiction.
```

This would leave only the same-row recurrence boundary.

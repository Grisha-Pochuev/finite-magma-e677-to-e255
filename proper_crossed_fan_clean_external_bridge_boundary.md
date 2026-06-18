# Proper Crossed-Fan Clean External-Bridge Boundary

Date: 2026-06-18.

Status:

```text
active residual boundary / not proved impossible
```

## Purpose

This file records the remaining clean residual after the proved routing splits
for a bad-target proper crossed fan.

It should be used as the next starting point instead of returning to the broad
crossed-fan statement.

## Base Crossed-Fan Skeleton

Fix a bad target `b` and `a!=b`.

Assume the selected proper crossed fan:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

The selected rows are proper:

```text
c!=a, d!=a,
u!=b, v!=b.
```

The fan certificates give:

```text
c!=d,
u!=v,
c*p=d*q=h=pred_b(a),
u*r=v*s=k=pred_a(b),
b*h=a,
a*k=b.
```

Badness of `b` gives:

```text
c,d,a != b,
a*b != b.
```

By injectivity in rows `r,s`:

```text
u,v != a.
```

## Already Routed Cases

The following cases are no longer part of the clean residual.

### Swap-row degeneracy

If a selected row swaps `a` and `b`, route to:

```text
crossed_fan_swap_row_degeneracy_lemma.md
swap_row_target_advance_loop_lemma.md
```

### Equal hubs

If:

```text
h=k,
```

then:

```text
{c,d} ∩ {u,v}=empty
```

and the row-a bridge edge specializes to `h -> a*b`.

Route through:

```text
crossed_fan_cross_tip_hub_separation_lemma.md
bad_target_crossed_fan_row_a_edge_lemma.md
```

### Cross-tip collision

If:

```text
{c,d} ∩ {u,v} != empty,
```

then necessarily `h!=k`, and any representative collision, e.g. `c=u`,
advances to a common new target:

```text
(b,a,c) -> (c,b,p*c),
(a,b,c) -> (c,a,r*c).
```

Route through:

```text
cross_tip_collision_target_advance_lemma.md
```

### Row-a bridge edge local attachments

Let:

```text
t=a*b.
```

The row-a bridge edge is:

```text
k -> t
```

in `H_b`.

The following are routed:

```text
k=a       -> row a joins F(a,b);
t=a       -> row a joins F(b,a);
k,t in {c,d} -> local H_b footprint attachment;
k,t in {u,v} -> dual-footprint attachment;
t=k       -> same-row loop (b,k,k)->(k,b,b)->(b,k,k);
t=h       -> impossible, because then (b*a)*b=b.
```

References:

```text
bad_target_crossed_fan_row_a_edge_lemma.md
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
first_right_b_successor_fan_attachment_lemma.md
right_b_orbit_second_successor_boundary.md
right_b_orbit_first_repeat_boundary.md
right_b_orbit_first_repeat_fan_lemma.md
right_b_orbit_repeat_core_attachment_gap.md
clean_external_bridge_returns_to_branch_relay_lemma.md
```

## Clean External-Bridge Residual

The remaining case may be assumed to satisfy:

```text
h!=k,
{c,d} ∩ {u,v}=empty,
t=a*b,
k -> t is a real H_b edge,
k,t not in {a,c,d,u,v},
t not in {b,h,k}.
```

Also:

```text
k not in {b,h}
```

because `k!=b` by badness and `k!=h` by `h!=k`.

The second certificate of the row-a bridge edge gives:

```text
ell=t*a=pred_b(k),
b*ell=k.
```

In the clean residual:

```text
ell!=h=pred_b(a),
```

because `ell=h` would force `k=a` by injectivity of row `b`.

Equivalently, row `b` now contains a genuine predecessor fan:

```text
b*h=a,
b*ell=k,
h!=ell,
a!=k.
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

The next clean residual after this second layer may additionally assume:

```text
ell not in {a,b,c,d,u,v,h,k,t}.
```

The first right-`b` successor fan-attachment tests are:

```text
first_right_b_successor_fan_attachment_lemma.md
right_b_orbit_second_successor_boundary.md
```

They route:

```text
ell=b  <=> t*a=b  -> t joins F(a,b),
t*b=a              -> t joins F(b,a) and a->t->a is a right-b orbit cycle.
```

Therefore the next clean residual may also assume:

```text
t*b != a.
```

The second-successor boundary also records:

```text
t*b=b    -> impossible by badness of b;
t*b=t    -> right-b fixed orbit boundary, not a bad-target contradiction;
t*b in {c,d,u,v,h,k} -> visible footprint / bridge-hub orbit hit.
```

Thus the row-a bridge edge is external to the immediately visible two-target
fan footprint:

```text
H_b outgoing footprint: a,c,d
dual footprint:         u,v
bridge hubs:            h,k
```

except that it starts at the bridge hub `k` itself.

## Next Proof Target

The clean external-bridge residual should be attacked as a two-target relay
problem:

```text
proper_crossed_fan_target_swap_self_duality_lemma.md
```

The object is self-dual on the unordered pair `{a,b}` while the badness
assumption remains one-sided on `b`.

The next useful lemma should show that the external row-a bridge edge either:

```text
1. enters the active H_b core after a finite target-swap relay;
2. repeats a full ported interval in an independent branch role;
3. or forces another bad target / same-row recurrence that is already routed.
```

Do not restart from the broad crossed-fan exclusion unless this residual
formulation is found to be too strong.

The current reduction is:

```text
clean_external_bridge_returns_to_branch_relay_lemma.md
right_b_orbit_repeat_core_attachment_gap.md
```

It shows that the clean external bridge regenerates a new incoming branch fan
at the first repeat of its right-`b` orbit.  The correction in
`right_b_orbit_repeat_core_attachment_gap.md` is important: the right-`b`
orbit is not itself an `H_b` path, so the regenerated fan is not yet proved to
lie in the original cyclic core component.  A core-attachment connector is
still needed before this can be used as an ordinary No-Free-Tail branch relay.

Current candidate for the next step:

```text
clean_external_bridge_predecessor_chain_candidate.md
bad_target_right_b_orbit_predecessor_recursion_lemma.md
```

The canonical successor after the fresh second bridge `ell` is now identified:

```text
x_{i+1}=x_i*b.
```

The remaining formal point is the first-repeat / first-visible-hit
classification of this right-`b` orbit predecessor chain.

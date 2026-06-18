# Lemma Status

## Active update 2026-06-17: pure-incoming boundary

New general proved:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

Status:

```text
general proved / boundary reduction for branch closure
```

Meaning: a pure incoming first-merge vertex of degree at least three is not a
new terminal obstruction. After target swap `b -> z`, it becomes a triple
outgoing fan in `H_z`. The remaining local boundary is the binary pure
incoming sink: exactly two incoming branches, no outgoing continuation, no
loop, and no third incoming incidence.

New graph proved:

```text
binary_sink_core_escape_lemma.md
```

Meaning: that binary sink is not an isolated endpoint in the forced bicyclic
core. The second independent cycle must attach to the active two-branch
corridor before the sink, so the next frontier is the earliest side attachment.

New graph proved:

```text
earliest_side_attachment_mixed_junction_lemma.md
```

Meaning: the earliest internal side attachment is automatically a mixed `2+1`
junction. Thus the binary-sink residue relays back to the existing triple
fan / mixed `2+1` framework and should not be treated as a third obstruction
type.

Stage summary:

```text
pure_incoming_boundary_stage_2026-06-17.md
```

## Active update 2026-06-09: branch-closure reduction

New general proved:

```text
double_interval_edge_certificate_lemma.md
bicyclic_component_branch_fan_lemma.md
bad_target_core_fan_lemma.md
bicyclic_core_junction_lemma.md
target_swap_fan_duality_lemma.md
right_fixer_to_balanced_witness_lemma.md
mixed_junction_target_swap_bridge_square.md
first_merge_certificate_separation_lemma.md
first_merge_target_swap_mixed_relay.md
first_merge_degenerate_continuation_boundary.md
first_merge_target_swap_junction_dichotomy.md
branch_closure_relay_stage_2026-06-17.md
```

The first file gives the complete certificate of every graph edge:

```text
row q: beta -> a -> b -> c
row c: q -> pred_b(a), A_b(c) -> b
row b: pred_b(a) -> a.
```

The second proves:

```text
every connected component of A_b(q)--R_b(q) with two independent cycles
contains a same-direction common-edge fan inside its cycle core.
```

The third combines this with badness and edge counting:

```text
every hypothetical bad target already forces such a fan in a bicyclic core.
```

The fourth retains the third core incidence and gives the exact dichotomy:

```text
triple core fan;
mixed 2+1 core junction.
```

The fifth proves that target change is an involutive fan duality:

```text
outgoing fan at a in H_b <-> incoming fan at b in H_a,
with the same source rows.
```

New candidate, not proved:

```text
crossed_double_fan_pressure_candidate.md
Branch-Closure No-Free-Tail Lemma.
branch_closure_no_free_tail_candidate.md
```

Valid finite evidence for crossed double-fan exclusion:

```text
raw-label arbitrary E677 searches of sizes 6 and 7: none.
```

Do not promote that exclusion to a lemma. The exact open step is to transport
two core branches from the forced fan until their first merge or cyclic
closure and force an aligned two-step overlap.

Audit correction:

```text
the earlier size-8/9 crossed-fan and size-9 directed-diamond claims used an
invalid double normalization and are withdrawn.
```

## Stop update 2026-06-09

New general proved:

```text
general_target_bridge_orbit_lemma.md
labeled_right_translation_graph_lemma.md
```

Already proved in the same active layer:

```text
right_p_orbit_bridge_recursion_lemma.md
right_p_orbit_collision_duality_lemma.md
cycle_entry_two_sided_fan_lemma.md
cycle_entry_hub_transport_lemma.md
good_p_unique_reverse_edge_lemma.md
right_fixed_point_uniqueness_lemma.md
```

Candidate, not proved:

```text
each component of the graph A_b(q)--R_b(q) is a pseudoforest;
full Main Bad-Cycle No-Free-Tail Lemma.
```

Full pause record:

```text
STOP_CHECKPOINT_2026-06-09.md
```

## Active update 2026-06-09: right-orbit termination layer

General proved:

```text
right_fixed_point_uniqueness_lemma.md
right_p_orbit_bridge_recursion_lemma.md
right_p_orbit_collision_duality_lemma.md
cycle_entry_two_sided_fan_lemma.md
cycle_entry_hub_transport_lemma.md
good_p_unique_reverse_edge_lemma.md
```

Proved consequence:

```text
there is no finite collision-free bridge tail;
first repetition creates a two-sided common-edge fan.
```

Still candidate:

```text
transport of the terminal bad-cycle anchor through a non-aligned fan-edge
change;
full Main Bad-Cycle No-Free-Tail Lemma.
```

Audit:

```text
bridge w=P <=> tip T fixes P on the right.
Under good P, this is equivalent to T=h by fixed-point uniqueness.
Do not justify it by general right cancellativity.
```

## Paused update 2026-06-08: bridge recursion and terminal anchor

General proved:

```text
fan_tip_bridge_expansion_lemma.md
fan_bridge_zipper_extension_lemma.md
terminal_source_anchored_fan_lemma.md
```

Candidate, not proved:

```text
three_source_good_six_pressure_candidate.md
main_bad_cycle_no_free_tail_lemma.md
```

The exact pause summary and continuation rule are in:

```text
STOP_CHECKPOINT_2026-06-08.md
```

Do not promote the size-9 closure to a general theorem. The next valid step is
the symbolic first-intersection classification for the three bridges.

## Active update 2026-06-08: two-sided fan and minimal descent

New general proved lemmas:

```text
two_sided_common_edge_fan_lemma.md
fan_spine_four_cycle_descent_lemma.md
tip_source_collision_zero_tooth_lemma.md
fan_tip_bad_cycle_alignment_lemma.md
zero_tooth_bad_cycle_return_lemma.md
fan_source_tip_graph_lemma.md
minimal_bad_short_cycle_reduction.md
fan_spine_fourth_predecessor_test.md
fan_spine_length_five_badness_lemma.md
good_p_occupied_tip_pressure_lemma.md
```

Main consequences:

```text
every common-edge source row has a distinct backward foot and forward tip;

e=C is a shared row-0 edge and transfers badness to a four-cycle;

under a minimal bad element with cycle length >=5, e=C is impossible;

tip-source collision creates v*q=0;

aligned occupied fan tips and aligned zero-tooth returns are old-tail descents;

distinct internal source tips cannot form a two-cycle;

minimal bad cycle length is at least 3, with exact base forms for lengths 3
and 4.

longer row-P closure is decided by:
  f*f=g <=> h*P=P <=> E255 at P.

an exact row-P five-cycle is always bad; the first unresolved good shorter
closure has length six.

for good P and occupied C=b_j, r_{j-2}=P is impossible; otherwise row b_{j-1}
has two distinct forced occupied edges.
```

Current unresolved long-cycle roles:

```text
fresh/non-aligned zero-tooth return;
non-aligned occupied fan tip;
longer row-P cycle closure.
```

The No-Free-Tail Lemma remains unproved.

## Stop checkpoint 2026-06-08: fan spine

New general proved lemmas:

```text
fixed_source_zero_descent_lemma.md
self_containing_fan_spine_lemma.md
```

The first lemma proves:

```text
x*0=x
x*x=c
=>
c*x=0*c
x*(0*c)=0.
```

The second packages this descent with a common-edge fan. For:

```text
P*0=P
C=P*P
h=0*C
e=h*(0*P),
```

row `P` contains:

```text
e -> h -> 0 -> P -> C,
```

and every fan source `q*0=P` has a distinct tip `T_q=q*P` returning by:

```text
T_q*q=h.
```

Local computational closure:

```text
C=b_7 -> status none, 46.31s, 640 nodes;
C=b_6 -> status none, 28.37s, 410 nodes.
```

Together with the two earlier internal roles, this closes the full normalized
size-9 role `u=b_3`.

Current candidate, not proved:

```text
fan_spine_termination_candidate.md
```

Open first-hit types:

```text
e=C four-cycle;
tip-source collision;
non-edge hit on the bad cycle;
separate source-row cycle closure.
```

The global No-Free-Tail Lemma and `E677 => E255` remain unproved.

## Update 2026-06-07: cross-source reconstruction upgrade

New general proved lemma:

```text
two_step_source_reconstruction_lemma.md
```

Statement:

```text
p*a=b
p*b=c
=>
p=pred_c(pred_b(a)).
```

Consequences:

```text
two distinct rows cannot contain the same ordered interval a -> b -> c;

for fixed s, the map x -> x*0 is injective on {x : x*s=0}.
```

New paired-cycle application:

```text
paired_chain_aligned_overlap_lemma.md
```

At:

```text
A_i=B_m,
```

it is impossible to have both:

```text
A_{i-1}=B_{m-1}
A_{i+1}=B_{m+1}.
```

Status:

```text
general proved application / genuine cross-source obstruction
```

New bad-tail application:

```text
bad_tail_double_zero_tooth_lemma.md
```

The role:

```text
u*0=b_4
```

forces:

```text
u*b_3=0
q=b_3*u
q*b_3=0,
```

but the next orbit point cannot also hit zero in column `b_3`.

For:

```text
R=q*0,
```

one has:

```text
R*q=b_4
R notin {0,b_4,u}.
```

Status:

```text
proved termination of the occupied r=b_4 relay
```

Current gap:

```text
Use the row-r_2 and row-b_4 fans to force either:
  a forbidden aligned two-edge overlap of the row-b_2 and row-b_3 cycles;
  or an already classified unequal-neighbor pressure / row-0 descent role.
```

Additional general proved tools:

```text
shared_edge_divergence_lemma.md
common_edge_fan_lemma.md
bad_cycle_shared_edge_descent_lemma.md
```

Audit boundary:

```text
common-edge fans are not contradictions by themselves;
the known size-496 E677 model has fibers of size 16 and satisfies E255.
```

Stop checkpoint:

```text
bad_tail_u_equals_s_fan_lemma.md
bad_tail_u_equals_s_zero_tip_closure.md
```

For size 9, the role `u=b_3` is reduced to:

```text
C=b_2*b_2 in {b_7,b_6}.
```

Closed:

```text
C=0;
C=0*0;
C=b_4.
```

Not yet checked:

```text
C=b_7;
C=b_6.
```

## Update 2026-06-04: main candidate

New strategic candidate:

```text
main_bad_cycle_no_free_tail_lemma.md
```

Status:

```text
main candidate / not proved
```

Proposed global statement:

```text
No-Free-Tail Lemma:
in a finite E677 magma, a bad element 0 cannot have r_2=b_2*0 != 0.
Thus r_2=0, which is E255 for 0.
```

Global pieces already proved:

```text
inverse edge chain;
bad-cycle predecessor ladder b_j*r_{j-1}=b_{j+1};
source-orbit ladder;
source-row zero trap.
```

Current gap:

```text
prove the termination/no-free-tail step:
every zero-avoiding source-orbit prefix generated by the bad-cycle ladder must
hit a pred0 zero-hit, descend to an older bad-cycle index, or collide with a
forced row output.
```

Update 2026-06-04:

```text
offset_bridge_orbit_dichotomy_lemma.md
```

New structural progress:

```text
For r_2=b_t, set p=(b_3*b_4)*b_3.

If a bridge row exists:
  a*b_t=b_4
  a*b_4=b_3

then:
  b_3*a=p.

There is at most one bridge row.
```

Interpretation:

```text
r_2=b_4 is the self-return/occupied-block case.
r_2=b_5 has row 0 as a bridge, hence b_3*0=p.
Farther offsets split into:
  bridge branch -> p is transferred into row b_3;
  no-bridge branch -> use the row-b_3 orbit relay.
```

Current sharpened gap:

```text
Prove no-bridge orbit termination:
the row-b_3 orbit relay cannot maintain a finite zero-avoiding free tail.
It must hit 0, form a short forced return cycle, or descend to an already
occupied lower source row.
```

New target file:

```text
no_bridge_orbit_tail_candidate.md
```

Current no-bridge role candidate:

```text
zero-hit role;
short-cycle return role;
compact zero-avoiding prefix-collapse.
```

This is supported by the old closed no-bridge self-layer diagnostics for
numeric `t=2,3`, but still needs a symbolic termination proof.

Refinement:

```text
offset_source_orbit_first_return_lemma.md
```

The offset relay is now understood as the first orbit relay of:

```text
c_0=b_t
c_1=b_4
c_{i+1}=b_3*c_i.
```

In particular:

```text
c_2=b_3*b_4
p=c_2*b_3
b_4*p=b_t.
```

So the no-bridge termination target is now:

```text
classify the first return of this source orbit to the occupied bad-cycle block.
```

Pressure refinement:

```text
first_return_row_pressure_lemma.md
```

If the first return is:

```text
c_i=b_j,
```

then row `b_j` has both:

```text
b_j*r_{j-1}=b_{j+1}
b_j*(c_{i+1}*b_3)=c_{i-1}.
```

So first return gives:

```text
descent to r_{j-1} OR extra occupied-row pressure in row b_j.
```

New remaining target:

```text
prove repeated occupied-row pressure terminates by collision or descent.
```

Zipper upgrade:

```text
source_orbit_zipper_lemma.md
```

For a source orbit:

```text
s*c_i=c_{i+1},
```

the backward zipper is:

```text
c_i*(c_{i+1}*s)=c_{i-1}.
```

Current sharpest gap:

```text
Prove that a no-bridge offset prefix cannot keep all forward values c_i and all
zipper columns c_{i+1}*s fresh until the orbit closes.
```

Pressure-expansion upgrade:

```text
edge_predecessor_triangle_lemma.md
```

Every edge:

```text
a*z=c
```

forces:

```text
a*(z*(c*a))=z
c*((a*c)*a)=z.
```

Applied to a zipper tooth, this creates second-predecessor and triangle
columns.  The current strongest gap is now:

```text
Prove that a no-bridge offset prefix cannot keep the full edge-triangle
expansion fresh.
```

Two-sided upgrade:

```text
two_sided_offset_orbit_lemma.md
```

The first offset edge:

```text
b_3*r_2=b_4
```

also gives the predecessor in row `b_3`:

```text
c_{-1}=r_2*(b_4*b_3)
b_3*c_{-1}=r_2.
```

Current strongest gap:

```text
Prove that the occupied edge r_2 -> b_4 cannot sit inside a completely fresh
two-sided interval of the finite row-b_3 cycle.
```

Backward-role refinement:

```text
c_{-1}=0:
  enters the global source-row zero trap for the row-b_3 segment
  0 -> r_2 -> b_4, and also gives row-b_4 pressure because r_3=r_2.

c_{-1}=b_4:
  is the general self-swap role b_3*r_2=b_4, b_3*b_4=r_2.
```

Row-`r_2` pressure:

```text
r2_row_pressure_lemma.md
```

Because:

```text
r_2=b_2*0,
```

row `r_2` has:

```text
r_2*((b_2*r_2)*b_2)=0.
```

The backward offset point gives:

```text
r_2*(b_4*b_3)=c_{-1}.
```

So the current obstruction is two-row pressure:

```text
row b_3: the two-sided orbit/zipper;
row r_2: zero edge plus backward offset edge.
```

Diamond upgrade:

```text
offset_pressure_diamond_lemma.md
```

The two defining edges:

```text
b_2*0=r_2
b_3*r_2=b_4
```

force a pressure diamond in rows:

```text
b_2, r_2, b_3, b_4.
```

Current strongest gap:

```text
Prove that this pressure diamond cannot be extended by a completely fresh
two-sided row-b_3 interval in a finite E677 magma.
```

Diamond classification:

```text
p=r_3 <=> r_2=b_5.
```

So outside the special bridge offset `r_2=b_5`, row `b_4` has two distinct
occupied columns:

```text
p -> r_2
r_3 -> b_5.
```

Final recorded frontier 2026-06-05:

```text
double_interval_pressure_lemma.md
```

Sharpened obstruction:

```text
row b_2:
  u_2 -> 0 -> t

row b_3:
  c_{-1} -> t -> b_4
```

Thus `t=r_2` is the shared pivot of two forced adjacent intervals, not a
single free tail point.  The next candidate lemma is:

```text
these two intervals cannot both keep fresh predecessors while also avoiding
row-t zero pressure and row-b_4 occupied-column pressure.
```

Next role split:

```text
u_2=t      -> origin self-swap;
u_2=b_j    -> bad-cycle row pressure/descent;
u_2 fresh  -> second fresh interval must be coupled to c_{-1}.
```

Occupied `u_2` refinement:

```text
occupied_u2_lift_lemma.md
```

If:

```text
u_2=b_j,
```

then:

```text
r_2*b_2=b_{j+1}.
```

So the occupied predecessor case lifts into row `r_2`.  If `r_2=b_k`, row
`r_2` now carries:

```text
r_2*z_t=0
r_2*(b_4*b_3)=c_{-1}
r_2*b_2=b_{j+1}
r_2*r_{k-1}=b_{k+1}.
```

This splits the occupied case into zero collision, predecessor coupling,
bad-cycle descent, or extra row-`r_2` pressure.

Fresh-branch refinement:

```text
double_interval_backward_extension_lemma.md
```

If `u_2` and `c_{-1}` are fresh, the edge-triangle rule extends both intervals:

```text
e_2=u_2*b_1
b_2*e_2=u_2

e_3=c_{-1}*(r_2*b_3)
b_3*e_3=c_{-1}.
```

Thus the hard branch is no longer a fixed diamond, but:

```text
row b_2:
  e_2 -> u_2 -> 0 -> r_2

row b_3:
  e_3 -> c_{-1} -> r_2 -> b_4
```

Current gap:

```text
prove that repeated double backward extension cannot remain fresh in a finite
E677 magma.
```

Recursion packaging:

```text
paired_predecessor_recursion_lemma.md
```

The fresh extension is now written as two forced recursions:

```text
A_1=r_2, A_0=0,
A_{i-1}=A_i*(A_{i+1}*b_2),
b_2*A_{i-1}=A_i;

B_1=b_4, B_0=r_2,
B_{i-1}=B_i*(B_{i+1}*b_3),
b_3*B_{i-1}=B_i.
```

Sharper current gap:

```text
classify the first repeat or cross-hit of the paired predecessor chains and
prove it cannot be harmless.
```

Bad-cycle hit role:

```text
paired_chain_bad_cycle_hit_lemma.md
```

If:

```text
A_i=b_j
```

then:

```text
b_j*(A_{i+1}*b_2)=A_{i-1}
```

in addition to:

```text
b_j*r_{j-1}=b_{j+1}.
```

If:

```text
B_i=b_j
```

then:

```text
b_j*(B_{i+1}*b_3)=B_{i-1}
```

in addition to the same bad-cycle ladder edge.  Therefore a bad-cycle hit gives
descent or extra occupied pressure.

Cross-hit role:

```text
paired_chain_cross_hit_lemma.md
```

If:

```text
A_i=B_m=x,
```

then row `x` has:

```text
x*(A_{i+1}*b_2)=A_{i-1}
x*(B_{m+1}*b_3)=B_{m-1}.
```

So the cross-hit gives column coupling or extra pressure in the meeting row.
The remaining unclassified finite event is same-chain repetition.

Same-chain repeat role:

```text
same_chain_repeat_pressure_lemma.md
```

A repeat:

```text
A_i=A_m=x
```

propagates exactly in both directions:

```text
A_{i+1}=A_{m+1}
A_{i-1}=A_{m-1}.
```

So it closes a cycle of row `b_2`; it does not automatically create extra
pressure.  The same holds for `B_i=B_m=x`.

Current sharpest global gap, strengthened later by
`paired_chain_aligned_overlap_lemma.md`:

```text
force the closed row-b_2 and row-b_3 cycles to share two aligned consecutive
edges, or force an unequal-neighbor cross-hit pressure role.
```

Combined classification:

```text
paired_chain_first_obstruction_lemma.md
```

Status:

```text
candidate role map / audited finite boundary
```

Meaning:

```text
finite paired chains eventually repeat, but a same-chain repeat may be ordinary
cycle closure.  Finiteness alone therefore does not prove No-Free-Tail.
```

Remaining bridge:

```text
find a genuine E677 coupling between the two closed source-row cycles.
```

New proved coupling:

```text
cross_source_predecessor_fan_lemma.md
```

For all `x,a`:

```text
pred_a(x)=x*((a*x)*a).
```

For two source rows `a,b`:

```text
pred_a(x)=pred_b(x)
<=>
(a*x)*a=(b*x)*b.
```

At `x=r_2=t`, `a=b_2`, `b=b_3`:

```text
pred_{b_2}(t)=0
pred_{b_3}(t)=c_{-1},
```

so:

```text
c_{-1}=0
<=>
(b_2*t)*b_2=b_4*b_3.
```

Current gap:

```text
propagate this predecessor fan around the two closed source-row cycles.
```

One-step fan propagation:

```text
pivot_return_fan_lemma.md
```

Let:

```text
alpha=b_2*r_2
v=b_3*r_2=b_4.
```

The successor rows have return edges:

```text
alpha*w=r_2
v*p=r_2.
```

The inverse edge chain lifts these into row `r_2`, so that row has four forced
outputs:

```text
r_2*z_t=0
r_2*(b_4*b_3)=c_{-1}
r_2*g_alpha=w
r_2*g_v=p.
```

Current gap:

```text
classify the output collisions and compare the four-distinct branch with the
bad-cycle ladder edge in row r_2=b_k.
```

Pivot ladder combination:

```text
pivot_ladder_fan_lemma.md
```

For `r_2=t=b_k`, row `t` has five explicit edges:

```text
t*z=0
t*h=c_{-1}
t*g_alpha=w
t*g_v=p
t*r_{k-1}=b_{k+1}.
```

Any collision with `b_{k+1}` identifies `r_{k-1}` with the corresponding fan
column.  Otherwise all five outputs and columns are distinct.

Current gap:

```text
classify the predecessor expansion of these five row-t edges.
```

Completed collision audit:

```text
pivot_fan_collision_audit.md
```

All ten output pairs in:

```text
0,c_{-1},w,p,b_{k+1}
```

are classified.

Proved trap:

```text
0=c_{-1}
```

is the backward-zero trap.

The remaining collision roles are not automatic contradictions:

```text
common-column couplings;
r_4=r_2 from p=0;
ladder-column couplings.
```

Next candidate:

```text
Bad-Tail Repeat Lemma for r_4=r_2!=0.
```

Bad-tail repeat normalization:

```text
bad_tail_repeat_zero_triangle_lemma.md
```

Proved:

```text
r_4=r_2
<=>
(b_3*b_4)*b_3=0.
```

With:

```text
u=b_3*b_4
r=u*0,
```

this forces:

```text
u*b_3=0
r*u=b_4.
```

The next source-orbit zipper edge gives:

```text
u*((b_3*u)*b_3)=b_4.
```

Current gap:

```text
classify r=u*0 as a bad-cycle hit or a fresh active row.
```

Pressure-network progress:

```text
bad_tail_repeat_pressure_network.md
```

The repeat branch forces coupled pressure in rows:

```text
u, r=u*0, b_4.
```

The occupied role:

```text
r=b_3
```

forces:

```text
u=r_2
b_3*b_4=r_2
r_2*b_3=0,
```

so row `b_3` swaps `r_2` and `b_4`.

Other occupied `r=b_j` values produce row-`b_j` pressure and an extra row-`b_4`
spoke.  Fresh `r` produces a three-row pressure network.

Occupied self-swap relay:

```text
bad_tail_repeat_self_swap_relay.md
```

For `r=b_3`, offsets `r_2=b_4,b_5` are closed.  For farther offsets:

```text
rho=r_3=b_3*0
rho*b_3=r_2
m=rho*r_2
m*rho=0.
```

Thus the self-swap boundary recursively creates a second zero triangle.

Four-spoke recursive role:

```text
bad_tail_repeat_four_spoke_relay.md
```

Rows `u` and `b_4` each receive four forced spokes.  The occupied role:

```text
r=u*0=b_4
```

is equivalent to:

```text
q*b_3=0
```

for `q=b_3*u`.  With `R=q*0`:

```text
R*q=b_4.
```

So the zero triangle recurs one step farther along the row-`b_3` orbit.

## Update 2026-05-31

New organizing candidate:

```text
special_branch_low_layer_meta_lemma.md
special_branch_role_split_lemma.md
```

Status:

```text
candidate / special-branch role split
```

Scope:

```text
case45, 7*0=5, 6*5=5
```

New evidence:

```text
In layer 6*6=2:
  6*2=0 closed by immediate zero-hit
  6*2=1 closed by prefix-collapse
  6*2=3 closed by prefix-collapse
  6*2=4 closed by prefix-collapse
  6*2=6 closed directly
  6*2=7 closed by zero-hit plus direct exits
  6*2=8 closed by zero-hit plus direct exits
  status: closed
```

Interpretation:

```text
This upgrades source-orbit ladder from isolated zero-hit checks to a broader
role split: zero-hit, eventual zero-hit, compact zero-avoiding prefix-collapse,
and double-fixed self-loop boundary.
The role split now closes one full neighboring layer, 6*6=2.
It also closes the next neighboring layer:

```text
In layer 6*6=3:
  6*3=0 closed by immediate zero-hit
  6*3=1 closed by prefix-collapse
  6*3=2 closed by prefix-collapse
  6*3=4 closed by prefix-collapse
  6*3=6 closed directly
  6*3=7 closed by zero-hit plus direct exits
  6*3=8 closed by zero-hit plus direct exits
  status: closed
```
```

Loop checkpoint:

```text
Do not continue layer-by-layer into 6*6=4.
The direct check 6*6=4, 6*4=1 timed out at 60s.
Use this as a boundary signal and work on the low-layer meta-lemma instead.
```

Update 2026-06-03:

```text
The low-layer meta-lemma has moved upward again.
General row-0 predecessor ladder:
  z*(succ0(z)*0)=pred0(z)

For L3 zero-hit:
  6*6=k
  6*k=0
  6*0=r
  r*6=pred0(k)

now also forces:
  5*r=4

Best next attack:
  let p=pred0(k);
  lift the two edges r*6=p and k*((k+1)*0)=p through the inverse-edge chain;
  attack row p instead of enumerating r.

Diagnostic correction:
  row p is not the active computational row in the hard representative.
  The active row is row 5.
  New candidate bridge:
    row5_descent_bridge_lemma.md
  Current bridge route:
    6*0=r, 5*r=4, w=5*6, a=5*0, 4*a=3, b=5*a, a*(b*5)=0.

  Update: the late row-3 trap in the hard representative is now symbolically
  closed.  The final residual `5*3=8, 8*5=3, 3*3=0, 5*8 in {1,6}` is closed:
    e=1 by row-8 injectivity and row-5 collision;
    e=6 by reducing to `3*5 in {4,6}`.
  The value `3*5=4` closes by E677 with x=7,y=8 after forcing `8*7=0`.
  The value `3*5=6` closes by forcing `1*1=0`, which violates
  `0*(y*y) != y` for y=1.

  Next target: transfer the row-5 descent + row-3 late trap from the hard
  representative `k=4,r=1,w=2,a=3` to all L3 zero-hit returns.
  New transfer-map file:
    l3_zero_hit_transfer_lemma.md

  Additional progress:
    for the k=4 L3 zero-hit layer, the row-5 marker w=5*6 satisfies
      w in {1,2,3,7,8} \ {r};
    w=7 is a quick-exit role;
    in the representative k=4,r=1,w=2, the next marker has
      a=5*0 in {1,3,8};
    a=1 is a quick exit;
    a=3 and a=8 continue to different b=5*a domains.
  Current shape: L3 is becoming an a/b cascade lemma, not a single late-trap
  lemma.

  New extracted sublemma:
    a_row_zero_trap_lemma.md
  It factors the common tail:
    5*0=a, 5*a=b, c=b*5 => a*c=0,
    d=a*0, d*a=pred0(c), c=a*(c*succ0(a)).
  The row-3 late trap is the a=3 instance; the current row-8 branch is the
  a=8 instance.
  The row-8 instance is now closed in the representative cascade.
  Current closed representative:
    k=4,r=1,w=2.
  Next target:
    transfer the same a/b/c cascade to the remaining allowed w-values and
    r-values in the k=4 L3 zero-hit layer.
```

Current strategic candidate:

```text
source_orbit_ladder_lemma.md
source_orbit_role_map.md
```

Status:

```text
candidate / role mechanism
```

Important correction:

```text
The ladder uses finite E677 left-row permutation / inverse edge chain.
It is not a bare one-substitution consequence of E677.
```

New confirmed roles:

```text
immediate zero-hit:
  q=2, 6*2=0 closes via r*6=pred0(2)=1, without requiring h=2
  q=4, 6*4=0 closes via t*6=pred0(4)=3
  q=7, 6*7=0 closes via t*6=pred0(7)=6

eventual zero-hit:
  q=4, 6*4=1, 6*1=0 closes via r*6=pred0(1)=0
  q=4, 6*4=2, 6*2=0 closes via r*6=pred0(2)=1
  q=7, 6*7=1, 6*1=2, 6*2=0 closes via r*6=pred0(2)=1
```

Scope:

```text
case45, 7*0=5, 6*5=5, 6*6=8
```

Remaining:

```text
classify zero-avoiding source-orbit roles for q in {2,4,7}
```

Transfer check:

```text
The zero-hit role also appears in neighboring layers:
6*6=2: 6*2=0 closes via r*6=pred0(2)=1 for r in {1,3,4,7,8}.
6*6=3: 6*3=0 closes via r*6=pred0(3)=2 for r in {1,2,4,7,8}.
6*6=4: 6*4=0 closes via r*6=pred0(4)=3 for r in {1,2,3,7,8}.
```

Boundary:

```text
6*6=6 is not covered by the same root zero-hit route; it is now classified as
a self-loop/no-tail boundary needing a different invariant.
```

Resolution:

```text
Double-fixed self-loop | local closed / candidate role principle |
case45, 7*0=5, 6*5=5, 6*6=6 | double_fixed_self_loop_lemma.md |
6*5=5 and 6*6=6 force u=5*6, 5*u=5; all u close.
```

## Update 2026-05-28

Current strategic candidate:

```text
source_orbit_ladder_lemma.md
```

Status:

```text
candidate / role classification
```

Scope:

```text
case45, special branch 7*0=5, 6*5=5, current layer 6*6=8
```

Known:

```text
if 6*q=0 and 6*0=t, then t*6=pred0(q)
```

This closes the residue `q=2, 6*2=0, 2*6=2`.  A second zero-hit check
`q=3, 6*3=0` closed `r=2,4,7` but timed out at `r=1`, so the lemma is not
complete.  Next role to classify: source orbit `8 -> 3 -> 0 -> 1`.

Дата: 2026-05-24.

Этот файл является навигационной картой. Он не заменяет доказательства,
сертификаты и журналы. Если есть противоречие между этим файлом и
`CONTINUE_HERE.md`, для продолжения работы считать актуальным
`CONTINUE_HERE.md`.

Правило обновления: если кандидат закрыт или доказан, сразу поменять его
статус в этом файле. Не оставлять закрытую лемму в статусе `candidate`, иначе
следующий агент может начать уже завершенную ветку заново.

## Статусы

```text
general proved      - общее доказанное следствие E677
local closed        - локальная лемма/сертификат закрывает указанный узел
candidate           - рабочая формулировка, еще не финальная лемма
audit / correction  - исправляет или ограничивает старую гипотезу
map / navigation    - карта переходов или вспомогательная структура
historical          - полезно как история, но не текущая точка продолжения
```

## Общие доказанные инструменты

| Имя | Статус | Область действия | Файл | Короткий смысл |
| --- | --- | --- | --- | --- |
| Inverse edge chain | general proved | любые конечные E677-магмы | `inverse_edge_chain.md` | Если `a*z=c`, то `z=c*((a*c)*a)`. Это базовая обратная цепочка. |
| Bad-cycle ladder | general proved | плохой элемент `0`, цикл строки `0` | `research_summary_current.md` | Для `b_j=L_0^{-j}(0)` и `r_j=b_j*0`: `b_j*r_{j-1}=b_{j+1}`. |
| Row-0 reduction | general proved | плохой элемент `0` | `research_summary_current.md` | `(0*0)*0=b_2`; E255 для `0` сводится к `b_2*0=0`. |

## Локально закрытые узлы case 45

| Имя | Статус | Что закрыто | Файл | Следующий смысл |
| --- | --- | --- | --- | --- |
| Self-swap structure | local closed / structural | `7*0=4, 6*6=6, 6*5=4` | `self_swap_lemma.md` | Первый крупный self-swap узел; дал релейную карту. |
| Senior/far transfer | local closed | senior/far transfer внутри self-swap ветки | `senior_far_transfer_lemma.md` | Закрыт через `q`-подлемму и конечный `(p,q)` слой. |
| Far-row killer | local closed | малые far-row остатки после строки `b3` | `far_row_killer_lemma.md` | Микролемма: остаток закрывается одной far-row клеткой. |
| U-transfer / no-tail trap | local closed | `7*0=4, 6*6=6`, все `6*5=s` | `u_transfer_no_tail_trap_lemma.md` | Полная локальная лемма для self-узла `6*6=6`. |
| Secondary self-type relay | local closed / candidate generalization | `6*6=8, 6*5=7`, включая `u=2,q=2` | `secondary_self_type_relay_lemma.md` | Вторичный self-type закрывается переносом анализа на строку `u`. |
| Row6 cross-pair transfer | local closed | обе ориентации `{6*6,6*5}={7,8}` | `row6_cross_pair_transfer_lemma.md` | Cross-pair не является тупиком; закрывается тем же `u,q` слоем. |
| Case45 branch `7*0=4` | local closed | вся ветка `case45, 7*0=4` | `case45_7zero4_closed.md` | `6*6=5` невозможно, а все остальные значения `6*6` закрыты: `0,1,2,3,4,6,7,8`. |
| T5 zero-pass-through layer | local closed | `7*0=5, 6*5=5, 6*6=0` | `t5_zero_pass_through_lemma.md` | Zero-pass-through дает `r=6*0 => r*6=5`; `r=1,2,3,4` закрываются прямо, `r=8` закрывается через следующий орбитальный разрез `s=6*8`. |
| T5 row-7 relay layer | local closed | `7*0=5, 6*5=5, 6*6=7` | `t5_k7_row7_relay_lemma.md` | Row-6 orbit relay gives `q=6*7`, `h=q*6`, `7*h=6`; `q=1` closes directly, `q=2,3,4` close by `h`, and the repeated `h=8` tail closes by `8*8`. |
| T5 row-1 relay layer | local closed | `7*0=5, 6*5=5, 6*6=1` | `t5_k1_row1_relay_progress.md` | Row-6 orbit relay gives `q=6*1`, `h=q*6`, `1*h=6`; hard `q=8` tails close by source-orbit return `6*8=m`, `m*6=k`, `8*k=1`. |

## Текущие кандидаты

Update 2026-05-24:

| Имя | Статус | Текущая область | Файл | Что известно сейчас | Следующий допустимый шаг |
| --- | --- | --- | --- | --- | --- |
| Marker bridge transfer | candidate / local closed bridge layer | перенос row-6 маркера из `7*0=4` на `7*0=2,3,5` | `marker_bridge_transfer_lemma.md` | Ручная формула: если `6*t=5`, `6*5=s`, `a*t=5`, `a*5=6`, то `6*a=s*6`. Bridge branches закрыты для `t=2` и `t=3` через split `u=t*6=6*a`. | Оформить bridge/no-bridge split как кандидат-лемму для self-layers `t=2,3`; затем проверить special branch `t=5`. |
| Senior column fallback | candidate / relay fallback | no-bridge ветки после `6*8=6*b1` | `senior_column_fallback_lemma.md` | Ручная цепочка: если `6*8=m`, `r=6*m`, `h=r*6`, то `m*h=8`. Для `m=0` строка `0` известна, поэтому `(6*0)*6=7`; контроль `6*0=3` принудил `3*6=7` и сжал row6 до 18. | Для `m != 0` изучать перенос активности в строку `m`, а не перечислять все row6-кандидаты. |
| Row-6 orbit relay | candidate / local closed no-bridge layer | no-bridge ветки после `6*8=m`, орбита элемента `8` в строке `6` | `row6_orbit_relay_lemma.md` | Обобщает fallback: если `6*z0=z1` и `6*z1=z2`, то `z1*(z2*6)=z0`. No-bridge закрыт для `t=2` и `t=3`: все соответствующие markers `6*8` закрыты. | Оформить вместе с bridge-transfer как candidate local lemma for self-layers `t=2,3`. |
| Bridge/no-bridge self-layer | candidate / local closed | self-layers `t=2,3` в `case45` | `bridge_no_bridge_self_layer_lemma.md` | Закрыто: `7*0=t`, `6*t=5`, `6*6=6`, `6*5=t`, `t in {2,3}`. Bridge branch закрывается через `6*a=t*6`; no-bridge через senior orbit `6*8`. | Проверить special branch `t=5`, не предполагая автоматический перенос. |

| Имя | Статус | Текущая область | Файл | Что известно сейчас | Следующий допустимый шаг |
| --- | --- | --- | --- | --- | --- |
| Low-pair transfer | candidate with stable two-layer form | низкие `6*5 in {1,2,3,4}` при `6*6=7/8` | `low_pair_transfer_lemma.md` | `u=6` закрывается мгновенно; слой `u=8=b1` закрыт для всех `s=1,2,3,4`; low-to-low слой теперь стабилен в `6*6=7` и `6*6=8`: endpoint targets `u=b5,b8` закрываются на `q=u*6`, interior targets `u=b6,b7` имеют единственный extra-tail `q=b2`, который закрывается через `r=b3*b2`. | Проверить недостающие представители только как sanity check; не расширять перебор; оформить low-to-low relay как ролевую подлемму и подняться к карте `7*0=4`. |
| Low-to-low role relay | candidate / local finite certificate | low-to-low targets внутри `7*0=4`, `6*6=7/8` | `low_to_low_role_lemma.md` | Ролевая форма оформлена: target `u` endpoint закрывается на `q`; target `u` interior имеет единственный хвост `q=b2`, закрываемый через `r=b3*b2`. Ручно выведен общий верхний список `q in {0,b8,b7,b3,b2}`. Субагентская сверка подтвердила `r`-слой для `6*6=7`, `u=2,3`. | Проверить недостающие sanity representatives; не объявлять `7*0=4` закрытой до подтверждения полного покрытия. |
| No-tail trap as broader principle | candidate | полный 9-цикл без внешнего хвоста | `u_transfer_no_tail_trap_lemma.md`, `relay_graph_lemma.md` | Работает локально сильно; нужно аккуратно формулировать область действия, не считать автоматической общей теоремой. | Сравнивать только с узлами, где понятно, есть ли внешний хвост. Не объявлять общей леммой без проверки границы применимости. |
| Secondary self-type as role pattern | candidate | случаи `q=u`, где активность переносится на строку `u` | `secondary_self_type_audit.md`, `secondary_self_type_relay_lemma.md` | После аудита старая лишняя связь убрана; валидная схема использует `u*h=0`, затем `u*0=r`, `r*u=pred0(h)`. | При новом `q=u` сначала переносить анализ на строку `u`, а не продолжать дробить старую активную строку. |
| Directed two-edge witness | candidate / model evidence / shallow saturation open | направленный путь `a->v->c` в `H_b` | `directed_two_edge_witness_candidate.md` | В модели 496 и линейных E677-моделях `Y=(b*c)*(u*k)` дает `Y*b=b`; глубина-2 синтез и два слоя ground-насыщения не дали локального доказательства. | Не углублять перебор без нового промежуточного тождества; основной фронт вернуть к тройному вееру и узлу `2+1`. |
| Right-fixer to balanced witness | general proved | любой `Y*b=b` в конечной E677-магме | `right_fixer_to_balanced_witness_lemma.md` | Два обратных шага по строке `b` дают `t=Y*((b*Y)*b)`, `z=t*b` и `(b*z)*b=z`. | Использовать как преобразователь; отдельный синтез `z` больше не нужен. |

## Аудиты и исправления

| Тема | Статус | Файл | Что важно помнить |
| --- | --- | --- | --- |
| Недоказанная связь `3*0=h` | audit / correction | `secondary_self_type_audit.md`, `research_log.md` | Связь не следует из использованной релейной цепочки и не должна применяться как условие. Закрытие соответствующего хвоста было перепроверено без нее и сохранилось. |
| Runtime `node.exe` через WindowsApps | workflow correction | `AGENT_WORKFLOW.md` | Если `node` дает `Access is denied`, не повторять тот же путь; использовать Node REPL / встроенный runtime Codex. |
| Старые логи size 8 | historical | `archive/size8_remaining_log.txt` | Содержит старые таймауты. Текущий результат размера 8 брать из `size8_verified_split_log.txt`. |

## Текущий фронт

Актуальную точку продолжения брать из `CONTINUE_HERE.md`.

На момент этой карты:

```text
case45
7*0=4 closed
next top branches: 7*0=2, 7*0=3, 7*0=5
```

Последний структурный результат:

```text
low-to-low transfer:
Low={b5,b6,b7,b8}.
endpoint u in {b5,b8} closes directly by q=u*b3 and b3*(0*q)=0.
interior u in {b6,b7} has one extra tail q=b2.
That extra tail closes by r=b3*b2 in Low \ {s,u}.
```

Проверенные представители:

```text
s=2,u=1 and s=2,u=4 compact representatives closed.
s=1,u=2 and s=1,u=3 wide representatives closed at q-layer except q=7.
q=7 representatives for (s,u)=(1,2),(4,2),(1,3),(4,3) closed by r=6*7.
```

Следующий правильный шаг:

```text
не работать дальше внутри 7*0=4;
сравнить верхние ветки 7*0=2,3,5 через row-6 relay;
начать с ролевой формулировки 7*0=t, 6*t=5, first split 6*6.
```

## Как пользоваться

1. Начинать с `CONTINUE_HERE.md`.
2. Проверять статус нужной леммы здесь.
3. Читать соответствующий файл леммы только если нужно доказательство,
   сертификат или детали.
4. Если найден новый аудит или изменение области действия, обновить этот файл
   короткой строкой, не переписывая старые журналы.

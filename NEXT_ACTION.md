# Next Action

Date: 2026-06-25.

Read this file first.  Then read `CURRENT_FRONTIER.md` only if more context is
needed.

## Current Goal

Continue the E677 -> E255 proof through the current G12 residual:

```text
shared-step anchored triangle / anchored-X3 / M7
```

Do not restart broad crossed-fan or relay-cycle case search.

## Current Narrow Frontier

For a shared step:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
alpha=pred_z(h),
```

the strong target is:

```text
U*h=W*h.
```

M496 verifies this for all `892800` shared-step row pairs.

The false branch `U*h!=W*h` has been reduced to anchored-X3:

```text
T=U*h,
S=W*h,
T!=S.
```

In `H_h`:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

and the second layer is the fixed-target source-successor layer:

```text
U -> T -> T*h -> ...
W -> S -> S*h -> ...
z -> b -> b*h -> ...
```

## Routed Part

The first finite event among the three right-`h` source-successor orbits is
routed unless it is a clean self-repeat inside one orbit:

```text
anchored_m7_first_event_routing_lemma.md
```

Routed events:

```text
cross-orbit source hit      -> full interval / same-source recurrence;
cross-orbit output merge    -> incoming fan or full interval;
input-output cross hit      -> actual H_h path attachment;
watched/core hit            -> visible/core relay attachment.
```

## Exact Live Residual

The only live branch is:

```text
clean same-orbit right-h self-repeat
```

with no earlier cross-orbit source hit, output merge, input-output cross hit,
watched/core hit, or shorter self-repeat.

Use:

```text
anchored_x3_clean_self_repeat_normal_form.md
anchored_m7_first_event_routing_lemma.md
anchored_m7_saturation_diagnostic.md
anchored_m7_cycle_end_template.md
anchored_m7_cycle_zipper_lemma.md
anchored_m7_cycle_end_saturation_diagnostic.md
anchored_m7_zipper_first_collision_target.md
anchored_m7_zipper_target_advance_lemma.md
anchored_m7_coupled_zipper_bridge_residual.md
anchored_m7_zipper_lift_advance_equivalence_lemma.md
anchored_m7_clean_v3_necklace_obstruction.md
anchored_m7_v3_necklace_measure_extension.md
anchored_m7_reduces_to_general_v3_admissibility.md
clean_same_input_v3_admissibility_frontier.md
```

## d-Term Detour: Deprioritized

The M496 d-term hint is now recorded as a warning, not the main next target:

```text
m496_anchored_d_term_scan_diagnostic.md
anchored_d_term_strong_branch_raw_diagnostic.md
```

Reason:

```text
M496 is fully idempotent: x*x=x for all elements.
```

So the M496 relations:

```text
z*d(h)=b,
d(h)=h,
h*h=h
```

mostly collapse to `z*h=b` plus idempotence.  A local raw check also showed
that the visible strong anchored triangle alone does not short-close
`h*h!=h` or `d(h)!=h`.

Only return to d-terms if a non-idempotent db model shows the same pattern or
a new structural reason appears.

## Next Proof Target

Do not test more one-step equalities among `T1=T*h`, `S1=S*h`, `B1=b*h`.
Those already did not close.  Return to the whole clean cycle.

Formulate the self-repeat with a cycle start/end:

```text
r_0*h=r_1,
r_{n-2}*h=r_{n-1},
r_{n-1}*h=r_0,
```

and the attached fixed-target predecessor edges:

```text
I_i=h*(r_{i+1}*r_i),
I_i -> r_{i+1} in H_h.
```

The cycle-end check did not force direct endpoint collisions.  It did prove
the zipper form:

```text
I_i = h*(r_{i+1}*r_i) = (r_{i-1}*r_i)*r_{i-1}.
```

Next, try to prove that this clean cyclic zipper either:

```text
1. creates strict clean theta;
2. repeats a full ported interval in an independent role;
3. regenerates anchored-X3 with smaller M7;
4. hits the old/core footprint.
```

Use the immediate collision split from:

```text
anchored_m7_zipper_first_collision_target.md
```

Input repeats give outgoing fans, output repeats contradict first-repeat
minimality, and input-output hits give actual `H_h` paths.  The live residual
is a fully clean cyclic zipper matching.

Target advance now sharpens the residual:

```text
H_h:       I_i -> r_{i+1}
H_{r_i}:  h   -> A_i,     A_i=r_{i-1}*r_i
I_i=A_i*r_{i-1}
```

So the active object is:

```text
clean cyclic zipper matching
+
clean same-input bridge necklace at common input h.
```

Use:

```text
anchored_m7_coupled_zipper_bridge_residual.md
anchored_m7_zipper_lift_advance_equivalence_lemma.md
anchored_m7_clean_v3_necklace_obstruction.md
```

The coupled object is now identified as a closed clean necklace of standard
V3-type same-input bridges at the common input `h`.

Next target: formalize the measure comparison:

```text
original M7 = first self-repeat rank of the right-h source orbit;
new bridge rank = first adjacent V3 bridge inside that orbit.
```

If that bridge is admissible under the existing V3 descent boundary, the M7
self-repeat is not terminal.  If not, record the exact obstruction in the V3
measure.

The measure extension is now named:

```text
anchored_m7_v3_necklace_measure_extension.md
```

Next exact task: prove or refute the admissibility sentence:

```text
An adjacent clean V3 bridge born inside the anchored M7 self-repeat cycle is
admissible as a smaller relay object under M8.
```

This is now reduced to the unified principle:

```text
Clean same-input two-target bridge admissibility.
```

It must cover both first-extra V3 bridges and anchored-M7 adjacent V3 bridges.
If this general V3 admissibility is proved, the clean M7 necklace closes.

Use:

```text
clean_same_input_v3_admissibility_frontier.md
```

The hard case is now:

```text
ungenerated clean same-input two-target bridge
whose lifted H_z pair is clean-disjoint.
```

Next target: prove such a bridge is admissible as a smaller measured relay
object, or prove its common input must be generated/watched/core in the
first-extra and anchored-M7 sources.

The external `eq677` repository suggests using an ATP/e-graph cycle-end
template rather than only first-layer closure:

```text
eq677_repo_idea_notes.md
atp/anchored_m7_cycle_end.p
```

The external db scan is now recorded in:

```text
eq677_db_shared_step_scan_diagnostic.md
tools/eq677_db_shared_step_scan.js
```

It downgrades the unrestricted strong hypothesis:

```text
shared-step anchored triangle => U*h=W*h
```

because the full public db has 18348 false shared-step pairs, including 17040
with all named terms distinct.  The same 17040 false pairs are clean
anchored-X3 triples `p,q,alpha -> T,S,b` in `H_h`; only 1308 route by visible
X3 hits.

The second triangle layer from `anchored_x3_second_triangle_pressure_lemma.md`
was also scanned.  It routes 5928 of the clean-X3 triples by visible endpoint
hits, but 11112 remain fully clean after both layers.  Therefore `U*h=W*h`
can only be pursued with extra bad-target/minimal-clean assumptions; local
two-layer pressure alone is not enough.  Otherwise continue the false branch
through the source-orbit/M7 route and then V3 admissibility.

The same db scanner now follows the three source-successor orbits in `H_h`.
Among the 17040 clean-X3 triples:

```text
10800 route by first source-orbit event;
6240 reach clean same-orbit self-repeat;
0 have no finite event.
```

So the external db supports the current theoretical path:

```text
clean-X3 -> M7 clean self-repeat -> zipper -> V3 necklace.
```

Next exact target remains the proof, not more broad diagnostics:

```text
prove the clean M7 self-repeat zipper/V3 necklace is admissible under the
unified clean same-input V3 measure, or isolate the missing hypothesis.
```

The unified V3 frontier has been sharpened by:

```text
clean_same_input_v3_second_layer_expansion_lemma.md
```

Any same-input V3 bridge:

```text
p*z=s,
q*z=r,
A=p*s,
B=q*r
```

forces, in `H_z`, not only:

```text
P=z*(s*p) -> s,
Q=z*(r*q) -> r,
```

but also:

```text
A*p -> s*z,
B*q -> r*z.
```

So the remaining clean V3 obstruction is a clean four-edge matching in `H_z`.
Next proof target: show this four-edge matching routes or is admissible as the
smaller relay object needed for both first-extra V3 and anchored-M7 necklace.

The four-edge V3 matching now also reduces to fixed-target source orbits:

```text
clean_v3_fixed_target_source_orbit_reduction.md
```

The two source orbits in `H_z` are:

```text
p -> s -> s*z -> ...
q -> r -> r*z -> ...
```

First source-orbit events route by existing fixed-target/same-target roles.
The only clean residual is a same-orbit right-`z` self-repeat, hence a zipper
with the same form as anchored-M7.  Next proof target: prove the V3-born
zipper/adjacent bridge is a smaller admissible relay object, or isolate the
missing hypothesis for that measure comparison.

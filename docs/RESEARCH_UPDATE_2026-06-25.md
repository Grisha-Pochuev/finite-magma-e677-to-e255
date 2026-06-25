# Research Update: 2026-06-25

This update publishes the post-2026-06-17 relay-reduction layer and the
current anchored-X3/M7 frontier.

## What Changed

The previous public frontier was the branch-closure No-Free-Tail candidate.
The current work has pushed that layer through a long sequence of local
reductions:

```text
crossed-fan clean external bridge routing;
right-b orbit and ported-interval transitions;
beta-layer and reversible-square reductions;
same-row recurrence inventory;
shared-step anchored triangle;
anchored-X3/M7 source-orbit routing.
```

The current public continuation point is now:

```text
NEXT_ACTION.md
```

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

The false branch `U*h != W*h` has been reduced to an anchored-X3/M7 source
orbit configuration.  Most first-event cases are routed; the live residual is:

```text
clean same-orbit right-h self-repeat.
```

## New Public Files

The update adds a large set of lemma, boundary, candidate, and diagnostic
files under `lemmas/`.  Use `docs/RESULTS_INDEX.md` for navigation rather than
reading them in timestamp order.

Important current files include:

```text
lemmas/shared_step_anchored_triangle_boundary.md
lemmas/anchored_identity_partial_reduction.md
lemmas/anchored_x3_three_target_bridge_boundary.md
lemmas/anchored_x3_source_orbit_boundary.md
lemmas/anchored_x3_second_triangle_pressure_lemma.md
lemmas/anchored_x3_visible_short_repeat_lemma.md
lemmas/anchored_x3_clean_self_repeat_normal_form.md
lemmas/anchored_m7_first_event_routing_lemma.md
lemmas/anchored_m7_cycle_end_template.md
lemmas/relay_minimality_measure_candidate.md
```

## Diagnostics and Tools

The update also publishes supporting diagnostic tools for M496 and anchored-M7
checks.  These diagnostics are evidence and guidance, not proof:

```text
tools/m496_shared_step_orbit_split.js
tools/m496_first_extra_intersection_roles.js
tools/m496_shared_step_relation_scan.js
tools/m496_target_advance_periods.js
tools/anchored_identity_saturation.js
tools/anchored_m7_saturation.js
tools/m496_anchored_d_term_scan.js
```

## ATP Templates

The new `atp/` folder contains experimental TPTP templates:

```text
atp/anchored_x3_m7_self_repeat.p
atp/anchored_m7_cycle_end.p
```

These files are meant as theorem-prover working surfaces for local residuals.
They are not a completed formalization.

## Boundary

No new finite size is claimed closed in this update.  The reproducible finite
status remains:

```text
sizes 5, 6, 7: public rerun script and recorded log
size 8: public rerun script and recorded log
size 9: recorded research closures, not yet a full public rerun certificate
```

The following remain open:

```text
clean same-orbit right-h self-repeat;
anchored identity U*h=W*h in full generality;
global No-Free-Tail Lemma;
E677 => E255 for all finite magmas.
```

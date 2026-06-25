# Next Action

Date: 2026-06-21.

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

The external `eq677` repository suggests using an ATP/e-graph cycle-end
template rather than only first-layer closure:

```text
eq677_repo_idea_notes.md
atp/anchored_m7_cycle_end.p
```

# Clean External-Bridge Fourth-Stage Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / removes clean same-target matching as independent residual
```

## Purpose

This updates:

```text
clean_external_bridge_third_stage_reduction_lemma.md
```

after adding the same-target and same-input transport tools:

```text
same_target_pair_collision_trichotomy_lemma.md
beta_coupled_same_target_pair_advance_lemma.md
same_input_lift_target_advance_lemma.md
```

## Third-Stage Residuals

The third-stage list was:

```text
U1. same-row recurrence boundaries;
U2. shared-edge divergence Beta_i=H_i;
U3. beta-coupled same-target pair;
U4. shifted-repeat same-input split lifted to H_T;
U5. beta-anchored reversible square.
```

## U3/U4 After Transport

For U3, local collisions inside:

```text
H_{A_j}: E_{i,j}->A_i and Beta_j->b
```

are routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
```

If the pair is clean-disjoint, then:

```text
beta_coupled_same_target_pair_advance_lemma.md
```

advances it to:

```text
H_{A_i}: A_j -> b,
H_b:     A_j -> x_{j+1}.
```

So U3 becomes a two-target bridge sharing the input `A_j`.

For U4, the same mechanism is general:

```text
same_input_lift_target_advance_lemma.md
```

A clean lifted same-input pair in `H_T` target-advances back to a two-target
bridge sharing the original input `T`.

Thus the clean same-target matching residual is removed.  It is just the
lifted face of a clean same-input two-target bridge.

## Fourth-Stage Residual List

After these transports, the clean external bridge is reduced to:

```text
V1. same-row recurrence boundaries;

V2. shared-edge divergence:
    rows b and x_i share H_i -> A_i;

V3. clean same-input two-target bridge:
    p*z=s, q*z=r with s!=r,
    whose lift has no local same-target collision;

V4. beta-anchored reversible square:
    containing Beta_j -> b in H_{A_j}.
```

The removed residual is:

```text
clean disjoint same-target matching.
```

## Next Useful Target

The next useful step is to compare V3 and V4.

Both are two-row, two-target configurations.  V3 is a lift/advance square from
a shared input.  V4 is a target-swap reversible square anchored at a beta foot.

A future reduction should show that a minimal clean residual cannot keep both
faces disjoint from the generated A/X/H layers and the visible crossed-fan
footprint; otherwise it must be recorded as the exact remaining two-row
two-target square boundary.

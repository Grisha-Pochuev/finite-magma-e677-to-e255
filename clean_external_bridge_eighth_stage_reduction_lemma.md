# Clean External-Bridge Eighth-Stage Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / Y2 removed; Y3 sharpened to coupled clean cycle shell
```

## Purpose

This updates:

```text
clean_external_bridge_seventh_stage_reduction_lemma.md
```

using:

```text
y2_shared_edge_divergence_folds_to_base_bridge_lemma.md
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_successor_lemma.md
y3_fixed_target_source_orbit_boundary.md
```

## Seventh-Stage Residuals

The previous residual list was:

```text
Y1. same-row recurrence boundaries;

Y2. shared-edge divergence:
    rows b and x_i share H_i -> A_i;

Y3. clean three-row cycle comparison at a generated input A_j.
```

## Y2 Reduction

The equality:

```text
Beta_i=H_i
```

means rows `b` and `x_i` share:

```text
H_i -> A_i.
```

The next step at `A_i` is the unavoidable row-b/generated bridge:

```text
row b:   A_i -> D_i=b*A_i,
row x_i: A_i -> b.
```

That bridge was already reduced in:

```text
row_b_generated_input_bridge_lemma.md
clean_external_bridge_sixth_stage_reduction_lemma.md
```

and the fresh row-b successor branch returns through:

```text
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
```

So Y2 is no longer an independent residual.

## Y3 Sharpening

The clean Y3 normal form is:

```text
row p:   P      -> A_j -> S,
row x_j: Beta_j -> A_j -> b,
row b:   H_j    -> A_j -> D_j.
```

The source-successor cycles through `A_j` give:

```text
row p   returns through P,
row x_j returns through Beta_j,
row b   returns through H_j.
```

By:

```text
y3_three_cycle_first_intersection_boundary.md
```

any first cross-hit between these three cycles routes to a same-input split,
same-target pair, fan, path, watched hit, or same-row recurrence.

Thus the only remaining Y3 case is:

```text
Z3. clean disjoint three-cycle shell through A_j.
```

Inside the fixed target graph `H_{A_j}`, the same object has a second
description.  By:

```text
fixed_target_source_successor_lemma.md
```

the source rows advance under:

```text
r -> r*A_j.
```

So the three Y3 source rows lie on two right-`A_j` source orbits:

```text
p -> S -> S*A_j -> ...
x_j -> b -> D_j -> D_j*A_j -> ...
```

The row `b` is therefore not a third independent source orbit; it is the next
generated source after `x_j`.

If these two source orbits cross, the same source row repeats the same full
ported interval in `H_{A_j}`.  If they do not cross before internal repeat,
the remaining source-side object is:

```text
Z3-source. two clean disjoint right-A_j source cycles in H_{A_j}.
```

## Eighth-Stage Residual List

The clean external bridge is now reduced to:

```text
Z1. same-row recurrence boundaries;

Z3. coupled clean cycle shell at A_j:
    - three disjoint left-row cycles through A_j
      for rows p, x_j, b;
    - two disjoint fixed-target source orbits in H_{A_j}
      born from p and from x_j -> b.
```

The removed residual is:

```text
Y2 shared-edge divergence Beta_i=H_i.
```

The sharpened residual is:

```text
Y3 -> Z3 coupled clean cycle shell.
```

## Next Useful Target

Attack the coupled shell, not the old X3/Y3 local matching.

The exact next question is whether the shared product:

```text
p*A_j=S
```

can keep both induced motions clean:

```text
left row-p cycle:
  A_j -> S -> p*S -> ...

right-A_j source orbit:
  p -> S -> S*A_j -> ...
```

without producing a watched hit, a source-row repeat that repeats a full
ported interval in `H_{A_j}`, or a cross-hit with the generated orbit:

```text
x_j -> b -> D_j -> ...
```


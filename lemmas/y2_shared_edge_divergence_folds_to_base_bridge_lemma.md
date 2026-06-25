# Y2 Shared-Edge Divergence Folds To Base Bridge Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / Y2 is not an independent residual
```

## Purpose

This removes the seventh-stage residual:

```text
Y2. shared-edge divergence Beta_i=H_i.
```

The equality is useful, but it does not create a new open branch.  It is a
stronger form of the unavoidable row-`b` / generated-row bridge that was
already reduced in:

```text
row_b_generated_input_bridge_lemma.md
clean_external_bridge_sixth_stage_reduction_lemma.md
```

## Setup

Use the generated data:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
H_i=pred_b(A_i),
Beta_i=pred_{x_i}(A_i),
D_i=b*A_i.
```

Thus:

```text
b*H_i=A_i,
x_i*Beta_i=A_i.
```

Assume Y2:

```text
Beta_i=H_i.
```

Then:

```text
b*H_i=A_i,
x_i*H_i=A_i.
```

So rows `b` and `x_i` share the directed edge:

```text
H_i -> A_i.
```

## Divergence Step

At the next input `A_i`, the two rows have outputs:

```text
row b:   A_i -> D_i,
row x_i: A_i -> b.
```

```text
D_i=b
```

is exactly the common-edge fan boundary where rows `b` and `x_i` share:

```text
A_i -> b.
```

This is the first branch from:

```text
row_b_generated_input_bridge_lemma.md
```

Otherwise the two rows split at the same generated input:

```text
A_i -> D_i,
A_i -> b.
```

This is the unavoidable base row-b/generated same-input bridge.

## Target-Advance Form

Target-advance of the two intervals gives:

```text
H_{D_i}: A_i -> b*D_i,
H_b:     A_i -> x_{i+1}.
```

This is precisely the bridge form routed in the sixth-stage reduction.

The extra Y2 equality also gives the shared-edge return coupling:

```text
D_i*b=b*x_i,
A_i*(D_i*b)=H_i,
```

but that coupling is additional structure on the same bridge, not a separate
residual.

## Consequence

Y2 folds into the already routed base row-b/generated bridge split:

```text
1. D_i=b:
   common-edge fan over A_i -> b;

2. D_i hits a watched layer:
   route by that hit;

3. D_i fresh:
   row-b successor chain from A_i eventually hits H_k and then A_k.
```

The fresh case is handled by:

```text
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
```

So `Beta_i=H_i` should no longer appear as an independent clean external
bridge residual.  It is a strengthened entrance into the same row-b/generated
bridge mechanism.

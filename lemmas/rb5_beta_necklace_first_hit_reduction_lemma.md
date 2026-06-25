# R-b5 Beta-Necklace First-Hit Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / beta necklace has no fresh residual beyond known beta/Z3 routes
```

## Purpose

This proves the coverage candidate from:

```text
rb5_beta_necklace_reduction_candidate.md
```

for the start-return R-b5 A-cycle boundary:

```text
rb5_start_return_a_cycle_beta_pair_boundary.md
```

## Setup

Let:

```text
A_{i_0} -> A_{i_1} -> ... -> A_{i_{n-1}} -> A_{i_0}
```

be a minimal row-`b` A-layer cycle:

```text
b*A_{i_r}=A_{i_{r+1}}.
```

At each vertex:

```text
x_{i_r}*A_{i_r}=b,
x_{i_r}*b=x_{i_r+1},
Beta_{i_r}=pred_{x_{i_r}}(A_{i_r}).
```

The lifted pair in `H_{A_{i_r}}` is:

```text
H_{i_r}    -> A_{i_{r+1}},
Beta_{i_r} -> b.
```

## First Nonfresh Beta Event

Scan the cycle and all beta predecessor chains:

```text
Z_{i_r}^1=Beta_{i_r},
Z_{i_r}^{m+1}=pred_{x_{i_r}}(Z_{i_r}^m).
```

Take the first event where a beta-chain vertex hits:

```text
visible footprint,
generated A-layer,
generated X-layer,
generated H-layer,
another beta-chain vertex,
or its own earlier vertex.
```

If the first event occurs already at:

```text
Beta_{i_r},
```

then:

```text
beta_layer_reduction_lemma.md
```

routes it as one of:

```text
Beta=H       -> shared-edge divergence folded into base bridge;
Beta=A       -> same-input split / beta-coupled same-target pair;
Beta=X       -> beta-X reversible square;
visible hit  -> core attachment;
fresh beta   -> continue the beta zipper.
```

The first four are already routed.  The fifth is handled below.

## All First Beta Feet Fresh

Assume every first beta foot around the A-cycle is fresh relative to the
watched layers.

For each fixed row `x_{i_r}`, the fresh beta extension is a backward traversal
of the same finite row cycle that contains:

```text
A_{i_r} -> b -> x_{i_r+1}.
```

Therefore:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

forces the beta zipper to hit the generated X-layer.

Take the earliest such generated X-hit over all cycle vertices:

```text
Z_{i_r}^m=x_j.
```

Then:

```text
deep_beta_x_hit_reduction_lemma.md
```

routes it to:

```text
1. watched-layer hit;
2. row-x_i same-row recurrence;
3. beta first-hit routing at Beta_j;
4. beta-anchored reversible square.
```

The beta-anchored reversible square is not independent by:

```text
fresh_reversible_square_beta_anchor_lemma.md
```

and was absorbed in the later clean bridge reductions through:

```text
clean_external_bridge_tenth_stage_reduction_lemma.md
```

## Cross-Chain Beta Collision

If before the generated X-hit two beta-chain vertices collide, then the
collision is not a fresh necklace event.

At equal target/input roles it is a same-target collision handled by:

```text
same_target_pair_collision_trichotomy_lemma.md
```

At a repeated source-row role it is a same-row recurrence already listed in:

```text
same_row_recurrence_inventory.md
```

At a generated A/X/H hit it falls under the beta first-hit routing above.

## Consequence

The R-b5 beta necklace has no independent fresh residual.

It reduces to:

```text
visible/core attachment;
same-target fan/path/full-interval collision;
base row-b/generated bridge;
beta-X reversible square already beta-anchored;
Z3/tenth-stage clean bridge reductions;
or same-row recurrence.
```

Thus the start-return R-b5 A-cycle is not a new branch outside E11.  Its only
remaining contribution is through the already unified same-row recurrence /
minimal relay descent frontier.

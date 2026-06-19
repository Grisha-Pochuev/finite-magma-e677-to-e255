# R-x Beta-Chain Recurrence Absorption Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / R-x recurrence is absorbed by beta-X and existing recurrence routes
```

## Purpose

This removes `R-x` from:

```text
same_row_recurrence_inventory.md
```

as an independent recurrence subtype.

`R-x` is a same-row recurrence inside the beta predecessor chain of some row
`x_i`.

## Setup

Use the beta zipper:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m).
```

So:

```text
x_i*Z_i^{m+1}=Z_i^m.
```

A same-row recurrence in this chain is:

```text
Z_i^r=Z_i^s,
r>s>=1.
```

## First-Hit Split

The fresh beta extension is already governed by:

```text
beta_fresh_extension_first_hit_boundary.md
```

Before a main-chain same-row recurrence can be treated as clean, one must
check:

```text
1. watched hits of Z_i^m;
2. watched hits of shifted columns T_i^m=Z_i^{m-2}*x_i;
3. shifted-column repeats T_i^r=T_i^s.
```

Watched hits route by layer.  Shifted-column repeats route by:

```text
beta_zipper_shifted_repeat_split_lemma.md
same_input_split_target_lift_lemma.md
```

to a same-input split and then to a same-target pair.

## No Clean Pure Beta Cycle

If no watched hit and no shifted-column repeat occurs before the main
row-`x_i` recurrence, then:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

applies.  The beta chain cannot remain disjoint: it must hit the generated
X-layer, at worst:

```text
Z_i^m=x_{i+1}.
```

The generated X-hit is routed by:

```text
deep_beta_x_hit_reduction_lemma.md
```

to:

```text
1. watched-layer hit;
2. row-x_i recurrence of a smaller/local swap type;
3. beta first-hit routing at Beta_j;
4. beta-anchored reversible square.
```

The beta-anchored reversible square is not independent:

```text
fresh_reversible_square_beta_anchor_lemma.md
```

and was absorbed by the later clean bridge reductions.

## Consequence

An `R-x` beta-chain recurrence is not an independent E11 residual.

It reduces to:

```text
visible/generated hit;
same-input split / same-target pair;
deep beta-X route;
beta-anchored reversible square already absorbed;
or a smaller same-row recurrence already covered by the unified recurrence
inventory.
```

So the global E11 recurrence frontier should not count `R-x` as a separate
clean branch.  It is an internal presentation of the beta/Z3 route already
reduced to E11.


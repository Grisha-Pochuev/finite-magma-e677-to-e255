# R-b5 Start-Return A-Cycle Beta-Pair Boundary

Date: 2026-06-19.

Status:

```text
boundary / exact remaining R-b5 start-return cycle after footprint descent
```

## Purpose

This records the only R-b5 case not removed by:

```text
rb5_a_layer_footprint_descent_boundary.md
relay_minimality_measure_candidate.md
```

The remaining case is a minimal start-return A-layer cycle:

```text
A_{i_0} -> A_{i_1} -> ... -> A_{i_{n-1}} -> A_{i_0}
```

under row `b`.

## Setup

For each cycle index `r`:

```text
b*A_{i_r}=A_{i_{r+1}},
```

with indices modulo `n`.

At the same generated input `A_{i_r}`:

```text
x_{i_r}*A_{i_r}=b,
x_{i_r}*b=x_{i_r+1}.
```

So the unavoidable base bridge is:

```text
row b:       A_{i_r} -> A_{i_{r+1}},
row x_{i_r}: A_{i_r} -> b.
```

## Lifted Pair At Each A Vertex

Lift the same-input bridge at `A_{i_r}` into `H_{A_{i_r}}`.

The pair is:

```text
H_{i_r}    -> A_{i_{r+1}}   carried by row b,
Beta_{i_r} -> b             carried by row x_{i_r},
```

where:

```text
b*H_{i_r}=A_{i_r},
x_{i_r}*Beta_{i_r}=A_{i_r}.
```

This is the same beta-anchor/row-b partner configuration used in:

```text
beta_anchor_row_b_partner_reduction_lemma.md
```

## First Collision Split Around The Cycle

As `r` runs around the minimal A-cycle, the lifted pairs may collide.

The first collision among:

```text
H_{i_r}, Beta_{i_r}, A_{i_{r+1}}, b
```

has one of the standard same-target roles:

```text
same input       -> outgoing fan;
same output      -> incoming fan;
input-output hit -> directed path;
same full interval -> source-row collision.
```

If the collision is between different cycle positions, it is an independent
branch-role event unless it is a same-row row-`b` recurrence already accounted
for by the A-cycle.

If no collision occurs before returning to the start, the remaining object is:

```text
a clean cyclic necklace of lifted beta-anchor pairs
over the A-layer row-b cycle.
```

## Boundary Statement

The R-b5 start-return obstruction is exactly:

```text
minimal row-b A-cycle
plus
clean cyclic necklace of lifted pairs
  H_i -> next A,
  Beta_i -> b
with no pair collision, no watched hit, and no independent full interval
repeat before the cycle closes.
```

This is now the next narrow residual inside E11.

It should be attacked with the beta-layer reductions already proved:

```text
beta_layer_reduction_lemma.md
deep_beta_x_hit_reduction_lemma.md
clean_external_bridge_tenth_stage_reduction_lemma.md
```

because each `Beta_i -> b` is exactly the beta anchor that previously forced
the W/X/Z reductions.


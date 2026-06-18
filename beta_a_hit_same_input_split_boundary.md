# Beta-A Hit Same-Input Split Boundary

Date: 2026-06-18.

Status:

```text
boundary correction / not a common-edge fan
```

## Purpose

This separates the beta-layer hit:

```text
Beta_i=A_j
```

from the shared-edge/common-fan cases.  It looks like a collision, but it is
not a common-edge fan because the two outputs are different.

Reference:

```text
beta_layer_first_hit_boundary.md
```

## Setup

Use:

```text
x_i*Beta_i=A_i,
x_i*A_i=b,
x_j*A_j=b,
x_j*b=x_{j+1}.
```

Assume:

```text
Beta_i=A_j.
```

Then:

```text
x_i*A_j=A_i,
x_j*A_j=b.
```

## Statement

Rows `x_i` and `x_j` share the same input:

```text
A_j.
```

But their outputs are:

```text
A_i and b.
```

In the clean residual:

```text
A_i!=b.
```

Therefore this is not a common-edge fan.  It is a same-input split across two
different targets:

```text
row x_i: A_j -> A_i
row x_j: A_j -> b
```

## Consequence

The `Beta_i=A_j` branch should not be routed through:

```text
common_edge_fan_lemma.md
shared_edge_divergence_lemma.md
```

unless an additional equality later makes the outputs coincide.

The correct next treatment is target-relative:

```text
target A_i for row x_i,
target b   for row x_j.
```

It is a two-target split boundary, parallel in spirit to the X-layer
target-bridge case:

```text
row_b_x_layer_hit_target_bridge_boundary.md
```

but with source rows `x_i,x_j` and shared input `A_j`.


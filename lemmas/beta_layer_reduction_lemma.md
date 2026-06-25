# Beta-Layer Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / beta-layer routed to exact residuals
```

## Purpose

This packages the beta-layer work for the independent row-`b` cycle boundary.

It starts from the generated-input cross-source pressure:

```text
H_i versus Beta_i.
```

and reduces the first beta-layer hit to exact roles.

## Setup

Use:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i),
Beta_i=pred_{x_i}(A_i).
```

Then:

```text
b*H_i=A_i,
x_i*Beta_i=A_i,
x_i*A_i=b,
x_i*b=x_{i+1}.
```

At pivot `A_i`, the cross-source predecessor pressure gives:

```text
A_i*((b*A_i)*b)=H_i,
A_i*(b*x_i)=Beta_i.
```

Reference:

```text
generated_input_cross_source_pressure_lemma.md
```

## Reduction

The first beta-layer hit is one of the following.

### 1. `Beta_i=H_i`

This is routed to shared-edge divergence:

```text
rows b and x_i share H_i -> A_i.
```

Then:

```text
(b*A_i)*b=b*x_i
```

and the rows split at `A_i`.

Reference:

```text
beta_equals_h_shared_edge_divergence_lemma.md
```

### 2. `Beta_i=A_j`

This is not a common-edge fan.  It is a same-input split:

```text
row x_i: A_j -> A_i
row x_j: A_j -> b.
```

Reference:

```text
beta_a_hit_same_input_split_boundary.md
same_input_split_target_lift_lemma.md
```

The target-lift form is sharper.  Define:

```text
E_{i,j}=A_j*(A_i*x_i).
```

Then in `H_{A_j}`:

```text
E_{i,j} -> A_i,
Beta_j  -> b.
```

So this branch is beta-coupled at index `j`; it is no longer an opaque
same-input residual.

### 3. `Beta_i=x_j`

This is a target-bridge boundary:

```text
x_i*x_j=A_i,
x_i*A_i=b.
```

After swapping target `A_i -> x_j`, row `x_i` gives:

```text
delta -> A_i
```

in `H_{x_j}`, where:

```text
delta=x_j*(A_i*x_i).
```

Reference:

```text
beta_x_hit_target_bridge_boundary.md
beta_x_bridge_pair_reversible_square_lemma.md
```

The fresh target-bridge part is actually a reversible two-target square:

```text
(A_i, x_j, b)      <-> (x_j, delta, A_i),
(b, A_j, x_{j+1}) <-> (A_j, Beta_j, b).
```

So `Beta_i=x_j` is controlled by hits of `delta` or `Beta_j`, or by this
fresh reversible-square residual.

### 4. Visible hit

If `Beta_i` lies in the visible crossed-fan/core footprint, then the
independent row-`b` cycle boundary attaches back to the visible skeleton.

### 5. Fresh beta

If `Beta_i` is fresh relative to:

```text
visible footprint,
generated A-layer,
generated X-layer,
and generated H-layer,
```

then a new predecessor layer begins in row `x_i`:

```text
pred_{x_i}(Beta_i).
```

This is a genuine remaining fresh-layer boundary.  It should not be folded
back into the row-`b` tower without an additional hit.

## Consequence

The independent row-`b` cycle boundary F/H is no longer just:

```text
row-b cycles on A_i.
```

Every generated input `A_i` also forces the beta-layer split above.  The
remaining unclassified part is:

```text
fresh beta-layer extension in rows x_i,
beta-coupled same-target pairs from Beta_i=A_j,
plus reversible-square residuals from Beta_i=x_j.
```

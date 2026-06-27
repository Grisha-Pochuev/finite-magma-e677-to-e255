# Beta-Layer First-Hit Boundary

Date: 2026-06-18.

Status:

```text
boundary / second predecessor layer after generated-input pressure
```

## Purpose

After the generated-input cross-source pressure lemma, every generated input
`A_i` has a second predecessor label:

```text
Beta_i=pred_{x_i}(A_i).
```

This file records the first-hit split for the `Beta_i` layer.

References:

```text
generated_input_cross_source_pressure_lemma.md
row_b_a_layer_cycle_boundary.md
```

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
x_i*Beta_i=A_i,
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

So row `x_i` contains the chain:

```text
Beta_i -> A_i -> b -> x_{i+1}.
```

The row `A_i` pressure pair is:

```text
A_i*((b*A_i)*b)=H_i,
A_i*(b*x_i)=Beta_i.
```

## First-Hit Split

Let the watched set be:

```text
W = visible footprint ∪ {A_j} ∪ {x_j} ∪ {H_j}.
```

The first nonfresh event for `Beta_i` is one of:

### 1. `Beta_i=H_i`

Then the two outputs in the row-`A_i` pressure pair coincide.  By injectivity
of row `A_i`:

```text
(b*A_i)*b = b*x_i.
```

This is an explicit column coupling between the row-`b` cycle through `A_i`
and the right-`b` orbit label `x_i`.

### 2. `Beta_i=A_j`

Then row `x_i` maps a generated `A` input to another generated `A` input:

```text
x_i*A_j=A_i.
```

This is an A-layer hit, but now in row `x_i`, not row `b`.

It creates a three-step row-`x_i` chain:

```text
A_j -> A_i -> b -> x_{i+1}.
```

### 3. `Beta_i=x_j`

Then row `x_i` maps an orbit/source label to a generated input:

```text
x_i*x_j=A_i.
```

This is an X-layer hit for the source row `x_i`.

### 4. `Beta_i` Visible

If `Beta_i` lies in the visible crossed-fan/core footprint, then the
generated-input pressure attaches the clean residual back to the visible
skeleton.

### 5. `Beta_i` Fresh

If none of the above happens, then the row-`x_i` predecessor chain extends
one step backward:

```text
pred_{x_i}(Beta_i).
```

This is a new layer and should not be silently identified with the row-`b`
tower.

## Consequence

The independent row-`b` cycle boundary is now sharpened:

```text
row-b cycle on A_i
```

is accompanied at every `A_i` by:

```text
row x_i chain Beta_i -> A_i -> b -> x_{i+1}
```

and by the row-`A_i` pressure pair:

```text
H_i versus Beta_i.
```

The next substantial target is to route the column-coupling case:

```text
Beta_i=H_i
<=> (b*A_i)*b = b*x_i.
```

If that coupling can be shown to force a visible hit or target-swap relay,
then the independent row-`b` cycle residual becomes much tighter.

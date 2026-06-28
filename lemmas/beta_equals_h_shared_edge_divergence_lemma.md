# Beta-Equals-H Shared-Edge Divergence Lemma

Date: 2026-06-18.

Status:

```text
general proved / routes the Beta_i=H_i coupling case
```

## Purpose

The equality:

```text
Beta_i=H_i
```

from the beta-layer first-hit boundary is not an isolated coincidence.  It is
exactly a shared-edge divergence between rows `b` and `x_i`.

References:

```text
beta_layer_first_hit_boundary.md
shared_edge_divergence_lemma.md
```

## Setup

Use:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i),
Beta_i=pred_{x_i}(A_i).
```

Thus:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i,
x_i*Beta_i=A_i.
```

Assume:

```text
Beta_i=H_i.
```

Then:

```text
x_i*H_i=A_i,
b*H_i=A_i.
```

So rows `b` and `x_i` share the directed edge:

```text
H_i -> A_i.
```

The rows are distinct because badness gives:

```text
x_i!=b.
```

## Divergence

Apply the shared-edge divergence lemma to the common edge:

```text
row b:   H_i -> A_i
row x_i: H_i -> A_i.
```

The next outputs at `A_i` are:

```text
D_i=b*A_i,
x_i*A_i=b.
```

Therefore:

```text
D_i!=b.
```

The common return hub is:

```text
D_i*b = b*x_i.
```

And row `A_i` sends this hub back to the shared input:

```text
A_i*(D_i*b)=H_i.
```

Equivalently:

```text
A_i*(b*x_i)=H_i.
```

## Relation To The Earlier Column Coupling

The beta-layer first-hit boundary gave:

```text
Beta_i=H_i
<=>
(b*A_i)*b = b*x_i.
```

With:

```text
D_i=b*A_i,
```

this is:

```text
D_i*b=b*x_i.
```

So the column coupling is exactly the shared-edge return coupling.

## Consequence

The `Beta_i=H_i` branch is routed to a standard common-edge fan:

```text
rows b and x_i share H_i -> A_i,
then split at A_i into D_i and b,
with common hub b*x_i.
```

This does not yet contradict badness of `b`, because:

```text
D_i!=b
```

only says row `b` does not return to `b` at `A_i` in this branch.

But it is no longer an anonymous fresh equality.  It is a generated common-edge
fan attached to the clean matching residual.

The next route should treat this as an ordinary fan/relay event unless the
new tip `D_i=b*A_i` remains entirely outside the visible footprint.

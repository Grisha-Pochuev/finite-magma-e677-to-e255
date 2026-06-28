# Bad-Target Right-b Orbit Predecessor Recursion Lemma

Date: 2026-06-18.

Status:

```text
general proved
```

## Setup

Fix a bad target `b`.  Start with any element `x_0` and define its right-`b`
orbit:

```text
x_{i+1}=x_i*b.
```

For each `i`, define the bridge input:

```text
A_i=pred_{x_i}(b),
```

so:

```text
x_i*A_i=b.
```

Then row `x_i` carries the self-labeled `H_b` edge:

```text
A_i -> x_{i+1}.
```

Define:

```text
H_i=x_{i+1}*x_i.
```

## Statement

For every `i`:

```text
H_i=pred_b(A_i),
b*H_i=A_i.
```

Thus the right-`b` orbit of any starting label produces a row-`b`
predecessor chain:

```text
H_i -> A_i
```

where each arrow is in row `b`.

The full self-labeled edge certificate is:

```text
row x_i:
  beta_i -> A_i -> b -> x_{i+1}

row x_{i+1}:
  x_i -> H_i
  A_{i+1} -> b

row b:
  H_i -> A_i.
```

In particular:

```text
A_{i+1}=(x_i*x_{i+1})*x_i.
```

## Proof

The row `x_i` has:

```text
x_i*A_i=b,
x_i*b=x_{i+1}.
```

Apply:

```text
bad_target_self_labeled_edge_recursion_lemma.md
```

with `x=x_i`, `A=A_i`, and `Y=x_{i+1}`.

It gives:

```text
x_{i+1}*x_i=pred_b(A_i),
b*(x_{i+1}*x_i)=A_i,
(x_i*x_{i+1})*x_i=pred_{x_{i+1}}(b)=A_{i+1}.
```

These are exactly the displayed formulas.

## Bad-Target Restrictions

For every `i`:

```text
x_i!=b,
x_{i+1}!=b,
A_i!=b,
x_{i+1}!=pred_b(x_i).
```

If `x_0!=b`, then `x_i!=b` for all `i`: otherwise the first index with
`x_i=b` would satisfy `x_{i-1}*b=b`, contradicting badness.  Then
`x_{i+1}!=b` follows directly from badness.  Also `A_i!=b`, because
`x_i*A_i=b` with `A_i=b` would give `x_i*b=b`.  Finally,
`x_{i+1}!=pred_b(x_i)` is:

```text
bad_target_no_predecessor_output_lemma.md
```

applied to `x_i`.

## Use In The Clean External-Bridge Residual

The row-a bridge chain is the instance:

```text
x_0=a,
x_1=t=a*b,
A_0=k=pred_a(b),
H_0=ell=t*a=pred_b(k).
```

The canonical successor after the fresh second bridge `ell` is therefore:

```text
x_1=t.
```

It produces:

```text
A_1=pred_t(b)=(a*t)*a,
H_1=(t*b)*t=pred_b(A_1),
b*H_1=A_1.
```

So the missing successor label in the predecessor-chain candidate is not
arbitrary: it is the next point of the right-`b` orbit.

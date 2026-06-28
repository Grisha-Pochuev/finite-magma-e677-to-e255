# Bad-Target Self-Labeled Edge Recursion Lemma

Date: 2026-06-18.

Status:

```text
general proved
```

## Setup

Fix a bad target `b`.  For any row label `x`, define:

```text
A=pred_x(b),   so x*A=b,
Y=x*b.
```

In the graph `H_b`, row `x` carries the self-labeled edge:

```text
A -> Y.
```

## Statement

This edge has the full certificate:

```text
row x:
  beta -> A -> b -> Y

row Y:
  x -> H
  W -> b

row b:
  H -> A,
```

where:

```text
H=Y*x=pred_b(A),
U=x*Y,
W=U*x=(x*Y)*x=A_b(Y),
beta=A*(b*x).
```

Thus every self-labeled edge recursively produces:

```text
b*(Y*x)=A,
Y*((x*Y)*x)=b.
```

Equivalently:

```text
Y*x=pred_b(pred_x(b)),
(x*Y)*x=pred_Y(b).
```

## Bad-Target Restrictions

Since `b` is bad:

```text
Y=x*b != b.
```

Also:

```text
A!=b.
```

because if `A=b`, then `x*b=b`.

Finally, by:

```text
bad_target_no_predecessor_output_lemma.md
```

we also have:

```text
Y != pred_b(x).
```

## Proof

The first line:

```text
x*A=b,
x*b=Y
```

is exactly an `H_b` edge with source row `x`, input `A`, and output `Y`.

Apply the double-interval edge certificate to:

```text
q=x,
a=A,
c=Y.
```

The certificate gives:

```text
Y*x=pred_b(A),
Y*((x*Y)*x)=b,
x*(A*(b*x))=A.
```

This is precisely the displayed recursion.

The bad-target restrictions are immediate from badness and the
no-predecessor-output lemma.

## Use

The row-a bridge edge in a proper crossed fan is the instance:

```text
x=a,
A=k=pred_a(b),
Y=t=a*b.
```

The clean external-bridge residual should therefore be viewed as one step of
this self-labeled edge recursion attached to the crossed-fan skeleton.

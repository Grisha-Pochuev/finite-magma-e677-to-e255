# Shared-Step Anchored Triangle Boundary

Date: 2026-06-21.

Status:

```text
boundary / anchored triangle around a shared target-advance step
```

## Purpose

This records the shared-step anchored triangle suggested after:

```text
two_row_target_advance_window_separation_lemma.md
general_v3_bridge_descent_boundary.md
```

It may replace both current final branches if the strong same-output identity
is proved.

## Setup

Let two distinct rows share one target-advance step:

```text
p*b=z,
q*b=z,
p!=q.
```

Define:

```text
U=p*z,
W=q*z.
```

By the first-merge certificate separation package:

```text
first_merge_certificate_separation_lemma.md
```

the common terminal bridge is:

```text
h=U*p=W*q=pred_z(b),
z*h=b.
```

Let:

```text
alpha=pred_z(h),
```

so:

```text
z*alpha=h.
```

## Anchored Triangle In `H_h`

In the target graph `H_h`, three rows give:

```text
row U:  p     -> U*h,
row W:  q     -> W*h,
row z:  alpha -> b.
```

Indeed:

```text
U*p=h,      U*h=U*h,
W*q=h,      W*h=W*h,
z*alpha=h,  z*h=b.
```

This is a three-edge configuration anchored at the old target `b` through the
row `z` edge:

```text
alpha -> b.
```

## Strong Hypothesis

The strong identity is:

```text
U*h=W*h.
```

If true, then in `H_h` the first two anchored-triangle edges form an incoming
fan:

```text
p -> T,
q -> T,
T=U*h=W*h.
```

Since `p!=q`, this immediately routes the shared-step residual to an ordinary
fan/relay object.  In particular, it removes:

```text
1. the clean first-extra V3 bridge branch;
2. the clean orbit-theta branch.
```

They would no longer need separate treatment.

## Algebraic Proof Target

In bare term notation the desired quasi-identity is:

```text
Assume:
  p*b = q*b = z,
  U = p*z,
  W = q*z,
  h = U*p = W*q.

Prove:
  U*h = W*h.
```

Eliminating the abbreviations, this is:

```text
p*b=q*b
and
(p*(p*b))*p = (q*(p*b))*q

=> (p*(p*b))*((p*(p*b))*p)
 = (q*(p*b))*((p*(p*b))*p).
```

The second assumption is not an extra empirical fact in the relay setting:
it is the first-merge certificate equality:

```text
h=U*p=W*q=pred_z(b).
```

So the real proof target is to derive the final equality from E677 plus the
shared-step certificate structure, not from M496.

## If The Strong Hypothesis Fails

If:

```text
U*h!=W*h,
```

then classify the three `H_h` edges:

```text
p     -> U*h,
q     -> W*h,
alpha -> b.
```

The local collision roles are the same as for X3/Y3:

```text
same input,
same output,
full interval collision,
input-output cross hit,
watched/core hit.
```

If all local hits are absent, target advance gives a three-target same-input
bridge at the common input `h`:

```text
H_{U*h}:  h -> U*(U*h),
H_{W*h}:  h -> W*(W*h),
H_b:      h -> z*b.
```

One of the three targets is the old target `b`.

## Relation To X3 -> Y3 -> Z3

This is an X3-like object, but it is not literally the old generated-input X3
residual.

The old route:

```text
x3_three_edge_matching_advance_boundary.md
x3_advanced_edge_triangle_pressure_lemma.md
clean_external_bridge_seventh_stage_reduction_lemma.md
```

uses the special generated input:

```text
A_j
```

and the generated row pair:

```text
row x_j: A_j -> b,
row b:   A_j -> D_j=b*A_j.
```

The anchored triangle has common target `h` and rows:

```text
U, W, z.
```

So the general triangle-pressure mechanism applies, but the later generated
row-b bridge parts of X3/Y3/Z3 cannot be reused as a black box without an
extra translation.

## Current Boundary

The next proof target is:

```text
prove U*h=W*h from E677 and shared-step data,
or build a general anchored-X3 route for the clean case where U*h!=W*h.
```

The M496 diagnostic for the strong identity is recorded in:

```text
m496_shared_step_anchored_triangle_diagnostic.md
```

A targeted raw-label diagnostic for the negation is recorded in:

```text
anchored_identity_negation_raw_diagnostic.md
```

A partial algebraic reduction of the negation is recorded in:

```text
anchored_identity_partial_reduction.md
```

It shows that if `T=U*h` and `S=W*h`, then:

```text
h*(T*U)=p,
h*(S*W)=q,
(h*(T*U))*b=(h*(S*W))*b=z.
```

So the negated branch is an anchored back-projection through the single row
`h`, not just an unstructured failure of the incoming fan.

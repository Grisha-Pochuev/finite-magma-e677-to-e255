# Anchored-X3 Three-Target Bridge Boundary

Date: 2026-06-21.

Status:

```text
boundary / exact false-branch route for shared-step anchored identity
```

## Setup

Start with the shared-step anchored triangle:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
alpha=pred_z(h).
```

Thus:

```text
z*alpha=h.
```

Define:

```text
T=U*h,
S=W*h.
```

In `H_h` the three anchored edges are:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

## Strong Branch

If:

```text
T=S,
```

then the first two edges give an incoming fan in `H_h`:

```text
p -> T,
q -> T.
```

This is the desired strong route from:

```text
shared_step_anchored_triangle_boundary.md
```

## False Branch

Assume:

```text
T!=S.
```

Then the first two edges are not an incoming fan.  Compare all endpoints of:

```text
p     -> T,
q     -> S,
alpha -> b.
```

Any same input, same output, full ported interval, input-output cross hit, or
watched/core hit is routed by the same local roles used for same-target pairs:

```text
same_target_pair_collision_trichotomy_lemma.md
```

The only clean false branch is therefore:

```text
p,q,alpha,T,S,b are locally disjoint,
T!=S,
and no input-output cross hit occurs among the three edges.
```

## Target Advance Of The Clean False Branch

Target-advance each `H_h` edge.

For row `U`:

```text
U*p=h,
U*h=T,
```

so in `H_T`:

```text
h -> U*T.
```

For row `W`:

```text
W*q=h,
W*h=S,
```

so in `H_S`:

```text
h -> W*S.
```

For row `z`:

```text
z*alpha=h,
z*h=b,
```

so in `H_b`:

```text
h -> z*b.
```

Therefore the clean false branch gives a three-target same-input bridge:

```text
H_T: h -> U*T,
H_S: h -> W*S,
H_b: h -> z*b.
```

One of the three targets is the old target `b`, and the common input is the
anchor `h`.

## Relation To The Back-Projection Reduction

The partial reduction:

```text
anchored_identity_partial_reduction.md
```

adds:

```text
h*(T*U)=p,
h*(S*W)=q,
(h*(T*U))*b=(h*(S*W))*b=z.
```

So the clean false branch has two simultaneous descriptions:

```text
1. an anchored three-target same-input bridge at h;
2. a back-projected shared step through row h.
```

This is stronger and more specific than the old generic X3 residual.

## Current Boundary

The old X3 route cannot be reused verbatim, because the old generated input
was `A_j` and included the special row-`b`/generated-row pair.  Here the
common input is the anchor `h`, and the rows are:

```text
U, W, z.
```

The next exact target is:

```text
prove T=S,
or show that the clean anchored-X3 bridge at h is a smaller measured relay
object than the original shared-step residual.
```

If neither can be proved directly, this file is the residual to attack next.

The next pressure layer is recorded in:

```text
anchored_x3_second_triangle_pressure_lemma.md
```

It shows that the clean false branch also forces a second triangle layer in
`H_h` carried by rows `T,S,b`, so the residual is coupled back to the old row
`b` and is not a free fresh X3 layer.

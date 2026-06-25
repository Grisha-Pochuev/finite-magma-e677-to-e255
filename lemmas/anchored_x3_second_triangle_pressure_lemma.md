# Anchored-X3 Second Triangle Pressure Lemma

Date: 2026-06-21.

Status:

```text
proved pressure expansion / second triangle layer for anchored-X3
```

## Purpose

This sharpens the clean false branch from:

```text
anchored_x3_three_target_bridge_boundary.md
```

The clean false branch is not just a three-target same-input bridge after
target advance.  The three original `H_h` edges also force a second triangle
layer back into the same target `h`.

This is the anchored analogue of:

```text
x3_advanced_edge_triangle_pressure_lemma.md
```

but with anchor `h` instead of generated input `A_j`.

## Setup

Use:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
alpha=pred_z(h),
T=U*h,
S=W*h.
```

The anchored `H_h` matching is:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

Assume the clean false branch:

```text
T!=S
```

and no local fan/path/full-interval/core hit among these three edges.

## First Predecessor Formulas

For any E677 edge:

```text
row r: P -> O in H_H
```

meaning:

```text
r*P=H,
r*H=O,
```

the standard predecessor formula gives:

```text
P=H*(O*r).
```

Apply this to the three anchored edges:

```text
p     = h*(T*U),
q     = h*(S*W),
alpha = h*(b*z).
```

The first two formulas are already recorded in:

```text
anchored_identity_partial_reduction.md
```

The third formula is the same row-`z` version.

## Second Triangle Formulas

Use the finite E677 consequence:

```text
if a=r*H and A=r*a, then a*(A*r)=H.
```

For row `U`:

```text
U*h=T,
U*T=advanced output,
therefore T*((U*T)*U)=h.
```

For row `W`:

```text
W*h=S,
W*S=advanced output,
therefore S*((W*S)*W)=h.
```

For row `z`:

```text
z*h=b,
z*b=advanced output,
therefore b*((z*b)*z)=h.
```

Thus the second triangle layer gives three more incoming-to-`h` rows:

```text
row T: (U*T)*U -> T*h,
row S: (W*S)*W -> S*h,
row b: (z*b)*z -> b*h
```

inside the same target graph `H_h`.

## Consequence

The clean anchored-X3 false branch now carries two coupled layers in `H_h`.

Original layer:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

Second triangle layer:

```text
row T: (U*T)*U -> T*h,
row S: (W*S)*W -> S*h,
row b: (z*b)*z -> b*h.
```

Any same input, same output, full ported interval, input-output cross hit, or
watched/core hit between these layers routes by the usual fan/path/collision
roles.

The remaining clean residual is therefore not just:

```text
H_T: h -> U*T,
H_S: h -> W*S,
H_b: h -> z*b.
```

It is a coupled anchored-X3 object:

```text
1. a clean three-edge matching in H_h carried by U,W,z;
2. its clean three-target same-input bridge at h;
3. a second clean triangle layer in H_h carried by T,S,b.
```

The row `b` in the second layer is important: it couples the anchored residual
back to the old target row instead of letting it become a free fresh X3 layer.

## Current Boundary

The next exact target is:

```text
prove that the second layer must hit the original anchored layer, the old
visible/core footprint, or an independent full ported interval;
otherwise define a measured anchored-X3 rank and show it descends.
```

Do not replace this by the old generated-input X3 route without checking the
missing generated-input assumptions.  The shared structure here is the anchor
`h` and the old row `b`, not a generated input `A_j`.

The fixed-target source-orbit form is recorded in:

```text
anchored_x3_source_orbit_boundary.md
```

It identifies the second triangle layer as the first source-successor layer in
`H_h`:

```text
U -> T,
W -> S,
z -> b.
```

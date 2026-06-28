# Period-3 Zipper Triangle Self-Renewal Lemma

Date: 2026-06-27.

Status:

```text
proved clarification / period-3 triangle pressure shifts the same zipper
```

## Purpose

This records what happens if the clean fixed-target zipper residual has the
short period-3 form isolated in:

```text
fixed_target_period3_zipper_boundary.md
```

The target-advanced triangle looks like the older advanced X3 object, but its
next triangle-pressure layer is not fresh.  It is exactly the same zipper
triangle shifted by one step.

## Generic Setup

Fix a target:

```text
t.
```

Assume a right-`t` period-3 source cycle:

```text
r0*t=r1,
r1*t=r2,
r2*t=r0.
```

For each row define the `H_t` predecessor input:

```text
I0=pred_{r0}(t),
I1=pred_{r1}(t),
I2=pred_{r2}(t).
```

The zipper edges in `H_t` are:

```text
I0 -> r1     carried by row r0,
I1 -> r2     carried by row r1,
I2 -> r0     carried by row r2.
```

Target advance gives the clean three-target same-input triangle:

```text
H_{r1}: t -> r0*r1,
H_{r2}: t -> r1*r2,
H_{r0}: t -> r2*r0.
```

## Triangle-Pressure Layer

Apply the standard V3/X3 second-layer expansion to each adjacent advanced
edge.  For the edge:

```text
r0*t=r1,
H_{r1}: t -> r0*r1,
```

the second-layer edge is:

```text
(r0*r1)*r0 -> r1*t
```

inside `H_t`, carried by row `r1`.

Since:

```text
r1*t=r2
```

and the fixed-target zipper formula gives:

```text
I1=(r0*r1)*r0,
```

this second-layer edge is exactly:

```text
I1 -> r2.
```

That is the next zipper edge already present in the period-3 triangle.

The same computation cyclically gives:

```text
(r1*r2)*r1 = I2,     I2 -> r0,
(r2*r0)*r2 = I0,     I0 -> r1.
```

## Consequence

The period-3 target-advanced triangle is self-renewing:

```text
advanced three-target triangle
-> triangle-pressure second layer
-> the same H_t zipper triangle shifted cyclically.
```

So this residual cannot be closed merely by applying the old X3
triangle-pressure step once more.  That step produces no new independent
four-edge matching and no new source layer; it returns to the same closed
period-3 zipper.

## Anchored Specialization

For the anchored-M7 period-3 residual:

```text
z*h=b,
b*h=c,
c*h=z,
```

the target-advanced triangle is:

```text
H_b: h -> z*b,
H_c: h -> b*c,
H_z: h -> c*z.
```

Its triangle-pressure layer in `H_h` is exactly:

```text
I_b -> c,
I_c -> z,
alpha -> b,
```

the same zipper triangle:

```text
alpha -> b,
I_b   -> c,
I_c   -> z.
```

Thus the exact remaining period-3 obstruction is:

```text
a clean self-renewing three-target same-input triangle coupled to its own
clean H_h zipper triangle.
```

It must be closed by a global measure/admissibility argument, by a watched/core
hit, or by showing that this self-renewing period-3 triangle is impossible in
the minimal G12 loop.

# Fixed-Target Period-3 Zipper Boundary

Date: 2026-06-26.

Status:

```text
db-supported boundary / short clean zipper obstruction shape
```

## Purpose

This records the extra information gained from the external `eq677` db scan:
the clean fixed-target self-repeat residuals visible in the public models are
not long arbitrary cycles.  They are first returns to the initial source at
depth 3.

This is evidence and a sharper target, not yet a general proof.

## Generic Period-3 Form

Fix a target:

```text
t.
```

A depth-3 first return in one right-`t` source orbit has:

```text
r_0*t=r_1,
r_1*t=r_2,
r_2*t=r_0.
```

For each source row define the `H_t` input:

```text
I_i=pred_{r_i}(t).
```

The zipper formula from:

```text
fixed_target_zipper_bridge_necklace_lemma.md
```

specializes to:

```text
I_0=t*(r_1*r_0)=(r_2*r_0)*r_2,
I_1=t*(r_2*r_1)=(r_0*r_1)*r_0,
I_2=t*(r_0*r_2)=(r_1*r_2)*r_1.
```

The corresponding `H_t` zipper triangle is:

```text
I_0 -> r_1,
I_1 -> r_2,
I_2 -> r_0.
```

Target advance gives the same-input three-target triangle:

```text
H_{r_0}: t -> r_2*r_0,
H_{r_1}: t -> r_0*r_1,
H_{r_2}: t -> r_1*r_2.
```

So a period-3 zipper is stronger than an isolated adjacent V3 bridge: it gives
three adjacent V3 bridges around a closed triangle.

## Anchored-X3 Specialization

In the anchored-X3 false branch:

```text
z*h=b.
```

The period-3 `z`-orbit case is:

```text
z*h=b,
b*h=c,
c*h=z,
where c=b*h.
```

The `H_h` zipper inputs are:

```text
alpha = h*(b*z) = (c*z)*c,
I_b   = h*(c*b) = (z*b)*z,
I_c   = h*(z*c) = (b*c)*b.
```

and the `H_h` zipper triangle is:

```text
alpha -> b,
I_b   -> c,
I_c   -> z.
```

Target advance gives:

```text
H_z: h -> c*z,
H_b: h -> z*b,
H_c: h -> b*c.
```

This is the short triangular form of the clean M7 zipper residual.

The triangle-pressure layer of this target-advanced triangle is not fresh.  It
is the same zipper triangle shifted cyclically:

```text
period3_zipper_triangle_self_renewal_lemma.md
```

So applying the old X3 pressure step again does not by itself create a new
independent residual.

## Earliest V3 Bridge In The Triangle

In the anchored period-3 case the first pre-return adjacent V3 bridge is:

```text
H_b: h -> z*b,
H_c: h -> b*c.
```

It is born from the first two source-successor steps:

```text
z*h=b,
b*h=c.
```

Its target-lift in `H_h` is the first two zipper edges:

```text
alpha -> b,
I_b   -> c.
```

The zipper-born second-layer shift then adds:

```text
I_c -> z,
```

which is exactly the terminal period-3 return:

```text
c*h=z.
```

So in the period-3 residual the measure comparison can be stated more
concretely:

```text
terminal event:       c*h=z;
earlier V3 bridge:    H_b,H_c at common input h.
```

If this bridge is admissible under the unified clean V3 measure, the period-3
zipper cannot be terminal.

The exact rank comparison is recorded in:

```text
period3_zipper_exact_measure_reduction.md
```

There the terminal event is `c*h=z`, while the earlier bridge is the adjacent
window:

```text
H_b: h -> z*b,
H_c: h -> b*c.
```

## External db Signature

The scanner:

```text
tools/eq677_db_shared_step_scan.js --all --totals-only
```

found among the `17040` clean anchored-X3 false pairs:

```text
10800 routed first source-orbit event;
6240 clean same-orbit self-repeat;
0 no finite event.
```

The clean self-repeat signatures are:

```text
z:3->0:       4320
W:3->0|z:3->0: 1050
U:3->0|z:3->0:  870
```

Thus every clean db self-repeat includes the anchored period-3 `z`-orbit:

```text
z -> b -> b*h -> z.
```

Sometimes the `U` or `W` source orbit also returns at depth 3, but the common
feature is the `z`-orbit triangle.

The target-advanced period-3 triangle was also classified.  All `6240`
examples have:

```text
period3-advance-clean: 6240
```

Idempotence split:

```text
idempotent:      0
non-idempotent: 6240
```

All public-db period-3 examples occur in the four non-idempotent size-77
models:

```text
77/65, 77/71, 77/72, 77/73.
```

Thus this short clean zipper obstruction should not be dismissed as an
idempotent/M496 artifact.

Here "clean" means that in:

```text
H_z: h -> c*z,
H_b: h -> z*b,
H_c: h -> b*c,
```

the targets `z,b,c` are distinct, the outputs `c*z,z*b,b*c` are distinct,
no output is the common input `h`, and no output hits one of the targets
`z,b,c`.

## Proof Target

The next useful target is no longer a generic long-cycle statement.  First try
to close or route the period-3 zipper triangle:

```text
z*h=b,
b*h=c,
c*h=z,
alpha -> b,
I_b -> c,
I_c -> z
in H_h.
```

Possible exits:

```text
1. the three target-advanced edges at common input h form a three-target
   same-input bridge covered by V3 admissibility or a stronger three-target
   version of it;
2. one of c, I_b, I_c, c*z, z*b, b*c hits old/watched/core data;
3. the period-3 triangle forces a full ported interval repeat in an
   independent role;
4. if none route, this period-3 zipper triangle is the sharper final
   obstruction inside the fixed-target necklace.
```

Do not attack this residual by only reapplying the old X3 triangle-pressure
step.  In the period-3 case that step self-renews:

```text
advanced triangle -> same H_h zipper triangle shifted.
```

The bounded local closure check:

```text
period3_zipper_saturation_diagnostic.md
```

confirms the expected zipper formulas through depth 5, but does not derive a
short clean collision, displayed idempotence, or direct E255 for `z,b,c,h`.

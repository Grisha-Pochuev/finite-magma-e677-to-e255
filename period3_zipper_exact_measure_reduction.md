# Period-3 Zipper Exact Measure Reduction

Date: 2026-06-27.

Status:

```text
conditional reduction / period-3 residual reduced to one V3 admissibility gap
```

## Purpose

This specializes:

```text
fixed_target_zipper_reduces_to_v3_admissibility.md
```

to the short period-3 residual from:

```text
fixed_target_period3_zipper_boundary.md
period3_zipper_triangle_self_renewal_lemma.md
```

The point is to remove the last ambiguity in the measure comparison.  In the
period-3 case there is no long necklace and no choice of a distant bridge: the
earlier bridge is explicit.

## Period-3 Data

Use the anchored notation:

```text
z*h=b,
b*h=c,
c*h=z.
```

The terminal event of the clean right-`h` source orbit is:

```text
c*h=z.
```

The `H_h` zipper triangle is:

```text
alpha -> b,
Ib    -> c,
Ic    -> z.
```

Target advance gives the three-target same-input triangle:

```text
H_z: h -> c*z,
H_b: h -> z*b,
H_c: h -> b*c.
```

## Exact Earlier Bridge

The adjacent V3 bridge born before the terminal return is:

```text
H_b: h -> z*b,
H_c: h -> b*c.
```

It is born from the first two source-successor steps:

```text
z*h=b,
b*h=c.
```

Its target-lift is:

```text
alpha -> b,
Ib    -> c
```

inside `H_h`.

By the shifted-window lemma, its second layer is the terminal zipper edge:

```text
Ic -> z.
```

So the period-3 object is exactly:

```text
earlier clean V3 bridge
+
terminal shifted zipper edge.
```

## Rank Comparison

The terminal clean self-repeat has rank:

```text
M7 = 3
```

for the `z`-orbit:

```text
z -> b -> c -> z.
```

The bridge:

```text
H_b,H_c
```

is born strictly before the terminal return, at the adjacent window:

```text
z -> b -> c.
```

Thus its fixed-target zipper-born bridge rank is:

```text
MZ < M7.
```

Concretely, under zero-based source positions it is the adjacent window
starting at position `1`, while the return event is at position `3`.

## Conditional Closure

Assume the unified zipper-born V3 admissibility sentence:

```text
A clean zipper-born adjacent V3 bridge born before the terminal fixed-target
self-repeat is admissible as a smaller measured relay object, unless it has a
local routed hit, watched/core hit, or independent full-interval repetition.
```

Then the clean period-3 zipper cannot be terminal in a minimal G12 loop.

Proof:

```text
1. in the clean period-3 residual, the bridge H_b,H_c is locally clean;
2. it is born before the terminal return c*h=z;
3. by admissibility it is a smaller measured relay object;
4. this contradicts minimality of the terminal period-3 self-repeat.
```

## Exact Remaining Obstruction

If the above conditional closure cannot be used, the remaining obstruction is
not the broad fixed-target necklace anymore.  It is the specific object:

```text
a clean self-renewing period-3 zipper triangle whose earlier bridge H_b,H_c
is not admissible under the global V3/relay measure.
```

Equivalently, the missing hypothesis must explain why this shifted-window V3
bridge:

```text
H_b: h -> z*b,
H_c: h -> b*c
```

cannot be inserted into the same measured relay class as a first-extra V3
bridge.

This is now the narrowest period-3 form of the M7 admissibility gap.


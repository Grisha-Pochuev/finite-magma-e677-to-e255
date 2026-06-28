# Period-3 Row b/Ib c-Input V3 Lemma

Date: 2026-06-28.

Status:

```text
proved reduction / clean period-3 always exposes the b/Ib split at input c
```

## Purpose

The named fan route focuses on:

```text
Ib*h=c.
```

But the same named row `Ib` also gives a more immediate same-input test at
the period-3 vertex `c`.  In the clean residual, rows `b` and `Ib` either
route by an output merge, or form a standard V3 bridge at the common input:

```text
c.
```

## Setup

Use the clean period-3 zipper:

```text
z*h=b,
b*h=c,
c*h=z.
```

The `H_h` zipper triangle includes:

```text
b*Ib=h.
```

Define:

```text
BC=b*c,
A=Ib*c,
K=A*Ib=(Ib*c)*Ib,
L=c*K.
```

By E677 with `x=c,y=Ib`:

```text
c = Ib*(c*((Ib*c)*Ib)),
```

so:

```text
Ib*L=c.
```

Thus row `Ib` has predecessor `L` of target `c`.

## The H_c Lift

In target `H_c`, row `b` gives:

```text
row b: h -> BC,
```

because:

```text
b*h=c,
b*c=BC.
```

Row `Ib` gives:

```text
row Ib: L -> A,
```

because:

```text
Ib*L=c,
Ib*c=A.
```

So the common-input comparison at `c`:

```text
b*c=BC,
Ib*c=A
```

lifts to the same-target pair in `H_c`:

```text
h -> BC,
L -> A.
```

## Output-Equality Route

If:

```text
A=BC,
```

then the lifted `H_c` pair has a common output.

If also:

```text
L=h,
```

then rows `b` and `Ib` realize the same full ported interval:

```text
(c,h,BC),
```

so:

```text
Ib=b
```

by ported-interval reconstruction, a clean local collision.

If:

```text
L!=h,
```

then the two `H_c` edges have distinct inputs and the same output, an incoming
merge in `H_c`.  This is routed by the ordinary same-target collision roles.

Therefore the fully clean residual may assume:

```text
A!=BC.
```

## Clean V3

With:

```text
A!=BC,
```

rows `b` and `Ib` form a standard same-input V3 bridge:

```text
row b:  c -> BC,
row Ib: c -> A.
```

The common input is:

```text
c.
```

Its target-lift is exactly the `H_c` pair:

```text
row b:  h -> BC,
row Ib: L -> A.
```

## Relation To The Named Fan

The shifted input identity:

```text
K=(Ib*c)*Ib=Ic
```

is equivalent, after applying row `c`, to:

```text
L=h,
```

because:

```text
c*K=L,
c*Ic=h,
```

and row `c` is left-cancellative.

So:

```text
K=Ic
```

makes the target-lift of the `c`-input V3 an outgoing fan in `H_c`:

```text
h -> BC,
h -> A.
```

By:

```text
period3_shifted_hook_pair_implies_named_fan_lemma.md
period3_named_fan_reduces_to_Ibhc_lemma.md
```

this is exactly the named fan route.

If:

```text
K!=Ic,
```

then:

```text
L!=h,
```

and the same V3 has a clean-disjoint lift in `H_c`, as recorded in:

```text
period3_shifted_input_failure_v3_bridge_lemma.md
```

## Consequence

The clean period-3 residual now has an unconditional b/Ib V3 exposure:

```text
either A=BC routes,
or rows b and Ib form a same-input V3 bridge at c.
```

The named fan equality is the special case where the target-lift of this V3
has equal input `h` in `H_c`.

Thus period-3 should be treated as a concrete instance of the unified clean
V3 admissibility frontier, with an extra possible strengthening to a named
middle-target fan.

For the exact second-layer split of this V3, use:

```text
period3_c_input_v3_second_layer_boundary.md
```

It records that the db identity `Ib*c=z` is a watched output hit, while the
fully clean failure becomes a generic four-edge V3 matching in `H_c`.

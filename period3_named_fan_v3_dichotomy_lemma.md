# Period-3 Named Fan / V3 Dichotomy Lemma

Date: 2026-06-28.

Status:

```text
proved reduction / period-3 residual splits to named fan or standard V3
```

## Purpose

This packages the current period-3 progress into one reusable dichotomy.

It replaces the broad question:

```text
is the shifted-window bridge admissible?
```

by a sharper two-way split:

```text
1. a named outgoing fan appears in H_c;
2. or the negation is a standard clean same-input V3 bridge.
```

## Setup

Use the clean period-3 zipper:

```text
z*h=b,
b*h=c,
c*h=z.
```

The `H_h` zipper triangle is:

```text
alpha -> b      carried by row z,
Ib    -> c      carried by row b,
Ic    -> z      carried by row c.
```

The target-advanced triangle is:

```text
H_z: h -> c*z,
H_b: h -> z*b,
H_c: h -> b*c.
```

The public db suggests the named row `Ib` as the second row through `h` in
target `c`.  The proof split below does not assume the db identity; it only
splits on whether it holds.

## Case 1: Named Fan

If:

```text
Ib*h=c,
```

then row `Ib` also gives an edge of `H_c` at input `h`:

```text
row Ib: h -> Ib*c.
```

Row `b` already gives:

```text
row b: h -> b*c.
```

By:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
```

the outputs are distinct in the clean residual.  If they were equal, rows
`Ib` and `b` would realize the same full ported interval:

```text
(c,h,b*c),
```

forcing:

```text
Ib=b,
```

which is a routed input-output hit in the `H_h` zipper triangle.

Thus `Ib*h=c` gives a genuine outgoing fan in:

```text
H_c
```

at the input:

```text
h.
```

## Case 2: Named Fan Fails

If:

```text
D=Ib*h,
D!=c,
```

then rows `b` and `Ib` share the input `h` with distinct outputs:

```text
b*h=c,
Ib*h=D.
```

Therefore this is a same-input V3 bridge:

```text
p=b,
q=Ib,
common input h,
outputs c and D.
```

By:

```text
period3_named_fan_negation_is_v3_bridge_lemma.md
```

its target-lift in `H_h` is exactly:

```text
row b:  Ib -> c,
row Ib: P  -> D,
```

where:

```text
P=pred_{Ib}(h)=h*(D*Ib).
```

The first lifted edge is the existing period-3 zipper edge; the second is the
new input-source edge.  The V3 second layer starts the two right-`h` source
orbits:

```text
b  -> c -> z -> b -> ...
Ib -> D -> D*h -> ...
```

So named fan failure is not a new local obstruction.  It is a standard V3
fixed-target source-orbit residual with one branch already locked into the
period-3 cycle.

## First-Event Reduction

Using:

```text
period3_named_fan_negation_orbit_first_event_boundary.md
```

all first events between the fresh orbit:

```text
Ib -> D -> ...
```

and the watched period-3 orbit:

```text
z -> b -> c -> z
```

route by the standard fixed-target roles:

```text
source hit,
output merge,
input repeat,
input-output cross hit,
watched/core hit.
```

If no such event occurs before the fresh orbit self-repeats, the remaining
object is a clean same-orbit fixed-target self-repeat starting at:

```text
r_0=Ib,
t=h,
```

with the period-3 cycle retained as watched data.  The generic zipper/V3
necklace machinery then applies.

## Consequence

The clean period-3 residual is now reduced to:

```text
named H_c fan
or
standard clean same-input V3 bridge b/Ib at input h.
```

Thus the next global proof should not treat period-3 as a separate local
equality hunt.  The remaining work is one of:

```text
1. prove the named fan equality Ib*h=c in the minimal G12 setting;
2. prove the resulting V3 bridge is admissible as a smaller relay object;
3. prove the fresh Ib-orbit cannot self-repeat cleanly while avoiding the
   watched period-3 cycle.
```

The db evidence supports case 1, but the formal reduction is valid without
assuming it.

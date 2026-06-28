# Period-3 Named-Fan Negation Orbit First-Event Boundary

Date: 2026-06-28.

Status:

```text
boundary / named fan failure becomes a two-orbit fixed-target residual
```

## Purpose

This continues:

```text
period3_input_source_fan_boundary.md
```

The named middle-target fan would follow from:

```text
Ib*h=c.
```

This file records what remains if the named fan fails cleanly.

## Setup

Use the period-3 right-`h` source cycle:

```text
z*h=b,
b*h=c,
c*h=z.
```

Its `H_h` zipper triangle is:

```text
alpha -> b      carried by row z,
Ib    -> c      carried by row b,
Ic    -> z      carried by row c.
```

Assume the named fan fails:

```text
D=Ib*h,
D!=c.
```

Let:

```text
P=pred_{Ib}(h)=h*(D*Ib).
```

Then row `Ib` gives a fourth edge in `H_h`:

```text
P -> D.
```

If this fourth edge has a local hit with the zipper triangle, it routes as in:

```text
period3_input_source_fan_boundary.md
```

So the clean negation has:

```text
D fresh,
P fresh,
P -> D in H_h.
```

## Forced Source-Orbit

Apply:

```text
fixed_target_source_successor_lemma.md
```

to the row-`Ib` edge:

```text
Ib*P=h,
Ib*h=D.
```

Define:

```text
E=Ib*D,
J=E*Ib,
F=D*h.
```

Then row `D` gives the next edge in `H_h`:

```text
J -> F.
```

Thus the clean named-fan negation creates a new right-`h` source-successor
orbit:

```text
Ib -> D -> F -> ...
```

with attached `H_h` edges:

```text
P -> D,
J -> F,
...
```

This orbit must be compared with the period-3 orbit:

```text
z -> b -> c -> z.
```

## First-Event Routing

Take the first event between the fresh orbit and the period-3 cycle, and also
the first self-event inside the fresh orbit.

The following route by existing fixed-target machinery:

```text
1. source hit:
   some fresh source equals z,b,c
   -> source recurrence / watched-cycle hit;

2. output merge:
   some fresh output equals z,b,c
   -> incoming fan or full ported interval collision in H_h;

3. input repeat:
   a fresh H_h input equals alpha,Ib,Ic, or an earlier fresh input
   -> same-input collision in H_h;

4. input-output cross hit:
   a fresh input equals z,b,c or a fresh output,
   or a fresh output equals alpha,Ib,Ic or a fresh input
   -> directed path attachment in H_h;

5. watched/core hit:
   any fresh source/input/output hits the old visible or core footprint
   -> ordinary relay/core attachment.
```

These are the same roles used in:

```text
anchored_m7_first_event_routing_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
clean_v3_fixed_target_source_orbit_reduction.md
```

## Clean Residual

If none of the first events above occurs, the named-fan negation becomes:

```text
a clean fresh right-h source-successor orbit starting at Ib,
disjoint from the period-3 cycle z -> b -> c -> z,
until its first clean same-orbit self-repeat.
```

At that first self-repeat, the generic fixed-target zipper machinery applies:

```text
fixed_target_zipper_bridge_necklace_lemma.md
fixed_target_zipper_reduces_to_v3_admissibility.md
```

So the clean named-fan negation does not produce a new local equality target.
It reduces back to the fixed-target zipper/V3 necklace frontier, but now with
a concrete start row:

```text
r_0=Ib,
t=h,
```

and with the old period-3 cycle retained as watched data.

## Diagnostic

The script:

```text
tools/period3_zipper_saturation.js
```

was extended to check the first successor layer:

```text
D=Ib*h,
P=h*(D*Ib),
E=Ib*D,
J=E*Ib,
F=D*h.
```

Depth-4 local closure:

```text
D=Ib*h hits z/b/h: false
P hits alpha/Ib/Ic/z/b/c: false
F=D*h hits z/b/c/D: false
J=(Ib*D)*Ib hits alpha/Ib/Ic/P/z/b/c/D: false
```

Thus the clean two-orbit residual is locally consistent at this shallow
closure level.

## Next Use

The useful next proof step is not another product fingerprint.  It is:

```text
show that a fresh right-h orbit starting at Ib cannot remain clean-disjoint
from the watched period-3 cycle until self-repeat in a minimal G12 loop.
```

Equivalently, prove that its first event routes before a fresh self-repeat, or
that the resulting self-repeat is a smaller admissible fixed-target zipper.

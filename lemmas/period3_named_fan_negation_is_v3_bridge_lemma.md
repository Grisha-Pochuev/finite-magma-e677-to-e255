# Period-3 Named-Fan Negation Is A V3 Bridge

Date: 2026-06-28.

Status:

```text
proved reduction / Ib*h!=c is a standard clean same-input V3 bridge
```

## Purpose

This clarifies the role of the named fan negation from:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
period3_input_source_fan_boundary.md
period3_named_fan_negation_orbit_first_event_boundary.md
```

The negation:

```text
Ib*h!=c
```

does not create a new kind of local object.  It is exactly a same-input V3
bridge at the common input `h`.

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

Assume the named fan fails:

```text
D=Ib*h,
D!=c.
```

Let:

```text
P=pred_{Ib}(h)=h*(D*Ib).
```

Then row `Ib` gives:

```text
P -> D
```

in `H_h`.

## V3 Identification

Rows `b` and `Ib` share the input:

```text
h.
```

Their outputs are distinct:

```text
b*h=c,
Ib*h=D,
D!=c.
```

So this is a same-input V3 bridge with:

```text
p=b,
q=Ib,
z_common=h,
s=c,
r=D.
```

The standard target-lift in `H_h` gives:

```text
row b:  Ib -> c,
row Ib: P  -> D.
```

The first edge is already the middle edge of the period-3 zipper.  The second
edge is the new input-source edge from the named fan negation.

Thus:

```text
named fan negation
=
clean same-input V3 bridge at h between rows b and Ib,
```

unless a local hit routes earlier.

## Second Layer

Apply:

```text
clean_same_input_v3_second_layer_expansion_lemma.md
clean_v3_fixed_target_source_orbit_reduction.md
```

to the V3 bridge:

```text
b*h=c,
Ib*h=D.
```

The two right-`h` source-successor orbits are:

```text
b  -> c -> z -> b -> ...
Ib -> D -> D*h -> ...
```

The first orbit is the already watched period-3 cycle.  The second orbit is
the fresh orbit from:

```text
period3_named_fan_negation_orbit_first_event_boundary.md
```

The second-layer edges in `H_h` are:

```text
row c:  Ic -> z,
row D:  (Ib*D)*Ib -> D*h.
```

So the four-edge object is:

```text
Ib -> c,
P  -> D,
Ic -> z,
J  -> F,
```

where:

```text
J=(Ib*D)*Ib,
F=D*h.
```

## Consequence

The named fan negation does not need a separate new local case tree.

It is the already-known V3 fixed-target source-orbit residual, with extra
period-3 watched data:

```text
one branch is b -> c -> z -> b,
the other branch is Ib -> D -> ...
```

Therefore the next proof has exactly the usual V3 alternatives:

```text
1. a first source/output/input/cross hit routes;
2. a watched/core hit routes;
3. the fresh branch has a clean same-orbit self-repeat.
```

If case 3 occurs, the generic fixed-target zipper/V3 necklace machinery
applies, but now the watched period-3 cycle remains available as additional
data.

## Boundary

This lemma does not prove:

```text
Ib*h=c.
```

It proves that failure of `Ib*h=c` is not a new obstruction.  It is a
specific instance of the common V3 bridge frontier:

```text
clean_same_input_v3_admissibility_frontier.md
clean_v3_fixed_target_source_orbit_reduction.md
```

with one branch already locked into the period-3 zipper cycle.

## Diagnostic

The local saturation script:

```text
tools/period3_zipper_saturation.js
```

checks the named-fan negation terms:

```text
D=Ib*h,
P=h*(D*Ib),
E=Ib*D,
J=(Ib*D)*Ib,
F=D*h.
```

Depth-4 closure confirms that the visible target-advance output:

```text
H_D: h -> E=Ib*D
```

does not locally hit the existing target-advanced triangle:

```text
E=ZB: false,
E=BC: false,
E=CZ: false,
E in {z,b,c,h}: false.
```

It also confirms the first successor layer remains locally clean:

```text
D hits z/b/h: false,
P hits alpha/Ib/Ic/z/b/c: false,
F hits z/b/c/D: false,
J hits alpha/Ib/Ic/P/z/b/c/D: false.
```

So the V3 identification is not immediately routed by the current bounded
local closure.

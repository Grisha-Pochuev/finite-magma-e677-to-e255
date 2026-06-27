# Period-3 Input-Source Fan Boundary

Date: 2026-06-27.

Status:

```text
boundary / exact split for the remaining named fan equality Ib*h=c
```

## Purpose

The named middle-target fan has been reduced to one equality:

```text
Ib*h=c.
```

This file records the exact split if that equality is not yet known.

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

where:

```text
z*alpha=h,
b*Ib=h,
c*Ic=h.
```

Define the input-source successor:

```text
D=Ib*h.
```

## Fan Case

If:

```text
D=c,
```

then:

```text
Ib*h=c.
```

By:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
```

the middle target `H_c` has an outgoing fan at `h`:

```text
row b:  h -> b*c,
row Ib: h -> Ib*c,
```

with distinct outputs in the clean residual.

## Negation

Assume:

```text
D!=c.
```

Then row `Ib` gives a new edge in `H_h`.  Let:

```text
P=pred_{Ib}(h)=h*(D*Ib).
```

So:

```text
Ib*P=h,
Ib*h=D,
```

and in `H_h`:

```text
P -> D      carried by row Ib.
```

Thus the named fan negation is not blank.  It adds a fourth edge to the
period-3 zipper target graph:

```text
alpha -> b,
Ib    -> c,
Ic    -> z,
P     -> D.
```

## Local Routing Split

If the fourth edge has any of the ordinary local hits against the zipper
triangle, it is routed:

```text
P in {alpha,Ib,Ic},
D in {b,c,z},
P in {b,c,z},
D in {alpha,Ib,Ic},
P=D,
watched/core hit,
full ported interval repetition.
```

The important special cases are:

```text
D=c      -> named middle-target fan;
D=b or D=z -> output hit with the zipper triangle;
P=Ib     -> same input as the row-b zipper edge;
P=b      -> input-output path through alpha -> b;
P=c      -> input-output path through Ib -> c;
P=z      -> input-output path through Ic -> z.
```

## Clean Residual

If none of the hits occurs, the exact remaining object is:

```text
clean period-3 zipper triangle
+
one clean input-source edge P -> D in H_h carried by row Ib,
with D=Ib*h fresh and D!=c.
```

This is strictly narrower than the old shifted-window admissibility gap.  It
is the direct negation of the db-supported named fan row.

## Local Closure Diagnostic

The script:

```text
tools/period3_zipper_saturation.js
```

now prints the main local hit checks for:

```text
D=Ib*h,
P=h*(D*Ib).
```

Depth-4 run:

```text
tools\node-portable\node.exe tools\period3_zipper_saturation.js 4 12 250000
```

Result:

```text
Ib*h=c: false
D=Ib*h hits z: false
D=Ib*h hits b: false
D=Ib*h hits h: false
P=pred_Ib(h) hits alpha: false
P=pred_Ib(h) hits Ib: false
P=pred_Ib(h) hits Ic: false
P=pred_Ib(h) hits z: false
P=pred_Ib(h) hits b: false
P=pred_Ib(h) hits c: false
```

So the named fan negation does not locally route at this shallow closure
level.  If it is impossible, the proof needs a global/core/minimality
argument or a deeper structural comparison, not just a one-step equality.

## Next Use

The next theoretical step should attack this clean four-edge residual.  Two
natural routes:

```text
1. apply fixed-target source-successor to the new row Ib edge and compare the
   next row D against the period-3 zipper rows z,b,c;
2. target-advance the new edge to H_D: h -> Ib*D and compare it with the
   existing target-advanced triangle H_z,H_b,H_c.
```

If either comparison routes, then the named fan negation cannot remain clean.

## Forced Successor Layer

For the clean fourth edge:

```text
row Ib: P -> D in H_h,
P=h*(D*Ib),
D=Ib*h,
```

apply:

```text
fixed_target_source_successor_lemma.md
```

with target `h` and source row `Ib`.

Let:

```text
E=Ib*D.
```

Then row `D` gives the next edge in `H_h`:

```text
(E*Ib) -> D*h.
```

So the named fan negation starts a new right-`h` source-successor orbit:

```text
Ib -> D -> D*h -> ...
```

parallel to the period-3 orbit:

```text
z -> b -> c -> z.
```

Immediate routed hits:

```text
D in {z,b,c}              -> source hit / output hit;
D*h in {z,b,c,D}          -> output hit or short self-repeat;
E*Ib in {alpha,Ib,Ic,P}   -> input repeat in H_h;
E*Ib in {z,b,c,D}         -> input-output path hit.
```

Thus the next clean residual after named fan failure is:

```text
period-3 right-h source cycle
+
fresh right-h source orbit starting at Ib,
with no early source/output/input/cross hit.
```

This has the same shape as a fixed-target first-event problem, but it is now
anchored to the specific input row `Ib`, not to the original `U,W,z` anchored
triple.  The next useful check is whether the first event between:

```text
Ib -> D -> ...
```

and:

```text
z -> b -> c -> z
```

routes by the existing fixed-target first-event lemmas.

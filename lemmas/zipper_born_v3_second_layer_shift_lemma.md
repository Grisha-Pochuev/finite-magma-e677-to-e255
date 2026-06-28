# Zipper-Born V3 Second-Layer Shift Lemma

Date: 2026-06-26.

Status:

```text
proved clarification / zipper-born V3 is a shifted window, not a fresh four-edge V3
```

## Purpose

This corrects an important ambiguity after:

```text
clean_same_input_v3_second_layer_expansion_lemma.md
fixed_target_zipper_bridge_necklace_lemma.md
fixed_target_zipper_reduces_to_v3_admissibility.md
```

A V3 bridge born from adjacent edges of a fixed-target zipper is not a generic
clean four-edge V3 residual.  Its second V3 layer overlaps the zipper by
construction.

This matters because the unified V3 frontier has two sources:

```text
1. first-extra V3 bridges, which may be generic four-edge V3 objects;
2. zipper-born adjacent V3 bridges, which are shifted windows in one zipper.
```

## Setup

Fix a target:

```text
t.
```

Take three consecutive source rows in a clean right-`t` zipper:

```text
a*t=b,
b*t=c.
```

The adjacent same-input V3 bridge is:

```text
H_b: t -> A,      A=a*b,
H_c: t -> B,      B=b*c.
```

In the generic V3 notation:

```text
p=a,
q=b,
z=t,
s=b,
r=c.
```

So:

```text
q=s.
```

This source/output overlap is inherent in a source-successor zipper.  It is
not a new watched/core hit.

## Lifted Pair

The target-lift of the same-input split:

```text
a*t=b,
b*t=c
```

is:

```text
P=t*(b*a),
Q=t*(c*b).
```

These are exactly the adjacent zipper inputs:

```text
P=I_a,
Q=I_b,
```

where:

```text
row a: I_a -> b in H_t,
row b: I_b -> c in H_t.
```

## Generic V3 Second Layer

Apply:

```text
clean_same_input_v3_second_layer_expansion_lemma.md
```

to this adjacent V3 bridge.

The generic second layer says:

```text
A*a -> b*t,
B*b -> c*t.
```

Since:

```text
b*t=c,
```

the first second-layer edge is:

```text
A*a -> c.
```

But the zipper formula gives:

```text
I_b=(a*b)*a=A*a.
```

Therefore:

```text
A*a -> c
```

is the same ported interval as the already existing zipper edge:

```text
I_b -> c
```

carried by row `b`.

The second second-layer edge is:

```text
B*b -> c*t.
```

By the same zipper formula one step later:

```text
I_c=(b*c)*b=B*b.
```

So this is the next zipper edge:

```text
I_c -> c*t
```

carried by row `c`.

## Shift Form

Thus the V3 second-layer expansion of a zipper-born adjacent bridge is:

```text
I_a -> b,
I_b -> c,
I_b -> c,
I_c -> c*t.
```

It is not a fresh four-edge matching.  It is a shifted three-edge zipper
window, with the middle edge repeated as the overlap:

```text
current adjacent pair + next zipper edge.
```

## Consequence

The generic clean four-edge V3 residual applies to ungenerated V3 bridges
whose second layer is clean-disjoint.

For zipper-born adjacent V3 bridges, the correct residual is instead:

```text
a clean shifted zipper window.
```

Therefore the remaining admissibility sentence should be phrased carefully:

```text
Zipper-born V3 admissibility is not the same as generic four-edge V3
admissibility.  It asks whether a clean shifted zipper window is a smaller
measured relay object than the terminal self-repeat that contains it.
```

This is why the final obstruction is a fixed-target zipper/V3 necklace, not a
generic four-edge V3 matching.

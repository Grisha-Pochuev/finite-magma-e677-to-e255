# Anchored-M7 Clean V3 Necklace Obstruction

Date: 2026-06-25.

Status:

```text
obstruction / exact remaining admissibility problem after lift-advance equivalence
```

## Starting Point

Use:

```text
anchored_m7_zipper_lift_advance_equivalence_lemma.md
anchored_m7_coupled_zipper_bridge_residual.md
general_v3_bridge_descent_boundary.md
```

The clean M7 self-repeat has been converted into a closed necklace of
same-input V3-type bridges.

## Necklace Data

There is a cyclic list of source rows:

```text
r_0,r_1,...,r_{n-1}
```

with:

```text
r_i*h=r_{i+1}.
```

For each `i`, define:

```text
A_{i+1}=r_i*r_{i+1}.
```

Target advance gives:

```text
H_{r_{i+1}}: h -> A_{i+1}
```

carried by row `r_i`.

Every adjacent pair is a clean V3-type bridge:

```text
H_{r_i}:     h -> A_i,
H_{r_{i+1}}: h -> A_{i+1}.
```

The lift of that bridge is the adjacent zipper pair in `H_h`:

```text
I_{i-1} -> r_i,
I_i     -> r_{i+1}.
```

## Fully Clean Assumptions

The obstruction assumes no immediate route:

```text
r_i all distinct before cyclic return,
I_i all distinct,
A_i all distinct,
no I_i equals any r_j,
no A_i equals any r_j,
no A_i equals any I_j,
no A_i=h,
no watched/core hit.
```

Thus:

```text
the H_h layer is a clean matching,
the advanced V3 layer is a clean same-input bridge necklace,
and the two layers have no cross-hit.
```

## Why This Is Narrower

Before the lift-advance equivalence, the live object was:

```text
clean cyclic zipper matching.
```

Now it is:

```text
closed clean necklace of standard V3 bridges at one common input h.
```

So the remaining problem is not to classify local fans/paths.  Those are
already routed.  The remaining problem is well-foundedness of a closed V3
necklace.

## Desired Descent

The desired statement is:

```text
In a minimal G12 loop, a fully clean V3 necklace at one common input h is not
terminal.  It either:

1. has a smaller admissible V3 bridge under the M5/M6/M7 measure;
2. creates strict clean theta;
3. repeats a full ported interval in an independent role;
4. hits watched/core data.
```

The likely descent parameter is:

```text
the first position inside the M7 self-repeat cycle at which a clean V3 bridge
is born.
```

Since every adjacent pair in the necklace is born before the chosen return,
any admissible bridge among them should be smaller than the original terminal
self-repeat event.

## Exact Next Step

Formalize the measure comparison:

```text
original M7 = first self-repeat rank of the right-h source orbit;
new bridge rank = first adjacent V3 bridge inside that orbit.
```

If the new bridge is admissible under the existing V3 descent boundary, the
M7 self-repeat is not terminal.

If not, record the precise reason why the existing V3 measure does not accept
this bridge.

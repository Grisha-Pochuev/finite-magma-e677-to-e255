# Period-3 Middle-Target Core-Hook Frontier

Date: 2026-06-27.

Status:

```text
active frontier / bridge-to-relay route for the shifted-window residual
```

## Purpose

This file turns the broad shifted-window admissibility gap into a more
concrete relay question.

The period-3 residual has:

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

Target advance gives:

```text
H_z: h -> c*z       carried by row c,
H_b: h -> z*b       carried by row z,
H_c: h -> b*c       carried by row b.
```

The local equality checks do not close this triangle.  The new question is
whether the middle target-advanced edge:

```text
H_c: h -> b*c
```

is already a genuine relay/core object.

## Key Observation

The edge:

```text
H_c: h -> b*c
```

is not artificial.  It is exactly the target advance of the row-`b` zipper
edge:

```text
H_h: Ib -> c.
```

In full ported interval notation:

```text
(h, Ib, c)  --row b target advance-->  (c, h, b*c).
```

Thus the middle hook is a transported full ported interval state, not a free
two-target bridge.

## Sharper db-Indicated Fan

The core-hook scan found something stronger than core membership:

```text
HcOutAtH=11,
HcInAtBC=1
```

in all `6240` public strict period-3 examples.

Here:

```text
HcOutAtH = number of rows r with r*h=c,
HcInAtBC = number of rows r with r*c=b*c.
```

Since row `b` satisfies:

```text
b*h=c,
b*c=BC,
```

the db pattern says that `H_c` has a genuine outgoing fan at the same input
`h`:

```text
row b: h -> b*c,
row r: h -> r*c
```

for some `r!=b`, with no output collision at `b*c`.

Thus the strongest current candidate is:

```text
middle-target fan-at-h lemma:
in the clean period-3 residual, there is a row r!=b with r*h=c and
r*c!=b*c.
```

If proved, this immediately turns the shifted window into a standard
target-`c` outgoing fan, avoiding the broad V3 admissibility gap.

The public db scan identifies a named second row:

```text
r=Ib.
```

The output separation is now proved in:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
```

So the named fan reduces to one equality:

```text
Ib*h=c.
```

As of 2026-06-28 this has a sharper V3 formulation:

```text
period3_row_b_Ib_c_input_v3_lemma.md
```

Rows `b` and `Ib` at the common input `c` give:

```text
row b:  c -> b*c,
row Ib: c -> Ib*c.
```

If `Ib*c=b*c`, the target-lift in `H_c` routes by output merge or full
ported-interval reconstruction.  Otherwise this is a standard same-input V3
bridge at `c`.  The named fan is the special subcase where the lifted input
of the row-`Ib` edge equals `h`, equivalently:

```text
(Ib*c)*Ib=Ic.
```

The db-supported identity:

```text
Ib*c=z
```

is a watched output hit of this same `c`-input V3 bridge.  Thus the current
middle-target task is sharper than only proving `Ib*h=c`: prove watched/core
attachment of `Ib*c`, prove the fan-lift input, or reduce the remaining clean
four-edge V3 in `H_c` by the unified V3 frontier.

Indeed, if `Ib*h=c` and `Ib*c=b*c`, then rows `Ib` and `b` realize the same
full ported interval `(c,h,b*c)`, forcing `Ib=b`, which is a routed clean
collision.  In the db examples the stronger identity holds:

```text
Ib*c=z.
```

Together with the clean condition `z!=b*c`, this gives the displayed fan:

```text
row b:  h -> b*c
row Ib: h -> z
```

inside `H_c`.

The negation is also concrete:

```text
unique-preimage middle residual:
b is the unique row with b*h=c.
```

Equivalently, in `H_h` the zipper edge:

```text
Ib -> c
```

is the only edge entering `c`.  This is much narrower than the previous
generic V3 admissibility obstruction.

## Core-Hook Split

Build the graph:

```text
H_c.
```

Look at the edge carried by row `b`:

```text
h -> b*c.
```

There are three cases.

### 1. The Edge Is In A Bicyclic Core Component

If the component of `H_c` containing this edge has positive cyclomatic excess,
then:

```text
bicyclic_component_branch_fan_lemma.md
bad_target_core_fan_lemma.md
```

in their graph form give a core fan or mixed junction in the same component.
This supplies a genuine target-`c` relay object.

This case is not a circular use of V3 admissibility.  The shifted window has
created a standard core/relay object after target swap to:

```text
c=b*h.
```

The remaining work is then ordinary relay minimality: compare this target-`c`
relay to the terminal period-3 return, or show it repeats a full ported
interval in an independent role.

### 2. The Edge Is In A Unicyclic Core Component

If the component has excess `0`, the hook lies on a single clean cycle of
`H_c` but does not itself force a fan.

This is a new narrower residual:

```text
unicyclic middle-hook residual.
```

It is strictly more concrete than the old shifted-window admissibility gap:
one must analyze a specific target-advanced row-`b` edge in `H_c`, not an
abstract V3 bridge.

Possible exits:

```text
1. the cycle contains an old/core vertex and becomes a side attachment;
2. the cycle repeats a full ported interval in an independent role;
3. target advance around the cycle returns to the period-3 zipper and creates
   a smaller same-row recurrence;
4. the unicyclic case is impossible under the bad-target minimality measure.
```

### 3. The Edge Is Outside The Core

If the edge is pruned by 2-core deletion, it is a tree/tail edge of `H_c`.

For a relay proof this would mean the shifted window has not yet become a
core object.  The proof would then need a separate argument showing that the
tail either:

```text
1. returns to the old target/core footprint;
2. ends at a right fixer;
3. or is incompatible with the fact that the original row-b zipper edge
   belongs to the active period-3 source recurrence.
```

## Public db Evidence

The diagnostic:

```text
period3_core_hook_diagnostic.md
tools/period3_core_hook_scan.js
```

found in all `6240` strict public period-3 examples:

```text
H_c hook row b is in the 2-core;
its core component has excess 9;
it contains neither the target vertex c nor a right-fixer edge for c.
```

So the public examples all fall into Case 1.

The old target hook:

```text
H_b: h -> z*b
```

also lies in the 2-core, but only in an excess-`0` component in the same
examples.  Therefore the middle target `c`, not the old target `b`, is the
better relay candidate.

## Next Lemma To Prove

The strongest next statement is:

```text
Named middle-target fan lemma:
in a minimal clean period-3 G12 residual, the zipper input Ib satisfies:

    Ib*h=c.

The db-supported stronger target is:

    Ib*h=c,
    Ib*c=z.
```

If this fails, record and attack the exact negation:

```text
named fan negation:
the clean period-3 zipper has Ib*h!=c; in particular the named db fan row
does not pass through c at input h.
```

The older unique-preimage residual is stronger:

```text
unique-preimage middle residual:
b is the unique row with b*h=c.
```

If this is too strong, fall back to the weaker core-hook statement:

```text
Middle-target core-hook lemma:
in a minimal clean period-3 G12 residual, the row-b edge h -> b*c in H_c is
not outside the core and not merely unicyclic, unless the residual already
routes by old/core attachment, independent full ported interval collision, or
a right-fixer/shorter same-row recurrence.
```

If this lemma is proved, the shifted-window admissibility gap becomes a
standard relay-minimality problem after target swap to `c`.

## Caution

Do not infer this lemma from the db scan alone.  The scan only suggests the
right target and the right core object.

Also do not use:

```text
MZ<n
```

as the whole proof.  The core-hook lemma must explain why the earlier
shifted window is a real relay/core object.

## Relation To Existing Target-Swap Squares

The known target-swap/reversible-square lemmas:

```text
x_layer_bridge_pair_reversible_square_lemma.md
beta_x_bridge_pair_reversible_square_lemma.md
mixed_junction_target_swap_bridge_square.md
```

do not directly prove:

```text
Ib*h=c.
```

They transport an already known full ported interval across a target swap and
show reversibility of that transported interval.  The present claim is
different: the input of the row-`b` zipper edge,

```text
Ib=pred_b(h),
```

would itself become a source row through the same input `h`:

```text
row Ib: h -> c.
```

So the live target should be treated as a new input-source fan mechanism:

```text
row b:  Ib -> c in H_h,
row Ib: h  -> ? in H_c.
```

The public db suggests the missing output is exactly:

```text
Ib*c=z.
```

but the fan only needs the input-source equality:

```text
Ib*h=c.
```

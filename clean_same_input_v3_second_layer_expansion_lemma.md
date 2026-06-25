# Clean Same-Input V3 Second-Layer Expansion Lemma

Date: 2026-06-26.

Status:

```text
proved expansion / sharper residual for ungenerated clean V3 bridges
```

## Purpose

This sharpens the active frontier:

```text
clean_same_input_v3_admissibility_frontier.md
```

The remaining V3 object is a clean same-input two-target bridge.  This lemma
shows that it is not just a two-edge bridge after target advance: it also
forces a second same-target layer in the original common target graph.

## Setup

Assume:

```text
p*z=s,
q*z=r,
s!=r.
```

The ordinary V3 bridge after target advance is:

```text
H_s: z -> A,     A=p*s,
H_r: z -> B,     B=q*r.
```

The usual target-lift in `H_z` is:

```text
P -> s,          P=z*(s*p),       row p,
Q -> r,          Q=z*(r*q),       row q.
```

Indeed, E677 gives:

```text
p*P=z,
q*Q=z.
```

## Second-Layer Expansion

Use the standard E677 two-step consequence:

```text
if a=y*x and c=y*a, then a*(c*y)=x.
```

Proof of the consequence.  E677 applied to `a` and `y` gives:

```text
a = y*(a*((y*a)*y)) = y*(a*(c*y)).
```

But `a=y*x`; since finite E677 rows are left-cancellative, cancelling the
left row `y` gives:

```text
x=a*(c*y).
```

Apply it first with:

```text
y=p,
x=z,
a=s=p*z,
c=A=p*s.
```

Then:

```text
s*(A*p)=z.
```

Apply it again with:

```text
y=q,
x=z,
a=r=q*z,
c=B=q*r.
```

Then:

```text
r*(B*q)=z.
```

Therefore the same target graph `H_z` contains a second layer:

```text
A*p -> s*z,      row s,
B*q -> r*z,      row r.
```

So every V3 same-input split carries a four-edge same-target object in `H_z`:

```text
row p:  P   -> s
row q:  Q   -> r
row s:  A*p -> s*z
row r:  B*q -> r*z
```

where:

```text
P=z*(s*p),
Q=z*(r*q),
A=p*s,
B=q*r.
```

## Immediate Routing Roles

If the second layer has any of the usual local hits against the first layer:

```text
same input,
same output,
input-output cross hit,
full ported interval repetition,
watched/core hit,
```

then the V3 bridge is not the fully clean residual.  It routes by the same
collision mechanisms already used in:

```text
same_input_split_target_lift_lemma.md
same_input_lift_target_advance_lemma.md
same_target_pair_collision_trichotomy_lemma.md
```

In particular:

```text
A*p=P or B*q=Q
```

is an input repeat in `H_z`;

```text
s*z=s, s*z=r, r*z=s, r*z=r
```

is an output hit;

and any equality between one layer's input and another layer's output gives
an actual directed path inside `H_z`.

## Clean Residual

The ungenerated clean V3 gap can now be stated more sharply.

It is not merely:

```text
P -> s,
Q -> r
```

with target advance:

```text
H_s: z -> A,
H_r: z -> B.
```

For a generic V3 bridge whose second layer is clean-disjoint, the true clean
residual is:

```text
a clean four-edge matching in H_z
carried by rows p,q,s,r,
plus its two-target same-input bridge at z.
```

This matters for the global measure: a fully clean V3 bridge has a second
internal layer before it can be treated as a terminal obstruction.

There is one important exception:

```text
zipper_born_v3_second_layer_shift_lemma.md
```

If the V3 bridge is born from adjacent edges of a fixed-target zipper, then
one source row is also the previous output.  In that case the second layer
overlaps the existing zipper and becomes a shifted zipper window, not a fresh
four-edge matching.

## Consequence For The Current Frontier

The current unified V3 admissibility target should use this sharper residual:

```text
generic ungenerated clean same-input V3
-> clean target-lift in H_z
-> second-layer four-edge expansion in H_z
-> either a local hit routes,
   or the remaining obstruction is a clean four-edge V3 matching.
```

Thus the next proof step should not attempt to close a bare two-edge V3
bridge.  It should either:

```text
1. prove that a generic clean four-edge matching is admissible as a smaller
   measured relay object;
2. use the shifted-window reduction for zipper-born V3 bridges;
3. or show that the V3 common input must hit generated/watched/core data.
```

# Clean V3 Fixed-Target Source-Orbit Reduction

Date: 2026-06-26.

Status:

```text
proved reduction / clean V3 four-edge matching becomes a two-orbit H_z residual
```

## Purpose

This refines:

```text
clean_same_input_v3_second_layer_expansion_lemma.md
```

The clean V3 four-edge matching in `H_z` is not an isolated four-edge object.
It is exactly the first two layers of two fixed-target source-successor orbits
inside the same graph `H_z`.

## Setup

Start with a same-input V3 bridge:

```text
p*z=s,
q*z=r,
s!=r.
```

Let:

```text
A=p*s,
B=q*r,
P=z*(s*p),
Q=z*(r*q).
```

Then `H_z` contains:

```text
row p:  P   -> s
row q:  Q   -> r
row s:  A*p -> s*z
row r:  B*q -> r*z
```

The first two edges are the ordinary same-input target lift.  The second two
edges are the second-layer expansion.

## Source-Orbit Interpretation

For fixed target `z`, use the source-successor map:

```text
R_z(x)=x*z.
```

The two V3 rows start two right-`z` source-successor orbits:

```text
p -> s -> s*z -> ...
q -> r -> r*z -> ...
```

The displayed four-edge matching is exactly the first two attached `H_z`
edges of those two source orbits.

This is a direct application of:

```text
fixed_target_source_successor_lemma.md
```

to the first-layer edges:

```text
row p: P -> s,
row q: Q -> r.
```

For row `p`, the next source is `s=p*z`, and the next input is:

```text
(p*s)*p=A*p.
```

For row `q`, the next source is `r=q*z`, and the next input is:

```text
(q*r)*q=B*q.
```

These are exactly the two second-layer edges.

## First-Event Split

Continue the two source-successor orbits:

```text
R_p^0=p,      R_p^{n+1}=R_p^n*z,
R_q^0=q,      R_q^{n+1}=R_q^n*z.
```

For each source row `R_p^n` or `R_q^n`, the fixed target graph `H_z` has an
attached ported interval:

```text
(z, I_n, R^{n+1}),
```

where:

```text
I_n=z*(R^{n+1}*R^n).
```

Now take the first event among these two orbits:

```text
1. a cross-orbit source hit;
2. an output merge;
3. an input repeat;
4. an input-output cross hit;
5. a watched/core hit;
6. a self-repeat inside one orbit.
```

The first five event types route by the standard fixed-target and same-target
roles:

```text
fixed_target_source_orbit_first_merge_boundary.md
same_target_pair_collision_trichotomy_lemma.md
ported_interval_state_lemma.md
```

The only clean finite residual is:

```text
a clean same-orbit right-z self-repeat inside one of the two V3 source orbits.
```

## Zipper Form Of The Self-Repeat

If the clean residual is a same-orbit repeat:

```text
r_0*z=r_1,
...
r_{n-1}*z=r_0,
```

then the generic zipper formula from:

```text
anchored_m7_cycle_zipper_lemma.md
```

applies with `h` replaced by `z`:

```text
z*(r_{i+1}*r_i) = (r_{i-1}*r_i)*r_{i-1}.
```

Thus the V3 obstruction has the same structural endpoint as anchored-M7:

```text
clean fixed-target source self-repeat
-> cyclic zipper
-> adjacent same-input V3 bridge necklace.
```

The difference is only the source of the two starting orbits:

```text
first-extra V3 starts from p,q at input w;
anchored-M7 necklace starts from adjacent cycle rows at input h.
```

## Consequence For Unified V3 Admissibility

The unified V3 admissibility problem can now be stated as:

```text
Any ungenerated clean V3 four-edge matching in H_z either has a routed
first source-orbit event, or reduces to a clean right-z self-repeat zipper.
```

Therefore the remaining proof should not treat first-extra V3 and anchored-M7
V3 as unrelated.

Both reduce to the same fixed-target source-orbit/zipper mechanism.  The
remaining missing statement is the measure/admissibility comparison:

```text
the zipper-born adjacent V3 bridge is smaller than the clean self-repeat that
generated it, unless it hits watched/core data or repeats a full ported
interval in an independent role.
```

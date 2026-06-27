# Anchored-X3 Source-Orbit Boundary

Date: 2026-06-21.

Status:

```text
boundary / fixed-target source-orbit form of anchored-X3
```

## Purpose

This converts the clean anchored-X3 false branch into a fixed-target
source-orbit problem inside one graph:

```text
H_h.
```

The point is to avoid treating the anchored false branch as a free
three-target object.  Its second triangle layer is exactly the source-successor
layer for the fixed target `h`.

References:

```text
fixed_target_source_successor_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
anchored_x3_second_triangle_pressure_lemma.md
```

## Setup

Use the clean false branch:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
alpha=pred_z(h),
T=U*h,
S=W*h,
T!=S.
```

The original anchored layer in `H_h` is:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

## Fixed-Target Source Successors

For a fixed target `h`, every edge:

```text
row r: I -> O in H_h
```

forces the next source row:

```text
r -> r*h = O.
```

Thus the three anchored rows start three source-successor orbits in `H_h`:

```text
U -> T -> T*h -> ...
W -> S -> S*h -> ...
z -> b -> b*h -> ...
```

The first successor layer is exactly:

```text
row T: (U*T)*U -> T*h,
row S: (W*S)*W -> S*h,
row b: (z*b)*z -> b*h.
```

as recorded in:

```text
anchored_x3_second_triangle_pressure_lemma.md
```

## First-Merge Routing

Apply the fixed-target first-merge boundary to these three source-successor
orbits in `H_h`.

If two source orbits first meet at a source row:

```text
r_i=s_j,
```

then the same source row occurs again in the same fixed target graph `H_h`.
This repeats the corresponding full ported interval unless the hit is already
a watched local equality.  Route it as:

```text
full ported interval collision,
same-source recurrence,
or watched/core hit.
```

If two next outputs first meet:

```text
r_{i+1}=s_{j+1}
```

while:

```text
r_i!=s_j,
```

then two different rows in `H_h` have the same output.  This is an incoming
fan in `H_h`, unless the pair has a fuller local collision already routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
```

If an input-output cross hit occurs between the two `H_h` edges, the edges
concatenate into a directed path in `H_h`.

## Clean Residual

Therefore the only clean anchored-X3 continuation is:

```text
three source-successor orbits in H_h,
started by U,W,z,
with first outputs T,S,b,
with no cross-orbit source hit,
no output merge,
no input-output cross hit,
no watched/core hit,
and no self-repeat yet.
```

Because the magma is finite, this can persist only until a first repeat or
first merge.  That first event is the next exact target.

## Relation To The Global Measure

This is not yet a proof of descent.

It gives the correct residual form:

```text
anchored-X3 false branch
-> clean fixed-target source-orbit residual in H_h.
```

The next step is to compare the first repeat/merge of these three `H_h`
source orbits with the global G12 measure.  A useful descent would be:

```text
first repeat/merge before a clean self-return
=> fan/path/full interval/core hit;
clean self-return
=> same-row recurrence boundary measured by anchored-X3 rank.
```

This is now narrower than the earlier statement "route anchored-X3 like old
X3": the fixed target is `h`, and the three initial source rows are
`U,W,z`.

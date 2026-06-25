# Fixed-Target Source-Orbit Ladder Lemma

Date: 2026-06-19.

Status:

```text
general proved / predecessor formula along a fixed-target source orbit
```

## Purpose

This extends:

```text
fixed_target_source_successor_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
```

It gives a reusable formula for the whole source-successor orbit in one fixed
target graph `H_T`, without assuming that right multiplication by `T` is a
permutation.

## Setup

Fix a target `T` and a starting source row:

```text
r_0.
```

Define the right-`T` source-successor orbit:

```text
r_{n+1}=r_n*T.
```

For every step define:

```text
U_n=r_n*r_{n+1}.
```

## Statement

For every `n >= 0`, row `r_n` gives an edge in `H_T`:

```text
I_n -> r_{n+1},
```

where:

```text
I_n=pred_{r_n}(T).
```

The next predecessor is:

```text
I_{n+1}=U_n*r_n=(r_n*r_{n+1})*r_n.
```

Equivalently:

```text
r_{n+1}*((r_n*r_{n+1})*r_n)=T.
```

So the fixed-target source orbit carries the ladder:

```text
row r_n:     I_n -> r_{n+1},
row r_{n+1}: (r_n*r_{n+1})*r_n -> r_{n+2}.
```

## Proof

Apply:

```text
fixed_target_source_successor_lemma.md
```

to the edge:

```text
row r_n: I_n -> r_{n+1}
```

in `H_T`.  With:

```text
O=r_{n+1},
U=r_n*r_{n+1}=U_n,
```

the lemma gives:

```text
r_{n+1}*(U_n*r_n)=T.
```

By uniqueness of predecessors in row `r_{n+1}`:

```text
I_{n+1}=U_n*r_n.
```

## Y3 Instances

For the extra-source orbit:

```text
r_0=p,
r_1=S,
r_2=V=S*A_j,
U_0=p*S=U.
```

The first two `H_{A_j}` edges are:

```text
row p: P -> S,
row S: U*p -> V.
```

For the generated orbit:

```text
r_0=x_j,
r_1=b,
r_2=D_j,
U_0=x_j*b=x_{j+1}.
```

The first two `H_{A_j}` edges are:

```text
row x_j: Beta_j -> b,
row b:   x_{j+1}*x_j -> D_j.
```

Since:

```text
x_{j+1}*x_j=H_j,
```

this recovers the known row-`b` edge:

```text
H_j -> D_j.
```

For the next generated step:

```text
r_1=b,
r_2=D_j,
r_3=D_j*A_j,
U_1=b*D_j.
```

the ladder gives:

```text
row D_j: (b*D_j)*b -> D_j*A_j.
```

This is exactly the third triangle edge from:

```text
x3_advanced_edge_triangle_pressure_lemma.md
```

## Consequence

The clean Z3 source-side residual can be studied as two ladder orbits in the
same fixed target graph:

```text
p   -> S -> S*A_j -> ...
x_j -> b -> D_j   -> D_j*A_j -> ...
```

At every step, a source hit, output merge, predecessor hit, or watched-layer
hit becomes a standard `H_{A_j}` collision handled by:

```text
same_target_pair_collision_trichotomy_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
```

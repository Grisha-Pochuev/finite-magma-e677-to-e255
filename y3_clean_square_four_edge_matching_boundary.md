# Y3 Clean Square Four-Edge Matching Boundary

Date: 2026-06-19.

Status:

```text
boundary / clean shared-successor square adds a fourth H_{A_j} edge
```

## Purpose

This treats case 5 from:

```text
y3_shared_successor_square_boundary.md
y3_shared_successor_watched_hit_routing_lemma.md
```

After watched hits and the convergence branch `U=V` are routed, the square has:

```text
p*A_j=S,
p*S=U,
S*A_j=V,
S*(U*p)=A_j,
```

with:

```text
U,V fresh and U!=V.
```

The point is that this is not merely a fresh two-step extension.  It adds a
fourth edge to the same fixed target graph `H_{A_j}`.

## Existing Z3 Edges

The clean Z3 shell already contains three edges in `H_{A_j}`:

```text
row p:   P      -> S,
row x_j: Beta_j -> b,
row b:   H_j    -> D_j.
```

where:

```text
p*P=A_j,
p*A_j=S,
x_j*Beta_j=A_j,
x_j*A_j=b,
b*H_j=A_j,
b*A_j=D_j.
```

## Fourth Edge

By the shared-successor square:

```text
S*(U*p)=A_j,
S*A_j=V.
```

So row `S` contributes the fourth edge:

```text
U*p -> V
```

inside:

```text
H_{A_j}.
```

This is exactly the first successor edge in the fixed-target source orbit:

```text
p -> S -> V -> ...
```

as recorded in:

```text
fixed_target_source_orbit_ladder_lemma.md
```

## Collision Split

Compare the fourth edge:

```text
U*p -> V
```

with the three old edges:

```text
P      -> S,
Beta_j -> b,
H_j    -> D_j.
```

Any equality among:

```text
U*p, V
```

and the old inputs/outputs gives one of the standard roles:

```text
same input       -> outgoing fan in H_{A_j};
same output      -> incoming fan in H_{A_j};
full interval    -> source-row collision;
input-output hit -> directed path in H_{A_j};
watched hit      -> generated/visible first-hit route.
```

These are routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_orbit_first_merge_boundary.md
```

## Clean Four-Edge Residual

If no collision occurs, the Z3 square residual becomes a clean four-edge
matching in `H_{A_j}`:

```text
P      -> S       carried by row p,
U*p    -> V       carried by row S,
Beta_j -> b       carried by row x_j,
H_j    -> D_j     carried by row b.
```

with all four inputs distinct, all four outputs distinct, no input-output
cross-hit among them, and no watched footprint hit beyond the named local
vertices.

## Consequence

The clean square residual is sharper than:

```text
U,V fresh.
```

It is:

```text
a four-edge matching in H_{A_j} whose source rows include
p -> S and x_j -> b under right multiplication by A_j.
```

The next useful target is to compare the two adjacent source-successor pairs:

```text
p -> S,
x_j -> b,
```

inside this four-edge matching.  In particular, the next generated row after
`b` is already:

```text
D_j=b*A_j,
```

so extending the generated side gives the fifth candidate edge:

```text
(b*D_j)*b -> D_j*A_j.
```


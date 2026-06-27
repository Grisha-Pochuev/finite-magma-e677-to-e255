# Clean External-Bridge Ninth-Stage Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / Z3 square sharpened to paired four-edge shell
```

## Purpose

This updates:

```text
clean_external_bridge_eighth_stage_reduction_lemma.md
```

using:

```text
fixed_target_source_orbit_first_merge_boundary.md
fixed_target_source_orbit_ladder_lemma.md
y3_shared_successor_watched_hit_routing_lemma.md
y3_clean_square_four_edge_matching_boundary.md
y3_four_edge_matching_target_advance_boundary.md
```

## Correction

Right multiplication by a fixed element is not known to be a permutation.
Therefore the fixed-target source motion:

```text
r -> r*A_j
```

must be treated as a forward orbit with first merge/repeat, not as an automatic
cycle through its starting source.

The correct first-merge roles are recorded in:

```text
fixed_target_source_orbit_first_merge_boundary.md
```

## Z3 Square

The coupled Z3 shell contains:

```text
p*A_j=S.
```

Define:

```text
U=p*S,
V=S*A_j.
```

E677 forces:

```text
S*(U*p)=A_j.
```

So the square is:

```text
A_j -> S -> U       under row p,
p   -> S -> V       under right A_j,
S*(U*p)=A_j.
```

## Routed Branches

The watched hits of `U` and `V` are routed by:

```text
y3_shared_successor_watched_hit_routing_lemma.md
```

The convergence branch:

```text
U=V
```

is routed by:

```text
y3_commuting_second_step_reduction_lemma.md
```

as a same-target pair in `H_U`.

## Clean Square Becomes Four Edges

If:

```text
U,V are fresh and U!=V,
```

then row `S` adds a fourth edge in `H_{A_j}`:

```text
U*p -> V.
```

The clean fixed-target matching is:

```text
row p:   P      -> S,
row S:   U*p    -> V,
row x_j: Beta_j -> b,
row b:   H_j    -> D_j.
```

Pair collisions among these four edges route by:

```text
same_target_pair_collision_trichotomy_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
```

So the clean residual is a four-edge matching in `H_{A_j}`.

## Target-Advance Shell

Target advance of the four clean edges gives:

```text
H_S:     A_j -> U,
H_V:     A_j -> S*V,
H_b:     A_j -> x_{j+1},
H_{D_j}: A_j -> b*D_j.
```

Any collision or watched hit among:

```text
U,
S*V,
x_{j+1},
b*D_j
```

routes to a same-input bridge, same-target pair, fan, path, or generated
hit.  If none occurs, the remaining Z3 object is the paired shell:

```text
four-edge matching in H_{A_j}
plus
four-target same-input bridge at A_j.
```

## Ninth-Stage Residual List

The clean external bridge is now reduced to:

```text
N1. same-row recurrence boundaries;

N3. clean paired four-edge shell at A_j:
    H_{A_j} matching
      P      -> S,
      U*p    -> V,
      Beta_j -> b,
      H_j    -> D_j;

    target-advance bridge
      H_S:     A_j -> U,
      H_V:     A_j -> S*V,
      H_b:     A_j -> x_{j+1},
      H_{D_j}: A_j -> b*D_j.
```

## Next Useful Target

Attack the first merge/repeat of the two source-successor orbits:

```text
p -> S -> V -> ...
x_j -> b -> D_j -> ...
```

using the ladder predecessor formula:

```text
pred_{r_{n+1}}(A_j)=(r_n*r_{n+1})*r_n.
```

Do not describe these as right-`A_j` cycles unless a repeat has actually been
found and classified.

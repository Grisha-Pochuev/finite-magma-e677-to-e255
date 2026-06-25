# Fixed-Target Source-Orbit First-Merge Boundary

Date: 2026-06-19.

Status:

```text
boundary correction / right-target source motion is not a permutation
```

## Purpose

This corrects the language used after:

```text
fixed_target_source_successor_lemma.md
y3_fixed_target_source_orbit_boundary.md
```

For a fixed target `T`, the map:

```text
R_T(r)=r*T
```

is a right multiplication map.  In an E677 magma, left rows are permutations,
but right multiplication by a fixed element is not known to be a permutation.

So the source-successor motion:

```text
r_0, r_1=r_0*T, r_2=r_1*T, ...
```

is a finite forward orbit with possible merges/repeats, not automatically a
cycle through `r_0`.

## Edge Attached To Each Source Step

For every source row `r_n`, the fixed target graph `H_T` has the edge:

```text
pred_{r_n}(T) -> r_{n+1}
```

carried by row `r_n`.

By:

```text
fixed_target_source_successor_lemma.md
```

if:

```text
r_n*T=r_{n+1},
U_n=r_n*r_{n+1},
```

then:

```text
pred_{r_{n+1}}(T)=U_n*r_n,
```

and the next edge in `H_T` is:

```text
U_n*r_n -> r_{n+2}
```

carried by row `r_{n+1}`.

## First-Merge Roles

Let a fixed-target source orbit first repeat:

```text
r_n=r_m,
0 <= m < n.
```

Then the same source row appears again with the same target `T`, hence the
same full ported interval in `H_T`:

```text
(T, pred_{r_m}(T), r_{m+1})
=
(T, pred_{r_n}(T), r_{n+1}).
```

This is a same-source recurrence boundary.  If the two occurrences belong to
independent branch roles, the ported-interval reconstruction route applies;
if they are on one self-orbit, it is a same-row recurrence boundary.

If two different source orbits first meet:

```text
r_n=s_m,
```

then they share the same source row in the same `H_T` graph.  This repeats the
same full ported interval unless the hit is already one of the watched local
identifications.  Thus a cross-orbit source hit is routed, not a new residual.

If instead the first merge is only at the next output:

```text
r_{n+1}=s_{m+1},  but  r_n!=s_m,
```

then two different rows in `H_T` have the same output.  Apply:

```text
same_target_pair_collision_trichotomy_lemma.md
```

to route it as an incoming fan, full interval collision, path, or clean
same-target pair.

## Correct Clean Residual

The clean source-orbit residual is therefore not:

```text
two disjoint source cycles.
```

It is:

```text
two source-successor orbits with no watched hit, no cross-orbit source hit,
no output merge, and no self-repeat yet.
```

Since the magma is finite, this can only persist until the first repeat/merge.
The proof still needs to show that the first repeat/merge has one of the
routed roles in the coupled Z3 shell.

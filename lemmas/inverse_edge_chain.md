# Inverse Edge Chain

Status:

```text
stable local consequence of E677
```

This is one of the basic local tools used throughout the project.

## Starting edge

Assume an edge

```text
a*z = c.
```

Applying `E677` with suitable substitutions forces predecessor identities
around the triple `(a,z,c)`.

The most important schematic consequence is:

```text
z = c*((a*c)*a).
```

In words: once row `a` sends `z` to `c`, the identity `E677` forces row `c` to
recover the predecessor `z` through a specific column expression.

## Role

This turns a single forward edge into backward pressure.  It is the seed of
the later ladder, zipper, and pressure-diamond arguments.

## Used by

```text
edge_predecessor_triangle_lemma.md
source_orbit_ladder_lemma.md
source_orbit_zipper_lemma.md
main_bad_cycle_no_free_tail_lemma.md
```


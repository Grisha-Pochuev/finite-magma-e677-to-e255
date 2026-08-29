# E677 counterexample search: nonabelian signed group-isotope boundary

Date: 2026-07-26.

## Class tested

Let `G` be a nonabelian finite group.  Let `A,B` range over all group
automorphisms and all automorphisms composed with inversion.  The first exact
layer consists of

```text
c A(x) B(y),   A(x) c B(y),   A(x) B(y) c.
```

The identity-constant presentation is counted once.  The second layer is the
full translated signed principal isotope

```text
p A(x) q B(y) r.
```

Every generated multiplication table has permutation left rows.  The script

```text
tools/e677_nonabelian_group_isotope_scan.py
```

validates each group table, inverse map, and automorphism before checking all
E677 pairs and then E255.

## Complete results

For the one-constant layer, the dihedral groups `D_(2m)`, `3<=m<=12`, and
`Q_8` gave

```text
5,314,112 presentations checked;
0 E677 models;
0 counterexamples.
```

For the full translated layer on `D_6,D_8,D_10,Q_8`, the exact counts were

```text
D_6:       31,104
D_8:      131,072
D_10:   1,600,000
Q_8:    1,179,648
total:  2,941,824 presentations;
0 E677 models;
0 counterexamples.
```

There were no timeouts.  This closes the named nonabelian signed
principal-isotope layers.  Since not even a Good E677 model occurs, extending
the same group list or adding another isolated constant is not the next
move.

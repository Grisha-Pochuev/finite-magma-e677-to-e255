# E677 order-9 terminal ZERO-shadow exclusion

Date: 2026-08-29.

Status:

```text
proved reduction: terminal ZERO equality at order 9 forces a five-point
                  idempotent Latin E677 shadow on Bad;
checked exactly: among shadow orders 2,...,8 only order 5 exists, and its
                 unique isomorphism type is the K5 table;
checked exactly: the resulting 5 Bad + 4 Good terminal completion is UNSAT
                 with both CaDiCaL195 and Glucose42;
consequence: an order-9 counterexample must have HIT or strict root surplus
             Z_Omega>|Bad|.  The equality/no-HIT branch is closed.
```

This is a finite order-9 exclusion, not a proof of the full implication
`E677 -> E255`.

## Exact reduction

Let `M` be an E677 magma of order `9`, put `B=Bad`, `G=Good`, and let
`Omega=B x B` carry the induced `tau` graph.  Assume

```text
D(B) contained in B,                 (no HIT)
Z_Omega=|B|.                         (terminal root equality)       (1)
```

The proved ZERO-shadow lemma gives

```text
s(x)=x*x in G for x in B,
r o u = r*u for r!=u,
r o r = r,
```

and `(B,o)` is an idempotent Latin E677 quasigroup.  Since `D(B)` is
contained in `B` and no Bad point is fixed by `D`, one has `|B|>=2`.
The inclusion `s(B) subset G` makes `G` nonempty, so `|B|<=8`.

It remains to classify the possible auxiliary shadow orders `2,...,8`.

## Exhaustive shadow classification

The checker

```text
tools/e677_idempotent_latin_order_scan.py
```

encodes, for each order `b`, all of the following:

```text
every row is a permutation;
every column is a permutation;
x o x=x for every x;
all b^2 instances of E677.
```

The isomorphism split is exhaustive.  Idempotence fixes `0` under row zero,
and the remaining cycle type of that row is an integer partition of `b-1`.
Relabelling the other points conjugates the row to the canonical
representative used by the checker.  The scan covers respectively

```text
1,2,3,5,7,11,15
```

cycle-type cubes at orders `2,...,8`, or `44` cubes in total.

CaDiCaL195 finds

```text
order 2: UNSAT
order 3: UNSAT
order 4: UNSAT
order 5: SAT VERIFIED
order 6: UNSAT
order 7: UNSAT
order 8: UNSAT.                                      (2)
```

The verified order-five model is

```text
0 2 1 4 3
3 1 4 0 2
4 3 2 1 0
2 4 0 3 1
1 0 3 2 4.                                           (3)
```

To check uniqueness, the script forms the full relabelling orbit of (3).
The `120` relabellings deduplicate to `6` labelled tables, consistently with
the known automorphism group of order `20`.  Blocking all six tables and
rescanning every order-five row-zero cycle type gives

```text
Glucose42: 5/5 cubes UNSAT.                           (4)
```

Thus the shadow in (1) has exactly five points and is isomorphic to (3).

## Full order-9 completion

For distinct Bad points, the original product and the shadow product agree.
After relabelling `B={0,1,2,3,4}`, the original magma therefore contains the
twenty off-diagonal K5 cells from (3).  The remaining four labels are Good.

The terminal mode of

```text
tools/e677_k5_block_tree_completion_sat.py
```

fixes exactly those twenty cells and encodes

```text
all nine permutation rows;
Bad={0,1,2,3,4} by the unique-fixer criterion;
Good={5,6,7,8};
D(B) contained in B;
all 81 E677 instances.                                (5)
```

The identical `27,528`-clause formula gives

```text
CaDiCaL195: UNSAT, 2.460 seconds;
Glucose42:  UNSAT, 1.204 seconds.                      (6)
```

Every SAT result in the checker is decoded and independently checked against
the fixed cells, row permutations, colours, no-HIT condition, and all E677
pairs.  Formula (6) has no SAT result to decode; agreement of two independent
engines is the reproducibility check for UNSAT.

Equations (1)--(6) exclude terminal root equality at order `9`.

## Exact continuation

The general root identity gives `Z_Omega>=|B|`.  Hence an order-nine
counterexample, if one exists, is now forced into the strict split

```text
HIT:       some Bad D-orbit first enters Good;
SURPLUS:   no HIT and Z_Omega>=|B|+1.                         (7)
```

Do not return to the K5 size ladder or rerun the terminal equality formula.
For size `9`, the next useful constraint must attach one named extra root in
the SURPLUS branch to its first merger/exit, or close the finite HIT branch.

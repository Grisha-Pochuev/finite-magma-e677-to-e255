# Order-9 three-Bad top form 16: canonical root split

Date: 2026-08-29.

## Exact normalized form

Top form 16 is

```text
Bad={0,2,3};
1 is Good;
D: 0->2->3->0;
0*0=1;
1*0=2;
2*0=2.
```

This is family C (`square-Good, D(0)=2`), the directed three-cycle, and the
first-column chain `f(1)=2, f(2)=2`.

After selecting a strict extra Omega-root before naming labels, the canonical
root pairs are exactly

```text
(0,2), (0,3).
```

For each pair, the strict root product is exhaustively

```text
Good;
row value 0;
the third Bad point.
```

Thus the canonical root split has six exact leaves.

For a Good root product, row zero already uses the Good output `1` at input
zero.  Residual relabelling is transitive on every other Good label, so each
aggregate Good outcome has one exact representative, named `4`.  The finer
Good-product split therefore has only two leaves:

```text
0*2=4 Good;
0*3=4 Good.
```

## Exact checker

The experiment uses the unchanged audited checker

```text
tools/e677_order9_no_hit_bad_count_sat.py
```

at Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d.
```

Every SAT answer must decode to a complete `9 x 9` table and pass independent
checks of all nine permutation rows, all 81 E677 substitutions, the exact Bad
set, the exact D-map, and no HIT.  A partial assignment is never treated as a
counterexample.

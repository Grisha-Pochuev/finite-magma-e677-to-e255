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

## Runs

```text
smoke: 33269622554
full:  33269852847
full head SHA: 5b0e8765b40fac638d1e09ba15908a9e01f3b347
```

The short gate passed in both engines and produced valid summaries and a
collected report.  The full run then gave:

```text
aggregate six outcomes / Glucose42:       6/6 UNSAT;
aggregate six outcomes / CaDiCaL195:      5/6 UNSAT, one Good aggregate UNKNOWN;
exact two Good representatives / Glucose42:  2/2 UNSAT;
exact two Good representatives / CaDiCaL195: 2/2 UNSAT.
```

The sole CaDiCaL aggregate UNKNOWN is `(0,2)` with Good product.  Its complete
residual relabelling orbit is represented by `0*2=4`, which is UNSAT in both
engines.  Consequently all six exhaustive outcomes are excluded and top form
16 is UNSAT.

No SAT model and therefore no complete order-nine counterexample was found.
The exact records are in `RESULTS.md`, `run-summary.json`, `RUN_REPORT.md`,
`closure-summary.json`, and the four compact solver logs in this folder.

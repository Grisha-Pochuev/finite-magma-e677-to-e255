# Codex handoff — order-9 three-Bad form 16

Date: 2026-08-29.

## Result

Top form `16` is exactly excluded.

```text
Bad={0,2,3};
D: 0->2->3->0;
0*0=1;
1*0=2;
2*0=2.
```

Its canonical extra root is `(0,2)` or `(0,3)`.  For each root the exhaustive
product classes are Good, the row label `0`, and the third Bad label.  Thus the
aggregate split has six leaves.  Residual Good-label symmetry fixes each Good
product to `4`, giving two exact Good representatives.

## Certificate

The unchanged checker is:

```text
tools/e677_order9_no_hit_bad_count_sat.py
Git blob: efe356acd0047eef8ae5645b2cb04ac2a493632d
```

Full run `33269852847` gave:

```text
Glucose42 aggregate root split:       6/6 UNSAT;
CaDiCaL195 aggregate root split:      5/6 UNSAT, (0,2)/Good UNKNOWN;
Glucose42 exact Good representatives: 2/2 UNSAT;
CaDiCaL195 exact Good representatives:2/2 UNSAT.
```

The only CaDiCaL aggregate UNKNOWN is exactly represented by `0*2=4`, already
UNSAT in its two-leaf exact refinement.  Therefore all six canonical outcomes
are excluded independently across the two engines.  No SAT model and no full
`9 x 9` counterexample occurred.

Exact records are in `RESULTS.md`, `run-summary.json`, `RUN_REPORT.md`,
`closure-summary.json`, and the four solver logs in this folder.

## New frontier

The three-Bad count is now

```text
18/24 closed.
```

Remaining forms:

```text
11, 15, 18, 21, 23, 24.
```

The smallest next aggregate split is form `11` or `18` (six root-outcome
leaves each).  Form `23` has nine aggregate leaves but only two Good-product
representatives.  Do not rerun form 16 or its unsplit cube.

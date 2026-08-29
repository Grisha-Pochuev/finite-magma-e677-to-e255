# Run report: order-9 three-Bad form 3

Full run: `33268434711`.

- Formula: 3,151 variables, 55,911 clauses.
- Root-outcome records: 2/2 present.
- Good-product refinement records: 2/2 present.
- Technical failures: 0.
- Verified complete counterexamples: 0.

| Split | Solver | UNSAT | UNKNOWN | SAT |
| --- | --- | ---: | ---: | ---: |
| Six canonical root outcomes | CaDiCaL195 | 6 | 0 | 0 |
| Six canonical root outcomes | Glucose42 | 6 | 0 | 0 |
| Four Good-product representatives | CaDiCaL195 | 4 | 0 | 0 |
| Four Good-product representatives | Glucose42 | 4 | 0 | 0 |

The aggregate six-outcome split is exhaustive and by itself proves top form 3
UNSAT.  The four Good-product representatives are an independent finer
cross-check of the two hardest aggregate outcomes.

Mathematical consequence:

```text
order-9 no-HIT |Bad|=3 top forms closed: 17/24;
remaining: 11,15,16,18,21,23,24.
```

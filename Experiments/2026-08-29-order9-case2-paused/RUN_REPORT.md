# Run report

Full run: `33267614227`.

- Expected summaries: 2
- Found summaries: 2
- Missing summaries: 0
- Engines proving all six leaves UNSAT: 2
- Verified no-HIT counterexamples: 0
- Engines with bounded UNKNOWN leaves: 0
- Technical failures: 0

| Solver | Result | UNSAT | UNKNOWN | SAT | Hard leaf time | Hard leaf conflicts |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| CaDiCaL195 | `ALL_SIX_UNSAT` | 6 | 0 | 0 | 3.501s | 63,138 |
| Glucose42 | `ALL_SIX_UNSAT` | 6 | 0 | 0 | 3.391s | 62,888 |

The hard leaf was

```text
(a,k)=(0,1), equivalently 0*3=0 and 3*1=2.
```

The formula contained 3,151 variables and 55,911 clauses.  Both engines used
the same pinned base checker and the same six exact assumption cubes.  No SAT
model was found.  Hence top form 2 is completely excluded.

# Order-9 form-16 run report

- expected summaries: 4
- received summaries: 4
- broken summaries: 0
- technical failures: 0
- verified complete counterexamples: 0
- all-UNSAT jobs: 3
- bounded-UNKNOWN jobs: 1

| mode | solver | result | UNSAT | UNKNOWN | SAT | seconds |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| good-products | cadical195 | ALL_UNSAT | 2 | 0 | 0 | 17.161 |
| good-products | glucose42 | ALL_UNSAT | 2 | 0 | 0 | 10.179 |
| root-outcomes | cadical195 | BOUNDED_UNKNOWN | 5 | 1 | 0 | 54.165 |
| root-outcomes | glucose42 | ALL_UNSAT | 6 | 0 | 0 | 59.265 |

The one bounded aggregate UNKNOWN is `(0,2)` with a Good product in
CaDiCaL195.  Residual Good-label symmetry gives the sole representative
`0*2=4`, which is independently UNSAT in both engines.  Therefore the
mathematical result is `FORM16_UNSAT` despite that deliberately bounded
aggregate run.

# Order-9 three-Bad form-2 paused continuation

Date: 2026-08-29.

## Mathematical target

This experiment resumes the exact paused point in
`lemmas/e677_order9_three_bad_root_and_case2_reduction.md`.

Assume an order-nine E677 magma, no HIT, and exactly

```text
Bad={0,1,2},
D: 0->1->2->0,
0*0=1, 1*0=2, 2*0=1.
```

The preceding certified reduction proves that the selected strict extra root
must be

```text
(0,2), with 0*2=3 Good.
```

Put

```text
a=0*3,
k=a*0.
```

E677 forces `3*k=2`.  Row injectivity and residual relabelling leave exactly
six representatives:

```text
(a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5).
```

The experiment checks these six leaves separately.  It does not repeat the
already closed eight root outcomes, the first 15/24 top-form scan, the
terminal K5 formula, or the two-Bad formulas.

## Exact checker

The base formula is

```text
tools/e677_order9_no_hit_bad_count_sat.py
```

at Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d.
```

`run_case2_paused.py` verifies that blob before making a narrowly scoped
in-memory extension.  The extension adds exactly the six assumptions above;
it does not alter the base CNF.  Every SAT result still passes the base
checker's independent audit of:

- all nine permutation rows;
- all 81 E677 substitutions;
- exact Bad set of size three;
- the exact D-map and no-HIT condition.

Therefore a SAT result is relevant only if the decoded complete 9x9 table
passes that audit.  A partial assignment is never reported as a
counterexample.

## Result meanings

```text
ALL_SIX_UNSAT
    This engine proves the sole form-2 residue impossible.

BOUNDED_UNKNOWN
    At least one leaf survives only because the fixed resource boundary was
    reached.  This is not evidence for a counterexample.

VERIFIED_NO_HIT_COUNTEREXAMPLE
    The base checker decoded a full 9x9 table and verified all semantic
    conditions.  This would be a genuine order-nine no-HIT counterexample.

TECHNICAL_FAILURE
    The checker, parser, dependency, artifact, or workflow failed.
```

Agreement of CaDiCaL195 and Glucose42 on all six UNSAT leaves is the intended
independent certificate standard.

## Workflow stages

1. Static checks and a short end-to-end smoke run in both engines.
2. Only after the smoke record is inspected, a bounded full run of the same
   six leaves in both engines.
3. A final collector writes `run-summary.json`, `run-summary.csv`, and
   `RUN_REPORT.md`.
4. The verified compact result is copied into this directory and the active
   workflow is disabled after the experiment.

## Scope warning

Even a complete `6/6 UNSAT` result closes only top form 2 among the nine
initially unresolved three-Bad forms.  It does not close the other eight
three-Bad forms, larger Bad cardinalities, HIT, or the full order-nine
implication.

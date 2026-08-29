# E677 order-9 three-Bad top-form 16 exclusion

Date: 2026-08-29.

Status:

```text
proved reduction: top form 16 has exactly two canonical strict extra-root
                  positions and six exhaustive product outcomes;
checked exactly: all six outcomes are UNSAT;
checked independently: every residual Good-product orbit is UNSAT in both
                       CaDiCaL195 and Glucose42;
consequence: normalized three-Bad top form 16 is impossible at order 9.
```

This is one finite no-HIT exclusion at order `9`.  It does not close the HIT
branch, the no-HIT cases with more than three Bad points, or the complete
order-nine implication.

## Exact normalized form

The form is

```text
B=Bad={0,2,3};
1 is Good;
D(0)=2, D(2)=3, D(3)=0;
0*0=1;
1*0=2;
2*0=2.                                                        (1)
```

In the exhaustive list of 24 three-Bad normal forms, this is family C
(`square-Good, D(0)=2`), the directed three-cycle, and the first-column chain
`f(1)=2, f(2)=2`.

The canonical-root argument from the general three-Bad reduction applies
before the remaining labels are named.  Since `D` is the cycle

```text
0 -> 2 -> 3 -> 0,
```

the selected strict extra root can be normalized to exactly one of

```text
(0,2), (0,3).                                                  (2)
```

## Six exhaustive root outcomes

Let `(v,h)` be either pair in (2), and write `u=v*h`.  The exact root witness
requires

```text
u is Good,
or u is Bad and N_B(u,v)=0.                                   (3)
```

The product cannot equal the input `h`: the equality `v*h=h` would be a left
fixer of the Bad point `h`.  Therefore, among the three Bad labels, only the
row label and the third Bad point remain.  For each of the two roots, the
product classes are exactly

```text
Good;
row label 0;
the third Bad point.                                          (4)
```

Thus (2)--(4) give six exhaustive leaves:

```text
(0,2): Good, 0, or 3;
(0,3): Good, 0, or 2.                                         (5)
```

No partial multiplication table or heuristic root placement is used in this
split.

## Exact Good-product representatives

In row zero, output `1` is already used at input zero by `0*0=1`.  Hence a
Good product in either non-diagonal root cannot be `1`.  The remaining Good
labels are unnamed and are permuted transitively by the residual relabelling
that fixes every label displayed in (1).  Consequently each aggregate Good
leaf has exactly one labelled representative, which may be named `4`:

```text
0*2=4;
0*3=4.                                                        (6)
```

Therefore an UNSAT check of the two leaves in (6) excludes the complete
aggregate Good disjunctions, not merely two arbitrarily chosen products.

## Exact SAT formula and semantic verification

The unchanged checker is

```text
tools/e677_order9_no_hit_bad_count_sat.py
```

at Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d.                      (7)
```

It encodes

```text
all nine left rows as permutations;
all 81 E677 instances;
exact Good/Bad colours by the unique-fixer criterion;
exact sigma and D values;
Bad={0,2,3};
D(Bad) contained in Bad;
the fixed cells and D-cycle in (1);
the strict-root assumptions in (3)--(6).                       (8)
```

Every SAT result is decoded as a complete `9 x 9` multiplication table and is
then checked independently against every item in (8).  Hence only a complete
verified table could be reported as a counterexample.

## Computation

Full GitHub Actions run:

```text
33269852847
head SHA: 5b0e8765b40fac638d1e09ba15908a9e01f3b347.                    (9)
```

The aggregate split (5) gave

```text
Glucose42:  6/6 UNSAT;
CaDiCaL195: 5/6 UNSAT, with only (0,2)/Good UNKNOWN at the fixed
             500,000-conflict boundary.                         (10)
```

The exact Good representatives (6) gave

```text
Glucose42:  2/2 UNSAT;
CaDiCaL195: 2/2 UNSAT.                                         (11)
```

The sole aggregate UNKNOWN in (10) is precisely the residual orbit represented
by `0*2=4`, which is UNSAT in both engines in (11).  Thus the UNKNOWN is fully
discharged by an exhaustive symmetry split.  Combining (10) and (11), every
leaf in (5) is independently excluded.

There was no SAT model and no technical failure.

## Consequence

Top form `16` is UNSAT.  The three-Bad order-nine count improves from

```text
17/24
```

to

```text
18/24.                                                         (12)
```

The remaining normalized three-Bad forms are exactly

```text
11, 15, 18, 21, 23, 24.                                       (13)
```

The full order-nine implication remains open because (13), all no-HIT cases
with at least four Bad points, and the HIT branch have not all been excluded.

## Reproduction and records

The dated experiment folder is

```text
Experiments/2026-08-29-order9-case16-root/
```

It contains the exact smoke and full workflows, the four compact solver logs,
`run-summary.csv`, `run-summary.json`, `RUN_REPORT.md`,
`closure-summary.json`, and `CODEX_HANDOFF.md`.

The local two-engine verifier is

```text
verify_order9_three_bad_case16.ps1
```

Do not rerun the unsplit top-form cube or count a bounded aggregate UNKNOWN as
a surviving mathematical case after the exhaustive representative (6) has
been excluded.

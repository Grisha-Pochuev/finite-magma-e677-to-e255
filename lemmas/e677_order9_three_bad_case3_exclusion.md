# E677 order-9 three-Bad top form 3 exclusion

Date: 2026-08-29.

Status:

```text
proved by an exact two-engine finite certificate:
normalized order-9 no-HIT three-Bad top form 3 is impossible.
```

This is a finite order-nine result.  It does not prove the full implication
`E677 -> E255` for order `9` or for arbitrary finite orders.

## Exact normalized form

Assume an order-nine E677 magma, no HIT, and exactly three Bad points.  Top
form `3` in the exhaustive 24-form normalization is

```text
Bad={0,1,2};
D(0)=1, D(1)=2, D(2)=0;
0*0=1;
1*0=3;
3*0=1.                                                          (1)
```

Thus the D-graph on Bad is the directed three-cycle

```text
0 -> 1 -> 2 -> 0.                                                (2)
```

The first-column chain differs from the already excluded top form `2` only by
replacing `1*0=2, 2*0=1` with the Good intermediate point `3` in (1).

## Exhaustive canonical roots

The terminal equality branch has already been excluded at order `9`.  Every
surviving three-Bad model therefore has a strict non-diagonal Omega-root.
Choose the cyclic label `0` after selecting such a root.  For the three-cycle
(2), its canonical pair is exactly one of

```text
(0,1), (0,2).                                                    (3)
```

For a non-diagonal Bad pair `(v,h)`, the product cannot be `h`, since that
would be a left fixer of the Bad input `h`.  The exact root condition then
leaves three exhaustive product outcomes:

```text
product Good;
product v;
product the third Bad point.                                    (4)
```

Combining (3) and (4) gives the six exact leaves

```text
(0,1): product Good, product 0, product 2;
(0,2): product Good, product 0, product 1.                       (5)
```

The checker represents a Good outcome as the disjunction of every exact root
witness whose product is Good.  Therefore the two Good leaves in (5) are
already aggregate exhaustive cases, not partial guesses.

## Exact SAT formula

The certificate uses

```text
tools/e677_order9_no_hit_bad_count_sat.py
```

at Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d.                       (6)
```

For each leaf, the formula contains

```text
3151 variables;
55911 clauses;
all nine rows constrained to be permutations;
all 81 E677 substitutions;
exact Bad={0,1,2};
exact normalized data (1)--(2);
exact no-HIT condition D(Bad) subset Bad;
one exact canonical root outcome from (5).                      (7)
```

Any SAT answer is decoded as a complete `9 x 9` table and independently
checked for all row permutations, all 81 E677 instances, exact Bad
cardinality, exact D-map, and no HIT.  A partial assignment is never reported
as a counterexample.

## Two-engine result

GitHub Actions run

```text
33268434711                                                        (8)
```

checked all six leaves independently with CaDiCaL195 and Glucose42:

```text
CaDiCaL195: 6/6 UNSAT, 0 UNKNOWN, 0 SAT;
Glucose42:  6/6 UNSAT, 0 UNKNOWN, 0 SAT.                          (9)
```

The two most expensive aggregate leaves were

```text
root=(0,1), product Good:
  CaDiCaL195 24.654s, 385240 conflicts;
  Glucose42  28.652s, 368640 conflicts;

root=(0,2), product Good:
  CaDiCaL195 15.930s, 173409 conflicts;
  Glucose42  18.221s, 162049 conflicts.                           (10)
```

There were no technical failures and no SAT model.

## Independent Good-product refinement

Residual relabelling fixes the displayed labels `0,1,2,3` and is transitive
on the unnamed Good labels.  Hence each aggregate Good outcome in (5) splits
into exactly two representatives:

```text
product 3;
product 4, where 4 names a new Good point.                        (11)
```

The resulting four exact leaves were also checked independently:

```text
CaDiCaL195: 4/4 UNSAT;
Glucose42:  4/4 UNSAT.                                           (12)
```

This refinement is not needed for exhaustiveness, because the aggregate Good
leaves in (5) are already exact.  It is an independent finer cross-check of
the difficult part of (9).

## Conclusion

Every model of normalized top form `3` must realize one of the six outcomes
(5), while (9) proves every one of them impossible.  Therefore

```text
normalized order-9 no-HIT three-Bad top form 3 is UNSAT.         (13)
```

The three-Bad frontier improves from

```text
16/24 closed
```

to

```text
17/24 closed.                                                     (14)
```

The unresolved top-form indices are now exactly

```text
11, 15, 16, 18, 21, 23, 24.                                    (15)
```

Reproduction:

```powershell
./verify_order9_three_bad_case3.ps1
```

Full records:

```text
Experiments/2026-08-29-order9-case3-root/RESULTS.md;
Experiments/2026-08-29-order9-case3-root/run-summary.json;
Experiments/2026-08-29-order9-case3-root/RUN_REPORT.md.
```

The seven forms in (15), larger Bad cardinalities, and HIT remain open.

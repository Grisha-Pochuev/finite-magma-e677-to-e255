# E677 order-9 three-Bad root normalization and case-2 exclusion

Date: 2026-08-29.

Status:

```text
proved: every order-9 no-HIT model with exactly three Bad points has one of
        24 normalized (square colour, D-graph, f-chain) forms;
checked boundary: 15/24 top forms are UNSAT in the first exact CaDiCaL scan;
proved and independently checked: in top form 2, eight canonical extra-root
        outcomes are UNSAT and the ninth reduces to six exhaustive companion
        leaves;
checked independently: all six companion leaves are UNSAT in CaDiCaL195 and
        Glucose42;
consequence: top form 2 is completely excluded, so 16/24 top forms are now
             closed;
open:   the eight top forms 3,11,15,16,18,21,23,24 remain unresolved.
```

This is a strict finite reduction for order `9`.  It does not close all
three-Bad models and does not prove the full implication `E677 -> E255`.

## Exact setting

Let `B=Bad`, assume `|B|=3`, and impose no HIT:

```text
D(B) contained in B.
```

The terminal equality branch is already excluded at order `9`.  The three
diagonal states in `B x B` are always roots, so every surviving model has a
non-diagonal state `(v,h)` of internal indegree zero.  If

```text
u=v*h,
```

the exact root condition is

```text
u is Good, or u is Bad and N_B(u,v)=0.                         (1)
```

The checker represents (1) directly: a root witness fixes `v*h=u`; when `u`
is Bad it additionally forbids every Bad carrier `r*u=v`.

## The 24 exhaustive normal forms

The map `D:B->B` has no fixed point.  Its functional graph is therefore one
of

```text
a directed 3-cycle;
a directed 2-cycle with one tail, aimed at either cycle point.             (2)
```

Choose `0` on a `D`-cycle and normalize

```text
0*0=1,   f(t)=t*0,   D(0)=f(f(1)).                              (3)
```

There are three square/D families:

```text
A: 1 is Bad and D(0)=1,       B={0,1,2};
B: 1 is Bad and D(0)=2,       B={0,1,2};
C: 1 is Good and D(0)=2,      B={0,2,3}.                         (4)
```

After residual relabelling, the possible `f`-chains are

```text
A: f(1)=1;
   f(1)=2, f(2)=1;
   f(1)=3, f(3)=1;

B: f(1)=2, f(2)=2;
   f(1)=3, f(3)=2;

C: f(1)=2, f(2)=2;
   f(1)=3, f(3)=2;
   f(1)=4, f(4)=2.                                               (5)
```

Combining the three graph orientations in (2) with (5) gives

```text
3*3 + 3*2 + 3*3 = 24.                                           (6)
```

The first bounded exact scan returned

```text
15/24 UNSAT; 9/24 UNKNOWN; no SAT model.                          (7)
```

The `UNKNOWN` forms were exactly

```text
2, 3, 11, 15, 16, 18, 21, 23, 24.                               (8)
```

The present result closes form `2`, so the unresolved list is now

```text
3, 11, 15, 16, 18, 21, 23, 24.                                  (9)
```

Fixing only the position of the extra root did not propagate: the first
`15/15` such trials were `UNKNOWN` and that split was intentionally stopped.
It is a retired diagnostic, not an exclusion.

## Canonical extra roots

The normalization can be chosen after selecting an extra root.  For a
3-cycle, choose its row coordinate as `0`; the root is then

```text
(0,D(0)) or (0,D^2(0)).                                         (10)
```

For a 2-cycle with tail `t`, a root whose row lies on the cycle becomes

```text
(0,D(0)) or (0,t),
```

while a root whose row is the tail becomes `(t,0)` by choosing its cycle
input as `0`.  These are exhaustive.

For any non-diagonal Bad state `(v,h)`, the product cannot equal `h`, since
that would be a left fixer of the Bad input `h`.  Hence the three exact root
outcomes are

```text
product Good;
product v;
product the third Bad point.                                    (11)
```

The first outcome split closed `23/66` cubes at its small boundary.  Naming
the Good product up to residual relabelling closed `6/37` further cubes.
Those two counts locate the frontier; they are not a closure of the remaining
forms.

## First reduction of top form 2

Top form 2 is

```text
B={0,1,2};
0*0=1;
D(0)=1, D(1)=2, D(2)=0;
1*0=2, 2*0=1.                                                     (12)
```

By (10), its selected extra root is `(0,1)` or `(0,2)`.  If its product is
Bad, (11) leaves exactly four cubes:

```text
(0,1) with product 0 or 2;
(0,2) with product 0 or 1.                                      (13)
```

All four are UNSAT in both engines.

If `(0,1)` has Good product, residual Good relabelling makes it

```text
0*1=3.                                                          (14)
```

Put `a=0*3`.  The four forced cells associated to E677 (called the companion
word in the internal notes) give, with `k=a*0`,

```text
0*1=3, 0*3=a, a*0=k, 3*k=1.                                    (15)
```

Row-zero injectivity gives `a!=1,3`.  If `a=0` or `a=2`, (12) gives `k=1`,
and then `3*1=1` fixes the Bad point `1`, impossible.  Thus a new Good label
may be normalized as

```text
a=4.                                                            (16)
```

The value `k` cannot be `0` (it would fix the Bad point `0`) or `1` (by the
last cell of (15)).  Up to residual Good relabelling,

```text
k in {2,3,4,5}.                                                  (17)
```

All four cubes in (17) are independently UNSAT in CaDiCaL195 and Glucose42.
Together with (13), this proves

```text
top form 2 -> selected extra root is (0,2) and 0*2=3 is Good.    (18)
```

The eight exclusions in (13) and (17) are checked by the first half of

```text
verify_order9_three_bad_case2.ps1.
```

## Completion of the paused continuation

For the sole residue in (18), put

```text
a=0*3, k=a*0; then 3*k=2.                                      (19)
```

Row-zero injectivity and residual relabelling reduce (19) to exactly

```text
(a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5).                      (20)
```

The six leaves in (20) were checked with the same exact order-nine formula.
The formula has

```text
3151 variables;
55911 clauses;
all nine permutation rows;
all 81 E677 instances;
exact Bad={0,1,2};
exact D-cycle 0->1->2->0;
no HIT;
the selected root (0,2) with 0*2=3 Good;
one exact pair (a,k) from (20).                                 (21)
```

The results are

```text
CaDiCaL195: 6/6 UNSAT, 0 UNKNOWN, 0 SAT;
Glucose42:  6/6 UNSAT, 0 UNKNOWN, 0 SAT.                         (22)
```

The only leaf requiring a nontrivial search was

```text
(a,k)=(0,1), equivalently 0*3=0 and 3*1=2:
CaDiCaL195 UNSAT in 3.501s with 63138 conflicts;
Glucose42  UNSAT in 3.391s with 62888 conflicts.                 (23)
```

The other five leaves were then immediately inconsistent under their own
exact assumption sets in each independent engine.

The experiment wrapper

```text
Experiments/2026-08-29-order9-case2-paused/run_case2_paused.py
```

pins the audited base checker by Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d
```

and adds only the six assumption cubes (20) in memory.  It does not alter the
base CNF.  Every SAT result would still be decoded and checked against all 81
E677 instances, every row permutation, the exact Bad set, the exact D-map,
and no HIT.  No SAT result occurred.

The full record is in

```text
Experiments/2026-08-29-order9-case2-paused/RESULTS.md;
Experiments/2026-08-29-order9-case2-paused/run-summary.json;
logs/e677_order9_three_bad_case2_complete_2026-08-29.txt.
```

Equations (18)--(23) exclude the final root outcome, hence

```text
top form 2 is UNSAT.                                             (24)
```

The complete fourteen-leaf certificate (the earlier eight leaves plus the
six paused leaves) is reproduced by

```text
verify_order9_three_bad_case2.ps1.
```

## Exact continuation

The three-Bad no-HIT frontier is now the eight forms

```text
3, 11, 15, 16, 18, 21, 23, 24.                                  (25)
```

Form `3` is the closest successor to the closed form `2`: it keeps the same
three-cycle D-pattern and changes only the first-column chain to

```text
1*0=3, 3*0=1.                                                    (26)
```

The next finite step should reuse the canonical-root split (10)--(11) and the
companion word, not rerun the unsplit top-form cube.  Larger Bad cardinalities
and HIT remain separate open branches.

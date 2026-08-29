# E677 order-9 three-Bad root normalization and case-2 reduction

Date: 2026-08-29.

Status:

```text
proved: every order-9 no-HIT model with exactly three Bad points has one of
        24 normalized (square colour, D-graph, f-chain) forms;
checked boundary: 15/24 top forms are UNSAT in the first exact CaDiCaL scan;
proved and independently checked: in top form 2, all canonical extra-root
        outcomes except root (0,2) with Good product 3 are UNSAT;
open:   top form 2 still has that one residual root outcome, and the other
        eight top forms from the first scan remain unresolved.
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
3*3 + 3*2 + 3*3 = 24                                            (6)
```

forms.  The first bounded exact scan returned

```text
15/24 UNSAT; 9/24 UNKNOWN; no SAT model.                          (7)
```

The `UNKNOWN` forms are exactly indices

```text
2, 3, 11, 15, 16, 18, 21, 23, 24.                               (8)
```

Fixing only the position of the extra root did not propagate: the first
`15/15` such trials were `UNKNOWN` and that split was intentionally stopped.
It is a retired diagnostic, not an exclusion.

## Canonical extra roots

The normalization can be chosen after selecting an extra root.  For a
3-cycle, choose its row coordinate as `0`; the root is then

```text
(0,D(0)) or (0,D^2(0)).                                         (9)
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
product the third Bad point.                                    (10)
```

The first outcome split closed `23/66` cubes at its small boundary.  Naming
the Good product up to residual relabelling closed `6/37` further cubes.
Those two counts locate the frontier; they are not a closure of the remaining
cubes.

## Complete reduction of top form 2

Top form 2 is

```text
B={0,1,2};
0*0=1;
D(0)=1, D(1)=2, D(2)=0;
1*0=2, 2*0=1.                                                     (11)
```

By (9), its selected extra root is `(0,1)` or `(0,2)`.  If its product is
Bad, (10) leaves exactly four cubes:

```text
(0,1) with product 0 or 2;
(0,2) with product 0 or 1.                                      (12)
```

All four are UNSAT in both engines.

If `(0,1)` has Good product, residual Good relabelling makes it

```text
0*1=3.                                                          (13)
```

Put `a=0*3`.  The four forced cells associated to E677 (called the companion
word in the internal notes) give, with `k=a*0`,

```text
0*1=3, 0*3=a, a*0=k, 3*k=1.                                    (14)
```

Row-zero injectivity gives `a!=1,3`.  If `a=0` or `a=2`, (11) gives `k=1`,
and then `3*1=1` fixes the Bad point `1`, impossible.  Thus a new Good label
may be normalized as

```text
a=4.                                                            (15)
```

The value `k` cannot be `0` (it would fix the Bad point `0`) or `1` (by the
last cell of (14)).  Up to residual Good relabelling,

```text
k in {2,3,4,5}.                                                  (16)
```

All four cubes in (16) are independently UNSAT in CaDiCaL195 and Glucose42.
Together with (12), this proves

```text
top form 2 -> selected extra root is (0,2) and 0*2=3 is Good.     (17)
```

The eight exclusions in (12) and (16) are checked by

```text
verify_order9_three_bad_case2.ps1
```

Every SAT result in the underlying checker would be decoded and checked
against all 81 E677 instances, all nine permutation rows, the exact Bad set,
and no HIT.  There is no SAT result in this certificate.

## Exact paused continuation

For the sole residue in (17), put

```text
a=0*3, k=a*0; then 3*k=2.                                      (18)
```

Row-zero injectivity and residual relabelling reduce (18) to

```text
a in {0,2,4};
a in {0,2} -> k=1;
a=4       -> k in {1,3,4,5}.                                   (19)
```

No calculation for (19) has been launched.  This is the exact restart point
after the requested pause.

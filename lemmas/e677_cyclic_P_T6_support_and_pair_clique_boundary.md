# E677 cyclic P: T6 support and pair-clique boundary

Date: 2026-07-26.

Status:

```text
the distinguished-target support split is completely permissive modulo
block capacity and is retired; the full tuple-6 kernel is reduced exactly
to a seven-row pair clique; no clique witness is known
```

## 1. Distinguished-target support alignment

For `s=0`, put

```text
q(t)=O7_t(0),
z(t)=O7_t^(-1)(0),
x(t)=q(t)-t,
rho(t)=D(x(t))-A(q(t)),
E={t:x(t) is in supp(D)}.
```

On a fibre `B` of `z`, `rho` is constant.  Both `q` and `x` are injective
on `B`:

- if `q(t)=q(u)`, equality of `rho` and injectivity of `D` give
  `q(t)-t=q(u)-u`, hence `t=u`;
- if `x(t)=x(u)`, equality of `rho` and injectivity of `A` give
  `q(t)=q(u)`, hence again `t=u`.

Every canonical `D` has support size four and fixed complement size three.
Consequently a block of size `m` has the sharp capacity bounds

```text
max(0,m-3) <= |E intersect B| <= min(m,4).       (SUPPORT-CAPACITY)
```

The exact classifier

```text
tools/e677_fiber7_T6_zero_target_support_alignment_classify.py
```

enumerates the `1854` nonzero displacement rows `z` for which `t+z(t)` is a
permutation.  They induce `427` unlabeled kernel partitions in the nine
surviving profiles.  It then eliminates `q` and the distinct `rho` labels
block by block for all `720` permutations `A` fixing zero and all four
canonical `D`.

For every canonical `D`:

```text
720/720 A occur in a feasible zero-target core;
427/427 realizable partitions occur in a feasible zero-target core.
```

For each profile, the attained total support counts are exactly those left
by `SUPPORT-CAPACITY`:

```text
largest block <= 3:  |E|=0..7;
largest block  = 4:  |E|=1..7;
profile (5,1,1):     |E|=2..6.
```

These are projection statements over `A` and partitions, not a claim that
every Cartesian pair `(A,partition)` works.  They suffice to show that total
support count, profile, and the elementary block-capacity bounds do not
provide the missing tuple-6 obstruction.  The CNF support-count extremes
`|E|=0,7` were also `UNKNOWN` at twenty seconds and must not be rerun.

## 2. Exact pair-clique form of tuple 6

Write `U_t=O7_t` and

```text
R_s(t)=D(U_t(s)-t)-A(U_t(s)).
```

For fixed `s`, `T6-KERNEL` says

```text
U_t^(-1)(s)=U_u^(-1)(s)  iff  R_s(t)=R_s(u).
```

Therefore tuple 6 for all targets is exactly the following pairwise law for
all row pairs `t,u` and all `s`:

```text
U_t^(-1)(s)=U_u^(-1)(s)
iff
D(U_t(s)-t)-A(U_t(s))
 = D(U_u(s)-u)-A(U_u(s)).                       (PAIR-KERNEL)
```

The cyclic `Q`-fibre condition is also pairwise:

```text
U_t(T-t) != U_u(T-u) for every T and t!=u.      (PAIR-LATIN)
```

Together with `U_t(0)!=0` and pairwise distinct rows, a seven-row solution
of `PAIR-KERNEL` and `PAIR-LATIN` is equivalent to the complete tuple-6
kernel core.  Indeed, for each `s`, the common kernel defines an injection
from the image of `z_s` to the image of `R_s`; it extends to the required
permutation row `K_s`.

The constructive search

```text
tools/e677_fiber7_T6_kernel_pair_clique_search.py
```

uses this exact seven-partite clique formulation.  Its bounded negative
outcomes are diagnostics, not exclusions:

```text
23 fixed (D,A) cases, 180 seconds total: no witness;
D=0125634, A=0132465, 60 seconds:
  678/4320 roots, 74666 nodes, maximum depth 3/7;
D=1023546, A=0132465, 60 seconds:
  1256/4320 roots, 65677 nodes, maximum depth 4/7.
```

The original exact CNF with the latter fixed pair gives the genuine result

```text
D=1023546, A=0132465: tuple-6 kernel UNSAT (3.069 seconds).
```

The former fixed pair remains `UNKNOWN` at sixty seconds.

## 3. Relative-permutation continuation

For a pair `t,u`, set

```text
pi_tu = U_u o U_t^(-1),
F_t(q)=D(q-t)-A(q),
H_tu(pi)={q:F_t(q)=F_u(pi(q))}.
```

Reparametrizing `PAIR-KERNEL` by `q=U_t(s)` gives the exact set identity

```text
H_tu(pi_tu)=U_t(Fix(pi_tu)).                    (FIX-COLLISION)
```

If `d=u-t` and

```text
tau_(U_t,d)=U_t o (r -> r+d) o U_t^(-1),
```

then `PAIR-LATIN` says that `pi_tu` and `tau_(U_t,d)` disagree at every
point.  Across triples the relative maps obey the cocycle law

```text
pi_tv = pi_uv o pi_tu.                          (TRIANGLE-COCYCLE)
```

This is the next exact invariant.  Classify relative pair types satisfying
`FIX-COLLISION` and the shifted derangement condition, then impose
`TRIANGLE-COCYCLE` before searching for seven actual rows.  Do not rerun the
raw clique search or the common kernel SAT formula unchanged.

## 4. Warning about the column-collision diagnostic

The quantity

```text
E_col(A,D)=sum_t sum_v C(|{q:F_t(q)=v}|,2)
```

is useful only for ordering constructive cases.  It counts collisions down
columns of the `R` array.  `T6-KERNEL` preserves collisions across each row,
and the extending permutations `K_s` depend on `s`; hence there is no valid
identity equating `E_col` to the sum of the `z_s` collision energies.

The diagnostic has the same distribution for all four canonical `D`; its
maximum `63` contains seven `A` per `D`, hence `28` fixed pairs.  One of these
pairs is the strict `UNSAT` case above, while their combined exact formula

```text
tools/e677_fiber7_T6_kernel_max_column_collision_sat.py
```

is `UNKNOWN` at `180` seconds.  This combined run is retired.  No exclusion
may be inferred merely from the value of `E_col`.

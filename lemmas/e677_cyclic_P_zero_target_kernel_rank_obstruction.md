# Cyclic `P`: zero-target kernel rank obstruction

Date: 2026-07-26.

Status:

```text
the distinguished tuple-6 kernel can have only ranks 3, 4, or 5; all nine
remaining block profiles are arithmetically realizable and form the next
support-alignment boundary
```

## Inverse-position displacement

For a permutation row table `O7` satisfying the cyclic transversal condition,
put for every output `s`

```text
z_s(t)=O7_t^(-1)(s).
```

For fixed total coordinate `T`, the transversal

```text
r -> O7_r(T-r)
```

contains `s` exactly once.  The equality `O7_t(z_s(t))=s` shows that this is
equivalent to

```text
phi_s(t)=t+z_s(t)
```

being a permutation.  Therefore

```text
sum_t z_s(t)=sum_t phi_s(t)-sum_t t=0 mod 7.   (ZERO-SUM)
```

For the distinguished output `s=0`, Badness gives

```text
z_0(t)!=0 for every t.
```

Thus `z_0` is exactly the nonzero displacement sequence of a derangement of
`F_7`.

## Manual rank exclusions

Let `r_0=|image(z_0)|`.

`r_0=7` is impossible because all values are nonzero.  If `r_0=6`, the
seven-term multiset contains every nonzero value except one value `m`, and
duplicates one value `d`.  Since the sum of all six nonzero field values is
zero, `(ZERO-SUM)` gives `d-m=0`, contradicting that the missing and duplicated
values differ.

If `r_0=2`, let the two values be `a!=b`, with multiplicities `k` and `7-k`.
Then `(ZERO-SUM)` is `k(a-b)=0`; since `1<=k<=6`, this is impossible.

The remaining rank-one displacement has `z_0(t)=c!=0`.  Apply the tuple-6
kernel lemma.  Put

```text
q(t)=O7_t(0),
rho(t)=D(q(t)-t)-A(q(t)).
```

Since `z_0` is constant, `T6-KERNEL` makes `rho` constant.  If
`q(t)=q(t')`, injectivity of `D` then forces `t=t'`; hence `q` is injective.
But Badness gives `q(t)!=0` for all seven `t`, impossible in the six-element
set `F_7\{0}`.

Consequently every full kernel core satisfies

```text
r_0 in {3,4,5}.                                (RANK-345)
```

## Complete arithmetic profiles

Exhausting the `1854` derangements of seven points confirms the manual rank
set

```text
rank 1:   6 derangements;
rank 3: 504 derangements;
rank 4: 588 derangements;
rank 5: 756 derangements.
```

Tuple 6 removes rank 1, leaving exactly nine multiplicity profiles:

```text
rank 3: (5,1,1), (4,2,1), (3,3,1), (3,2,2);
rank 4: (4,1,1,1), (3,2,1,1), (2,2,2,1);
rank 5: (3,1,1,1,1), (2,2,1,1,1).
```

There are `108` labelled nonzero zero-sum multiplicity vectors of these
types, forming `18` scalar orbits.  Every one of the nine profiles is realized
by an actual derangement, so no further profile can be removed by
`(ZERO-SUM)` alone.

## Exact computational boundary

The reduced `T6-KERNEL` formula has only `886` variables and `73991` clauses,
but the common four-`D` formula is UNKNOWN after `180.404` seconds.  A direct
rank split gives

```text
rank 1: UNSAT;
rank 2: UNSAT;
rank 3: UNKNOWN;
rank 4: UNKNOWN;
rank 5: UNKNOWN;
rank 6: UNSAT;
rank 7: UNSAT.
```

The four UNSAT ranks now also have the manual proofs above.  Splitting ranks
`3,4,5` into all nine block profiles leaves all nine UNKNOWN at twenty seconds
each.  Do not repeat or lengthen either kernel scan.

## Continuation

For `s=0`, retain

```text
q(t)=O7_t(0) != 0,
z(t)=O7_t^(-1)(0),
rho(t)=D(q(t)-t)-A(q(t)),
ker(z)=ker(rho).
```

The next invariant must record how the nine possible zero-sum block types
meet the four-point support `S` of the canonical double swap `D`.  In
particular mark

```text
E={t:q(t)-t in S}
```

and couple its blockwise distribution to the values `A(q(t))`.  A split only
by block sizes has reached its exact negative boundary.

## Verification

```text
python tools/e677_fiber7_T6_zero_target_displacement_classify.py
python tools/e677_fiber7_T6_kernel_sat.py --seconds 180
python tools/e677_fiber7_T6_kernel_rank_scan.py --per-rank-seconds 20
python tools/e677_fiber7_T6_kernel_profile_scan.py --per-profile-seconds 20
```

# Cyclic `P`: two-role shift and pure-dilation exclusions

Date: 2026-07-26.

Status:

```text
two complete translation families and the AD pure-dilation family excluded
already by tuples 0,2,6,7; mixed affine symbol maps remain open
```

## Exact pair invariant

Use the losslessly normalized cyclic isotope representation

```text
D(C_q(u))=A(q)+B(u),
A(0)=0, A(1)=1, B(0)=0.
```

Exactly two of `A,B,D` are now nonidentity.  For a pair `(X,Y)` use

```text
r_X=|image(X-id)|,
r_Y=|image(Y-id)|,
lambda=cycle type of X^(-1)Y.
```

For each fixed pair, the common exact formula imposes the routing forms of
tuples 0 and 2 together with original tuples 6 and 7.  A SAT answer is
decoded and audited against all `49` cells of each original identity.

## Two exact `AB` regions

The normalized `AB,D=id` family has `85561` labelled pairs and `120` exact
`(r_A,r_B,lambda)` types.  Its five smallest types contain respectively

```text
16, 18, 19, 20, 20 pairs.
```

All `93/93` pairs are UNSAT, with no SAT or UNKNOWN.  The opposite,
maximally long relative type

```text
(r_A,r_B,lambda)=(5,7,(1,6))
```

contains `170` pairs.  Its first short scan left two UNKNOWN; checking only
those two closes them, giving `170/170` UNSAT.  Thus `263` normalized `AB`
pairs in six named types are exactly excluded.  This is not an exclusion of
the whole `AB` family.

Removing tuple 0 from the smallest 16-pair type does not produce a model:
at ten seconds per pair the exact tuple-`2,6,7` result is `8` UNSAT and `8`
UNKNOWN.  Do not lengthen that diagnostic; it makes no theorem claim.

## Complete nonzero-translation exclusion

Now let the nonidentity symbol role be a translation

```text
D(x)=x+c, c!=0.
```

There are six choices of `c`.  In `AD,B=id`, `A` ranges over all `119`
normalized nonidentity permutations, giving exactly `714` pairs.  An
incremental fixed-pair scan gives

```text
AD translation: 714/714 UNSAT, 0 SAT, 0 UNKNOWN, 168.199 s.
```

In `BD,A=id`, `B` ranges over all `719` normalized nonidentity permutations,
giving `4314` pairs.  The first `0.1`-second scan proves `4299` UNSAT and
leaves `15` UNKNOWN.  Rechecking exactly those `15` at two seconds each
proves every one UNSAT:

```text
BD translation: 4314/4314 UNSAT, 0 SAT, 0 UNKNOWN.
```

Consequently no normalized two-role cyclic isotope with a nonzero
translation in the `D` role can be a counterexample, whether the other role
is `A` or `B`.

## Complete `AD` pure-dilation exclusion

For

```text
D(x)=k*x, k in {2,3,4,5,6}, B=id,
```

the common solver with all `119` values of `A` proves UNSAT for
`k=2,4,5,6`.  The `k=3` common formula is UNKNOWN, but its exact incremental
decomposition proves all `119/119` fixed `A` cases UNSAT.  Hence

```text
AD pure dilations: 5*119=595/595 UNSAT,
0 SAT, 0 UNKNOWN.
```

Together with the translation result, this excludes `1309` exact `AD`
pairs.  It does **not** exclude the mixed affine maps

```text
D(x)=k*x+c, k!=1, c!=0.
```

An attempted short fixed-pair scan of that mixed class was stopped after
the first `150` pairs produced `149` UNKNOWN and only one UNSAT.  Increasing
that computation is not a continuation.

For `BD` even the common class with `D(x)=2x` is UNKNOWN at `60.348`
seconds.  A fixed-`B` scan was stopped after its first `150/150` cases were
UNKNOWN.  Thus the pure-dilation exclusion is currently directional: it is
proved for `AD`, not for `BD`.

## Exact continuation

The next counterexample invariant is the unique fixed point of a mixed
affine symbol map `D(x)=kx+c`, relative to the distinguished Bad fibre
coordinate.  A useful reduction must couple that pointed fixed location to
`T2-ROUTING`; it must not enumerate the remaining affine pairs one by one.
Equivalently one may change to the full three-role normalized class and use
the isotope gauge to move the fixed point while tracking which role becomes
nonidentity.

Do not repeat the undivided `AB/AD/BD` formulas, the stopped mixed-affine
scan, or the stopped `BD,D=2x` scan.

## Reproduction

```text
python tools/e677_fiber7_cyclic_p_two_role_pair_scan.py --branch AB --left-rank 4 --right-rank 7 --relative-cycle 1,2,2,2 --per-pair-seconds 2
python tools/e677_fiber7_cyclic_p_two_role_pair_scan.py --branch AB --left-rank 5 --right-rank 7 --relative-cycle 1,6 --per-pair-seconds 1
python tools/e677_fiber7_cyclic_p_two_role_pair_scan.py --branch AD --left-rank 0 --right-rank 1 --relative-cycle any --per-pair-seconds 2
python tools/e677_fiber7_cyclic_p_two_role_pair_scan.py --branch BD --left-rank 0 --right-rank 1 --relative-cycle any --per-pair-seconds 0.1
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --free-systems AD --fix-d 0246135 --seconds 60
python tools/e677_fiber7_cyclic_p_two_role_pair_scan.py --branch AD --left-rank 0 --right-rank 0 --relative-cycle any --fix-right-only 0362514 --per-pair-seconds 2
```

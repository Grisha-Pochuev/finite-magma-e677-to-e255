# Cyclic `P`: minimum `D` curvature and the four-transversal boundary

Date: 2026-07-26.

Status:

```text
the first genuinely nonlinear D layer is classified exactly and reduced to
four canonical harmonic double swaps; the complete T0/T2/T6/T7 formula is
still UNKNOWN, so the layer is open and all equivalent SAT reruns are retired
```

## Translation curvature

For a permutation `D` of `F_7` and `t!=0`, put

```text
partial_t D(x)=D(x+t)-D(x),
m_t(D)=max_v |{x:partial_t D(x)=v}|,
kappa(D)=sum_(t!=0) (7-m_t(D)).
```

An affine permutation has six constant derivative rows and `kappa=0`.  An
exact exhaustion of all `7!=5040` permutations gives

```text
42 affine permutations;
4998 nonlinear permutations;
minimum nonlinear kappa: 18;
permutations at kappa=18: 294.
```

For every one of the `294` maps and every nonzero `t`, the derivative
multiplicity profile is exactly

```text
(4,2,1).
```

## Harmonic double-swap normal form

The `294` maps have the exact structural form

```text
D=L o pi_(a,d),
pi_(a,d)=(a,a+d)(a+4d,a+5d),
d!=0,
L(x)=alpha*x+beta, alpha!=0.
```

All arithmetic is in `F_7`.  Set equality between this class and the complete
`kappa=18` layer is checked exhaustively, not inferred from matching counts.
Every such `D` is at Hamming distance four from exactly three affine maps.
The `294` labelled maps form `50` scalar-conjugacy orbits before using the
isotope representation gauge.

The internal gauge

```text
A'=hA+p, B'=hB+q, D'=hD+p+q
```

sends an affine centre `L` to the identity.  Therefore the whole labelled
layer is represented losslessly by the `21` distinct maps `pi_(a,d)`.  The
remaining split-translation gauge fixes `A(0)=0`.  Scalar fibre conjugacy

```text
D_r(x)=r*D(r^(-1)*x)
```

preserves cyclic `P`, Badness, the isotope equation, and the routing
identities, and reduces the `21` maps to the four representatives

```text
0125634,
0145236,
1023546,
1024356.
```

Thus these four cases are a complete symmetry quotient of the first
nonlinear `D` layer.

## Four defect transversals

Every canonical `D` is an involution.  Hence

```text
D(C_q(u))=A(q)+B(u)
```

is exactly

```text
C_q(u)=D(A(q)+B(u)).                           (FOUR-TRANSVERSAL)
```

Let `S` be the four-point support of the double swap `D`.  Outside `S`, the
cell is the affine-background value `A(q)+B(u)`.  The nonlinear cells are
exactly

```text
E_s={(q,u):A(q)+B(u)=s},  s in S.
```

For every `s`, `E_s` is a permutation transversal of the `7x7` table; the
four are disjoint.  Consequently every row and every column has exactly four
defect cells and three affine-background cells.  This is an exact global
description of the remaining nonlinearity, not a heuristic support pattern.

## Bounded exact formulas

All formulas below impose the original tuples `0,2,6,7`, block literal affine
`C`, and audit any SAT model cell by cell:

```text
all 294 normalized D, anchors exposed:
UNKNOWN 181.071 s, 1,647,141 conflicts;

21-map identity-centre gauge quotient:
UNKNOWN 180.292 s, 1,676,209 conflicts;

21 fixed gauge maps, 10 seconds each:
0 SAT, 0 UNSAT, 21 UNKNOWN, 216.580 s;

four scalar representatives with C=D(A+B) exposed directly:
UNKNOWN 183.840 s, 1,690,754 conflicts.
```

No counterexample or exclusion follows from `UNKNOWN`.  The agreement of all
four encodings is the exact negative boundary: do not repeat them, increase
their limits, or fix the same `D` maps again.

## Exact continuation

The remaining obstruction is not the choice of `D`; it is the placement of
the four canonical transversals through `A,B` inside `T2-ROUTING`.  Substitute
`(FOUR-TRANSVERSAL)` into

```text
h=H_t(r),
V(r,t)=W_h(t-C_t(h)).
```

For every fixed `t`, exactly four values of `h` satisfy
`A(t)+B(h) in S`, and the other three are affine-background cells.  The next
manual target is a collision or permutation-balance lemma for this exact
`4+3` split.  A useful lemma must couple the four marked `h` values across
different `t` through the common permutations `A,B`; treating the seven rows
independently would discard the new invariant.

## Reproduction

```text
python tools/e677_fiber7_D_curvature_classify.py
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --d-min-curvature --seconds 180
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --d-min-curvature-gauge --seconds 180
python tools/e677_fiber7_D_min_curvature_gauge_scan.py --per-d-seconds 10
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --d-min-curvature-canonical --seconds 180
```

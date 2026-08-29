# Cyclic `P`: normalized isotope one-role exclusion

Date: 2026-07-26.

Status:

```text
all normalized nonaffine isotope cores with exactly one nonidentity role
are excluded already by tuples 0,2,6,7; two-role cores remain open
```

## Lossless normalized isotope class

Continue in the order-49 cyclic branch

```text
P_t(s)=t-s,
D(C_q(u))=A(q)+B(u) mod 7,
```

where `A,B,D` are permutations.  The representation gauge

```text
A'=kA+p, B'=kB+q, D'=kD+p+q
```

preserves the same `C`.  Since `A` is injective, every representation has a
unique gauge with

```text
A(0)=0, A(1)=1, B(0)=0.                         (ISO-NORM)
```

Thus `(ISO-NORM)` loses no cyclic isotope.  All `252` literal affine tables

```text
C_q(u)=alpha*q+beta*u+gamma
```

are blocked, because their full E677 exclusion was proved separately.

The isotope equations are attached to the lossless routing reduction

```text
V(r,t)=W_(H_t(r))(t-C_t(H_t(r)))=O0_r(t),
W_(V(t,s))(s-C_s(H_t(s)))=t,
```

together with the exact cyclic tuple-6 equation and `O1=W^(-1)`.  Hence any
SAT answer is an original tuple-`0,2,6,7` Bad core, audited cell by cell.

The undivided normalized nonaffine isotope class remains UNKNOWN after
`180.268` seconds (`1720541` conflicts).  It is retired in that form.

## Exactly one nonidentity normalized role

Split by which one of the normalized `A,B,D` differs from the identity.
The first two classes are directly UNSAT:

```text
A free, B=D=id: UNSAT 45.744 s;
B free, A=D=id: UNSAT  0.147 s.
```

The direct `D`-free formula was initially UNKNOWN.  It can instead be
exhausted exactly.  Put

```text
delta_D(x)=D(x)-x.
```

Outside the `42` affine permutations, the `4998` labelled permutations `D`
have only ranks and counts

```text
rank 3:  882 labelled, 149 scalar-conjugacy orbits;
rank 4: 1372 labelled, 232 scalar-conjugacy orbits;
rank 5: 2646 labelled, 446 scalar-conjugacy orbits;
rank 7:   98 labelled,  17 scalar-conjugacy orbits.
```

Scalar fibre conjugacy

```text
D_k(x)=k*D(k^(-1)*x)
```

preserves `A=B=id`, cyclic `P`, Badness, and all routing identities.  Hence
the `844` orbits above are exhaustive.  An incremental exact scan fixes one
representative at a time in the common formula and gives

```text
rank 3: 149/149 UNSAT, 24.884 s;
rank 4: 232/232 UNSAT, 33.324 s;
rank 5: 446/446 UNSAT, 62.947 s;
rank 7:  17/17  UNSAT, 11.587 s;
total:  844/844 UNSAT, 0 SAT, 0 UNKNOWN.
```

Therefore no normalized cyclic isotope with exactly one nonidentity role
can be a counterexample; it already fails before tuples 1, 3, 4, and 5 are
introduced.

## Two-role boundary

The next three normalized classes require exactly two roles to be
nonidentity, with the third fixed to the identity.  Their undivided routing
formulas give

```text
AB free, D=id: UNKNOWN 60.128 s;
AD free, B=id: UNKNOWN 60.149 s;
BD free, A=id: UNKNOWN 60.344 s.
```

No model or exclusion follows.  Do not rerun or lengthen these three
formulas.  The next exact invariant is the pair

```text
(|image(X-id)|, |image(Y-id)|)
```

together with the cycle type of the relative permutation `X^(-1)Y` in each
of `AB,AD,BD`.  A useful next computation fixes one such relative type and
uses scalar-conjugacy representatives; a bare enumeration of all ordered
permutation pairs is not the continuation.

## Reproduction

```text
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --seconds 180
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --single-nonlinear A --seconds 60
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --single-nonlinear B --seconds 60
python tools/e677_fiber7_cyclic_p_single_D_orbit_scan.py --ranks 3 --per-orbit-seconds 2
python tools/e677_fiber7_cyclic_p_single_D_orbit_scan.py --ranks 4 --per-orbit-seconds 2
python tools/e677_fiber7_cyclic_p_single_D_orbit_scan.py --ranks 5 --per-orbit-seconds 2
python tools/e677_fiber7_cyclic_p_single_D_orbit_scan.py --ranks 7 --per-orbit-seconds 2
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --free-systems AB --seconds 60
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --free-systems AD --seconds 60
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --free-systems BD --seconds 60
```

# Cyclic `P`: mixed-affine gauge transfer and anchored-law boundary

Date: 2026-07-26.

Status:

```text
the mixed-affine AD class has two exact gauge transfers and an exact anchored
cell law; three bounded common encodings are UNKNOWN and are retired
```

## Exact gauge transfers

Start with the losslessly normalized `AD,B=id` representation

```text
D(C_q(u))=A(q)+u,
A(0)=0, A(1)=1,
D(x)=k*x+c,  k!=1, c!=0.
```

The representation gauge

```text
A'=h*A+p, B'=h*B+q, D'=h*D+p+q
```

preserves the same literal Latin table `C`.  Taking `h=1,p=-c,q=0` gives

```text
A*(x)=A(x)-c,
B*(x)=x,
D*(x)=k*x.
```

Thus the mixed affine constant can be removed from `D` only by leaving the
normalized slice.  The new left role satisfies

```text
A*(1)=A*(0)+1,  A*(0)=-c!=0.
```

Conversely every such unit-step representation returns to the normalized
mixed class by subtracting `A*(0)` from both `A*` and `D*`.  Excluding the
case whose normalized `A` is the identity, this is an exact bijection of

```text
5 slopes * 6 nonzero constants * 119 normalized A = 3570 pairs.
```

A second gauge choice, `h=1,p=0,q=-c`, gives the same `3570` candidates as

```text
A*=A,
B*(x)=x-c,
D*(x)=k*x.
```

This is a three-role representation in which the two right roles are simple:
a nonzero translation and a pure dilation.  It explains precisely which role
absorbs the fixed-point translation.  A direct enumeration verifies that
both transferred descriptions contain exactly `3570` distinct pairs.

## Anchored elimination of `A` and `B`

The normalized isotope equation itself gives

```text
A(q)=D(C_q(0)),
B(u)=D(C_0(u)).
```

Hence `A` and `B` are not independent data.  The full normalized isotope
condition is equivalently the anchored rectangle law

```text
D(C_q(u))=D(C_q(0))+D(C_0(u)),                 (ANCHOR)
D(C_0(0))=0,
D(C_1(0))=1.
```

Because `C` is Latin and `D` is a permutation, the anchored first column and
row automatically define permutation roles `A` and `B`.  In the `AD,B=id`
branch this specializes to the stronger-looking exact cell law

```text
D(C_q(u))=D(C_q(0))+u.                         (AD-ANCHOR)
```

This is a proved algebraic elimination, not a diagnostic assumption.

## Exact bounded computations

The following three common formulas describe the same `3570` mixed-affine
normalized `AD` candidates and impose routing tuples `0,2,6,7`:

```text
normalized A, B=id, mixed-affine D:
UNKNOWN 182.279 s, 1,113,761 conflicts;

normalized A, translated B, pure-dilation D (gauge transfer):
UNKNOWN 180.265 s, 1,659,618 conflicts;

normalized AD with (AD-ANCHOR) encoded directly:
UNKNOWN 180.394 s, 1,133,648 conflicts.
```

No SAT model, UNSAT proof, or counterexample follows.  These are three exact
negative computational boundaries.  Do not repeat them, extend their time
limits, or return to fixed-pair enumeration of the same affine class.

## Consequence and continuation

The affine fixed point does not by itself create enough propagation in the
`T0/T2/T6/T7` core.  The useful surviving result is `(ANCHOR)`: the full
three-role normalized isotope search should eliminate `A,B` and work with
the pair `(C,D)`, not enumerate permutation triples.

The next structural split must be genuinely nonlinear.  Classify `D` by an
exact translation-curvature invariant of the tables

```text
x -> D(x+t)-D(x),  t!=0,
```

starting with the smallest nonconstant profile up to scalar conjugacy.  Couple
that profile directly to `(ANCHOR)` and `T2-ROUTING`.  Do not add another
affine `D` subdivision.

## Reproduction

```text
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --free-systems AD --d-affine-class mixed --seconds 180
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --mixed-ad-transfer --seconds 180
python tools/e677_fiber7_cyclic_p_isotope_t0267_sat.py --anchored-ad-mixed --seconds 180
```

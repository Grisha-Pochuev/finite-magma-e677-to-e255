# E677 counterexample search: uniform-Z and order-11 x=0 boundary

Date: 2026-07-26.

Status:

```text
uniform-Z degree data is too permissive and the canonical order-49 route is
parked; a new exact x=0 row/column law was added to the independent direct
order-11 search, but all three remaining normalized Bad cases stay open
```

## 1. Pure uniform-Z graph boundary

In the uniform profile `(2,2,1,1,1)`, retain only

```text
Z_s(t)=O_t^(-1)(s).
```

The exact Latin-side conditions are:

```text
s -> Z_s(t) is a permutation for every t;
t -> t+Z_s(t) is a permutation for every s;
Z_0(t)!=0;
the seven inverse-permutation columns are distinct;
each row Z_s has two disjoint equal-value pairs.
```

There are exactly

```text
1911 general displacement rows with profile (2,2,1,1,1);
546 such rows with no zero, eligible for s=0.
```

Every seven-row system has fourteen colored matching edges, so its seven
vertex degrees lie in `0..7` and sum to `28`.  There are only `155`
arithmetically possible sorted degree multisets.

The exact graph-only classifier

```text
tools/e677_fiber7_uniform_Z_degree_multiset_classify.py
```

contains no `A,D,rho` variables.  In a fixed 120-second run it constructed
models for at least

```text
131/155
```

degree multisets before reaching `UNKNOWN`.  The run did not complete, so the
remaining `24` classes are not excluded.  More importantly, degrees are far
too permissive to be the missing obstruction.  Do not rerun or lengthen this
classifier merely to finish the list.

This completes the stop audit for the current minimum-curvature canonical-D
order-49 route: support counts, signed collisions, profiles, and uncolored
degrees all fail to give a decisive barrier, while the exact pair formulas
remain UNKNOWN.  The route is parked until a genuinely new invariant is
found.

## 2. A second direct order-11 row/column law

Return to an arbitrary finite E677 magma with a Bad point labelled zero.  Put

```text
s(t)=0*t,
f(y)=y*0,
g(y)=the unique input with y*g(y)=0.
```

Every left translation is a permutation, so `g` is defined.  E677 at `x=0`
is

```text
0 = y*(0*((y*0)*y)).
```

Applying `L_y^(-1)` and then `s^(-1)` gives the exact law

```text
f(y)*y=s^(-1)(g(y)).                           (X0-COUPLING)
```

For `y!=0`, the two inputs `0,y` in row `f(y)` are distinct.  Comparing

```text
f(y)*0=f(f(y)),
f(y)*y=s^(-1)(g(y))
```

gives

```text
f(f(y)) != s^(-1)(g(y)).                       (X0-COLLISION)
```

These are independent in shape from the earlier `Y0-COUPLING`

```text
x*f(s(x))=s^(-1)(x).
```

Both new consequences were added as redundant exact clauses to

```text
tools/e677_direct_order_sat.py --redundant-x0
```

The known Good order-11 control remains SAT and is directly verified on all
`121` E677 pairs.

## 3. Exact bounded direct search

The earlier isomorphism normalization leaves exactly three Bad-zero classes

```text
0*0=1,
1*0=2,
2*0 in {1,2,3}.
```

With both `--redundant-y0` and `--redundant-x0`, separate twenty-second runs
give

```text
2*0=1: UNKNOWN, 252661 conflicts;
2*0=2: UNKNOWN, 247387 conflicts;
2*0=3: UNKNOWN, 243064 conflicts.
```

No counterexample or exclusion follows.  These exact bounded runs are not to
be repeated or lengthened unchanged.

## 4. Structural continuation

Write `R=f o s`.  Comparing `X0-COUPLING` and `Y0-COUPLING` inside the same
left row gives the exact cross equivalence

```text
g(y)=f(y)     iff  y=R(f(y)).                   (XY0-CROSS)
```

It compares in row `f(y)` the cells at inputs `y` and `R(f(y))`; their
outputs are respectively `s^-1(g(y))` and `s^-1(f(y))`.  Row injectivity
proves the equivalence.  The formerly displayed formula

```text
g(s(x))=R(x) iff s(x)=R(R(x))
```

is exactly the same statement after substituting `y=s(x)`, not an
independent second restriction.

The next direct-order pass must exploit the finite functional graphs of
`s,f,g,R` and `XY0-CROSS`, not add another timeout or split a raw table cell.
If this cross system again gives no strict finite descent, leave order 11 and
choose a different construction family.

## 5. Exact functional stop test

The two formerly displayed cross formulas were the same law under
`y=s(x)`.  After correcting that duplication, the exact necessary system was
encoded using only `s,f,g` and the following consequences:

```text
s is a permutation;
s(0)=1, f(0)=1, f(1)=2, f(2) in {1,2,3};
s(s(2))=0;
s(f(x))!=x;
y -> (f(y),g(y)) is injective;
g(y)!=s(f(f(y))) for y!=0;
g(y)=f(y) iff y=(f o s)(f(y));
g(0)=s^-1(0), g(1)=(f o s)(1).
```

The constructive exact-completion script

```text
tools/e677_order11_xy0_functional_sat.py
```

found audited functional witnesses in all three normalized cases, after
respectively `4,1,1` trials.  These are not magma tables, but they prove that
the corrected functional system excludes none of `f(2)=1,2,3`.

Thus `XY0-CROSS` supplies no strict orbit restriction and the direct order-11
route is parked at `0/3` closed cases.  Do not add more local functional
conditions or repeat the twenty-second full-table runs without a new global
invariant.

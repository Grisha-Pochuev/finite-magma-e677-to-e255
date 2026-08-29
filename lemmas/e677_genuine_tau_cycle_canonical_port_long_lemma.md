# E677 genuine tau cycle: canonical-port strict-length lemma

Date: 2026-07-27.

Status:

```text
proved: every state of a genuine all-Bad tau cycle has a distinct canonical
        port state and an exact E677 successor;
proved: if all canonical ports are reused by the same cycle, every row-word
        label occurs at least twice;
proved: equality at exactly two occurrences per label is impossible;
therefore: a closed canonical-port cycle is always strictly PORT-LONG.
```

Work in a finite E677 magma.  Recall

```text
tau(r,u)=(r*u,(r*u)\u).
```

Let `C` be a genuine directed `tau` cycle of length `ell`, all of whose two
coordinates are Bad.  Enumerate its states cyclically as `e_i`.  If `r_i`
is the first coordinate of `e_i`, then the definition of `tau` gives the
standard cyclic word

```text
e_i=(r_i,r_(i+2)),
r_i*r_(i+2)=r_(i+1).                            (1)
```

The word has least period `ell`, since a smaller period would repeat the
ordered states.  It has no equal adjacent letters.  Indeed, if
`r_i=r_(i+1)=a`, then the preceding cell in (1) is

```text
r_(i-1)*a=a,
```

which is a left fixer of the Bad point `a`, impossible by the unique-fixer
lemma.

## The canonical port of a cycle state

For every cycle state put

```text
Phi(e_i)=(r_i,r_i\r_(i+2)).                     (2)
```

This is an actual multiplication state in row `r_i`, with output
`r_(i+2)`.  The states in (2) are pairwise distinct: their `(row,output)`
pairs are the distinct `(row,input)` pairs of the original cycle.

The port never equals its own source state.  Equality would give

```text
r_i\r_(i+2)=r_(i+2),
r_i*r_(i+2)=r_(i+2),
```

so some row would fix the Bad point `r_(i+2)`.

The port also has an exact E677 successor.  The left-division form

```text
q\(p\q)=(p*q)*p
```

with `p=r_i`, `q=r_(i+2)`, together with (1), gives

```text
tau(Phi(e_i))
  =(r_(i+2),r_(i+2)\(r_i\r_(i+2)))
  =(r_(i+2),r_(i+1)*r_i).                       (3)
```

Thus `Phi(C)` is a set of `ell` distinct genuine port states with named
successors.  It is exactly the canonical target map
`eta(a,b)=(a,a\b)` from the external-predecessor one-cell lemma, evaluated
on the ordered pairs of the cycle.

## Closed reuse forces multiplicity at least two

Assume first that every port is reused by the same cycle:

```text
Phi(C)=C.                                       (4)
```

There is then a permutation `F` of the cyclic positions such that

```text
Phi(e_i)=e_(F(i)).                               (5)
```

Comparison of rows and outputs in (1)--(2) gives

```text
r_(F(i))=r_i,
r_(F(i)+1)=r_(i+2).                             (6)
```

Moreover `F(i)!=i`, by the no-fixed-port observation above.  Hence `F`
restricts to a fixed-point-free permutation of the occurrence positions of
each row-word label.  If `m` is the number of distinct labels in the cyclic
word and `mu(a)` is the multiplicity of `a`, then

```text
mu(a)>=2 for every used a,
ell=sum_a mu(a)>=2m.                            (7)
```

## The equality case is impossible

Suppose equality holds in (7).  Every used label then occurs exactly twice,
and `F` is the involution pairing its two occurrence positions.  Let `S` be
the cyclic shift `S(i)=i+1` on the `ell` positions.

The second equation in (6) says that positions `S F(i)` and `S^2(i)` carry
the same label.  They cannot be the same position: otherwise
`F(i)=S(i)`, while the first equation in (6) would give the forbidden
adjacent equality `r_i=r_(i+1)`.  Since every label has exactly two
occurrences, the other occurrence of the label at `S^2(i)` is
`F S^2(i)`.  Therefore

```text
S F=F S^2.                                      (8)
```

As `F^2=id`, equation (8) gives

```text
F S F=S^2.                                      (9)
```

Conjugate permutations have the same order.  But `S` has order `ell`,
whereas `S^2` has order `ell/gcd(ell,2)`.  Equality in (7) makes
`ell=2m` even, so these two orders are different.  This contradiction
excludes equality.

Consequently (4) implies the strict bound

```text
ell>=2m+1.                                      (10)
```

## Exact port alternative

Every genuine all-Bad `tau` cycle therefore has the size-free alternative

```text
Phi(C)\C is nonempty: a distinct actual canonical port state exists;
or
Phi(C)=C: the cycle is strictly PORT-LONG, ell>=2m+1.              (11)
```

In particular, an arbitrary genuine cycle can never close as a
two-occurrences-per-label PORT-MINIMAL word.  This conclusion does not use
the specialized clean `H,D,sigma,A` route and so bridges the applicability
gap left by the older PORT-MINIMAL analysis.

What remains is global rather than local: route the external states in the
first branch, or the extra occurrence in the second branch, to a distinct
EXIT/ZERO/merger charge.  The strict object is now an actual state or an
actual row-word occurrence; it is not an auxiliary permutation cycle.

## Global periodic closure

There is also a useful version in which `Phi` may move states between
different genuine all-Bad `tau` cycles.  Let `P` be the union of all states
lying on such cycles, and let `S=tau|P`.  Suppose first that

```text
Phi(P) is contained in P.                       (12)
```

Since `Phi` is rowwise bijective on the whole state space and `P` is finite,
its restriction `F=Phi|P` is a permutation of `P`.  It preserves the first
coordinate and has no fixed point.  Thus every row label used in `P` occurs
at least twice.

The global equality case in which every used row label occurs exactly twice
is impossible.  In that case `F` is the involution pairing the two states
with a common first coordinate.  If `lambda` denotes first coordinate, the
definitions give

```text
lambda(F e)=lambda(e),
lambda(S F e)=lambda(S^2 e).                    (13)
```

The two states in the second equality cannot be equal: `S F e=S^2 e`
would imply `F e=S e` and hence equal adjacent row labels on an all-Bad
cycle.  Since the common label has exactly two occurrences in `P`, its
other occurrences must agree, and therefore

```text
S F=F S^2,
F S F=S^2.                                      (14)
```

Conjugating twice and using `F^2=id` gives `S=S^4`, so `S^3=id`.  A
one-state all-Bad `tau` cycle is impossible, hence every cycle of `S` has
length three.

Take one such cycle with row word `(a,b,c)`.  Its states are

```text
(a,c), (b,a), (c,b),
```

and `a,b,c` are distinct.  Relations (13)--(14) show that the cycle paired
by `F` has reversed row word `(a,c,b)`.  Consequently the two cycles force

```text
a*c=b, b*a=c, c*b=a,
a*b=c, c*a=b, b*c=a.                            (15)
```

But the left-division form of E677 with `p=a,q=c` now has

```text
c\(a\c)=a,
(a*c)*a=c,
```

where the first equality uses `a*b=c,c*a=b` and the second uses
`a*c=b,b*a=c`.  It forces `a=c`, contradicting distinctness.  Hence (12)
always has a strict global occurrence surplus:

```text
some used Bad row label occurs at least three times in P.          (16)
```

If (12) fails, choose `z in Phi(P)\P`.  If `z` is not an all-Bad state, it
is already a coloured port exit.  If it is all-Bad, inspect its backward
component in the induced all-Bad `tau` graph.  Because `z` is not periodic,
an arbitrarily long backward chain would repeat and create a directed cycle
whose forward orbit leaves that cycle to reach `z`, which is impossible.
Thus the backward component has an actual indegree-zero root.  By the exact
indegree formula this root is one of

```text
product Good:                 a Bad*Bad -> Good crossing;
product Bad, full indegree 0: a genuine ZERO certificate;
product Bad, only Good rows:  a Good-row -> Bad crossing.          (17)
```

Combining (16)--(17), perfect reuse of canonical ports over *all* genuine
all-Bad cycles cannot recreate the old uncharged auxiliary-cycle problem.
It yields a coloured/ZERO root or a strict third occurrence in the actual
periodic state set.  The remaining accounting question is only whether
distinct third occurrences can be absorbed by already counted merger
units.

## The second closure is a branched triangle graph

The strict occurrence in (16) can be retained geometrically rather than as
an anonymous length.  Define two permutations of the full state set by

```text
A_0(r,u)=(r,r*u),
Psi(r,u)=(r*u,r).
```

Here `A_0=Phi^(-1)` and `Psi=J A_0`, where `J(r,u)=(u,r)` is coordinate
swap.  If `Psi(P)` is not contained in `P`, the same finite backward-tree
argument as for `Phi(P)\P` gives a coloured boundary or an actual
indegree-zero root.

It remains to describe the completely closed case

```text
Phi(P)=P,
Psi(P)=P.                                       (18)
```

Since `J=Psi Phi`, the set `P` is then invariant under coordinate swap as
well as under every restricted row successor `A_0`.  For a used Bad label
`a`, put

```text
U_a={u:(a,u) in P}.
```

Equations (18) give

```text
u in U_a iff a in U_u,
L_a(U_a)=U_a.                                   (19)
```

No `a` belongs to `U_a`, because the all-Bad diagonal state `(a,a)` has
internal indegree zero and cannot be periodic.  Also `L_a` has no fixed
point on `U_a`, since `a*u=u` would make the Bad input `u` Good.  Thus (19)
is a finite simple undirected graph on the used labels, with

```text
deg(a)=|U_a|>=2.                                (20)
```

Not all degrees can equal two, by the global equality exclusion above.
The handshaking lemma then sharpens the third-occurrence conclusion to

```text
sum_a (deg(a)-2) >= 2.                          (21)
```

Every edge lies in an actual triangle.  Indeed, for `u in U_a` put
`v=a*u`.  Row invariance gives `v in U_a`.  Since

```text
tau(a,u)=(v,h) in P,
v*h=u,
```

we have `h in U_v`, and row invariance in row `v` gives `u in U_v`.
Therefore `{a,u,v}` is a triangle of (19).  Its vertices are distinct:
`v=u` would fix the Bad point `u`, while `v=a` would put `a` in `U_a`.

Consequently the fully reused CYCLE residue is no longer a bare
permutation cycle.  It is the exact alternative

```text
coloured/ZERO root;
or a finite simple symmetric graph with minimum degree 2,
every edge in a forced multiplication triangle,
and at least two units of branching surplus.    (22)
```

The next invariant must attach the two units in (21) to distinct tau
merger fibres, or show that complete absorption forces a smaller triangle
component.  Merely extending the old PORT-MINIMAL permutation scan cannot
see (19)--(22).

There is a further exact local sharpening.  Every connected component of
the graph in (19) contains a vertex of degree at least four.

Indeed, a connected simple graph of minimum degree two, maximum degree at
most three, and with every edge in a triangle is one of

```text
K3;
K4;
K4 with one edge deleted (the diamond).          (23)
```

To see the classification, start with a triangle.  If one of its vertices
has a third neighbour, the new incident edge must complete a triangle with
one of the two old neighbours.  Those two vertices then have full degree
three.  The remaining two vertices are either adjacent, giving `K4`, or
both have degree two, giving the diamond.  If no vertex has a third
neighbour, the component is `K3`.

All three graphs contradict E677 using only the closed row restrictions.

* On `K3`, every row swaps its two neighbours.  For vertices `a,b,c` this
  forces the six off-diagonal cells in (15), already contradicted there.
* On `K4`, choose a row cycle
  `a*b=c, a*c=d, a*d=b`.  The left-division identity at `p=a,q=b` says

  ```text
  b\d=c*a.                                      (24)
  ```

  The left side belongs to `{a,c}`, because row `b` is a 3-cycle on its
  three neighbours; the right side belongs to `{b,d}`, because row `c` is
  a 3-cycle and cannot fix the input `a`.  The sets are disjoint.
* In the diamond, let `a,b` be the degree-three vertices and `c,d` the two
  degree-two vertices.  Rows `c,d` swap `a,b`.  The left-division identity
  at `(p,q)=(c,a)` and `(d,a)` gives simultaneously

  ```text
  a\b=b*c=b*d,                                  (25)
  ```

  contradicting injectivity of row `b`.

Thus the completely reused alternative (22) actually contains, in every
component, a named row with at least four distinct periodic inputs.  The
next accounting target can be localized to that four-port row instead of
summing an unspecified global LONG surplus.

As a calibration only, exhaustive canonical cyclic-word search found no
single `Phi`-closed word of lengths `3` through `14`; complete bidirected
profiles on four and five labels also had no one-cycle transition.  This is
not used in the proof and is not a size-free exclusion.

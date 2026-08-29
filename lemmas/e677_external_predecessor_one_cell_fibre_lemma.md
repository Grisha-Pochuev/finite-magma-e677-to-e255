# E677 external predecessors: one-cell fibre and genuine companion edge

Date: 2026-07-27.

Status:

```text
proved an exact actual-cell signature for every external tau source;
all repeated signatures inject into the local N-collision surplus;
the canonical representatives have distinct genuine companion tau targets
```

## 1. The one-cell word

Work in any finite E677 magma.  Every left row is a permutation, and the
left-division form of E677 is

```text
q\(p\q)=(p*q)*p.                                (1)
```

For arbitrary `y,a`, put

```text
b=y\a,
v=y*a,
c=a\b.                                         (2)
```

By definition,

```text
y*b=a,
a*c=b.                                         (3)
```

Apply (1) with `p=y,q=a`.  It gives

```text
v*y=(y*a)*y=a\(y\a)=a\b=c.                    (4)
```

Equivalently, direct E677 at `(x,y)=(a,y)` says

```text
a=y*(a*(v*y));
```

comparison with `y*b=a` in the injective row `y` again gives

```text
a*(v*y)=b.                                     (5)
```

Thus the four cells

```text
y*a=v,
y*b=a,
v*y=c,
a*c=b                                          (6)
```

form one exact E677 word.  The last cell is the canonical actual-cell label

```text
a*(a\b)=b.                                     (7)
```

## 2. Genuine companion tau edge

Recall

```text
rho(s,t)=(t,t\s),
tau(y,z)=rho(z,y*z).
```

Since `y*b=a`, (2)--(3) give

```text
tau(y,b)=rho(b,a)=(a,a\b)=(a,c).               (8)
```

This is a genuine tau edge, not a cycle of auxiliary row permutations.  It
is the companion of the original source cell `y*a=v`.

If `a` is Bad, then `b!=a`: equality would give `y*a=a`, a left fixer of
`a`, and the unique-fixer lemma would make `a` Good.  Consequently the two
inputs `a,b` in row `y` are distinct, and row injectivity also gives
`v!=a`.

## 3. Exact fibre count

Attach to a source pair `(y,a)` the signature

```text
kappa(y,a)=(a,y\a)=(a,b).                      (9)
```

For a fixed ordered pair `(a,b)`, its possible sources are exactly

```text
{y:y*b=a}.
```

Hence

```text
|kappa^-1(a,b)|=N(b,a).                        (10)
```

For any finite set `E` of distinct source pairs, let `m(a,b)` be the number
of its sources with signature `(a,b)`.  Then

```text
|E|=|kappa(E)|+sum_(a,b:m(a,b)>0)(m(a,b)-1),   (11)
m(a,b)<=N(b,a).                                (12)
```

Every repeated use of a signature therefore consumes its own distinct unit
of the local collision surplus `N(b,a)-1`.  Different ordered pairs use
disjoint fibres, so these charges cannot reuse a `J/M` or another
`N`-collision unit.

## 4. Distinct canonical targets

Choose one representative source for each occupied signature `(a,b)`.  Its
companion target is

```text
eta(a,b)=(a,a\b).                              (13)
```

The map `eta` is injective.  Indeed, equality of two targets gives the same
first coordinate `a` and the same input `c=a\b`; applying row `a` recovers
the same output `b=a*c`.

Thus after all multiplicities have been charged by (11), the remaining
external-source representatives land at distinct, actual tau states.  This
replaces the former anonymous external-predecessor count by a one-cell
certificate:

```text
repetition  -> a distinct N(b,a)-1 collision unit;
representative -> the distinct genuine state (a,a\b).              (14)
```

## 5. Canonical linkage dichotomy

Let `X` be the selected Bad set and assume `a in X`.  For a canonical
representative, the companion edge is

```text
(y,b) -> (a,a\b)
```

with target `rho(b,a)`.  There are exactly three cases.

### EXIT

If `b` is outside `X`, then the companion target `rho(b,a)` leaves the
selected first-coordinate set.  The support edge `b->a` is real because
`N(b,a)>0` by (10).

### ZERO

Suppose `b in X` but `N(a,y)=0`.  The target `rho(b,a)` is selected, while
the externality criterion applied to its predecessor `(y,b)` says precisely

```text
(y,b) is outside S_X iff a is outside X or N(a,y)=0.
```

Since `a in X`, this is a new ZERO external certificate.

### INTERNAL

Suppose `b in X` and `N(a,y)>0`.  From `b=y\a`,

```text
(y,b)=(y,y\a)=rho(a,y).
```

Thus both endpoints are selected canonical states and (8) becomes the
genuine internal edge

```text
tau(rho(a,y))=rho(b,a).                         (15)
```

This proves the required linkage; no auxiliary permutation cycle is used.

## 6. Finite closed route

Iterate (15) whenever the INTERNAL case occurs.  Every step is an actual
tau edge between support states.  Therefore a finite route has exactly the
following alternatives:

```text
it reaches EXIT;
it reaches a new ZERO certificate;
it remains selected forever and contains a genuine tau cycle.             (16)
```

The multiplicity decomposition (11) ensures that no repeated signature is
used to manufacture this cycle: repetitions have already consumed distinct
`N(b,a)-1` units, and canonical targets are distinct.

This closes the former global external-predecessor linkage obstacle.  The
remaining direct-proof task is the length/port analysis of the genuine tau
cycle in (16), or transfer of EXIT/ZERO to the existing HIT and collision
branches.  Do not return to a selected D-component DAG or to coarse
sign/cycle counts.

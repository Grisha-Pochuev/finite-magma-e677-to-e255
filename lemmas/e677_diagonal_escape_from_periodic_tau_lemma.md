# E677 diagonal escape from the periodic tau graph

Date: 2026-08-22.

Status:

```text
proved: complete Phi/Psi reuse of all genuine all-Bad tau cycles still
        produces a canonical nonperiodic all-Bad state or a coloured cell;
therefore: every genuine all-Bad tau cycle has a coloured boundary or an
           actual ZERO root;
consequence: the K5 port core and all its local block gluings are not a
             terminal CYCLE obstruction once diagonal cells are restored.
```

## Setup

Work in a finite E677 magma.  Every left row is a permutation.  Let `P` be
the union of all states on genuine all-Bad `tau` cycles, where

```text
tau(r,u)=(r*u,(r*u)\u).
```

The canonical-port lemma already handles either failed closure

```text
Phi(P) not contained in P  or  Psi(P) not contained in P:          (1)
```

an all-Bad state outside `P` has a finite backward tree and hence a coloured
boundary or a genuine indegree-zero root.  It remains only to treat

```text
Phi(P)=P,  Psi(P)=P.                                                (2)
```

Under (2), `A0=Phi^{-1}` and coordinate swap `J=Psi Phi` both preserve
`P`.  For every used Bad label `a`, put

```text
U_a={u:(a,u) in P}.
```

Then

```text
a notin U_a,
L_a(U_a)=U_a,
u in U_a iff a in U_u.                                             (3)
```

## The diagonal word

Fix a used label `a` and set

```text
d=a*a,
h=d*a=((a*a)*a).
```

The self-instance of E677 is

```text
a=a*(a*h),
```

or equivalently

```text
L_a^2(h)=a.                                                        (4)
```

It follows at once from (3)--(4) that

```text
h notin U_a.                                                       (5)
```

Indeed, membership of `h` in `U_a` would put `L_a^2(h)=a` in `U_a`,
contrary to (3).  Notice that this uses the missing diagonal cell and is
invisible in the closed periodic-port graph.

Now use the actual cell

```text
h*a=D(a)
```

in the one-cell predecessor lemma.  Put

```text
b=h\a,
c=a\b.
```

The exact four-cell E677 word is

```text
h*a=D(a),
h*b=a,
D(a)*h=c,
a*c=b,                                                            (6)
```

and in particular

```text
tau(h,b)=(a,c).                                                    (7)
```

## The source state cannot be periodic

If either coordinate of `(h,b)` is Good, (6) is already a coloured
certificate.  Suppose both are Bad and assume for contradiction that

```text
(h,b) in P.
```

Since `A0` preserves `P`, the second cell in (6) gives

```text
A0(h,b)=(h,h*b)=(h,a) in P.
```

Coordinate-swap invariance then gives `(a,h) in P`, or `h in U_a`.  This
contradicts (5).  Therefore

```text
(h,b) is an all-Bad nonperiodic state.                             (8)
```

The backward component of a nonperiodic state in a finite functional graph
has finite depth: an arbitrarily long backward path would repeat a state,
creating a directed cycle whose forward orbit could not later leave that
cycle to reach (8).  Hence the all-Bad backward component of `(h,b)` has an
actual root.  The exact indegree classification from the canonical-port
lemma makes that root one of

```text
Bad*Bad -> Good;
Good-row -> Bad;
genuine all-Bad ZERO.                                              (9)
```

Thus (2) also yields a coloured boundary or ZERO.  Together with (1), this
proves the unconditional alternative

```text
nonempty P  ->  coloured boundary or genuine ZERO root.           (10)
```

## Consequence for the former K5 obstruction

The off-diagonal K5 cores and their vertex gluings live entirely in `P`.
They appeared terminal only because their diagonal states were omitted.
For each used vertex, (4)--(8) constructs a state outside the periodic
part, so no such core is terminal in a full E677 magma.  No enumeration of
larger K5 block trees or higher graph degree is needed.

This lemma closes the periodic-reuse obstacle only.  The remaining direct
proof task is to send the three root types in (9) through the HIT/ZERO
descent without reusing a collision charge.

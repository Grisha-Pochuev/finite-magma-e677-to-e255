# E677 defect-graph reverse lift and coloured HIT block

Date: 2026-07-21.

Status:

```text
proved whole-cycle reverse-lift trichotomy;
proved carrier-coloured pairing of canonical HIT exits with full bad blocks;
strict descent from the first fork is still open
```

Put

```text
sigma(x)=((x*x)*x),
D(x)=sigma(x)*x,
H(x)=D(x)\x.
```

Thus `H(x)` is the input of the reverse companion of the canonical `D`
edge. If `r=sigma(x)` and `z=D(x)`, companion factorization gives

```text
z*H(x)=x,
H(x)=(r*z)*r.                                   (1)
```

The point of `H` is that it compares the reverse companion with the
canonical edge at its new input, rather than extending the page at `x`
locally.

## The aligned / collision / fork trichotomy

At the common input `q=H(x)` there are always the two cells

```text
row D(x):        q -> x,                         (2)
row sigma(q):    q -> D(q).                      (3)
```

Exactly one of the following occurs.

```text
ALIGNED:    sigma(q)=D(x).
COLLISION:  sigma(q)!=D(x), but D(q)=x.
FORK:       D(q)!=x.
```

In the aligned case, (1) immediately gives

```text
D(H(x))=x.                                      (4)
```

In the collision case, (2)--(3) have distinct row labels and the same input
and output. Since `x=D(q)`, this is a collision at the canonical cell of
`q`:

```text
N(q,D(q))>=2,
c_D(q)>=1.                                      (5)
```

Different collision cases charge different ordered cells `(q,D(q))`: if
`H(x)=H(y)=q` and both are collision cases, then `x=D(q)=y`. Hence for every
set `X` of vertices,

```text
|{x in X : x is a COLLISION case}|
    <= sum_q c_D(q).                            (6)
```

The right side may be restricted to the distinct charged values `q=H(x)`.
The fork case is the exact remaining obstruction: the reverse edge `q -> x`
is then a genuinely off-canonical occupied support cell next to the
canonical edge `q -> D(q)`.

This trichotomy uses the carrier label. Merely asking whether the underlying
reverse edge is also a `D` edge would merge ALIGNED and COLLISION and would
lose the charge (5).

## Global fork-free and deepest-tail consequences

If there are no FORK points anywhere, then (2)--(3) give

```text
D(H(x))=x for every x.                          (7)
```

Thus `D` is surjective and hence, on the finite set `M`, a permutation with
inverse `H`. If there are also no COLLISION points, every point is aligned;
putting `x=D(y)` in `sigma(H(x))=D(x)` gives the global identity

```text
sigma(y)=D^2(y).                                (8)
```

There is also a useful local forcing statement. In a functional component
of `D`, let `depth(v)` be the distance from `v` to its directed cycle. If
the component has a tail, choose `x` of maximum positive depth and put
`q=H(x)`. The ALIGNED and COLLISION cases would both give `D(q)=x`, placing
`q` in the same component at depth `depth(x)+1`. This contradicts maximality.
Therefore

```text
every D-component with a tail has a FORK at each maximum-depth point.  (9)
```

Cross-component forks have an exact row-balance charge. For a `D`-component
`Gamma`, put

```text
I_Gamma=|{(r,u): r in Gamma, u outside Gamma, r*u in Gamma}|,
O_Gamma=|{(r,u): r in Gamma, u in Gamma, r*u outside Gamma}|.
```

Every row `L_r` is a permutation, so its crossings into and out of `Gamma`
balance. Summing over `r in Gamma` gives

```text
I_Gamma=O_Gamma.                                (10)
```

If `x in Gamma` and `H(x)` is outside `Gamma`, the reverse cell

```text
row D(x): H(x) -> x
```

is a distinct contribution to `I_Gamma`, because `D(x)` and `x` both lie in
`Gamma`. Hence

```text
|{x in Gamma : H(x) outside Gamma}| <= I_Gamma=O_Gamma.               (11)
```

Thus every cross-component reverse fork is charged to an exit cell

```text
r*u=v,  with r,u in Gamma and v outside Gamma.  (12)
```

For a component whose cycle is nontrivial and bad, all its vertices are bad,
so an exit (12) landing in `Good` is immediately a `Bad*Bad -> Good` witness.
The uncharged fork boundary is now precise: it consists of internal forks,
plus cross-component forks whose balanced exit still lands at a bad point.

## Whole-cycle reverse lift

Let `C` be a directed `D`-cycle. Starting with all points of `C`, close
backwards under `H`:

```text
S = union_(j>=0) H^j(C).                       (13)
```

There is an exact finite dichotomy.

1. Some point of `S` is the first non-aligned point. At that point the
   entire simultaneous lift of the cycle reaches either the charged
   collision (5) or the carrier fork (2)--(3).
2. Every point of `S` is aligned. Then

   ```text
   S=C,
   H|C=D^(-1)|C,
   sigma|C=D^2|C.                              (14)
   ```

For the proof of the second branch, alignment gives `D H=id` on `S` by
(4). Hence `H` is injective on the finite `H`-closed set `S`, so it is a
permutation of `S` and `D=H^(-1)` there. The inverse of `D` preserves the
original `D`-cycle `C`; therefore `H(C)=C` and (13) gives `S=C`. Finally,
`sigma(H(x))=D(x)` and `H=D^(-1)` give `sigma=D^2` after reindexing.

Thus an indefinitely clean reverse lift is not an unstructured tower. It
collapses to the rigid common-carrier cycle (14). On a cycle of length `m`,
`sigma=D^2` gives one sigma cycle of length `m` when `m` is odd, and two
sigma cycles of length `m/2` when `m` is even. Under `Good=empty`, `m=2`
is impossible because it would make `sigma` fix both cycle points. The
remaining aligned branch can therefore be handed back to the simultaneous
sigma-page reduction with an exact length relation.

## Carrier-coloured accounting of a canonical HIT edge

Now let

```text
x in Bad,
z=D(x) in Good,
r=sigma(x).
```

In the permutation cycle of `L_r`, take the complete maximal bad block ending
at the canonical exit `x -> z`:

```text
row r:  g Good -> b_0 -> b_1 -> ... -> b_(ell-1)=x -> z Good.         (15)
```

Here `ell>=1`. Put

```text
u=r*b_0,
q=u*r.                                          (16)
```

Thus `u=b_1` if `ell>=2`, while `u=z` if `ell=1`. Companion transport of
the entry edge `r*g=b_0`, using `r*b_0=u`, gives the exact other end of the
whole block:

```text
b_0*q=g.                                        (17)
```

Companion transport of the exit is the already known reverse cell

```text
z*((r*z)*r)=x.                                  (18)
```

Canonical HIT exits in a fixed row lie on different maximal bad blocks, so
the assignment from an exit to its entry edge in (15) is injective. It is
also carrier-coloured: the row label `r` is unchanged. The good entry `g`
is necessarily unmarked in row `r`, because `sigma(g)=r` would make the
canonical edge of the good point `g` equal to `r*g=b_0!=g`.

Equation (17) gives the following exact colour split.

```text
q in Bad   => b_0*q=g is a Bad*Bad -> Good witness;
q in Good  => the entry hinge itself is Good.                         (19)
```

If additionally `r` is bad and `ell>=2`, then `u=b_1` is bad. In the
second line of (19), (16) is itself the Bad*Bad -> Good witness

```text
b_1*r=q.                                        (20)
```

Consequently a canonical HIT block can avoid exposing a Bad*Bad -> Good
cell at its entry only in the narrow residual situation

```text
q is Good, and either r is Good or ell=1.        (21)
```

In particular, if closure (C) is assumed, every canonical Bad -> Good HIT
has a good carrier `r`, and its paired entry hinge `q` is also good.

## Exact continuation point

The CYCLE branch is now reduced to one of two named objects:

```text
- a first carrier fork, whose off-canonical edge must be charged to u_D;
- an aligned cycle with sigma=D^2, already coupled to the sigma-cycle pages.
```

The HIT branch is reduced to the residual good-carrier/good-hinge block
(21). The next useful invariant must compare the first fork orbit or these
residual blocks globally. Repeating the local two-cell trichotomy does not
by itself give a strict descent.

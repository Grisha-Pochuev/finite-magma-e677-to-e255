# E677 square-band word surplus and clean-absorption exclusion

Date: 2026-07-23.

Status:

```text
proved: every rank-three top zero path in the final DIRECT/MINIMAL HIT core
        forces a genuine extra top vertex in its own reserved source block;
proved: ranks above three and rank three therefore give a pointwise word
        surplus of at least one unit per selected top anchor;
proved: the square state has a unique E677 predecessor and its complete
        backward ancestry is a lower-depth bridge, a rootless all-Bad tau
        cycle, or an actual top zero path;
proved: the completely clean rank-three absorption of all square states by
        distinct top zero paths is impossible by one row-cancellation
        collision;
reduced: the final HIT core has no zero-length square/kappa remainder; only
         named RETURN/boundary defects, a genuine word-LONG unit, or the
         existing lower-bridge/CYCLE handoff remains
```

Assume the fully aligned HIT equality core and the final DIRECT/MINIMAL
returned-root remainder of

```text
e677_returned_root_matching_and_minimal_direct_rank_boundary.md.
```

Thus `T` is the global maximum Bad `D`-depth layer, the maximum depth is at
least two, `T_S` is a nonempty clean terminal anchor component, and

```text
Pi in Sym(T_S),
Pi(t)=r_t,
n_t>=3.                                         (1)
```

Here `n_t` is the `tau` distance from the diagonal zero source of `t` to its
reserved terminal entry.  Put

```text
s_t=t*t,
k_t=kappa(t)=t*sigma(t),
j_t=(k_t*sigma(t))*k_t.                         (2)
```

The beginning of the zero path is

```text
(t,k_t) -> (t,sigma(t)) ->
(k_t,s_t) -> (sigma(t),j_t),                    (3)
```

and `k_t,s_t,sigma(t)` all belong to `T`.

## Rank three forces source-block length

Retain the closed zero-block matching

```text
P in Sym(T),
sigma(T) subset T.                              (4)
```

The reserved zero path rooted at `t` ends in a top row

```text
r_t=sigma(P(t)).                                (5)
```

In the returned-root core the same row is `Pi(t)`, so

```text
Pi(t)=sigma(P(t)).                              (6)
```

Suppose `n_t=3`.  Then (3) itself ends at the reserved entry and the
rank-three conclusion of the returned-root lemma gives

```text
r_t=sigma(t),
g_t=j_t in Good,
b_t=s_t.                                       (7)
```

The DIRECT Q_GOOD_LONG transition has the exact cells

```text
r_t*g_t=s_t,
c_t=r_t*s_t in T,
q_t=c_t*r_t in Good.                            (8)
```

The reserved maximal top block in row `r_t=sigma(P(t))` begins with

```text
g_t Good -> s_t -> c_t -> ...
```

and ends at the top input `P(t)` before its canonical exit.  It cannot have

```text
c_t=P(t).                                      (9)
```

Indeed (5), (7), and (9) would turn the last cell in (8) into

```text
q_t=P(t)*sigma(P(t))=kappa(P(t)).               (10)
```

But `P(t)` has maximum Bad depth at least two.  Hence `P(t)*P(t)` and
`sigma(P(t))` are Bad: otherwise two successive uses of
`Good*Bad subset Good` would make `D(P(t))` Good.  The companion cell

```text
kappa(P(t))*(P(t)*P(t))=sigma(P(t))             (11)
```

then shows that `kappa(P(t))` is Bad as well.  This contradicts the Good
colour of `q_t` in (8).

Consequently `c_t` is a strict internal top vertex before `P(t)`.  In
particular every rank-three path forces one genuine source-block TOP-LONG
unit which was not used by the terminal zero entry or by the returned target
bridge.

For `n_t>3`, the zero path itself contains at least one state beyond the
rank-three baseline.  If `ell_t` denotes the number of strict internal
top-block vertices beyond the minimal first-successor/end placement, then
pointwise

```text
(n_t-3)+ell_t >= 1  for every t in T_S.         (12)
```

The zero-path witnesses for `n_t>3` are distinct because the zero paths are
disjoint.  The source-block witnesses for `n_t=3` are distinct because the
reserved maximal blocks are distinct.  If a witness from the two families
coincides, this is a literal zero-path/block RETURN, already one of the
named word-intersection defects.  Otherwise (12) gives at least `|T_S|`
distinct unused word-LONG units.  Thus the final core is never simultaneously
rank-minimal and source-block-minimal.

## The unique predecessor of every square state

For `t in T_S` put

```text
E_t=(s_t,t),
s_t*t=sigma(t).                                (13)
```

The Bad points `s_t` and `sigma(t)` are distinct by the proved right-orbit
lemma.  The equality core has exactly one source at every off-diagonal
Bad/Bad input-target pair.  Since a Good row cannot map the Bad input
`sigma(t)` to the Bad target `s_t`, there is a unique Bad point `a_t` with

```text
a_t*sigma(t)=s_t.                               (14)
```

The companion of (14) gives

```text
s_t*((a_t*s_t)*a_t)=sigma(t).                   (15)
```

Comparison with (13) in the permutation row `s_t` yields

```text
(a_t*s_t)*a_t=t.                               (16)
```

Equations (14)--(16) say exactly

```text
tau(a_t,sigma(t))=E_t.                          (17)
```

This is the unique predecessor of `E_t`.  Continue backwards.  For any
all-top state `(r,u)` with Bad output `v`, its predecessor count is
`N(v,r)`: it is zero when `v=r`, and exactly one when `v!=r`.  In the first
case the state is the diagonal zero source `(r,kappa(r))`.  In the second
case the unique source row is Bad.  Therefore finite backward ancestry has
the exhaustive trichotomy

```text
LOWER-ROOT:
    the first predecessor row outside T is a literal lower-Bad-to-top
    supported bridge;

TOP-ROOT:
    E_t lies on the actual merger-free zero path of one top root;

ROOTLESS:
    the all-top backward orbit closes to a genuine all-Bad tau cycle.
                                                            (18)
```

The ROOTLESS case is precisely the existing CYCLE U-polygon.  Its lengths
one through three are impossible; length four has the four proved square
exits and returns; lengths at least five remain the named CYCLE branch.

After removing LOWER-ROOT and ROOTLESS, label every `E_t` by the top zero
root of the path which contains it.  Let `E_square` count labels outside
`T_S`, let `K_square` be the repeated-root surplus among labels in `T_S`,
and let `U_square` count roots of `T_S` not used by an internal label.  There
are `|T_S|-E_square` internal labels, so the elementary fibre count gives

```text
U_square=E_square+K_square.                     (19)
```

Thus an outside square root or two square states on one top zero path forces
an actual unhit top root.  The sole boundary-free, collision-free case is a
bijection between the square states and the top zero paths of `T_S`.  No new
abstract renewal map is needed: only these actual root labels are retained.

## No completely clean rank-three absorption

It remains to check that TOP-ROOT in (18) does not create another clean
permutation remainder at the rank-three boundary.  Suppose all square states
`E_t`, `t in T_S`, are absorbed by top zero paths rooted in `T_S`, no two use
the same root, no member of `T_S` is unhit, and every involved zero path has
rank exactly three.  This is the only boundary-free, collision-free
absorption matching.

For a top root `y`, its first four states are

```text
Z_0(y)=(y,kappa(y)),
Z_1(y)=(y,sigma(y)),
Z_2(y)=(kappa(y),s_y),
Z_3(y)=(sigma(y),j_y).                          (20)
```

The square state `E_t=(s_t,t)` cannot be `Z_0(y)`: equality of the state and
its output would give `s_t=sigma(t)`.  It cannot be `Z_3(y)`, whose input is
Good at rank three, while `t` is Bad.

Nor can it be `Z_2(y)`.  Rank three gives

```text
Pi(x)=sigma(x)  for every x in T_S,              (21)
```

so `sigma` is a permutation of `T_S`.  Equality `E_t=Z_2(y)` gives
`sigma(y)=sigma(t)` and `s_y=t`; hence `y=t` and `s_t=t`, making `t`
idempotent.

Thus every clean absorption must occur at rank one:

```text
E_t=Z_1(y),
y=s_t,
sigma(y)=t.                                    (22)
```

Because the root matching is a bijection of `T_S`, (22) says on this set

```text
s=sigma^(-1).                                  (23)
```

Now use only the self-band identities.  For `x in T_S`, apply
`s(z)*z=sigma(z)` at `z=sigma(x)`.  Equation (23) gives

```text
x*sigma(x)=sigma^2(x),
kappa(x)=sigma^2(x).                            (24)
```

Next apply `kappa(z)*s(z)=sigma(z)` at `z=sigma^(-2)(x)`.  Equations
(23)--(24) give

```text
x*sigma^(-3)(x)=sigma^(-1)(x).                  (25)
```

But the square cell is

```text
x*x=sigma^(-1)(x).                              (26)
```

Left cancellation in row `x` yields `sigma^(-3)(x)=x`.  Hence
`kappa(x)=sigma^2(x)=sigma^(-1)(x)=s(x)`.  Comparing

```text
x*sigma(x)=kappa(x),
x*x=s(x)
```

in the same permutation row gives `sigma(x)=x`, and then (23) gives
`s(x)=x`.  This makes `x` Good, a contradiction.

Therefore the clean rank-three TOP-ROOT matching does not exist.

## Exact continuation boundary

The simultaneous square/kappa band no longer has a zero-charge remainder.
For the final DIRECT/MINIMAL component, at least one of the following is
present, with its actual cell or word segment retained:

```text
SQUARE-BOUNDARY: a square ancestry root leaves T_S;
SQUARE-DEFECT:   two square states use one zero root, or one root is unhit;
LOWER-ROOT:      a lower-depth supported bridge;
ROOTLESS:        the existing all-Bad CYCLE tau polygon;
ZERO-RANK-LONG:  n_t>3;
SOURCE-TOP-LONG: n_t=3 and the reserved source block has c_t!=P(t);
WORD-RETURN:     a chosen zero-path and source-block surplus state coincide.
```

The decisive point is (12): every selected top anchor contributes a real
word-length unit before any new quotient is formed.  The next invariant must
sum these units together with CYCLE PORT-LONG in one actual-word potential.
Do not introduce another renewal permutation and do not extend the order-11
PORT-MINIMAL scan.

# E677 Good-row bad-block renewal and Bad-target collision handoff

Date: 2026-07-22.

Status:

```text
proved common-hinge colour handoff for every Good-input/Bad-target collision;
proved a global partial renewal on all Good-row Good-to-Bad crossings;
proved its exact terminal/collision/unhit conservation law;
reduced the clean remainder to two transition types on marked renewal cycles
```

Let

```text
G={x:D(x)=x},  B=M\G,
N(u,v)=|{r:r*u=v}|.
```

Use the two coloured crossing sets

```text
C={(y,x,z): y,x in B, z in G, y*x=z},
E={(r,g,b): r,g in G, b in B, r*g=b}.            (1)
```

The set `C` is the Bad-row crossing set used by the coloured bad-block
renewal lemma.  The set `E` records the complementary crossings carried by
Good rows.

## The common page of a Bad-target collision

Fix `u in G`, `b in B`, and suppose

```text
F={r:r*u=b},  |F|=N(u,b)>=2.                     (2)
```

For every `r in F` put

```text
a_r=r*b,
alpha_r=u*(b*r),
h=b\u.
```

The common-edge fan and companion identities give

```text
r*alpha_r=u,
r*u=b,
r*b=a_r,
a_r*r=h,
b*h=u.                                          (3)
```

Both families `r -> alpha_r` and `r -> a_r` are injective on `F`.  In
particular all collision arms have distinct backward feet and forward tips,
but the same return hinge `h`.

The colours in (3) give an exact first handoff.

* If `h in B`, then

  ```text
  (b,h,u) in C.                                  (4)
  ```

  All `|F|` source cells `r*u=b` have this same companion cell, so the
  original multiplicity is retained as marked ancestry of (4).

* Suppose `h in G` and `r in F cap B`.  If `a_r in G`, then

  ```text
  (r,b,a_r) in C;
  ```

  while if `a_r in B`, then

  ```text
  (a_r,r,h) in C.                                (5)
  ```

Consequently, if the collision page produces no `C` certificate, then

```text
h in G and F subset G.                           (6)
```

In that residual case all `|F|` cells

```text
(r,u,b),  r in F,
```

are distinct members of `E` with the same marked input/output pair `(u,b)`.
Thus a Good-input/Bad-target collision cannot disappear into unrelated
colour bookkeeping: it either reaches `C` immediately or starts at least two
marked strands in the one global system below.

## Maximal Bad blocks in Good rows

Every `c=(r,g,b) in E` starts a unique complete maximal Bad block in the
cycle of the permutation `L_r`:

```text
row r: g Good -> b=b_0 -> ... -> x Bad -> z Good. (7)
```

Put

```text
h=(r*b)*r=b\g,
w=r*z,
q=w*r.                                           (8)
```

Companion factorization at the entry and exit gives

```text
b*h=g,
z*q=x.                                           (9)
```

If `h in B`, the first cell in (9) is the terminal crossing

```text
(b,h,g) in C.                                    (10)
```

Assume henceforth that `h in G`.  There are three exhaustive cases after
the exit of (7).

```text
A: q in G.
   Then (z,q,x) in E.

B: q in B and w in G.
   Then (w,r,q) in E.

T: q in B and w in B.
   Then w*r=q is a Good-input/Bad-output crossing in the Bad row w.  In the
   L_w cycle it starts a unique maximal Bad block, whose exit belongs to C.
                                                        (11)
```

Define the partial Good-row renewal

```text
R_G:E -> E                                         (12)
```

by the displayed crossing in case A or B.  It is undefined exactly on the
terminal occurrences (10) and T.  Every terminal retains its originating
member of `E` as a mark.  Different marks may reach the same actual `C`
cell; that coincidence is a terminal multiplicity and is not silently
treated as an injection.

The two nonterminal transitions have concrete meanings:

```text
A is the tau-companion z*q=x of the old block exit r*x=z;
B is the factor cell w*r=q, where r*z=w.           (13)
```

Thus the clean remainder has only these two transition types.  There is no
third anonymous Good-carrier/Good-hinge case.

## Exact conservation

Let

```text
T = number of terminal occurrences of (10) or T in (11),
I = number of distinct members of E hit by R_G,
K = sum_(e in image R_G)(|R_G^(-1)(e)|-1),
U = number of members of E with no R_G-predecessor.      (14)
```

The defined part of `R_G` has `|E|-T` elements counted with multiplicity, so

```text
|E|-T=I+K.
```

Since `U=|E|-I`,

```text
U=T+K.                                            (15)
```

Therefore the forward orbit of every marked strand from (2) either reaches a
terminal or eventually reaches an `R_G` cycle.  If two distinct marked
ancestries first coalesce, their common image is counted by `K`.  Equivalently
the marked network has only the following finite events:

```text
1. a terminal C crossing;
2. a first merger counted by K;
3. an eventual directed R_G-cycle made only of A/B transitions.  (16)
```

If `T=K=0` globally, `R_G` is a permutation of `E`.  A collision (2) then
places its at least two distinct marks on clean `R_G` cycles.  They may lie
on different cycles, or at different positions of one cycle, but they keep
the same original pair `(u,b)`.  This is the exact charge-free remainder to
compare with the Bad-row renewal and the unique fixer of the Good input `u`.

## Local-shortcut boundary

The named bounded ground diagnostic

```text
tools\node.cmd tools\e677_good_input_bad_target_collision_saturation.js 7 10 180000
```

stabilizes after `5` rounds with `83948` terms.  From

```text
D(u)=u,  r*u=b=s*u
```

it proves the common hinge

```text
(r*b)*r=(s*b)*s,
```

but proves neither `D(b)=b` nor `r=s`.  This is only a negative boundary for
the short equational route; it is not a partial model or a counterexample.
Do not deepen the saturation.

## Continuation boundary

Do not iterate an isolated Good-input/Bad-target collision again.  The next
object is simultaneous:

```text
the Bad-row renewal on C
+ the Good-row A/B renewal on E
+ the at-least-two marked E positions sharing one pair (u,b).       (17)
```

At an A transition the next crossing is the actual `tau` companion of the
old exit.  At a B transition the old Good carrier becomes the next Good
input.  These are precisely the two places where the canonical unique-fixer
cell of that Good point must be inserted.  The required next result is
either a merger/terminal charge without reuse, or a closed marked coloured
cycle whose repeated Good input can be compared directly with the absent
fixer of its neighbouring Bad output.

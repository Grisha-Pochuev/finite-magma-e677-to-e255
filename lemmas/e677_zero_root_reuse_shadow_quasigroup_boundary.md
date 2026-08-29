# E677 ZERO-root reuse: shadow quasigroup and first-fork boundary

Date: 2026-08-29.

Status:

```text
proved: exact Omega-root equality forces a Latin idempotent E677 shadow on
        the Bad set;
proved: if there is no HIT, every Bad square is a canonical SHORT block;
proved: every canonical Bad D-cell then has one Bad and one Good carrier,
        and its companion is either a pure zipper equality or a Good-row
        Good-to-Bad crossing;
checked exactly: the smallest two-layer K5 realization, order 10, is UNSAT;
checked exactly: the equivariant pure-zipper K5 shell, order 15, is UNSAT;
open:   the simultaneous network of the forced Good-row crossings is not yet
        proved to decrease D-depth/cycle length or produce HIT;
therefore: the proposed two-outcome statement is neither proved nor refuted;
           its exact remaining obstruction is now a mixed Good-row network.
```

This does not give a complete counterexample and therefore refutes neither
the proposed root-reuse statement nor the full implication E677 -> E255.  It
does prove that a local root-count argument cannot establish the statement,
and identifies the additional mixed equations that a complete proof needs.

## Auditable dependencies

Only the following earlier proved statements are used.

- `lemmas/e677_bad_square_tau_subgraph_root_merger_cycle_lemma.md`: the `B x B`
  root reserve, its exact indegree formula, and off-diagonal Bad closure at
  equality.
- `lemmas/e677_omega_root_equality_forces_all_bad_points_hit_lemma.md`: only the
  deductions `kappa(B) subset G` and `sigma(B) subset G`; the later auxiliary
  assumption `Good*Bad subset Good` from that file is **not** used here.
- `lemmas/e677_square_band_word_surplus_and_clean_absorption_exclusion_lemma.md`:
  the displayed self-band cells.
- `lemmas/e677_defect_graph_reverse_lift_and_hit_block_lemma.md`: companion
  factorization and the ALIGNED/COLLISION/FORK reverse-lift trichotomy.
- `lemmas/e677_coloured_bad_block_renewal_lemma.md` and
  `lemmas/e677_good_row_bad_block_renewal_and_bad_target_collision_handoff.md`: the
  SHORT terminology and the simultaneous coloured renewal target.
- `lemmas/e677_K5_periodic_block_gluing_and_completion_boundary.md`: the exact K5
  shadow used only in the bounded completion audits.

All other deductions below are given explicitly in this file.

## Terminal equality assumptions

Let

```text
B=Bad, G=Good, b=|B|,
Omega=B x B.
```

Assume the exact root equality

```text
Z_Omega=b,                                                        (1)
```

so the square states `delta_x=(x,x)`, `x in B`, are all the internal
indegree-zero states.  Assume also the no-HIT residue

```text
D(B) contained in B.                                             (2)
```

The proved Omega-root equality lemma supplies

```text
r,u in B, r!=u  =>  r*u in B,                                   (3)
kappa(x)=x\x in G,
sigma(x)=(x*x)*x in G.                                           (4)
```

Put `s(x)=x*x`.  Then in fact

```text
s(x) in G for every x in B.                                     (5)
```

Indeed, if `s(x)` were Bad, then `s(x)!=x` and the off-diagonal Bad
closure (3) would make `s(x)*x` Bad.  But this product is `sigma(x)`, which
is Good by (4).

Thus every Bad point has the exact colour band

```text
x*x=s(x) in G,
s(x)*x=sigma(x) in G,
x*sigma(x)=kappa(x) in G,
x*kappa(x)=x in B,
sigma(x)*x=D(x) in B.                                            (6)
```

The first four cells are the self-band consequences of E677; the last cell
is the definition of `D` together with (2).

## Every Bad row exchanges exactly one colour

Fix `r in B`.  On Bad inputs, (3) and (5) say

```text
r*r is Good,
r*u is Bad for every u in B\{r}.                                 (7)
```

The cell `r*kappa(r)=r` has Good input and Bad output.  Since `L_r` is a
permutation, the number of `B -> G` crossings equals the number of
`G -> B` crossings.  Equation (7) gives exactly one of the first kind, so
`kappa(r) -> r` is the unique crossing of the second kind.  Consequently

```text
L_r maps B\{r} bijectively to B\{r},                             (8)
L_r maps G\{kappa(r)} bijectively to G\{s(r)}.                    (9)
```

In particular, the maximal Bad block in row `r` which begins at the known
entry `kappa(r) -> r` has length one:

```text
kappa(r) Good -> r Bad -> s(r) Good.                             (10)
```

It is exactly the SHORT block of the coloured renewal lemma, with return
hinge `sigma(r)`.

## Exact Latin multiplicities on Bad

Let `u,v` be distinct Bad points.  The left-division input

```text
w=v\u,
v*w=u,                                                           (11)
```

must be Bad.  Otherwise (11) would be a `G -> B` crossing in the Bad row
`v`; by uniqueness in (9) it would have to be `kappa(v) -> v`, forcing
`u=v`.

Hence `rho(u,v)=(v,w)` is an all-Bad state.  It is not a square state:
`w=v` would give `u=v*v=s(v)` Good.  By root equality (1), its internal
indegree is positive.  The exact tau-indegree formula therefore gives

```text
N_B(u,v)>=1 for u!=v.                                             (12)
```

For fixed `u`, exactly the `b-1` Bad rows other than `u` send `u` to a Bad
output, while `u*u` is Good.  Also `N_B(u,u)=0`, because a source would fix
the Bad input `u`.  Summing (12) over the `b-1` possible targets gives

```text
N_B(u,v)=1 for all distinct u,v in B.                            (13)
```

## The Bad shadow is itself an E677 quasigroup

Define an operation `o` on `B` by

```text
r o u = r*u  when r!=u,
r o r = r.                                                       (14)
```

Equations (8) and (13) show that every row and every column of (14) is a
permutation.  Thus `(B,o)` is an idempotent quasigroup.

It also satisfies E677.  The diagonal instance is immediate from
idempotence.  For distinct `x,y`, the original E677 word cannot use a
diagonal or a Good intermediate:

```text
a=y*x,
p=a*y,
q=x*p,
y*q=x.                                                           (15)
```

Closure (3) gives Bad intermediates whenever the two inputs are distinct.
The equality `a=x` would fix the Bad input `x`, while (8) directly gives
`a!=y`; hence `p` is Bad.  If `p=x`, then `q=x*x=s(x)` is Good, and the last
cell `y*q=x` is a `G -> B` crossing in the Bad row `y`.  Its unique such
crossing has output `y`, contradicting `x!=y`.  Thus `p!=x` and `q` is Bad.
Finally `q!=y`, because otherwise the last product would be the Good square
`y*y`.  Therefore every cell in (15) is off-diagonal and agrees with (14).
The original E677 equality proves the shadow equality.

Thus perfect ZERO-root reuse is not an anonymous functional-graph equality:

```text
root equality + no HIT
    => an idempotent Latin E677 shadow on B
       coupled to G by the SHORT bands (6).                       (16)
```

## Every canonical D-cell is a mixed collision

Fix `q in B` and put

```text
e=D(q) in B,
t=sigma(q) in G,
h=H(q)=e\q in B.                                                 (C1)
```

Here `e!=q`, since `D(q)=q` would make `q` Good.  Equation (13) gives a
unique Bad carrier `r` with

```text
r*q=e.                                                           (C2)
```

The canonical carrier gives the same cell,

```text
t*q=e,                                                           (C3)
```

and `r!=t` by colour.  Thus every Bad point supplies a distinct canonical
mixed collision

```text
N(q,D(q))>=2.                                                     (C4)
```

This is the exact way in which the `b` missing Bad fixers can be reused: one
collision unit is placed at the ordered cell `(q,D(q))` for every `q in B`.
Merely summing ZERO and collision counts therefore cannot force a shorter
cycle.

The companion identity turns (C3) into a sharper dichotomy.  Put `z=t*e`.
Since every carrier `c` with `c*q=e` satisfies

```text
(c*e)*c=e\q=h,
```

we have `z*t=h`.  If `z` is Bad, this is a Good-input/Bad-output cell in the
Bad row `z`.  The unique colour exchange (9) forces

```text
z=h,  t=kappa(h),  t*e=h.                         ZIPPER        (C5)
```

If `z` is Good, instead there is the actual mixed crossing

```text
(z,t,h) in G x G x B,  z*t=h.                     G-CROSS       (C6)
```

Hence perfect canonical reuse has no third anonymous local case:

```text
q  ->  ZIPPER at q, or a marked Good-row G-CROSS.                 (C7)
```

## A Bad D-cycle cannot remain fully aligned

Let `X` be a Bad directed cycle of `D`.  The whole-cycle reverse-lift lemma
says that an indefinitely ALIGNED lift would force

```text
sigma|X=D^2|X.                                                     (17)
```

But (4) makes the left side Good, while (2) makes the right side Bad.  Hence
(17) is impossible.  Every such cycle reaches a first actual

```text
COLLISION or FORK.                                                (18)
```

COLLISION carries its distinct canonical multiplicity charge.  FORK is the
remaining reverse-lift obstruction: the reverse cell points to the old cycle
while the canonical `D` cell at the same input points elsewhere.  Equations
(C4)--(C7) now attach that canonical cell to a ZIPPER or G-CROSS.  Nothing
proved so far makes the G-CROSS network land on a shorter `D`-cycle.

This is why the desired dichotomy

```text
strictly smaller D-cycle/depth or HIT
```

cannot yet be asserted.  The proved replacement must retain the marked
G-CROSS network after the first FORK.

## Minimal full-completion audit

The order-five K5 periodic core is the smallest shadow (14).  The targeted
mode

```text
tools/e677_k5_block_tree_completion_sat.py --blocks 1 --extra 5
  --terminal-k5 --seconds 300
```

fixes that Bad shadow, makes the five other points exactly Good, enforces
`D(B) subset B`, all permutation rows, and every E677 pair.  The result,
independently checked with two SAT engines, is

```text
order 10: Glucose42 UNSAT, 191.684 seconds;
          CaDiCaL195 UNSAT, 97.484 seconds.                      (19)
```

Thus the smallest perfectly reused two-layer shell is not a counterexample.
A selector-core run was `UNKNOWN(300s)`, so no small trustworthy E677-pair
core was extracted.  Adding exactly one unused Good point gives

```text
order 11: UNKNOWN(300s).                                         (20)
```

Do not extend this size ladder.  Equations (19)--(20) say that the order-10
obstruction may use exact shell saturation; they are not a size-independent
exclusion.

## Equivariant zipper audit

The pure ZIPPER alternative (C5) has a natural smallest completion test.
Index the K5 shadow along an order-five automorphism, force `D` to be that
five-cycle, identify

```text
sigma(q)=kappa(H(q))
```

around the whole orbit, and retain only two five-point Good layers (the
square layer and the common sigma/kappa layer).  The mode

```text
tools/e677_k5_block_tree_completion_sat.py --blocks 1 --extra 10
  --terminal-k5 --equivariant-three-layer-zipper --seconds 300
```

enforces every E677 pair, every permutation row, exact Bad/Good colours, the
Bad D-cycle, and the simultaneous order-five automorphism.  It makes no
idempotence assumption on the Good points.  The exact result, independently
checked with two SAT engines, is

```text
order 15 pure ZIPPER: Glucose42 UNSAT, 0.809 seconds;
                      CaDiCaL195 UNSAT, 1.621 seconds.            (Z1)
```

With the identical row, colour, orbit, and ZIPPER constraints but all E677
pair selectors disabled, `--skip-e677` gives

```text
order 15 base shell: SAT VERIFIED, 0.134 seconds.                 (Z0)
```

Thus (Z1) is caused by the mixed E677 equations, not by an inconsistent
partial permutation shell.

Thus the smallest symmetric perfect-zipper shell is not a counterexample.
This is a bounded exclusion, not a proof that arbitrary shadows or
non-equivariant ZIPPER networks are impossible.

For comparison, keeping three independent Good layers and only the local
bands gives an equivariant order-20 counterexample ansatz.  With idempotent
Good diagonals it remained

```text
order 20 four-layer shell: UNKNOWN, 600.481 seconds.              (Z2)
```

Do not repeat either run or enlarge this symmetry ladder.  The next
size-independent object is the simultaneous G-CROSS network in (C6).

## Exact local negative boundary

The shadow and SHORT data themselves are consistent as a partial
row-injective multiplication system.  Take the K5 shadow on Bad labels
`x_i`, `i in Z/5`, and fifteen distinct Good labels `s_i,t_i,k_i`.  Prescribe

```text
x_i*x_i=s_i,
s_i*x_i=t_i,
x_i*t_i=k_i,
x_i*k_i=x_i,
t_i*x_i=x_(i+1),
k_i*s_i=t_i,                                                    (21)
```

and make every Good diagonal idempotent.  Together with the twenty K5
off-diagonal cells, all rows in (21) are injective, all E677 instances whose
two variables are Bad hold, every displayed Good label is Good, and
`D(x_i)=x_(i+1)` is a Bad 5-cycle.  The unspecified mixed cells are essential:
this is a partial system, not a magma and not a counterexample.

Therefore no proof using only root counts, the self bands, off-diagonal Bad
E677, and row injectivity can force descent or HIT.  A successful general
proof must use the simultaneous mixed E677 equations on the marked G-CROSS
cells (C6), together with the first FORK, to obtain descent, renewal
collision, or HIT.  The requested root-reuse statement remains open at
exactly this point; the partial system (21) is not its counterexample.

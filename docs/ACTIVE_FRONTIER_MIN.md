# Active Frontier Min

Date: 2026-08-29.

Read this file first and normally no other status file.  Open a linked lemma
only for the exact statement currently being used.  The full pre-compaction
snapshot is historical and is not startup context:
`archive/ACTIVE_FRONTIER_MIN_full_2026-07-26.md`.

Use one CPU-heavy process at a time.  A research pass must end at a substantial
lemma, a complete model, or one exact negative boundary.  Do not repeat an
unchanged UNKNOWN run or enlarge it blindly.

## Problem and exact success condition

For every finite magma satisfying

```text
E677: x = y * (x * ((y*x)*y))
```

decide whether

```text
E255: x = ((x*x)*x)*x
```

must hold.  Put

```text
sigma(a)=(a*a)*a,
D(a)=sigma(a)*a.
Good={a:D(a)=a},  Bad=M\Good.
```

The unique-fixer lemma gives

```text
E255 at a  <=>  some r satisfies r*a=a  <=>  D(a)=a.
```

Success is either a size-independent proof `Bad=empty` or a complete finite
multiplication table checked on every E677 pair and with at least one Bad
point.  Partial SAT cores are not counterexamples.

## Size-free facts retained

1. Every left translation is a permutation.  In left-division notation,
   E677 is `b\(a\b)=(a*b)*a`.
2. A Good point has the unique left fixer `sigma(a)`.
3. `N(u,v)=|{r:r*u=v}|` is integer doubly stochastic; its support components
   are invariant submagmas.
4. In a minimum counterexample the support is strongly connected, the left
   translation group is transitive, and every Bad element generates the
   magma.
5. The parked direct proof uses the exhaustive Bad-orbit split HIT/CYCLE.
   Return to it only if the constructive route reaches a proved structural
   dead end.

## Primary route: an unexpected finite counterexample

Affine constructions `x*y=Px+Qy` have been excluded in the named finite
matrix layers.  The active nonlinear search is the size-7 orbit extension.
The most developed exact reduction uses cyclic `P` and a normalized cyclic
isotope Latin layer

```text
D(C_q(u))=A(q)+B(u) mod 7,
A(0)=0, A(1)=1, B(0)=0,
```

where `A,B,D` are permutations.  Exact routing includes original tuples
`0,2,6,7`; every SAT candidate must be audited against those tuples and then
against the full E677 table.

The full affine `C_q(u)=alpha*q+beta*u+gamma` layer is UNSAT.  In the normalized
isotope layer, every class with exactly one nonidentity role is also UNSAT:

```text
A only: direct UNSAT;
B only: direct UNSAT;
D only: all 844 scalar-conjugacy orbits UNSAT.
```

Therefore a survivor needs at least two nonidentity roles.

## Current two-role boundary

Classify a pair `(X,Y)` by

```text
(|image(X-id)|, |image(Y-id)|, cycle type of X^(-1)Y).
```

Closed exact classes:

```text
AB, D=id: 263 labelled pairs in six named types UNSAT;
AD, B=id, D(x)=x+c, c!=0:       714/714 UNSAT;
BD, A=id, D(x)=x+c, c!=0:      4314/4314 UNSAT;
AD, B=id, D(x)=k*x, k=2..6:     595/595 UNSAT.
```

Open but retired unchanged:

```text
AD with mixed affine D(x)=k*x+c, k!=1, c!=0:
first 150 fixed-pair cases gave 149 UNKNOWN;

BD with D(x)=2*x:
common formula UNKNOWN and first 150 fixed-B cases all UNKNOWN.
```

Do not extend those timeouts.  Their message is that fixing the partner
permutation without exploiting the affine fixed point gives no propagation.

Exact current proof and scripts:
`lemmas/e677_cyclic_P_two_role_shift_and_dilation_exclusion.md`.
Preceding normalization proof:
`lemmas/e677_cyclic_P_normalized_isotope_one_role_exclusion.md`.

## Exact next question

The mixed-affine fixed-point route is retired.  Exact gauge transfer shows
that its constant is absorbed either by a unit-step unnormalized `A` or by a
nonzero translation in `B`.  Three common encodings, including the direct
anchored law, are all UNKNOWN at the fixed three-minute boundary.  Exact
derivation and counts are in
`lemmas/e677_cyclic_P_mixed_affine_gauge_and_anchor_boundary.md`.

The reusable result is that normalized `A,B` can be eliminated completely:

```text
D(C_q(u))=D(C_q(0))+D(C_0(u)),
D(C_0(0))=0,
D(C_1(0))=1.                                  (ANCHOR)
```

The first nonlinear translation-curvature layer is now classified exactly.
With

```text
kappa(D)=sum_(t!=0) (7-max_v |{x:D(x+t)-D(x)=v}|),
```

the minimum nonlinear value is `18`.  Exactly `294` permutations attain it,
and all have the harmonic double-swap form

```text
D=L o (a,a+d)(a+4d,a+5d).
```

Output gauge reduces them to `21` identity-centre maps; scalar conjugacy then
reduces those to four canonical representatives.  All canonical `D` are
involutions, so the isotope table is exactly

```text
C_q(u)=D(A(q)+B(u)).
```

Its nonlinear cells form four disjoint permutation transversals; every row
and column has the exact split `4 defect + 3 affine-background`.  Complete
common, gauge, fixed-map, and four-canonical SAT encodings are all UNKNOWN at
their fixed boundaries.  They are retired.  Exact classification, counts,
and commands are in
`lemmas/e677_cyclic_P_minimum_D_curvature_four_transversal_boundary.md`.

`T2` alone cannot exclude this layer.  For fixed `C,W`, define

```text
f_t(h)=W_h(t-C_t(h)).
```

Permutation rows `H_t,V_r` satisfying `V(r,t)=f_t(H_t(r))` exist exactly when
every output value occurs seven times among the `49` values `f_t(h)`.  This is
the 1-factorization criterion for a 7-regular bipartite multigraph.  An
explicit complete-mapping construction supplies seven distinct Bad `O7` rows
and satisfies this balance for every permutation `D`, including all four
canonical maps.

Tuple 6 supplies the missing obstruction.  Put

```text
q_s(t)=O7_t(s),
z_s(t)=O7_t^(-1)(s),
rho_s(t)=D(q_s(t)-t)-A(q_s(t)).
```

It admits a permutation row `H_s` exactly when

```text
z_s(t)=z_s(t')  <=>  rho_s(t)=rho_s(t')        (T6-KERNEL)
```

for all `t,t'`.  This eliminates `H` and, importantly, `B` from tuple-6
feasibility.  All `42` complete-mapping absorbers times all four canonical
`D` fail this condition: `168/168` excluded with no UNKNOWN.  Exact proof,
counts, explicit matching witnesses, and verifiers are in
`lemmas/e677_cyclic_P_tuple6_kernel_and_T2_matching_absorber.md`.

The distinguished `s=0` kernel has an additional exact displacement law.  Put

```text
z(t)=O7_t^(-1)(0).
```

The cyclic transversals make `t->t+z(t)` a permutation, Badness makes every
`z(t)` nonzero, and hence `sum_t z(t)=0`.  Together with `T6-KERNEL`, this
excludes ranks `1,2,6,7` manually.  Therefore

```text
|image(z)| in {3,4,5}.
```

Exactly nine block profiles remain, represented by `108` labelled nonzero
zero-sum multiplicity vectors and `18` scalar orbits.  All nine are realized
by derangements.  The common kernel formula and all nine profile splits are
UNKNOWN at their fixed boundaries and are retired.  Exact proofs, counts,
and verifiers are in
`lemmas/e677_cyclic_P_zero_target_kernel_rank_obstruction.md`.

The distinguished-target support alignment is now classified exactly.  On
a `z`-block of size `m`, both `q(t)` and `q(t)-t` are injective, so

```text
max(0,m-3) <= |E intersect block| <= min(m,4).
```

An exact block classifier covers all `1854` displacement rows, `427`
realizable partitions, `720` maps `A`, and four canonical `D`.  Every `A` and
every partition occurs in a feasible zero-target core, and every total
support count allowed by the displayed capacity bounds occurs.  Thus the
support split is permissive and retired.

Tuple 6 for all targets has the exact pair-clique form.  For rows `U_t=O7_t`,
all `t,u,s` must satisfy

```text
U_t^(-1)(s)=U_u^(-1)(s)
iff
D(U_t(s)-t)-A(U_t(s))=D(U_u(s)-u)-A(U_u(s)).
```

The cyclic `Q` condition is the pairwise shifted-row inequality

```text
U_t(T-t) != U_u(T-u) for every T and t!=u.
```

Hence the complete T6 kernel is exactly a seven-partite clique of bad,
distinct permutation rows.  A bounded constructive clique search found no
witness in `23` fixed `(D,A)` cases.  Two selected extremes reached only
depth `3/7` and `4/7`, respectively; these are diagnostics, not exclusions.
The fixed pair

```text
D=1023546, A=0132465
```

is strictly `UNSAT` in the exact T6 formula.  The analogous low-collision
pair is `UNKNOWN`, and the combined 28-pair maximum column-collision layer is
also `UNKNOWN` at 180 seconds.  The column-collision quantity used to choose
those pairs is only a search heuristic, not a T6 invariant; row and column
collision energies must not be equated.

The exact continuation is the relative-permutation cocycle.  Put

```text
pi_tu=U_u o U_t^(-1),
F_t(q)=D(q-t)-A(q),
H_tu(pi)={q:F_t(q)=F_u(pi(q))}.
```

Pair-kernel gives

```text
H_tu(pi_tu)=U_t(Fix(pi_tu)),
```

pair-Latin says `pi_tu` disagrees everywhere with the conjugated shift
`U_t o (+u-t) o U_t^(-1)`, and triples obey

```text
pi_tv=pi_uv o pi_tu.
```

Classify these relative pair types and impose the triangle cocycle before
another seven-row search.  Do not rerun raw clique search, support-count SAT,
the 28-pair formula, or the common kernel formula unchanged.  Exact proof,
scripts, and computation boundaries are in
`lemmas/e677_cyclic_P_T6_support_and_pair_clique_boundary.md`.

The cocycle has now been imposed constructively through the exact Latin
representation

```text
L(t,T)=O_t(T-t).
```

Here cyclic `Q` is exactly the Latin column law and Badness is the nonzero
diagonal `L(t,t)!=0`.  A randomized nonlinear Latin search checked `4936`
admissible labelled seeds over all `720` maps `A` and four canonical `D`.
Latin trades and joint changes of `A,D` then produced the near-core

```text
D=1023546,
A=0246135,
O7=6425130/2536041/1642350/4051263/3164502/4203615/5314026.
```

It violates only two of the `147` pair-kernel equivalences:

```text
s=0, rows (0,2): z=6,6 but rho=1,4;
s=4, rows (4,6): z=3,3 but rho=4,0.
```

Both are splits and there are no false merges.  Exact cardinality formulas
exclude all repairs with `O`-Hamming radii `8`, `12`, and `16`; at radius 16
all normalized `A` are allowed.  Therefore every exact T6 core with this `D`
is at least `17` O-cells from the near-core, regardless of `A`.

The direct pair-kernel CNF eliminates `K_s` and enforces the 147 equivalences
on one-hot `rho_s(t)`.  For fixed `D=1023546` it is still `UNKNOWN` at the
retired 180-second boundary.  Do not rerun the Latin search, local trades,
three Hamming balls, or this fixed pair formula unchanged.  Exact derivation,
near-core, and audits are in
`lemmas/e677_cyclic_P_T6_latin_near_core_boundary.md`.

The signed partition diagnostic is defined by

```text
C(w_s)=sum_blocks binomial(block_size,2),
Delta_s=C(z_s)-C(rho_s),
Delta=sum_s Delta_s.
```

Every exact T6 core has `Delta_s=0` for every `s`; the near-core has
`Delta=2`.  This compares row collisions at fixed `s` and must not be
confused with the invalid row/column energy identity already retired.  The
subsequent scan shows that even the full signed vector is too weak.

The signed defect has now been tested and is permissive.  In a coherent
sample of `14,143,680` triples `(O,A,D)`, scalar `Delta=0` occurred `450,988`
times and the full vector `Delta_s=0` occurred `297` times.  Thus signed
collision counts are retired as an obstruction.

The full block-size profile is determined on seven points by

```text
C2=sum_B binomial(|B|,2),
C3=sum_B binomial(|B|,3).
```

Among `14,201,280` coherent triples, only `155` matched both invariants for
all seven targets.  None matched the resulting seven row-degree totals.  The
best profile-matched seed has `epsilon=20/147` and the uniform profile

```text
(2,2,1,1,1)
```

for every target.  Hence each target contributes a matching of two disjoint
row edges, fourteen colored edges in total.

The exact full uniform-profile formula for `D=0125634` is `UNKNOWN` at its
retired 180-second boundary.  A weaker formula requiring only uniform
profiles and equality of the seven uncolored vertex degrees is also
`UNKNOWN`; an equivalent incidence encoding reduced it from `26,940` to
`3,028` variables without resolving it.  Do not rerun these formulas.

The exact continuation is now purely graph structural: classify the possible
fourteen-edge matching multigraphs arising from the Latin rows and from rho.
Use the triangle cocycle and shifted-derangement law to restrict degree
sequences or repeated row-pair multiplicities.  Only after obtaining a named
graph identity should computation return.  Exact sample counts, encodings,
and warnings are in
`lemmas/e677_cyclic_P_T6_signed_profile_matching_boundary.md`.

That final pure-Z degree test is now complete as a stop audit.  There are
`1911` admissible uniform displacement rows (`546` nonzero for `s=0`) and
`155` arithmetically possible degree multisets.  A graph-only exact formula
realized at least `131/155` before its fixed timeout.  Thus uncolored degrees
are also permissive; completing the remaining list would not solve T6.  The
minimum-curvature canonical-D order-49 route is parked.  Do not continue it
without a new invariant stronger than support, signed collisions, profiles,
and degree multisets.

The independent direct order-11 route has reached an exact stop boundary.
Besides the earlier `Y0-COUPLING`, put

```text
s(t)=0*t,
f(y)=y*0,
g(y)=L_y^(-1)(0).
```

E677 at `x=0` gives the new exact law

```text
f(y)*y=s^(-1)(g(y)),
```

and row injectivity gives, for `y!=0`,

```text
f(f(y))!=s^(-1)(g(y)).
```

The known Good control remains verified after adding these clauses.  The
three normalized Bad cases `2*0=1,2,3` all remain `UNKNOWN` at twenty seconds,
so these runs are retired.  Put `R=f o s`; comparing the `x=0` and `y=0`
cells in a common row yields the single cross law

```text
g(y)=f(y) iff y=R(f(y)).
```

The formerly listed first formula is just this one with `y=s(x)`, not an
independent constraint.

The corrected necessary functional system for `s,f,g` has audited witnesses
in all three normalized cases `f(2)=1,2,3`, found after `4,1,1` constructive
trials.  These are not magma tables, but they prove that `XY0-CROSS` excludes
none of the three cases.  The direct order-11 frontier remains `0/3` closed
and is parked.  Exact derivations, witnesses, and warnings are in
`lemmas/e677_uniform_Z_and_order11_x0_boundary.md`.

Two genuinely different constructive families have now been tested.  For a
nonabelian group `G`, let `A,B` be automorphisms or automorphisms followed by
inversion.  The complete one-constant scan

```text
c A(x) B(y), A(x) c B(y), A(x) B(y) c
```

checked `5,314,112` presentations over `D_6,...,D_24,Q_8`; the full translated
layer `p A(x) q B(y) r` checked another `2,941,824` presentations over
`D_6,D_8,D_10,Q_8`.  Neither layer contains even one E677 model.  They are
closed and must not be extended unchanged.  Exact scope and verifier are in
`lemmas/e677_nonabelian_group_isotope_boundary.md`.

The current structural frontier is permutation covers.  Over a Good E677
base, put

```text
(a,i)*(b,j)=(a*b,P[a,i,b](j)).
```

There is now a size-independent proof that every binary such cover satisfying
E677 also satisfies E255.  Over the verified Good order-11 base, exact full
cover formulas additionally exclude every Bad target for fibres `3` and `4`:

```text
fibre 2 / order 22: 22/22 UNSAT;
fibre 3 / order 33: 33/33 UNSAT;
fibre 4 / order 44: 44/44 UNSAT.
```

The general local fixed-point question has now been resolved far enough to
park uniform covers.  With `p=x*x,q=p*x,r=x*q`, the two local E677 pairs
`(x,q),(x,x)` force a fixer in fibres 2 and 3, but admit audited
fixed-point-free seeds in fibres 4 and 5.  The missing pair `(r,x)` is exactly
the partition kernel

```text
U_i(j)=F_{C_j(i)}(j), V_i(j)=B_j^-1(i),
U_i(j)=U_i(k) iff V_i(j)=V_i(k).
```

For fibre 4, each order-seven base is already killed by a single idempotent
base pair: the fibre above that point would have to be an E677 magma of order
4.  Fibre 5 is the first admissible size.  Two full order-35 completions,
over the two Good order-seven bases with a verified E677 fibre-five table
fixed, both reached the retired 180-second `UNKNOWN` boundary.  A concrete
local fibre-five seed is separately UNSAT at the single pair `(r,x)`; direct
and kernel encodings of the strengthened local system both reached the
retired 60-second boundary.

Do not run fibre 5, order 35, or the three-pair local system unchanged.  The
next constructive family was therefore taken to be a skew/imprimitive
extension in which the permutation induced on base blocks depends on the
left fibre coordinate.  Exact uniform-cover equations, seeds, cores, and
boundaries are in
`lemmas/e677_binary_and_small_permutation_cover_boundary.md`.

That skew row-label class is now sharply reduced.  Over the verified
order-five base, put

```text
(a,i)*(b,j)=(B[phi_i(a)][b],P[a,i,b](j)).
```

The exact base-coordinate condition `BASE-REACH` classifies all power
families `phi_i=theta^i`: `95/120` theta fail immediately; the identity and
all `24` five-cycles survive.  The five-cycles form two automorphism orbits,
and the full E677 formula is UNSAT for both representatives even with Good
models allowed.  Identity is the parked ordinary cover.

For arbitrary families containing the identity, fewer than five distinct
maps are impossible.  At five maps exactly three automorphism orbits survive
`BASE-REACH`; all three full order-25 formulas are UNSAT.  Thus the anchored
skew class is completely closed.

For unanchored families, fewer than five maps are again impossible.  There
are exactly `75` automorphism orbits at five maps.  A combined exact
classifier checked every full order-25 formula, allowing Good models:

```text
75/75 UNSAT; 0 Good models; 0 UNKNOWN.
```

Three orbit-distinct representatives were minimized structurally.  In every
case an inclusion-minimal core consists of the same pattern

```text
(a,a), (a,b).
```

Each pair separately is satisfiable.  Signs and complete cycle types of all
30 shared permutations can agree, so both coarse invariants are retired.
Exact equality minimization reduces each representative to one shared
permutation and then one conflicting cell: the two pairs force respectively
`4!=3`, `0!=3`, and `4!=3`.

Combining the `75` unanchored orbits with the two nonidentity power orbits and
three anchored nonpower orbits closes `80/80` nontrivial row-label formulas.
The only surviving row-label action is constant identity, exactly the parked
ordinary cover.  Therefore the skew row-label construction is closed and
must not be extended by more family enumeration.  Exact classifiers,
representatives, cores, and one-cell certificates are in
`lemmas/e677_skew_rowlabel_base_reach_and_twopair_boundary.md`.

The constructive program has now reached a structural dead end in its named
families: affine layers, the canonical order-49 isotope, nonabelian signed
group isotopes, uniform covers, and nontrivial skew row-label extensions are
all either exactly closed or parked at a precise nonlocal kernel.  The active
route returns to the size-free HIT/CYCLE proof.  Reuse the new lesson in the
terminal component: do not sum coarse signs or cycle profiles; isolate a
shared row permutation and force a single cell from two E677 routes.  The
next proof target is a size-independent analogue of this one-cell collision
for the external-predecessor network.

That analogue is now proved.  For every external source cell `y*a=v`, put

```text
b=y\a, c=a\b.
```

The left-division form of E677 gives the exact four-cell word

```text
y*a=v, y*b=a, v*y=c, a*c=b,
```

and therefore the genuine companion edge

```text
tau(y,b)=(a,a\b).
```

The signature `kappa(y,a)=(a,b)` has fibre size exactly `N(b,a)`.  Hence all
repeated signatures inject into distinct local units `N(b,a)-1`, while one
canonical representative per signature has a distinct actual-cell target
`(a,a\b)`.  This removes the old ambiguity about repeatedly reusing SOURCE
defects or `J/M` charges.

The canonical linkage is now also exact.  If `a in X` and `b=y\a`, then:

```text
b outside X                    -> EXIT;
b in X and N(a,y)=0            -> new ZERO certificate;
b in X and N(a,y)>0            -> (y,b)=rho(a,y) and
                                   tau(rho(a,y))=rho(b,a).
```

Thus a finite route either reaches EXIT/ZERO or contains a genuine tau
cycle.  This fixes the earlier invalid conversion of an auxiliary
permutation cycle into a tau cycle.  The remaining direct-proof task is now
the length/port analysis of this actual tau cycle, with EXIT passed to HIT
and ZERO passed to the distinct collision surplus.  Exact proof and
accounting are in
`lemmas/e677_external_predecessor_one_cell_fibre_lemma.md`.

The applicability gap in the old port lemmas is now bridged directly.  If
`C` is any genuine all-Bad tau cycle with cyclic row word

```text
e_i=(r_i,r_(i+2)),  r_i*r_(i+2)=r_(i+1),
```

then every state has the distinct canonical port

```text
Phi(e_i)=(r_i,r_i\r_(i+2)),
tau(Phi(e_i))=(r_(i+2),r_(i+1)*r_i).
```

If `Phi(C)=C`, the induced port permutation is fixed-point-free on the
occurrences of every row label.  Hence every label occurs at least twice.
The exact two-occurrence equality would conjugate the cyclic shift `S` to
`S^2`; because the word length is even, this is impossible.  Therefore an
internally reused arbitrary cycle is size-free PORT-LONG:

```text
ell >= 2*|labels(C)|+1.
```

The global reuse audit is stronger.  Let `P` be all genuine all-Bad periodic
tau states.  If `Phi(P)` leaves `P`, finite backward ancestry yields a
coloured boundary or a genuine ZERO root.  If `Phi(P)=P`, a used row label
occurs at least three times somewhere in `P`; the global exact-two case
would force paired opposite tau 3-cycles, contradicted by one application of
the left-division form of E677.

Add the second forced state permutation `Psi(r,u)=(r*u,r)`.  If it also
preserves `P`, then `P` is invariant under coordinate swap and defines a
finite simple symmetric graph

```text
U_a={u:(a,u) in P},
u in U_a iff a in U_u,
L_a(U_a)=U_a.
```

Every vertex has degree at least two, every edge belongs to a forced
multiplication triangle, and the total branching surplus satisfies

```text
sum_a (|U_a|-2) >= 2.
```

The low-degree equality core is also excluded size-free.  A connected
simple graph with minimum degree two, maximum degree at most three, and
every edge in a triangle is `K3`, `K4`, or the diamond.  Respectively, the
closed row restrictions are swaps, 3-cycles, or two identical degree-two
arms; one use of the left-division identity contradicts each case.  Hence
every completely reused periodic component contains a named row of degree
at least four.

Thus the arbitrary-cycle PORT-MINIMAL residue is excluded without a size
bound.  Exact proof is in
`lemmas/e677_genuine_tau_cycle_canonical_port_long_lemma.md`.  A diagnostic
found no closed single cyclic word through length 14, but this bounded fact
is not used.

The proposed continuation "charge the four ports to merger fibres" has now
been audited and retired as a sole invariant.  The degree-four residue is
real: there is an explicit `K5` port core whose twenty oriented off-diagonal
states form five genuine tau 4-cycles and satisfy every internal
left-division E677 instance.  Copies glue at vertices into connected partial
cores of arbitrary size; all port maps stay within their original block and
there are no internal tau mergers.  Therefore local degree, triangle, port,
and merger accounting cannot contradict CYCLE.

The missing information is exactly outside the periodic state set.  One
isolated `K5` core completes to the verified Good order-five E677 table:
row saturation forces `a*a=a`.  Exact full-completion tests give

```text
one K5 block / order 5 / Good allowed:          SAT, all Good;
two-block chain / order 9 / Good allowed:       UNSAT;
three-block chain / order 13 / Good allowed:    UNSAT.
```

For one fixed block with a proper ambient extension, orders `6,7,8,9` are
also exactly `UNSAT` even when Good is allowed.  The first two-layer
threshold, order `10`, is `UNKNOWN(180s)` and is parked.  This size boundary
is diagnostic only; do not continue the size ladder.  The order-13
five-carrier row profile is exact but disappears after adding a free label,
so it is not the size-free mechanism.

Relative to the fixed block cells and permutation rows, inclusion-minimal
E677 pair cores have sizes `8` and `6`; every deletion trial was decided.
The size-independent diagonal mechanism is now proved, and is stronger than
the finite completion boundary.  In the completely reused periodic graph,
fix a used Bad label `a` and put

```text
d=a*a,
h=d*a.
```

Self-E677 gives `L_a^2(h)=a`.  Since `a` is not a periodic neighbour of
itself and `L_a` preserves the periodic neighbour set `U_a`, necessarily
`h` is outside `U_a`.  Apply the exact one-cell word to `h*a=D(a)`:

```text
b=h\a, c=a\b,
h*b=a, D(a)*h=c, a*c=b,
tau(h,b)=(a,c).
```

The state `(h,b)` cannot be periodic.  If it were, `A0`-closure would put
`(h,a)` in the periodic set and coordinate-swap closure would put `(a,h)`
there, contradicting `h` outside `U_a`.  If a coordinate is Good this is a
coloured boundary; otherwise the finite backward tree of `(h,b)` has an
actual ZERO/coloured root.

Together with the already proved handling of failed `Phi/Psi` closure, this
gives the unconditional size-free reduction

```text
genuine all-Bad tau cycle -> coloured boundary or genuine ZERO root.       (*)
```

Thus perfect periodic reuse, including every K5 block gluing, is no longer
the CYCLE obstruction.  Exact proof is in
`lemmas/e677_diagonal_escape_from_periodic_tau_lemma.md`.  K5 tables,
completion boundaries, and the two failed local shortcuts (diagonal
collision and one isolated row 5-cycle) are recorded in
`lemmas/e677_K5_periodic_block_gluing_and_completion_boundary.md`.

The terminal ZERO-reuse equality is now classified much more sharply.  Put
`B=Bad` and assume `Z_(B x B)=|B|` and no HIT, so `D(B) subset B`.  Then

```text
s(x)=x*x, sigma(x), kappa(x) are Good for every x in B;
each Bad row has the one-point SHORT block
    kappa(x) Good -> x Bad -> s(x) Good;
N_B(u,v)=1 for all distinct u,v in B;
r o u = r*u (r!=u), r o r=r
is an idempotent Latin E677 quasigroup on B.                     (**)
```

In particular, every canonical Bad D-cell is already a mixed collision.  For

```text
e=D(q), t=sigma(q), h=H(q)=e\q
```

there is one Bad carrier and the distinct Good carrier `t` of `q -> e`, so
`N(q,e)>=2`.  Companion factorization gives the exact local alternative

```text
ZIPPER:  t*e=h and t=kappa(h);
G-CROSS: z=t*e is Good and z*t=h is a Good-row Good-to-Bad crossing.  (***)
```

Thus ZERO reuse is not arbitrary and cannot be closed by root/collision
counts alone: the `|B|` missing fixer cells can be paired one-for-one with
the `|B|` canonical mixed collisions.  A partial order-20 K5/SHORT skeleton
realizes all local data and a Bad D-cycle, so mixed E677 equations are
essential; it is not a complete magma.

The smallest symmetric pure-ZIPPER completion is exactly excluded.  The
UNSAT result was independently reproduced by Glucose42 and CaDiCaL195, while
the decoded control model was checked directly against every fixed shell
cell, colour condition, no-HIT condition, and equivariance constraint:

```text
same shell with E677 disabled, order 15:      SAT VERIFIED(0.134s);
full E677 / Glucose42:                              UNSAT(0.809s);
full E677 / CaDiCaL195:                             UNSAT(1.621s).
```

The independent three-Good-layer equivariant order-20 ansatz remained
`UNKNOWN(600s)` and is parked.  Do not repeat or enlarge either size test.
Exact proof, the local negative boundary, and commands are in
`lemmas/e677_zero_root_reuse_shadow_quasigroup_boundary.md`.

## Order-9 terminal ZERO side closure

The late global ZERO lemma now gives a strict finite reduction at order `9`.
Under

```text
D(Bad) contained in Bad,
Z_(Bad x Bad)=|Bad|,
```

the Bad shadow is an idempotent Latin E677 quasigroup.  An exhaustive
cycle-type scan proves that among possible shadow orders `2,...,8` only
order `5` exists.  Blocking the full relabelling orbit proves that its unique
isomorphism type is the K5 table.  Hence the order-nine terminal residue is
exactly `5 Bad + 4 Good` with the twenty off-diagonal K5 cells fixed.

The full terminal completion is independently UNSAT in both engines:

```text
CaDiCaL195: UNSAT(2.460s);
Glucose42:  UNSAT(1.204s).
```

Therefore the exact finite continuation is

```text
order-9 counterexample -> HIT or Z_(Bad x Bad)>|Bad|.             (O9)
```

The terminal equality/no-HIT class is closed and must not be rerun.  The
checker, certificate wrapper, output record, and proof are respectively

```text
tools/e677_idempotent_latin_order_scan.py;
verify_order9_terminal_zero.ps1;
logs/e677_order9_terminal_zero_shadow_2026-08-29.txt;
lemmas/e677_order9_terminal_zero_shadow_exclusion.md.
```

For the finite order-nine side route, the next named question is whether one
strict extra `Omega` root can be attached injectively to its first merger or
coloured exit; the other top branch is HIT.  Do not rerun raw full order-nine
SAT or the terminal K5 formula unchanged.

The first strict-surplus cardinality is now also closed.  If `|Bad|=2`, every
state in `Bad x Bad` is an internal indegree-zero state: an off-diagonal Bad
product is either Good or the row label, and the latter has multiplicity
`N_B(r,r)=0`.  Hence every `tau` edge leaves `Bad x Bad`.

At order `9`, normalize `0*0=1` and put `f(t)=t*0`.  Exact no-HIT routing has
only four forms:

```text
B={0,1}: f(1)=1;
B={0,1}: f(1)=2, f(2)=1;
B={0,2}: f(1)=2, f(2)=2;
B={0,2}: f(1)=3, f(3)=2.
```

The first two are direct UNSAT.  In the third form, the colour split leaves
one profile and residual relabelling gives five renewal cores; all are
independently `5/5 UNSAT` in CaDiCaL195 and Glucose42.  In the fourth form,
the sole colour survivor has all four `Bad*Bad` products Good; the joint
first-new-label split of `0*2,2*0,2*2` has twenty orbits, independently
`20/20 UNSAT` in both engines.

Therefore the exact order-nine continuation improves to

```text
order-9 counterexample
  -> HIT
  or no HIT, |Bad| in {3,4,5,6,7,8,9}, Z_(Bad x Bad)>|Bad|.      (O9+)
```

Do not rerun the two-Bad formulas.  Exact proof, checker, record, and wrapper:

```text
lemmas/e677_order9_two_bad_no_hit_exclusion.md;
tools/e677_order9_no_hit_bad_count_sat.py;
logs/e677_order9_two_bad_no_hit_2026-08-29.txt;
verify_order9_two_bad_no_hit.ps1.
```

The next finite question is the three-Bad `D`-orbit/root pattern.  Unlike
the two-Bad case, an off-diagonal product may be the third Bad label, so
`Omega` is not automatically root-only.

That three-Bad pattern is now normalized exactly.  Select one strict extra
Omega-root before naming the labels.  The fixed-point-free map `D` on three
Bad points is either a 3-cycle or a 2-cycle with one tail.  After setting
`0*0=1`, the square colour, the value `D(0)`, and the chain
`f(t)=t*0` give exactly `24` top forms:

```text
family A (square Bad, D(0)=1): 3 D-types * 3 f-chains = 9;
family B (square Bad, D(0)=2): 3 D-types * 2 f-chains = 6;
family C (square Good,D(0)=2): 3 D-types * 3 f-chains = 9.
```

The first exact CaDiCaL scan closed `15/24`; the nine bounded UNKNOWN forms
are indices `2,3,11,15,16,18,21,23,24`.  Fixing only the root position gave
`15/15 UNKNOWN` before an intentional stop and is retired.  Splitting the
canonical root by Good/row/third-Bad product closed `23/66` small cubes;
naming the Good product up to residual symmetry closed `6/37` further cubes.
These counts locate the boundary and do not close all three-Bad models.

One full top-form reduction is certified independently.  In form `2`,

```text
B={0,1,2}; D: 0->1->2->0;
0*0=1; 1*0=2; 2*0=1,
```

all four Bad-product extra roots and all four companion cases for a Good
root `(0,1)` are `8/8 UNSAT` in both CaDiCaL195 and Glucose42.  Therefore
the selected extra root must be exactly

```text
(0,2), with 0*2=3 Good.
```

For this sole form-2 residue, put `a=0*3`, `k=a*0`; E677 forces `3*k=2` and
the exact paused split is

```text
a in {0,2,4};
a in {0,2} -> k=1;
a=4       -> k in {1,3,4,5}.
```

No calculation of that split has been started.  Exact proof, checker, log,
and wrapper are

```text
lemmas/e677_order9_three_bad_root_and_case2_reduction.md;
tools/e677_order9_no_hit_bad_count_sat.py;
logs/e677_order9_three_bad_case2_2026-08-29.txt;
verify_order9_three_bad_case2.ps1.
```

The size-free active structural question remains the simultaneous G-CROSS
network.
For every non-ZIPPER point mark

```text
E_q=(z_q, sigma(q), H(q)),
z_q=sigma(q)*D(q) in Good,
z_q*sigma(q)=H(q) in Bad.
```

Follow all such marks together through the already proved Good-row renewal,
not one at a time.  The next strict lemma must obtain one of

```text
1. a first merger/terminal whose companion is a new non-square root;
2. a smaller D-depth/cycle or HIT;
3. exclusion of the clean marked renewal cycle by comparing its repeated
   Good input with sigma(q)=kappa(H(q)) at every missing ZIPPER.   (NEXT)
```

Do not return to periodic graph degree, K5 size ladders, isolated FORKs, or
issue lookup.

## Stop rules and reporting

- No web or issue lookup without a new concrete mathematical claim.
- Open old material only for a named lemma.
- One combined process, concise output, and no repeated progress dumps.
- After two structurally identical UNKNOWN outcomes, change the invariant.
- Report only: key result, what class was closed/opened, next barrier, and
  research estimates.

Progress reporting is recalibrated.  Earlier `94--96%` numbers measured how
much of one construction route had been explored and were misleading as a
measure of solution.  Report instead:

```text
final certificate (proof or checked counterexample):       0%;
periodic-reuse subgate inside CYCLE:                    1/1 (100%);
ZERO-reuse structural gates:                            2/3 (67%);
  terminal shadow/SHORT classification:                1/1 (100%);
  canonical ZIPPER/G-CROSS routing:                    1/1 (100%);
  global G-CROSS outcomes in (NEXT):                     0/3 (0%);
current CYCLE outcome fully excluded:                         no;
current HIT outcome fully excluded:                           no;
equivariant pure-ZIPPER K5 shell (diagnostic):            1/1 (100%);
proper K5 extension sizes 6--9 (diagnostic only):       4/4 (100%);
completed nonabelian presentations:  8,255,936/8,255,936 (100%);
completed cover Bad-target tests:                 99/99 (100%).
completed nontrivial row-label orbit formulas:     80/80 (100%).
order-9 terminal ZERO equality/no-HIT subgate:        1/1 (100%).
order-9 |Bad|=2 no-HIT subgate:                       1/1 (100%).
order-9 |Bad|=3 top forms initially closed:          15/24 (62.5%).
order-9 |Bad|=3 form-2 root outcomes excluded:         8/9 (88.9%).
order-9 remaining no-HIT Bad cardinalities:             0/7 (0%).
full order-9 implication certificate:                  0/1 (0%).
```

Every `100%` entry certifies only its explicitly named subproblem, not
closeness to the theorem.  The order-35 cover frontier remains `0/2`
resolved (`2/2 UNKNOWN`) and parked.  No complete counterexample has been
found.

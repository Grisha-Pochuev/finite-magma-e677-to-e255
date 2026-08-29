# E677 cyclic P: T6 Latin near-core boundary

Date: 2026-07-26.

Status:

```text
the pair-cocycle search has a two-failure Latin near-core, but the complete
Hamming ball of radius 16 around it is T6-UNSAT for every normalized A;
the direct pair-kernel formula remains UNKNOWN, so no T6 core is known
```

## 1. Latin-square realization of the cocycle

For permutation rows `O_t`, define

```text
L(t,T)=O_t(T-t),
O_t(s)=L(t,t+s).
```

The row-permutation and cyclic `Q`-fibre requirements are exactly the row and
column permutation requirements for `L`.  Thus `L` is a Latin square of order
seven.  Badness is the nonzero diagonal condition

```text
L(t,t)=O_t(0)!=0.
```

Every relative map `pi_tu=O_u o O_t^(-1)` obtained from a single Latin square
automatically satisfies the triangle cocycle.  Consequently a nonlinear
Latin-square generator is a constructive search over globally coherent
pair types, not an independent row-pair relaxation.

For fixed `O,A,D`, put

```text
z_s(t)=O_t^(-1)(s),
rho_s(t)=D(O_t(s)-t)-A(O_t(s)).
```

The exact T6 defect score is

```text
epsilon(O,A,D)
  = sum_(s,t<u) 1[(z_s(t)=z_s(u)) xor (rho_s(t)=rho_s(u))].
```

An exact tuple-6 kernel core is equivalent to `epsilon=0`.

## 2. Constructive Latin search

The script

```text
tools/e677_fiber7_T6_latin_seed_search.py
```

generates randomized reduced Latin squares, relabels them to a nonzero
diagonal, and checks all `720` normalized maps `A` and four canonical `D` by
the exact pair-kernel condition.  One bounded run gave

```text
50 distinct reduced bases;
4936 admissible labelled O tables;
best epsilon=12/147;
no exact T6 core.
```

This is a search boundary, not an exclusion.

Starting from that named seed, two-row and two-column Latin trades preserve
the complete Latin/Q structure.  The fixed `(D,A)` annealing checked
`1,141,220` admissible moves and improved `epsilon` from `12` to `9`.
Allowing simultaneous transpositions of `A` and changes among the four
canonical `D` checked `1,001,279` further moves and reached the exact near-core

```text
D=1023546,
A=0246135,
O7=6425130/2536041/1642350/4051263/3164502/4203615/5314026,
epsilon=2/147.
```

Its only failures are

```text
s=0, rows (0,2): z=6,6 but rho=1,4;
s=4, rows (4,6): z=3,3 but rho=4,0.
```

Both are splits of a true two-point `z` block; there are no false merges.
The stochastic counts above do not prove local optimality.

## 3. Exact Hamming-ball exclusion

The exact repair formula

```text
tools/e677_fiber7_T6_kernel_near_seed_repair_sat.py
```

uses the complete older `K_s` encoding, fixes the displayed canonical `D`,
and imposes cardinality bounds around the named `O,A`.  It gave strict
results:

```text
distance(O)<=8,  distance(A)<=2: UNSAT,  0.146 s;
distance(O)<=12, distance(A)<=4: UNSAT,  1.365 s;
distance(O)<=16, distance(A)<=6: UNSAT, 42.489 s.
```

Because normalized `A` fixes zero, its maximum possible Hamming distance from
the displayed `A` is six.  Therefore the last line says:

```text
for D=1023546, every exact T6 core is at O-Hamming distance at least 17
from the displayed near-core, independently of A.                (BALL-17)
```

`BALL-17` is a genuine finite exclusion.  The two visible local failures
cannot be repaired by a small trade or by changing `A`.

## 4. Direct pair-kernel encoding

The pair-clique lemma permits elimination of the permutation rows `K_s`.
The new exact formula

```text
tools/e677_fiber7_T6_pair_kernel_sat.py
```

introduces one-hot values `rho_s(t)` and directly forbids the two kernel
mismatches:

```text
same z, different rho;
different z, same rho.
```

It has `886` variables and `101726` clauses for fixed `D`.  A SAT model is
audited by reconstructing `K_s`, so this formula is equivalent to the older
T6 kernel core, not a relaxation.  For

```text
D=1023546
```

the new formula is `UNKNOWN` after `180.320` seconds with `1,328,768`
conflicts.  This fixed run is retired and must not be extended unchanged.

## 5. Exact continuation: signed partition defect

For a partition-valued row `w_s(t)`, write

```text
C(w_s)=sum_blocks binomial(block_size,2).
```

Define the signed global defect

```text
Delta_s=C(z_s)-C(rho_s),
Delta=sum_s Delta_s.
```

An exact T6 core requires every `Delta_s=0`.  The displayed near-core has two
splits and no merges, hence `Delta=2`.  This is not the invalid column-energy
identity rejected in the preceding lemma: both terms here count collisions
across row indices at fixed target `s`.

The next structural question is to express `Delta` as the affine-background
contribution plus the changes caused by the four defect transversals of `D`.
If Badness and the Latin diagonal force `Delta!=0`, the whole minimum-curvature
canonical layer is excluded.  If cancellation is possible, its exact signed
pattern should supply a new Latin seed.  Do not rerun the Latin annealing,
the three Hamming balls, or the fixed direct pair formula unchanged.

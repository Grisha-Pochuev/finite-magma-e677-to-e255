# E677 K5 periodic block gluing and completion boundary

Date: 2026-08-22.

Status:

```text
proved: the first degree-four periodic-port residue is a real K5 core;
proved: copies of this core glue at vertices into arbitrarily large exact
        closed periodic-port partial structures;
therefore: degree/triangle/port accounting alone cannot close CYCLE;
checked exactly: one block completes to the Good order-5 E677 table;
checked exactly: the two-block order-9 and three-block-chain order-13 cores
                 have no full E677 completion, even when Good is allowed;
checked exactly: a proper one-block completion of orders 6,7,8,9 is UNSAT;
bounded only:   the first two-layer threshold, order 10, is UNKNOWN(180s).
```

## The K5 core is real

On labels `0,...,4`, prescribe the following table.  First ignore the five
diagonal cells.

```text
    0 1 2 3 4
0 : - 2 1 4 3
1 : 3 - 4 0 2
2 : 4 3 - 1 0
3 : 2 4 0 - 1
4 : 1 0 3 2 -
```

For each row `a`, the displayed map `p_a` is a fixed-point-free permutation
of the other four labels.  Put

```text
P5={(a,u):a!=u}.
```

On these twenty states, all of the state maps used in the genuine-cycle
port reduction remain inside `P5`:

```text
A0(a,u) =(a,a*u),
Phi(a,u)=(a,a\u),
Psi(a,u)=(a*u,a),
J(a,u)  =(u,a),
tau(a,u)=(a*u,(a*u)\u).
```

The restricted `tau` map is a permutation.  Its cycles are

```text
(0,1) (2,3) (1,0) (3,2)
(0,2) (1,4) (2,0) (4,1)
(0,3) (4,2) (3,0) (2,4)
(0,4) (3,1) (4,0) (1,3)
(1,2) (4,3) (2,1) (3,4).
```

Every left-division E677 instance on two distinct labels closes inside the
displayed cells and holds.  Equivalently, filling the diagonal by

```text
a*a=a
```

gives the complete table displayed above with `-` replaced by its row
label, and direct verification on all `25` ordered pairs proves E677.  All
five points of this completion are Good.

The degree-four object left by the canonical-port lemma is therefore not a
spurious counting equality.  It is realized by an actual E677 magma once
the diagonal is Good.

An exact enumeration of the `9^5` choices of fixed-point-free neighbor
permutations on labelled `K5` finds exactly six local E677 systems.  The
table above has automorphism group of order `20`, so these six systems form
one relabelling orbit.  This enumeration is diagnostic; the displayed
table itself is the proof of existence.

## Arbitrarily large local block gluings

Take copies of the displayed five-point core and glue their vertex sets so
that two blocks meet in at most one vertex.  A tree of blocks is enough.
At a shared vertex `a`, the four-neighbor sets contributed by the incident
blocks are disjoint.  Define `p_a` as the disjoint union of the corresponding
four-point row permutations.

There is no row collision.  For a state `(a,u)` belonging to one block,
all values and divisions in `A0,Phi,Psi,J,tau` stay in that same block.
Likewise, the left-division form

```text
q\(p\q)=(p*q)*p
```

for `p,q` in one block uses only that block and is the verified K5 identity.
Consequently the union `P` of all oriented block edges is a closed union of
genuine `tau` cycles and satisfies every local equation used in the
periodic-port graph argument.

For example, two blocks sharing one vertex have `9` labels, `40` oriented
states, and ten genuine `tau` cycles of length four.  More blocks give
connected examples of unbounded size.  These are partial multiplication
systems, not magmas and not counterexamples: diagonal cells and products
between different blocks have not been assigned.

This proves the negative boundary

```text
closed periodic graph + degree >=4 + every edge in a forced triangle
does not imply an EXIT, ZERO, merger, or contradiction locally.          (1)
```

In particular, charging the four ports of a high-degree row to merger
fibres cannot be the sole next invariant.  In the block cores, `tau` is
already a permutation and has no internal merger at all.

## Exact full-completion tests

The script

```text
tools/e677_k5_block_tree_completion_sat.py
```

fixes the displayed block cells, enforces permutation rows, encodes every
E677 pair, decodes every SAT result, and verifies it independently.

The exact results are

```text
one block, order 5, Good allowed:       SAT, the displayed Good table;
two-block chain, order 9, Good allowed: UNSAT;
three-block chain, order 13, Good allowed: UNSAT.                 (2)
```

A separate proper-extension test fixes just one off-diagonal block and
allows arbitrary Good points.  It gives

```text
order 6 (one outside label): UNSAT;
order 7 (two outside labels): UNSAT;
order 8 (three outside labels): UNSAT;
order 9 (four outside labels): UNSAT;
order 10 (five outside labels): UNKNOWN at 180 seconds.           (2a)
```

The sharp change at order 10 is only a search boundary.  It does not prove
that an extension exists there, and the size ladder must not be continued.
In particular, a Good direct-product extension exists at larger order, so
unconditional non-embeddability of the K5 core is false.

The two-block union has one universal shared vertex, so row bijectivity
already forces its diagonal cell `a*a=a`; nevertheless the stronger result
in (2) says that even a Good completion of all cross-block cells is
impossible.

Gating the E677 equations gives small inclusion-minimal pair cores relative
to all displayed block cells and the permutation-row axioms:

```text
order 9, blocks (0,1,2,3,4),(4,5,6,7,8):
  (0,5) (0,8) (1,5) (1,8) (2,5) (2,8) (3,5) (3,8);

order 13, add (8,9,10,11,12):
  (0,8) (1,1) (1,8) (2,8) (3,8) (8,1).         (3)
```

For the order-13 core, restricting row `8` to its forced five-element
complement carrier gives exactly five survivors for the four equations
with second variable `8`:

```text
01238, 01283, 01832, 08231, 81230.
```

Adding `(1,1)` leaves only `08231`; adding `(8,1)` leaves none.  This is an
exact explanation of that order-13 core, but it uses saturation of a
five-element complement and is not size-independent.  Adding one free
label (order 14) remains UNSAT, while its minimized pair core moves to a
different twelve-pair pattern.  Hence the six-pair carrier explanation is
not stable under extension.

For one block at order 9, pair-core deletion produced a 50-pair core with
all 50 deletion trials `UNKNOWN`; it contains no trustworthy minimal hand
pattern and must not be rerun.

All deletion trials in (3) were decided; there were no `UNKNOWN` trials.
An attempted minimization over the forty individual fixed cells was stopped
after it entered a hard completion subcase.  Do not rerun that minimization:
the useful structure is the cross-block pair core, not a smaller SAT proof.

## Correct continuation

The port graph itself is now exhausted as a strict invariant.  A valid next
step must use cells outside `P`.  The canonical choice is the family of
diagonal roots

```text
Delta_a=(a,a),
```

and the first cross-block/complement cell on each of their forward `tau`
paths.  For one isolated K5 block, row saturation forces every `Delta_a` to
be Good.  For a block gluing, the pair cores (3) show that E677 couples a
diagonal/complement row to a nonadjacent block before any local port count
can close.

The next hand target is therefore:

```text
derive one size-independent cross-block equation from the six-pair pattern
in (3), and show that its first complement return is either coloured/ZERO
or identifies two distinct inputs in one row.                         (4)
```

Do not continue by increasing the minimum degree, enumerating larger block
trees, or summing the same periodic branching surplus.

## Subsequent diagonal resolution

The size-independent diagonal continuation is now proved in

```text
lemmas/e677_diagonal_escape_from_periodic_tau_lemma.md.
```

In the fully reused periodic graph, self-E677 gives, with
`d=a*a,h=d*a`,

```text
L_a^2(h)=a.
```

Since the periodic neighbour set `U_a` is `L_a`-invariant and does not
contain `a`, this forces `h` outside `U_a`.  The one-cell word for `h*a=D(a)`
then creates a state `(h,h\a)` which cannot itself be periodic: periodicity
would force `h` back into `U_a`.  Its finite backward tree reaches a coloured
boundary or an actual ZERO root.  Thus K5 block gluings are no longer a
terminal CYCLE obstruction; no larger completion test is needed.

The bounded ground diagnostic

```text
tools/e677_k5_diagonal_collision_saturation.js
```

also records two tempting but unsupported local shortcuts.  In the bounded
complete core/diagonal root shell, neither the equality `a0*a0=a1*a1` nor a
single row first-return of length five forced a fixer or identified K5
vertices.  This negative diagnostic is not a consistency proof.  The actual
proof uses the global periodic-neighbour closure, as the diagonal-escape
lemma does.

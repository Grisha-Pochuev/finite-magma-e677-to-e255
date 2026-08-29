# E677 skew row-label extensions: base reach and two-pair boundary

Date: 2026-07-26.

## 1. Construction

Let `B` be the verified order-five E677 table.  On `B x F_5`, choose one
permutation `phi_i` of the base labels for every left fibre label and put

```text
(a,i)*(b,j)=(B[phi_i(a)][b], P[a,i,b](j)),
```

where every `P[a,i,b]` is an arbitrary permutation of the fibre.  Every left
row of the resulting order-25 table is a permutation.  Unlike an ordinary
cover, the induced base-block action depends on the left fibre coordinate.

The exact full formula and verifier are in

```text
tools/e677_skew_rowlabel_counterexample_sat.py.
```

## 2. Base-coordinate reachability

For a full E677 pair with base coordinates `a,b`, left fibre coordinates
`i,j`, and first intermediate fibre value `t`, the base-coordinate path is

```text
u = B[phi_j(b)][a],
v = B[phi_t(u)][b],
w = B[phi_i(a)][v],
z = B[phi_j(b)][w].
```

Hence a necessary condition is

```text
for every a,b,i,j, some t satisfies z=a.        (BASE-REACH)
```

For the power family `phi_i=theta^i`, the exact classifier

```text
tools/e677_skew_rowlabel_base_reach.py
```

checks all `120` permutations `theta`.  Exactly `25` survive: the identity
and all `24` five-cycles.  The `95` failures split exactly as

```text
transposition:       10
double transposition:15
3-cycle:             20
3-cycle times 2-cycle:20
4-cycle:             30.
```

The order-five base has `20` automorphisms, transitive on its labels.  Their
conjugation action has two orbits on the five-cycles, of sizes `20` and `4`.
The full E677 formula, with no Bad requirement, is UNSAT for a representative
of each orbit.  Thus every nonidentity power family is closed; identity is
the already parked ordinary-cover case.

## 3. Arbitrary anchored families

For a set `S` of at most five base permutations, `BASE-REACH` is the exact
finite closure condition

```text
for all alpha,beta in S and a,b,
some gamma in S returns the displayed path to a.
```

The classifier

```text
tools/e677_skew_rowlabel_family_reach_sat.py
```

uses one Boolean variable per permutation and an exact cardinality counter.
After excluding the six cyclic power sets, an anchored family containing the
identity has the complete classification

```text
at most 2 maps: UNSAT;
at most 3 maps: UNSAT;
at most 4 maps: UNSAT;
5 maps: exactly three automorphism orbits, of sizes 20,10,20.
```

Representatives are

```text
01234/12403/20341/34012/43120
01234/14320/20143/32401/43012
01234/10342/24103/32410/43021.
```

All three exact full order-25 formulas are UNSAT even when Good models are
allowed.  Therefore the arbitrary anchored row-label class is completely
closed.

## 4. Unanchored classification

When the identity permutation is forbidden, `BASE-REACH` again excludes
families with at most four distinct maps.  At size five it has exactly `75`
automorphism orbits.  Three representatives used for structural diagnosis
are

```text
04123/10342/21034/32410/43201
02341/14023/20134/31402/43210
04312/12043/20134/31420/43201.
```

Each of these full E677 formulas is strictly UNSAT without imposing Badness.
Selector minimization reduces every failure to two base pairs of the common form

```text
(a,a), (a,b).
```

For the three displayed representatives the cores are respectively

```text
{(2,2),(2,4)}, {(0,0),(0,3)}, {(2,2),(2,4)}.
```

Each pair alone is satisfiable.  The obstruction is therefore not
`BASE-REACH` but a joint two-pair permutation/Hall condition on their shared
fibre blocks.  In all three cores the intersection has the identical
30-block form

```text
P[a,i,c] for all five i and all five base inputs c;  (25 blocks)
P[b,i,a] for all five i.                         (5 blocks)
```

Thus all nonshared fibre permutations can be existentially eliminated.  The
missing invariant is a compatibility criterion on these five complete rows
over `a` plus the single incoming block family from `b`.

Parity does not explain the obstruction: two independent pair models can
agree on the signs of all 30 shared permutations.  They can even agree on
the full cycle type of every shared permutation.  Thus sign and conjugacy
profile are exact negative boundaries and must not be reused.

Exact equality minimization is much sharper.  For each of the three
representatives, a single shared permutation already separates the two
pairs:

```text
family 1: block P[4,1,2]
          pair (2,2): 24 possibilities, exactly P(0)=4
          pair (2,4): unique 32410, hence P(0)=3;

family 2: block P[3,3,0]
          pair (0,0): 24 possibilities, exactly P(1)=0
          pair (0,3): unique 13420, hence P(1)=3;

family 3: block P[4,0,2]
          pair (2,2): 24 possibilities, exactly P(2)=4
          pair (2,4): unique 14302, hence P(2)=3.
```

So the diagnosed two-pair Hall obstruction is an actual one-cell collision,
not a coarse counting defect.

After obtaining that criterion, the unanchored `BASE-REACH` enumeration was
completed.  It has exactly `75` automorphism orbits.  A single combined
classifier ran the exact full order-25 E677 formula for every orbit, allowing
Good models and using a five-second bound per orbit.  The complete result is

```text
75/75 UNSAT;
0 Good E677 models;
0 UNKNOWN.
```

Together with the two nonidentity power orbits and three arbitrary anchored
orbits, this closes `80/80` nontrivial row-label orbit formulas.  Families
with fewer than five distinct maps were already excluded by `BASE-REACH`;
the constant nonidentity case is included there.  The only surviving row-map
family is the constant identity family, which is precisely the parked
ordinary permutation-cover construction.

Thus the entire nontrivial skew row-label class is closed.  No E677 model or
counterexample was found.

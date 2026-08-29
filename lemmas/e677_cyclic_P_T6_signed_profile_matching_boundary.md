# E677 cyclic P: T6 signed, profile, and matching boundary

Date: 2026-07-26.

Status:

```text
signed collision balance is too weak; full block-size profiles can match,
but no degree-matched profile seed occurred in 14.2 million coherent cases;
the exact uniform matching relaxation remains UNKNOWN
```

## 1. Signed partition defect is not an obstruction

For fixed target `s`, let

```text
C(w_s)=sum_blocks binomial(block_size,2),
Delta_s=C(z_s)-C(rho_s),
Delta=sum_s Delta_s.
```

Both collision counts are across row indices at the same target.  Thus this
is a valid necessary T6 invariant, unlike the previously rejected comparison
of row and column collision energies.

The exact coherent-seed scanner

```text
tools/e677_fiber7_T6_signed_partition_defect_scan.py
```

generated nonlinear Latin/Q tables and evaluated all `720` normalized `A`
and four canonical `D`.  On one bounded sample it checked

```text
50 reduced Latin bases;
4911 admissible labelled O tables;
14,143,680 triples (O,A,D).
```

It found

```text
450,988 cases with scalar Delta=0;
297 cases with Delta_s=0 for all seven s.
```

Therefore neither the scalar nor the seven-vector signed balance is the
missing obstruction.  The best exact pair-kernel score among the zero-vector
cases in this sample was `20/147`.  These sample counts are diagnostics, not
universal existence or exclusion theorems.

## 2. Full fibre-size profile

For a partition of seven points define

```text
C2=sum_B binomial(|B|,2),
C3=sum_B binomial(|B|,3).
```

The pair `(C2,C3)` uniquely determines the block-size profile of a partition
of seven.  This follows by checking the fifteen integer partitions of seven;
the only collisions in `C2` are separated by `C3`.

The exact finite classifier

```text
tools/e677_fiber7_T6_partition_profile_scan.py
```

requires equality of `C2,C3` for `z_s` and `rho_s` at every target.  On a
bounded sample of

```text
50 reduced bases;
4931 labelled O tables;
14,201,280 triples (O,A,D),
```

only `155` triples matched all seven profiles.  The best remaining exact
pair-placement defect was `20/147`, at

```text
D=0125634,
A=0342651,
O7=4501326/2104635/4325016/6045312/6120435/3460521/1236450.
```

For this seed, every target has

```text
C2=2, C3=0,
profile (2,2,1,1,1).
```

Thus each target defines a matching of two disjoint edges on the seven row
vertices.  There are fourteen colored edges in total.  The score `20` means
that the `z` and `rho` matching systems share only four of their fourteen
colored edges.

## 3. Matching-degree obstruction

Forget the target colors but retain row vertices.  For each row `t`, put

```text
d_z(t)=number of z-matching edges incident with t,
d_rho(t)=number of rho-matching edges incident with t.
```

Every exact T6 core must have `d_z(t)=d_rho(t)` for all seven rows.  Among the
same `155` all-target profile matches, the classifier found

```text
0/155 degree-vector matches.
```

This is a meaningful negative empirical boundary, but not a proof that degree
matching is impossible.

The exact uniform-profile formula

```text
tools/e677_fiber7_T6_uniform_two_pair_profile_sat.py
```

requires the true pair-kernel condition together with profile
`(2,2,1,1,1)` at every target.  For fixed `D=0125634` it is `UNKNOWN` at
`180.628` seconds.

The weaker exact relaxation

```text
tools/e677_fiber7_T6_uniform_profile_degree_relaxation_sat.py
```

requires only:

```text
both sides have two disjoint edges at every target;
the seven uncolored vertex degrees agree.
```

The first sequential-counter encoding was `UNKNOWN` with `26,940` variables.
Using one incidence bit per `(row,target)` reduces it equivalently to

```text
3,028 variables;
33,882 clauses.
```

It is still `UNKNOWN` for `D=0125634` after `182.718` seconds.  These two
degree-formula runs are retired and must not be extended.

## 4. Exact continuation

Classify the possible fourteen-edge matching multigraphs by hand or by a
small graph enumerator that does not contain `O,A,D`.  The Latin side has

```text
{t,u} in M_s  iff  O_t^(-1)(s)=O_u^(-1)(s),
sum_s |M_s|=14,
```

and the relative maps obey the triangle cocycle and shifted-derangement law.
The rho side has the same two-edge color sizes in the uniform layer.  The
next target is a theorem restricting the possible degree sequences or edge
multiplicities on one side enough to separate them.

Do not rerun the signed scan, profile scan, uniform full formula, or either
degree encoding unchanged.  Computation should next check only a named graph
identity derived without the magma variables.

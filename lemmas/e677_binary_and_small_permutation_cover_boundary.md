# E677 permutation covers: binary theorem and small-fibre boundary

Date: 2026-07-26.

## 1. Cover construction

Let `B` be a finite E677 magma satisfying E255.  A permutation cover with
fibre `F` has underlying set `B x F` and operation

```text
(a,i)*(b,j)=(a*b, P[a,i,b](j)),
```

where every `P[a,i,b]` is a permutation of `F`.

For `F=F_2`, write

```text
P[a,i,b](j)=j+c(a,b,i).
```

## 2. Binary covers preserve E255

Fix `x` in the base and put

```text
p=x*x, q=p*x, r=x*q.
```

Base E255 gives `q*x=x`.  E677 at the base pair `(x,q)` gives `q*(x*r)=x`;
row injectivity against `q*x=x` yields `x*r=x`.

For the five Boolean maps

```text
A(j)=c(q,x,j), P(t)=c(x,q,t), C(t)=c(x,r,t),
F(t)=c(x,x,t), G(t)=c(p,x,t),
```

the fibre coordinate of E677 at `(x,q)` is

```text
P(i+A(j))+C(i)+A(j)=i+j.                       (1)
```

If `A` were constant, (1) would have a left side independent of `j` and a
right side depending on `j`.  Hence `A(j)=j+a`.  Equation (1) then forces

```text
P(t)=p0, C(i)=i+a+p0.
```

The fibre coordinate at `(x,x)` is

```text
G(i+F(j))+P(i)+C(j)=i+j,
```

so

```text
G(i+F(j))=i+a.                                  (2)
```

If `F` were nonconstant, varying `j` would make `G` constant on both bits,
and varying `i` would give the opposite constant.  Therefore `F=f0` and

```text
G(t)=t+f0+a.
```

Starting from `(x,i)`, the three successive right multiplications by itself
have fibre coordinates

```text
i+f0,  a,  i+A(a)=i.
```

Thus every point of every binary permutation cover satisfying E677 also
satisfies E255.

## 3. Exact higher-fibre boundary over the order-11 base

The general cover formula was encoded by

```text
tools/e677_permutation_cover_counterexample_sat.py
```

over the verified Good order-11 table `cache/eq677-db/11/0`.  Every fibre
map is an arbitrary permutation; every E677 instance is exact; each possible
lifted Bad target is tested and any SAT table is decoded and checked in full.

Complete results are

```text
fibre 2, order 22: 22/22 Bad targets UNSAT;
fibre 3, order 33: 33/33 Bad targets UNSAT;
fibre 4, order 44: 44/44 Bad targets UNSAT.
```

There were no UNKNOWN cases.  Fibre 2 independently audits the manual
theorem.  Fibre 3 and 4 are exact only for this named base and are not a
size-independent theorem.

The next structural question is not fibre 5.  For a fixed Good base point,
write `q=((x*x)*x)` and study the family of permutations induced by rows over
`q` on the fibre over `x`.  Either E677 forces one of those permutations to
fix each fibre point, proving all such covers Good, or an abstract
fixed-point-free fibre system supplies a precise seed for the next
counterexample construction.

## 4. Local fixed-point system

Put

```text
p=x*x, q=p*x, r=x*q.
```

Base Goodness and E677 imply `q*x=x` and `x*r=x`.  For the fibre permutation
families

```text
A_j=P[q,j,x], B_i=P[x,i,q], C_i=P[x,i,r],
F_j=P[x,j,x], G_i=P[p,i,x],
```

the lifted E677 instances at `(x_i,q_j)` and `(x_i,x_j)` are exactly

```text
A_j(C_i(B_{A_j(i)}(j)))=i,                     (L1)
C_j(B_i(G_{F_j(i)}(j)))=i.                     (L2)
```

A Bad lifted point over fibre value zero requires

```text
A_j(0)!=0 for every j.
```

The exact local formula `tools/e677_cover_local_fixer_sat.py` gives

```text
fibre 2: UNSAT;
fibre 3: UNSAT;
fibre 4: SAT, with an audited fixed-point-free local seed;
fibre 5: SAT, with an audited fixed-point-free local seed.
```

Thus `(L1),(L2)` force a fixer only in fibres two and three.  The fibre-five
seed is stored in `lemmas/e677_cover_local_seed_k5.txt`; it is a local object,
not a magma table.

## 5. The missing `(r,x)` pair

For the order-seven base `cache/eq677-db/7/0` and target `x=5`, the four roles

```text
x=5, p=4, q=6, r=3
```

are distinct.  Fixing the fibre-five local seed in the full cover is exactly
UNSAT.  A selector-core computation reduces the failure to the single
additional base pair `(r,x)=(3,5)`.  Its path is

```text
x*r=x, (x*r)*x=p, r*p=q, x*q=r.
```

Writing `K_i=P[r,i,p]`, its fibre equation is

```text
B_j(K_i(F_{C_j(i)}(j)))=i.                     (L3)
```

For fixed `i`, eliminate `K_i` by putting

```text
U_i(j)=F_{C_j(i)}(j),
V_i(j)=B_j^-1(i).
```

A permutation `K_i` exists exactly when

```text
U_i(j)=U_i(k) iff V_i(j)=V_i(k)                 (KERNEL-rx)
```

for every `j,k`.  This is the precise new global obstruction.  Two exact
encodings of `(L1)--(L3)`, direct and kernel-eliminated, both reached the
fixed 60-second `UNKNOWN` boundary at fibre five.  They are retired rather
than lengthened.

## 6. Idempotent-fibre obstruction and order 35

If a base point `e` is idempotent, the fibre over `e` is a closed E677
submagma.  Therefore a uniform cover with fibre order `k` requires an E677
magma of order `k` independently of the intended Bad point.

The base-pair core at fibre four is one idempotent pair in each order-seven
base:

```text
base 7/0, target x=5: core {(q,q)}, q=6;
base 7/1, target x=5: core {(p,p)}, p=6.
```

This explains the complete fibre `2,3,4` exclusions without treating them as
evidence for a general cover fixed-point theorem.  Fibre five is the first
available layer because `cache/eq677-db/5/0` is a verified E677 model.

Two named order-35 completions were then tested with that fibre table fixed
over the relevant idempotent point:

```text
base 7/0, target (5,0), fibre over q fixed: UNKNOWN at 180 seconds;
base 7/1, target (5,0), fibre over p fixed: UNKNOWN at 180 seconds.
```

The first fixed local fibre-five seed is UNSAT already at `(r,x)`; it must not
be reused.  The two full order-35 runs and the two `(L1)--(L3)` encodings are
retired.  No counterexample was found.

The uniform permutation-cover route is now parked.  A genuinely new
constructive family must let the induced permutation of base blocks depend
on the left fibre coordinate; otherwise the same closed idempotent fibre and
`KERNEL-rx` mechanisms recur.

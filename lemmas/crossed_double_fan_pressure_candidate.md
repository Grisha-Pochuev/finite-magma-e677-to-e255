# Crossed Double-Fan Pressure Candidate

Date: 2026-06-09.

Status:

```text
candidate / strong finite evidence / not proved
```

## Structural Question

Fix distinct values `a,b`. Can both opposite source fibers be nontrivial?

```text
F(a,b)={p : p*a=b}
F(b,a)={r : r*b=a}
```

The candidate is:

```text
min(|F(a,b)|, |F(b,a)|) <= 1.
```

Equivalently, in the oriented graph `A_b(q)->R_b(q)`, a vertex `a` cannot
simultaneously have:

```text
at least two outgoing incidences;
at least two incoming incidences.
```

This is called the crossed double-fan exclusion.

## Forced Double Pressure

Assume:

```text
p*a=b
q*a=b
p!=q
```

and define:

```text
c=p*b
d=q*b
h=pred_b(a).
```

The common-edge fan lemma gives:

```text
c!=d
c*p=d*q=h
b*h=a.
```

Assume also:

```text
r*b=a
s*b=a
r!=s
```

and define:

```text
u=r*a
v=s*a
k=pred_a(b).
```

The opposite fan gives:

```text
u!=v
u*r=v*s=k
a*k=b.
```

Thus the hypothetical crossed configuration creates two opposite
two-sided fans:

```text
rows p,q:  ... -> a -> b -> c,d -> h
rows r,s:  ... -> b -> a -> u,v -> k.
```

Each of its four primary edges also carries the complete certificate from:

```text
double_interval_edge_certificate_lemma.md
```

The unresolved proof step is to show that iterating those four certificates
forces two source rows to acquire the same ordered two-step interval.

## Finite Evidence

The crossed configuration was tested as an arbitrary E677 model, without the
bad-element restriction:

```text
2*0=1
3*0=1
4*1=0
5*1=0.
```

After correcting the row-0 normalization audit, complete raw-label searches
returned:

```text
size 6: none, 0.28s
size 7: none, 13.28s
```

The size-496 model at target `b=0` has endpoint multiplicity pairs:

```text
(A-degree,R-degree) in
  (0,1), (1,0), (1,1), (1,16), (16,1).
```

It has no `(16,16)` vertex. The checked affine models have degree pair
`(1,1)` at every used vertex.

These are supporting observations, not a proof. Earlier size-8 and size-9
claims used canonical row-0 representatives together with independently fixed
role labels. That double normalization was invalid and those claims are
withdrawn.

## Relation To The Pseudoforest Frontier

Crossed double-fan exclusion alone does not prove that every component is a
pseudoforest. A directed barbell can still have:

```text
one split vertex with outdegree > 1 and indegree = 1;
one merge vertex with indegree > 1 and outdegree = 1.
```

However, every connected bicyclic obstruction has a branching vertex in its
two-cycle core. At least two incidences at that vertex have the same
orientation, hence form one of the two common-edge fans above.

```text
one fan creates at least two branches;
the finite core transports both branches;
then they either merge, enter two different cycles, or enter one cycle at
different places.
```

The next general target is therefore:

```text
Branch-Closure No-Free-Tail Lemma.

The complete edge certificates transported from two branches of one fan force
an aligned two-step overlap before the two branches can merge or close
cyclically.
```

This is narrower than the original unconstrained pseudoforest conjecture and
matches the recursive double-interval pressure mechanism directly.

## Boundary

Do not promote crossed double-fan exclusion to a lemma until the four
certificate families are closed symbolically. The valid finite evidence is
only the raw-label size-6 and size-7 table above.

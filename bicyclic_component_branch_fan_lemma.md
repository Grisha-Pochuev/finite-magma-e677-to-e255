# Bicyclic Component Branch-Fan Lemma

Date: 2026-06-09.

Status:

```text
general proved / graph reduction
```

## Setup

Fix `b`. Give every edge of the graph:

```text
H_b: A_b(q)--R_b(q)
```

its natural orientation:

```text
A_b(q) -> R_b(q).
```

The source row `q` contains:

```text
A_b(q) -> b -> R_b(q).
```

Two distinct rows cannot give the same oriented edge, because the ordered
two-step interval reconstructs its source.

## Statement

If a connected component of `H_b` contains at least two independent cycles,
then its cycle core contains a vertex `v` with at least two incident core
edges oriented in the same direction at `v`.

Consequently, every failure of the pseudoforest conjecture contains one of
the following core fans.

Outgoing branch fan:

```text
p*v=b, p*b=c
q*v=b, q*b=d
p!=q
c!=d.
```

Incoming branch fan:

```text
p*a=b, p*b=v
q*e=b, q*b=v
p!=q
a!=e.
```

The two selected edges belong to the cycle core. They are not disposable
tree leaves.

## Proof

Repeatedly delete vertices of undirected degree `0` or `1` from the component.
This does not change its number of independent cycles. The remaining
two-core therefore still has at least two independent cycles.

If every vertex of that core had degree exactly `2`, every connected core
component would be a single cycle and would have only one independent cycle.
Hence some core vertex `v` has degree at least `3`.

Every incident edge either enters or leaves `v`. By the pigeonhole principle,
at least two of the at least three incidences have the same orientation.

If two leave `v`, their source rows share:

```text
v -> b.
```

The common-edge fan lemma gives distinct tips:

```text
c!=d
```

and the common return:

```text
c*p=d*q=pred_b(v).
```

Writing:

```text
h=pred_b(v),
```

we also have:

```text
b*h=v.
```

Thus the outgoing branch changes the target from `b` to `v`: in the graph
`H_v`, the edge indexed by row `b` begins at `h`.

If two enter `v`, their source rows share:

```text
b -> v.
```

The two-sided common-edge fan lemma gives distinct backward feet:

```text
a!=e,
```

distinct forward tips:

```text
p*v!=q*v,
```

and the common return:

```text
(p*v)*p=(q*v)*q=pred_v(b).
```

But:

```text
pred_v(b)=A_b(v).
```

Therefore an incoming branch has a canonical next edge in the same graph
`H_b`, namely the edge indexed by row `v`:

```text
A_b(v) -> v*b.
```

So the two branch orientations have different transport rules:

```text
incoming branch at v -> same target b, next source row v;
outgoing branch at v -> new target v, distinguished source row b.
```

Because the selected incidences lie in the two-core, both continue through
the cyclic part of the component.

## Consequence For No-Free-Tail

The pseudoforest conjecture no longer needs to be attacked as an arbitrary
edge-count statement. Any counterexample to it supplies:

```text
one genuine common-edge fan;
two branches already trapped in the finite cycle core;
one complete edge certificate on every step of both branches.
```

Thus the exact remaining graph target is:

```text
two core branches born from one fan cannot both close without producing the
same ordered two-step interval in two distinct source rows.
```

Equivalently, one must rule out an endless finite alternation of:

```text
same-target bridge steps at incoming branch points;
target-changing hub steps at outgoing branch points.
```

This is the branch-closure form of the No-Free-Tail problem.

## Boundary

This lemma finds the forced fan but does not yet prove that its two core
branches collide. That termination step remains open.

# Bad-Target Core-Fan Lemma

Date: 2026-06-09.

Status:

```text
general proved / global bad-element consequence
```

## Setup

Let `M` be a finite E677 magma of size `n`. Fix an element `b` for which E255
fails.

The standard bad-element consequence is:

```text
q*b!=b
```

for every row `q`.

Build the oriented graph:

```text
H_b:
  A_b(q) -> R_b(q)=q*b
```

with one edge for every row `q`.

## Edge Count

The right endpoint never equals `b`:

```text
R_b(q)=q*b!=b.
```

The left endpoint also never equals `b`. Indeed:

```text
A_b(q)=b
```

would mean:

```text
q*b=b,
```

which is impossible for bad `b`.

Therefore all `n` graph edges lie on at most:

```text
n-1
```

vertices.

Let the nonempty connected components have vertex and edge counts:

```text
V_i,E_i.
```

Then:

```text
sum E_i=n
sum V_i<=n-1.
```

If every component had at most one independent cycle, then:

```text
E_i<=V_i
```

for every `i`, hence:

```text
n=sum E_i<=sum V_i<=n-1,
```

a contradiction.

Thus at least one component contains at least two independent cycles.

## Forced Core Fan

Apply:

```text
bicyclic_component_branch_fan_lemma.md
```

to that component. Its cycle core contains a vertex `v` and two core edges
with the same orientation at `v`.

Hence every hypothetical bad target forces one of two configurations.

Outgoing core fan:

```text
p*v=b, p*b=c
q*v=b, q*b=d
p!=q
c!=d
c*p=d*q=pred_b(v).
```

Incoming core fan:

```text
p*a=b, p*b=v
q*e=b, q*b=v
p!=q
a!=e
p*v!=q*v
(p*v)*p=(q*v)*q=pred_v(b)=A_b(v).
```

Both chosen graph edges lie in the cycle core, so both branches participate
in cyclic closure.

## Significance

This removes an earlier gap in the double-interval strategy:

```text
a bad element does not merely force some column collision;
it forces a two-sided common-edge fan whose two selected branches already
belong to a finite bicyclic core.
```

The remaining No-Free-Tail problem is now exactly:

```text
prove that the two core branches of this forced fan cannot both close under
the complete edge-certificate transport.
```

The third core incidence at the branch vertex is retained and classified in:

```text
bicyclic_core_junction_lemma.md
```

It reduces the closure problem to a triple core fan or a mixed `2+1` junction.

If that branch-closure statement is proved, the bad target cannot exist and
E255 follows.

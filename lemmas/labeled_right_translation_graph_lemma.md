# Labeled Right-Translation Graph Lemma

Date: 2026-06-09.

Status:

```text
general proved / graph form of double-interval pressure
```

## Graph

Fix `b`. Build the functional graph:

```text
q -> R_b(q)=q*b.
```

Label every vertex `q` by:

```text
A_b(q)=the unique a with q*a=b.
```

Equivalently, the directed edge leaving `q` carries the interval:

```text
A_b(q) -> b -> R_b(q)
```

in row `q`.

## Incoming Labels Are Distinct

Suppose two distinct vertices enter the same point:

```text
x*b=Q
y*b=Q
x!=y.
```

If their labels were equal:

```text
A_b(x)=A_b(y)=a,
```

then rows `x,y` would contain the same ordered interval:

```text
a -> b -> Q.
```

Two-step source reconstruction would force:

```text
x=y,
```

a contradiction.

Therefore all incoming edges at a graph vertex have pairwise distinct labels.

## Label Fibers Are Fans

Conversely, suppose:

```text
A_b(x)=A_b(y)=a
x!=y.
```

Then:

```text
x*a=b
y*a=b.
```

So `x,y` belong to the common-edge fan `F(a,b)`, and their graph successors
are distinct:

```text
R_b(x)!=R_b(y).
```

Thus the two coordinate collisions are dual:

```text
same graph successor -> different labels;
same label           -> different graph successors.
```

## First Cycle Entry

A tail entering a cycle creates a graph vertex with two incoming edges:

```text
one from the tail;
one from the cycle.
```

Their labels are distinct. These two incoming rows form the two-sided fan over:

```text
b -> Q.
```

The common hub of that fan is the label of `Q`:

```text
A_b(Q).
```

## Boundary

This graph theorem explains exactly why one free tail cannot survive in a
finite target graph. It does not by itself forbid a tower that changes the
target:

```text
b -> Q -> R -> ...
```

The bad-cycle proof must show that the distinguished initial label
`r_{m-2}` in the terminal-source interval cannot be lost through these target
changes.


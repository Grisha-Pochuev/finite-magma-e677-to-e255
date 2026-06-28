# Right-P Orbit Collision Duality Lemma

Date: 2026-06-09.

Status:

```text
general proved / classifies both coordinate collisions in the double interval
```

## Setup

Let two distinct rows satisfy:

```text
x*a=P
y*b=P
x!=y.
```

Define their next right-`P` orbit points:

```text
X=x*P
Y=y*P.
```

Thus the two active intervals are:

```text
row x: a -> P -> X
row y: b -> P -> Y.
```

## Predecessor Collision

Assume:

```text
a=b=w.
```

Then rows `x,y` share:

```text
w -> P.
```

The common-edge fan lemma gives:

```text
X!=Y
X*x=Y*y=pred_P(w).
```

This is exactly the earlier bridge-collision expansion.

So a collision in the predecessor coordinate forces separation in the next
right-orbit coordinate.

## Orbit Merger

Assume instead:

```text
X=Y=T.
```

Then rows `x,y` share:

```text
P -> T.
```

The two-sided common-edge fan lemma gives:

```text
a!=b
x*T!=y*T
(x*T)*x=(y*T)*y=pred_T(P).
```

Indeed, the backward feet of the common edge `P -> T` are exactly `a,b`,
because:

```text
x*a=P
y*b=P.
```

So a collision in the next right-orbit coordinate forces separation in the
predecessor coordinate and creates the dual common-edge fan.

## Mutual Exclusion

For distinct `x,y`, the equalities:

```text
a=b
X=Y
```

cannot hold simultaneously. Otherwise rows `x,y` would contain the same
ordered interval:

```text
a -> P -> X,
```

and two-step source reconstruction would force `x=y`.

Therefore every collision of two active double intervals has one of two
opposite forms:

```text
same predecessor, different next orbit point;
same next orbit point, different predecessor.
```

Both forms create a common-edge fan and a common return hub.

## Relevance To No-Free-Tail

At every level of several source-started right-`P` orbits, track:

```text
(q_i,a_i)
```

where:

```text
q_i*a_i=P
q_{i+1}=q_i*P.
```

Then:

```text
collision among a_i
  -> fan over a_i -> P;

collision among q_{i+1}
  -> fan over P -> q_{i+1};

no collision in either coordinate
  -> both coordinate families remain separated.
```

Thus a putative free tail must avoid two different fan-generating collision
mechanisms at every generation, not only repeated bridge values.


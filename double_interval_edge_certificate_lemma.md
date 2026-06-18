# Double-Interval Edge Certificate Lemma

Date: 2026-06-09.

Status:

```text
general proved
```

## Statement

Fix a target `b`. Let one row `q` carry:

```text
q*a=b
q*b=c.
```

Equivalently, this is the oriented edge:

```text
a -> c
```

of the graph `A_b(q)--R_b(q)`.

Define:

```text
h=c*q
u=q*c
w=u*q=(q*c)*q
beta=a*(b*q).
```

Then the following cells are forced:

```text
row q:
  beta -> a -> b -> c

row c:
  q -> h
  w -> b

row b:
  h -> a.
```

Thus every graph edge has the full certificate:

```text
q*a=b
q*b=c
c*q=h
b*h=a
c*w=b
q*beta=a.
```

In predecessor notation:

```text
h=pred_b(a)
w=A_b(c).
```

## Proof

The ordered interval:

```text
q*a=b
q*b=c
```

and Lemma 13.1(iii) give:

```text
b*(c*q)=a.
```

Hence:

```text
h=c*q=pred_b(a).
```

Apply the same identity to the edge:

```text
q*b=c.
```

It gives:

```text
c*((q*c)*q)=b.
```

Therefore:

```text
w=(q*c)*q
c*w=b,
```

so `w=A_b(c)`.

Finally, the edge-predecessor triangle applied to:

```text
q*a=b
```

gives:

```text
q*(a*(b*q))=a.
```

Thus:

```text
beta=a*(b*q)
q*beta=a.
```

All displayed cells follow.

## Significance

The graph edge `a--c` is not only a pair of endpoints. It carries two linked
double intervals:

```text
beta -> a -> b -> c
w    -> b          in row c,
```

plus the return:

```text
c -> h -> a
```

through rows `c` and `b`.

The bridge recursion is therefore intrinsic to every edge:

```text
the right endpoint c immediately supplies the next predecessor A_b(c)=w.
```

This is the local certificate to use when comparing two cycles in one
component. No unproved right cancellativity is used.

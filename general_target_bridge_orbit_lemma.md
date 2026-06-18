# General-Target Bridge Orbit Lemma

Date: 2026-06-09.

Status:

```text
general proved / arbitrary common-edge version of bridge recursion
```

## Setup

Fix a target `b`. For every row `q`, define:

```text
A_b(q)=the unique a with q*a=b
R_b(q)=q*b.
```

The first map exists because every left row is a permutation.

Thus every row has the interval:

```text
A_b(q) -> b -> R_b(q).
```

## Bridge Recursion

Let:

```text
q_{i+1}=R_b(q_i)=q_i*b
a_i=A_b(q_i).
```

Then:

```text
q_i*a_i=b.
```

E677 with `x=b,y=q_i` gives:

```text
b=(q_i*b)*((q_i*(q_i*b))*q_i).
```

Therefore:

```text
a_{i+1}=(q_i*q_{i+1})*q_i.
```

The bridge is exactly the next predecessor label.

## Row-b Return

The inverse edge chain for:

```text
q_i*a_i=b
```

gives:

```text
a_i=b*((q_i*b)*q_i)
   =b*(q_{i+1}*q_i).
```

Hence:

```text
q_{i+1}*q_i=pred_b(a_i).
```

Every state therefore has:

```text
row q_i:
  beta_i -> a_i -> b -> q_{i+1}

row b:
  pred_b(a_i) -> a_i,
```

where:

```text
beta_i=a_i*(b*q_i).
```

## Source-Fiber Return

Suppose:

```text
q_0*a=b.
```

Then:

```text
a_0=a.
```

At every later step:

```text
a_i=a
<=>
q_i*a=b
<=>
q_i in F(a,b).
```

Thus return of the predecessor label to `a` is exactly return of the orbit to
the original common-edge source fiber.

## First Repetition

If the orbit does not return to `F(a,b)`, choose its first repeated point:

```text
q_j=q_k=Q
0<j<k.
```

The two distinct predecessors:

```text
x=q_{j-1}
y=q_{k-1}
```

share:

```text
b -> Q.
```

They form a new two-sided common-edge fan. Its common hub is:

```text
pred_Q(b)=A_b(Q),
```

which is also the old state label:

```text
A_b(Q).
```

Indeed both names denote the unique `u` satisfying:

```text
Q*u=b.
```

So the edge change:

```text
a -> b
becomes
b -> Q
```

and transports the current predecessor label as the new fan hub.

## Significance

The bridge/cycle-entry mechanism is not special to `0 -> P`. It applies to
every common edge:

```text
a -> b.
```

The exact remaining No-Free-Tail problem is therefore a tower of labeled edge
changes:

```text
a_0 -> a_1
a_1 -> a_2
a_2 -> a_3
...
```

At each change, the new fan hub is the predecessor label of the repeated state
in the preceding target graph.

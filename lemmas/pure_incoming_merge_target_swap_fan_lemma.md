# Pure-Incoming Merge Target-Swap Fan Lemma

Date: 2026-06-17.

Status:

```text
general proved / boundary reduction for branch closure
```

## Setup

Fix a target `b`. In the graph `H_b`, suppose a vertex `z` has several
incoming incidences:

```text
p_i*x_i=b,
p_i*b=z
```

for `i=1,...,k`.

Graphically, these are incoming edges:

```text
x_i -> z
```

in `H_b`, all with the same target vertex `z`.

For each row define:

```text
U_i=p_i*z.
```

Then after changing target from `b` to `z`, the same row `p_i` gives in
`H_z`:

```text
p_i*b=z,
p_i*z=U_i.
```

So every incoming edge into `z` in `H_b` becomes an outgoing edge from `b` in
`H_z`:

```text
b -> U_i.
```

## Separation Of The New Tips

If two distinct incoming incidences have the same new tip:

```text
U_i=U_j,
```

then the two rows contain the same ordered two-step interval:

```text
b -> z -> U_i.
```

Indeed:

```text
p_i*b=z, p_i*z=U_i,
p_j*b=z, p_j*z=U_i.
```

By the two-step source reconstruction lemma:

```text
p_i=p_j.
```

Then row injectivity gives:

```text
x_i=x_j.
```

Thus distinct incoming incidences at `z` produce distinct outgoing tips after
the target swap:

```text
U_i!=U_j  for i!=j.
```

## Genuine First-Merge Form

For a genuine first merge of branches, the last inputs are not equal to the
merge vertex:

```text
x_i!=z.
```

In that case:

```text
U_i!=b.
```

Otherwise `U_i=b` would mean:

```text
p_i*z=b,
p_i*x_i=b,
```

and row injectivity would force:

```text
x_i=z,
```

contradicting genuine first arrival at `z`.

## Consequence

A pure incoming merge of degree at least three is not a new terminal boundary.
After target swap `b -> z`, it becomes a triple outgoing fan:

```text
b -> U_1,
b -> U_2,
b -> U_3
```

in `H_z`, with:

```text
U_1,U_2,U_3 pairwise distinct,
U_i!=b
```

in the genuine first-merge setting.

Therefore the pure-incoming boundary is reduced to the binary sink case:

```text
exactly two incoming branch incidences at z,
no outgoing continuation from z,
no third incoming incidence at z,
no loop z -> z.
```

This is now the only local first-merge shape not relayed back to a mixed
`2+1` junction or a triple outgoing fan.

## Relation To The Existing Relay Stage

The previous relay stage proved:

```text
first merge + outgoing continuation
=> mixed 2+1 or triple fan after target swap.
```

The present lemma adds:

```text
first merge + at least three incoming incidences
=> triple fan after target swap.
```

So the remaining branch-closure obstruction is not a general pure incoming
merge. It is specifically a binary pure incoming sink.

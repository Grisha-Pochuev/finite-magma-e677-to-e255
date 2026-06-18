# First-Merge Target-Swap Junction Dichotomy

Date: 2026-06-17.

Status:

```text
general proved / relay dichotomy for a first merge with outgoing continuation
```

## Setup

Fix a target `b`. Let two directed branches genuinely first merge at `z`:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
```

with:

```text
x!=z,
y!=z,
x!=y.
```

Let the cyclic core continue from `z` by an outgoing edge:

```text
t*z=b,
t*b=m.
```

Define:

```text
U=p*z,
W=q*z.
```

By first-merge separation:

```text
U!=W.
```

Also:

```text
U!=b,
W!=b.
```

Indeed, if `U=b`, then:

```text
p*z=b
p*x=b
```

and row injectivity gives `x=z`, contradiction. The proof for `W` is the
same.

## Dichotomy After Target Swap

Change the target from `b` to `z`.

The two merging rows always become two outgoing edges from `b` in `H_z`:

```text
p*b=z, p*z=U,
q*b=z, q*z=W.
```

Thus:

```text
b -> U
b -> W
```

with distinct tips.

Now split by the continuation edge from `z` in `H_b`.

### Case 1: non-loop continuation

If:

```text
m!=z,
```

then the continuation edge is:

```text
z -> m
```

in `H_b`. By target-swap duality, the same row `t` becomes an incoming edge
to `b` in `H_z`:

```text
theta -> b,
theta=z*(b*t).
```

Therefore in `H_z` the first merge relays to an outgoing-majority mixed
`2+1` junction:

```text
b -> U
b -> W
theta -> b.
```

### Case 2: loop continuation

If:

```text
m=z,
```

then in `H_b` the continuation is the loop:

```text
z -> z.
```

After target swap, row `t` gives:

```text
t*b=z,
t*z=b.
```

So in `H_z` it is the loop:

```text
b -> b.
```

Since:

```text
U!=W,
U!=b,
W!=b,
```

the three incidences:

```text
b -> U
b -> W
b -> b
```

form an outgoing triple fan at `b` in `H_z`.

## Conclusion

A genuine first merge with any outgoing continuation does not create a new
kind of obstruction. After swapping target `b -> z`, it relays to exactly one
of the two already known core junction types:

```text
non-loop continuation -> mixed 2+1 junction;
loop continuation     -> triple fan.
```

Thus the first-merge closure problem is closed under the same two-type split
as the original bicyclic core reduction.

## Boundary

This lemma assumes an outgoing continuation from the merge vertex in `H_b`.
If a first merge only has incoming or loop incidences in the undirected core,
that purely incoming core shape must be treated separately.

# First-Merge Degenerate Continuation Boundary

Date: 2026-06-17.

Status:

```text
general proved / boundary split for first-merge relay
```

## Setup

Fix a target `b`. Let two directed branches first merge at `z` with last
edges:

```text
p*x=b, p*b=z,
q*y=b, q*b=z.
```

For a genuine first arrival at `z`, the penultimate vertices satisfy:

```text
x!=z,
y!=z.
```

Now consider an outgoing continuation from the merge vertex:

```text
t*z=b,
t*b=m.
```

## Same-Row Degeneracy Is Impossible

If:

```text
t=p,
```

then:

```text
p*z=b
```

and also:

```text
p*x=b.
```

Since row `p` is injective:

```text
x=z,
```

contradicting genuine first arrival.

Similarly:

```text
t=q
```

would imply:

```text
y=z.
```

Therefore in a genuine first merge any outgoing continuation row is
automatically distinct from the two last incoming rows:

```text
t notin {p,q}.
```

## Loop Continuation Boundary

There remains a separate degeneracy:

```text
t*z=b,
t*b=z.
```

In `H_b`, this is a loop at the merge vertex:

```text
z -> z.
```

After changing the target from `b` to `z`, the same row gives:

```text
t*b=z,
t*z=b.
```

Thus in `H_z` it becomes a loop at `b`:

```text
b -> b.
```

This is not a right fixed point for `b`, because the right-fixer equation
would be:

```text
t*b=b,
```

whereas the loop gives:

```text
t*b=z.
```

## Consequence

For a genuine first merge, the mixed relay lemma covers every non-loop
outgoing continuation. The only remaining local boundary at the merge vertex
is:

```text
an outgoing loop z -> z in H_b,
which becomes a loop b -> b in H_z.
```

This loop case must be analyzed separately. It must not be confused with a
right fixer or with an immediate E255 witness.

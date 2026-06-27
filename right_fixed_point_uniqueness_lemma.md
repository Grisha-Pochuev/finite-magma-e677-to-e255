# Right Fixed-Point Uniqueness Lemma

Date: 2026-06-09.

Status:

```text
general proved
```

## Statement

Fix `a`. There is at most one element `p` satisfying:

```text
p*a=a.
```

## Proof

If:

```text
p*a=a
q*a=a,
```

then both rows contain the same ordered two-step interval:

```text
a -> a -> a.
```

The two-step source reconstruction lemma gives:

```text
p=q.
```

## Bridge Corollary

For a fan bridge:

```text
T*w=P,
```

one has:

```text
w=P
<=>
T*P=P.
```

If `P` is good and its hub satisfies:

```text
h*P=P,
```

then fixed-point uniqueness gives:

```text
w=P
<=>
T=h.
```

This corollary does not require right cancellativity.


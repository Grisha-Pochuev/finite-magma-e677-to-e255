# Target-Swap Fan Duality Lemma

Date: 2026-06-09.

Status:

```text
general proved / exact target-change mechanism
```

## One Edge

Fix an edge of `H_b`:

```text
p*a=b
p*b=c.
```

Define its backward foot:

```text
alpha=a*(b*p).
```

The edge-predecessor triangle gives:

```text
p*alpha=a.
```

Now change the graph target from `b` to `a`. In `H_a`, the edge indexed by
the same source row `p` is:

```text
A_a(p) -> R_a(p).
```

The two values are:

```text
A_a(p)=alpha
R_a(p)=p*a=b.
```

Therefore:

```text
edge a -> c in H_b
becomes
edge alpha -> b in H_a.
```

The source row is unchanged.

## Outgoing Fan Becomes Incoming Fan

Suppose distinct rows form an outgoing fan at `a` in `H_b`:

```text
p_i*a=b
p_i*b=c_i.
```

Define:

```text
alpha_i=a*(b*p_i).
```

The two-sided common-edge fan lemma gives pairwise distinct feet:

```text
alpha_i!=alpha_j
```

for `i!=j`.

In `H_a`, the same source rows give:

```text
alpha_i -> b.
```

Thus an outgoing fan at `a` in `H_b` becomes an incoming fan at `b` in
`H_a`.

## Incoming Fan Becomes Outgoing Fan

Suppose distinct rows form an incoming fan at `a` in `H_b`:

```text
p_i*x_i=b
p_i*b=a.
```

In `H_a`:

```text
A_a(p_i)=b
R_a(p_i)=p_i*a.
```

The values `p_i*a` are pairwise distinct by the two-sided fan lemma applied
to the common edge:

```text
b -> a.
```

Therefore the same rows give an outgoing fan:

```text
b -> p_i*a
```

at `b` in `H_a`.

## Mixed Junction Relay

An outgoing-majority `2+1` junction in `H_b`:

```text
p*a=b, p*b=c
q*a=b, q*b=d
r*x=b, r*b=a
```

becomes the incoming-majority junction in `H_a`:

```text
p*alpha_p=a, p*a=b
q*alpha_q=a, q*a=b
r*b=a,       r*a=u.
```

So:

```text
alpha_p -> b
alpha_q -> b
b -> u.
```

Conversely, an incoming-majority junction becomes an outgoing-majority
junction after the same target swap.

## Involutive Nature

Applying the construction again, now swapping target `a` back to `b`,
recovers the original three source rows and their original `H_b` edges.

The target-change mechanism is therefore not an arbitrary tower:

```text
(target b, junction a)
<->
(target a, junction b).
```

It reverses fan orientation and preserves the source-row set.

## Significance

The recursive No-Free-Tail gap can now be studied on an unordered target
pair:

```text
{a,b}.
```

A cycle-entry fan does not lose its ancestry when the target changes. The
same source rows reappear as the dual fan after swapping the target and the
junction vertex.

The remaining task is to combine this exact two-target relay with:

```text
badness of one target;
the third core incidence;
finite cyclic closure of the selected branches.
```

## Boundary

This lemma preserves and reverses the local junction. It does not by itself
show that the relayed edges remain in a bicyclic core of the new target graph.

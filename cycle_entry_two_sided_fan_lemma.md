# Cycle-Entry Two-Sided Fan Lemma

Date: 2026-06-09.

Status:

```text
general proved / finite collision-free tails are impossible
```

## Setup

Fix `P` and let:

```text
q_{i+1}=q_i*P.
```

For every `i`, let `a_i` be the unique value satisfying:

```text
q_i*a_i=P.
```

Thus row `q_i` contains:

```text
a_i -> P -> q_{i+1}.
```

Assume:

```text
q_0*0=P,
```

so:

```text
a_0=0.
```

## First Repetition

If some:

```text
q_i in F(0,P)
```

with `i>0`, the source-return outcome has already occurred. Assume from now on
that no such return occurs.

Because the magma is finite, choose the first repetition:

```text
q_j=q_k=Q
```

with:

```text
0<=j<k,
```

and `k` minimal.

If `j=0`, the orbit has returned to its initial source:

```text
q_k=q_0 in F(0,P).
```

Equivalently:

```text
a_k=0.
```

Under the no-return assumption this cannot happen, so:

```text
j>0.
```

Set:

```text
x=q_{j-1}
y=q_{k-1}.
```

Minimality of the first repetition gives:

```text
x!=y.
```

Both rows contain the same edge:

```text
x*P=Q
y*P=Q.
```

## Forced Two-Sided Fan

The backward feet of this common edge are exactly:

```text
a_{j-1}
a_{k-1},
```

because:

```text
x*a_{j-1}=P
y*a_{k-1}=P.
```

The two-sided common-edge fan lemma gives:

```text
a_{j-1}!=a_{k-1}.
```

Define the forward tips:

```text
X=x*Q
Y=y*Q.
```

Then:

```text
X!=Y
X*x=Y*y=pred_Q(P).
```

So the first entry into an external right-`P` cycle creates:

```text
row x:
  a_{j-1} -> P -> Q -> X

row y:
  a_{k-1} -> P -> Q -> Y,
```

with distinct backward feet, distinct forward tips, and one common return hub.

## No Collision-Free Tail

Therefore every source-started right-`P` orbit has the dichotomy:

```text
return to the source fiber;
or create a new two-sided common-edge fan at its first repetition.
```

There is no third possibility in which a finite fresh tail simply disappears
into an external cycle without producing new pressure.

## Boundary Of The Result

This proves termination of a single collision-free bridge chain. It does not
yet prove the full bad-element contradiction, because the new fan has common
edge:

```text
P -> Q
```

rather than the original:

```text
0 -> P.
```

The remaining No-Free-Tail step is to show that repeated changes of the common
edge cannot avoid the anchored bad-cycle interval forever.

The hub of the new fan is not free. It is the bridge label of the repeated
orbit state:

```text
cycle_entry_hub_transport_lemma.md
```

If `Q*a_Q=P`, then the cycle-entry tips return to exactly `a_Q`.

When `P` is good, the possible alignment of this new edge with row `P` is
already classified in:

```text
good_p_unique_reverse_edge_lemma.md
```

The only reverse-aligned right-`P` edge is:

```text
e*P=f
P*f=e.
```

So a cycle-entry fan is either attached to the known spine edge `e -> f`, or
is genuinely non-aligned.

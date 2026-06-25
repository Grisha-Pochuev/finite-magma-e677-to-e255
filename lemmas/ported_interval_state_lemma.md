# Ported Interval State Lemma

Date: 2026-06-17.

Status:

```text
general proved / relay-state correction
```

## Statement

Fix a target `b`.  In the graph `H_b`, an oriented edge:

```text
x -> y
```

means that some row `t` satisfies:

```text
t*x=b,
t*b=y.
```

The full ported interval state:

```text
(b,x,y)
```

determines the source row `t`.

Indeed, by two-step source reconstruction:

```text
t=pred_y(pred_b(x)).
```

Thus two rows cannot realize the same ported interval:

```text
t*x=b, t*b=y,
u*x=b, u*b=y
=> t=u.
```

## Why Bridge-Pair State Is Weaker

The bridge-pair state:

```text
(b,x,pred_b(x),pred_x(b))
```

records the two bridge labels around `x`, but it does not record the outgoing
port `y`.

Repeating a bridge-pair state therefore only says that the relay returned to
the same target-vertex pair.  It does not by itself force two source rows to
share a complete ordered interval.

The relay-termination argument must therefore force repetition of:

```text
(target, input vertex, output vertex),
```

not merely:

```text
(target, vertex, two bridge labels).
```

## Consequence For Relay Termination

A finite relay chain can be safely stopped if it produces the same ported
interval state in two distinct active occurrences.  Then the source row is the
same, and if the occurrences were supposed to be independent branch rows, the
branch closure contradicts the first-merge or distinct-fan assumptions.

So the corrected final target is:

```text
prove that recursive triple/mixed relay forces a repeated ported interval
state, or else produces a right fixer.
```

This replaces the weaker bridge-pair repetition target.

## Target-Advance Form

There is one more bookkeeping fact needed for relay termination.

If row `p` realizes the ported interval:

```text
p*x=b,
p*b=z,
```

then, after changing the target from `b` to `z`, the same row realizes:

```text
p*b=z,
p*z=U,
```

that is, the new ported interval:

```text
(z,b,U), where U=p*z.
```

So a first-merge relay does not create a new anonymous edge. It advances the
same source row by one step along its own row orbit:

```text
(b,x,z) --same row p--> (z,b,p*z).
```

This advance is injective at the level of ported intervals.  Indeed, the
target interval `(z,b,U)` reconstructs the same source row by:

```text
p=pred_U(pred_z(b)).
```

Thus if two relayed occurrences have the same advanced state `(z,b,U)`, they
come from the same row.  In a genuine two-branch first-merge setting this is
exactly the contradiction supplied by two-step source reconstruction.

The No-Free-Tail termination proof should therefore track these advanced
states, not only the endpoint pair `(b,z)` or the bridge pair
`(pred_b(z),pred_z(b))`.

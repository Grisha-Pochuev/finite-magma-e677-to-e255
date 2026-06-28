# Earliest Side-Attachment Mixed-Junction Lemma

Date: 2026-06-17.

Status:

```text
graph proved / branch-closure reduction to mixed 2+1
```

## Setup

Work in the branch corridor before a binary pure incoming sink.  Let an active
directed branch path in `H_b` pass through an internal vertex `v`:

```text
x -> v -> y.
```

Write the two active path edges as:

```text
p*x=b, p*b=v,
q*v=b, q*b=y.
```

So at `v`, the active path already contributes:

```text
one incoming incidence: x -> v,
one outgoing incidence: v -> y.
```

Suppose an extra core incidence attaches at this internal vertex `v`.  This is
the first side attachment to the two-branch corridor before the binary sink.

## Classification

There are two non-loop orientations for the side incidence.

### Extra Incoming Incidence

If:

```text
r*a=b,
r*b=v,
```

then at `v` we have two incoming incidences and one outgoing incidence:

```text
p*x=b, p*b=v,
r*a=b, r*b=v,
q*v=b, q*b=y.
```

This is an incoming-majority mixed `2+1` junction in `H_b`.

### Extra Outgoing Incidence

If:

```text
r*v=b,
r*b=c,
```

then at `v` we have one incoming incidence and two outgoing incidences:

```text
p*x=b, p*b=v,
q*v=b, q*b=y,
r*v=b, r*b=c.
```

This is an outgoing-majority mixed `2+1` junction in `H_b`.

## Loop Side Incidence

If the side incidence is a loop:

```text
r*v=b,
r*b=v,
```

then it is both incoming and outgoing at `v`. Together with the active path
edges, it still gives a mixed junction, and also supplies the loop case already
handled by the target-swap junction dichotomy.

## Consequence

The binary pure incoming sink does not create a third closure type.

By the core-escape lemma, the second independent cycle must attach to the
two-branch corridor before the sink.  If it attaches at an internal branch
vertex, the active path already gives one incoming and one outgoing incidence,
so the extra core incidence forces a mixed `2+1` junction.

If the extra core incidence attaches at the initial split, then it is the
original retained third core incidence from the triple fan or mixed `2+1`
setup.

Therefore every binary-sink escape relays back to one of the two already
classified core-junction types:

```text
triple fan,
mixed 2+1 junction.
```

The next algebraic work should not treat binary sinks as independent
obstructions. It should continue the mixed-junction target-swap/first-merge
relay using the earliest side attachment.

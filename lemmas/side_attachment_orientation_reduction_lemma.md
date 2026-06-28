# Side-Attachment Orientation Reduction Lemma

Date: 2026-06-17.

Status:

```text
general proved / orientation reduction after binary-sink escape
```

## Setup

Fix a target `b`.  Let the active branch corridor pass through an internal
vertex `v`:

```text
x -> v -> y
```

with rows:

```text
p*x=b, p*b=v,      path enters v
q*v=b, q*b=y.      path leaves v
```

Suppose the second core cycle attaches to this corridor for the first time at
`v`.

By the side-attachment mixed-junction lemma, any extra core incidence at `v`
creates a mixed `2+1` junction.  This lemma separates the two orientations and
shows which one is actually new.

## Incoming Side Attachment Is Already A First-Merge Relay

Assume the side incidence enters `v`:

```text
r*a=b,
r*b=v.
```

Then rows `p` and `r` are two incoming branches that meet at `v`:

```text
p*x=b, p*b=v,
r*a=b, r*b=v.
```

The active path row `q` gives an outgoing continuation from the merge vertex:

```text
q*v=b,
q*b=y.
```

Thus this configuration is exactly the first-merge-with-outgoing-continuation
case already handled by:

```text
first_merge_target_swap_junction_dichotomy.md
```

After target swap `b -> v`, it relays to one of the two standard types:

```text
non-loop continuation -> mixed 2+1,
loop continuation     -> triple fan.
```

Therefore an incoming side attachment is not a new branch-closure boundary.

## Outgoing Side Attachment Is The Only New Orientation

Assume instead that the side incidence leaves `v`:

```text
r*v=b,
r*b=c.
```

Then `q` and `r` are two outgoing branches born at the internal vertex `v`:

```text
q*v=b, q*b=y,
r*v=b, r*b=c.
```

The old path row `p` is the incoming minority incidence:

```text
p*x=b, p*b=v.
```

So the earliest side attachment becomes an outgoing-majority mixed `2+1`
junction:

```text
two branches leave v,
one old branch enters v.
```

This is the only orientation that is not immediately reduced to the already
proved first-merge relay.

## Consequence

After the pure-incoming boundary reduction, future branch-closure work can use
the following sharper frontier:

```text
If the second core cycle first attaches to the active corridor at an internal
vertex, then either:

1. it enters the corridor, and the case is already a first-merge relay;
2. it leaves the corridor, and it creates an outgoing-majority mixed 2+1 split.
```

Thus the remaining nontrivial continuation is:

```text
outgoing side attachment before the binary sink.
```

It should be treated as a new split point earlier than the sink, not as a
terminal endpoint phenomenon.

# Minority Core-Return Relay Lemma

Date: 2026-06-17.

Status:

```text
graph proved / relay classification for clean mixed theta
```

## Setup

Fix a target `b`.  Start with an outgoing-majority mixed `2+1` core junction:

```text
p*v=b, p*b=c,
q*v=b, q*b=d,
r*a=b, r*b=v.
```

Rows `p,q` start two outgoing branches from `v`.  Suppose those two branches
first meet at a binary pure incoming sink `z`, forming the current clean
mixed-theta corridor:

```text
v -> ... -> z,
v -> ... -> z.
```

Assume the interiors of those two outgoing branches have no already usable
side attachment.

The minority edge:

```text
a -> v
```

is still a core edge.  It is not a disposable tree tail.

## Core-Return Principle

Because the minority edge lies in the cycle core, it belongs to some
undirected cycle.  Therefore, after traversing the minority edge away from
`v`, there is a core path from `a` back to the already selected corridor,
without using the same minority edge again.

Let `w` be the first vertex of the outgoing corridor reached by such a return
path.  Then:

```text
w is v,
or w is an internal vertex of one outgoing branch,
or w is z.
```

There is no fourth possibility, because the outgoing corridor consists only
of the two paths from `v` to `z`.

## Case 1: Return Hits An Internal Branch Vertex

If `w` is internal to one of the outgoing branches, the last return incidence
is a side attachment to an internal branch vertex.

This is exactly the situation classified in:

```text
side_attachment_orientation_reduction_lemma.md
```

If the return incidence enters the branch corridor, it is already a first
merge with outgoing continuation.  If it leaves the branch corridor, it is a
new outgoing-majority mixed `2+1` split before the sink.

Thus an internal return is not a new clean-theta endpoint case.

## Case 2: Return Hits The Sink `z`

If the return first hits `z`, then the binary sink is no longer isolated.

The return incidence at `z` is one of:

```text
an additional incoming incidence,
an outgoing continuation,
a loop.
```

An additional incoming incidence gives pure incoming degree at least three,
which target-swaps to a triple fan by:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

An outgoing continuation or loop is classified by:

```text
first_merge_target_swap_junction_dichotomy.md
```

So a return at `z` is already relayed to:

```text
mixed 2+1,
or triple fan.
```

## Case 3: Return Hits The Initial Split `v`

If the return first hits `v`, then the original mixed junction has an
additional core incidence at its split vertex.

If that incidence leaves `v`, then together with the two existing outgoing
majority rows `p,q` it gives a triple outgoing fan at `v`.

If that incidence enters `v`, then it gives a second incoming incidence at
`v`; together with either outgoing row `p` or `q`, this is a first merge with
outgoing continuation and relays by the same first-merge dichotomy.

Thus a return at `v` also gives one of the already known junction types.

## Consequence

A clean mixed theta cannot be treated as only two outgoing branches plus a
passive minority edge.

The minority edge is part of the core and must return to the selected
corridor.  Its first return is always one of:

```text
internal side attachment,
sink relay,
split-vertex extra fan/junction.
```

Therefore the real remaining obstruction is not an isolated clean theta.  It
is a possible recursive relay among triple fan and mixed `2+1` junctions.

The next proof needs a well-founded measure for this relay, such as:

```text
choose the first return closest to the current split;
or choose a minimal clean-theta corridor among all mixed junctions in the core.
```

Under such a minimal choice, the return cases above should force a repeated
ordered two-step interval or a strictly earlier mixed split.

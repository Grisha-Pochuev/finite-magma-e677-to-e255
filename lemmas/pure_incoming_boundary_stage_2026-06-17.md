# Pure-Incoming Boundary Stage

Date: 2026-06-17.

Status:

```text
stage summary / No-Free-Tail still open
```

## Purpose

The previous branch-closure relay stage left one local boundary:

```text
a first merge with no outgoing continuation from the merge vertex.
```

This was the pure incoming merge/sink case.

This stage reduces that boundary and shows it does not create a new third
obstruction type beyond:

```text
triple fan,
mixed 2+1 junction.
```

## Lemmas Produced

```text
pure_incoming_merge_target_swap_fan_lemma.md
binary_sink_core_escape_lemma.md
earliest_side_attachment_mixed_junction_lemma.md
```

## Result 1: High-Degree Pure Incoming Merge Relays To Triple Fan

If a merge vertex `z` has incoming incidences:

```text
p_i*x_i=b,
p_i*b=z,
```

then after target swap `b -> z`, the same rows give:

```text
b -> U_i,
U_i=p_i*z
```

in `H_z`.

The tips `U_i` are pairwise distinct by two-step source reconstruction.  In a
genuine first-merge setting, none of them equals `b`.

Therefore, if there are at least three incoming incidences at `z`, the pure
incoming merge becomes a triple outgoing fan after target swap.

## Result 2: Binary Sink Cannot Be Isolated In A Bicyclic Core

If exactly two branches merge at `z` and there is no third incidence or
outgoing continuation at `z`, then those two branches form only one simple
cycle.

But the forced bad-target core is bicyclic.  Hence the second independent
cycle must attach to the two-branch corridor before `z`:

```text
at the initial split,
or at an internal branch vertex.
```

## Result 3: Earliest Internal Side Attachment Is Mixed 2+1

At an internal branch vertex `v`, the active branch path already has:

```text
one incoming incidence,
one outgoing incidence.
```

Any extra core incidence at `v` therefore creates a mixed `2+1` junction:

```text
incoming-majority, if the side incidence enters v;
outgoing-majority, if the side incidence leaves v.
```

A loop side incidence falls into the already classified loop/mixed relay.

## Conclusion

The pure incoming first-merge boundary is no longer an independent local
obstruction.

It reduces as follows:

```text
degree >= 3 pure incoming merge
=> target-swap triple fan;

binary pure incoming sink
=> second cycle attaches before the sink
=> earliest side attachment is mixed 2+1 or the original retained split.
```

Thus future work should not restart a separate "pure incoming sink" analysis.
The active No-Free-Tail frontier returns to the two existing junction types:

```text
triple fan closure;
mixed 2+1 closure.
```

## Next Meaningful Step

Continue with the mixed `2+1` relay, now using the fact that every attempted
binary-sink closure must expose an earlier side attachment.  The desired next
lemma should connect this earliest side attachment to the existing
target-swap/first-merge relay chain, rather than treating the sink endpoint as
the source of pressure.

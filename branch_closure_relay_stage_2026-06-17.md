# Branch-Closure Relay Stage

Date: 2026-06-17.

Status:

```text
stage summary / No-Free-Tail still open
```

## What Was Proved In This Stage

This stage analyzed the first merge of two directed branches after a mixed
`2+1` or fan split. The main outcome is that a first merge is not a terminal
object whenever the merge vertex has an outgoing continuation.

The stage produced four general proved lemmas:

```text
mixed_junction_target_swap_bridge_square.md
first_merge_certificate_separation_lemma.md
first_merge_target_swap_mixed_relay.md
first_merge_degenerate_continuation_boundary.md
first_merge_target_swap_junction_dichotomy.md
```

## Core Relay Picture

Let two branches in `H_b` first merge at `z`:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
x!=y.
```

The last-edge certificates give:

```text
U=p*z,
W=q*z,
K=U*p=W*q=pred_z(b).
```

The common terminal `K` is real but weak. At first merge:

```text
z*p != z*q,
p*z != q*z.
```

So equality cannot simply be propagated backward from `K`.

## Outgoing Continuation From The Merge

If the core continues from `z` through:

```text
t*z=b,
t*b=m,
```

then after swapping target `b -> z`, the two merging rows become:

```text
b -> U,
b -> W
```

in `H_z`.

There are two cases:

```text
m!=z  =>  mixed 2+1 junction in H_z;
m=z   =>  triple outgoing fan in H_z.
```

Thus a first merge with outgoing continuation relays back to the same two
junction types already forced by the bicyclic-core reduction:

```text
mixed 2+1;
triple fan.
```

No new obstruction type appears.

## Degenerate Rows

If the merge is genuine, the outgoing continuation row cannot be one of the
two last merge rows:

```text
t=p => x=z,
t=q => y=z.
```

So same-row degeneracy is removed. The only local degeneracy is the loop:

```text
z -> z in H_b,
```

which becomes:

```text
b -> b in H_z.
```

This is a graph loop, not a right fixer.

## Model Diagnostic

The script:

```text
tools/core_orientation_diagnostics.js
```

was run on targets:

```text
0, 1, 17, 31, 255, 495
```

of the known size-496 model. Every sampled 2-core vertex had orientation:

```text
indegree=1,
outdegree=1.
```

This model therefore gives no evidence about pure incoming or pure outgoing
branch vertices in a hypothetical bad target. The result is a boundary note,
not mathematical support for the remaining case.

## Remaining Boundary

The current open local boundary is:

```text
a first merge in the selected cyclic core with no outgoing continuation
from the merge vertex.
```

Equivalently, in the chosen directed branch process, the merge behaves as a
pure incoming sink. This case is not handled by the target-swap relay above.

The next mathematical question is:

```text
Can a pure incoming first-merge vertex lie in the relevant two-cycle core
without forcing an earlier split, loop relay, or ordered two-step overlap?
```

This should be attacked structurally, not by increasing model search depth.

## Continuation: Pure-Incoming Degree Reduction

The first pure-incoming follow-up is now recorded in:

```text
pure_incoming_merge_target_swap_fan_lemma.md
```

It proves that a pure incoming merge is not a new obstruction when the merge
vertex has at least three incoming incidences. After target swap `b -> z`,
those incoming edges become a triple outgoing fan from `b` in `H_z`, with
pairwise distinct tips.

Thus the remaining boundary is sharper:

```text
binary pure incoming sink:
exactly two incoming branch incidences,
no outgoing continuation,
no loop,
no third incoming incidence.
```

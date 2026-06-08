# Same-Chain Repeat Pressure Lemma

Date: 2026-06-05.

Status:

```text
audit correction / exact cycle-closure role
```

Purpose:

```text
Classify the last unavoidable finite event for the paired predecessor chains:
a repeat inside one chain before any bad-cycle hit or cross-hit.
```

## Setup

Use either paired predecessor chain:

```text
b_2*A_i=A_{i+1}
```

or:

```text
b_3*B_i=B_{i+1}.
```

The zipper identities are:

```text
A_i*(A_{i+1}*b_2)=A_{i-1}
B_i*(B_{i+1}*b_3)=B_{i-1}.
```

## Repeat In The A Chain

Suppose one element appears twice in the `A` chain:

```text
A_i=A_m=x
```

with `i!=m`.

Because row `b_2` is a function:

```text
b_2*A_i=A_{i+1}
b_2*A_m=A_{m+1},
```

the equality `A_i=A_m` immediately gives:

```text
A_{i+1}=A_{m+1}.
```

Because row `b_2` is also injective, it also gives:

```text
A_{i-1}=A_{m-1}.
```

Thus the repeat propagates in both directions and closes the row-`b_2` cycle.

The two zipper edges are:

```text
x*(A_{i+1}*b_2)=A_{i-1}
x*(A_{m+1}*b_2)=A_{m-1}.
```

Their outputs and columns coincide automatically:

```text
A_{i+1}*b_2=A_{m+1}*b_2.
```

The adjacent repeat cases are the familiar boundaries:

```text
A_{i-1}=A_i      -> self-loop boundary;
A_{i-1}=A_{i+1}  -> row-b_2 self-swap boundary.
```

## Repeat In The B Chain

Suppose:

```text
B_i=B_m=x
```

with `i!=m`.

Exactly the same argument gives:

```text
B_{i+1}=B_{m+1}
B_{i-1}=B_{m-1}.
```

So the repeat closes the row-`b_3` cycle and does not by itself create two
distinct outputs in row `x`.

## Consequence

A same-chain repeat gives:

```text
exact cycle closure in the active source row.
```

This is not yet a contradiction.  A permutation row is expected to decompose
into cycles.  Therefore finiteness alone does not close the fresh branch.

## Remaining Proof Obligation

Together with:

```text
paired_chain_bad_cycle_hit_lemma.md
paired_chain_cross_hit_lemma.md
```

this audit shows that same-chain repetition is the genuine boundary of the
previous first-obstruction argument.  The remaining global step must use an
additional E677 relation between the two source-row cycles:

```text
prove that the row-b_2 cycle containing 0 -> t and the row-b_3 cycle containing
t -> b_4 cannot close independently under the surrounding pressure diamond.
```

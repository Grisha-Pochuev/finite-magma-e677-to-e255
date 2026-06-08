# Bad-Cycle Shared-Edge Descent Lemma

Date: 2026-06-07.

Status:

```text
general proved
```

Purpose:

```text
Turn an edge shared with row 0 into an explicit bad-cycle tail descent.
```

## Setup

Use the row-`0` bad cycle:

```text
0*b_{k+1}=b_k
0*b_k=b_{k-1}.
```

Let a nonzero row `p` share the first edge:

```text
p*b_{k+1}=b_k.
```

Define:

```text
c=p*b_k.
```

## Divergence And Descent

Rows `p` and `0` share:

```text
b_{k+1} -> b_k.
```

Since `p!=0`, the shared-edge divergence lemma gives:

```text
c!=b_{k-1}
c*p=(b_{k-1})*0.
```

By definition:

```text
r_{k-1}=b_{k-1}*0.
```

Therefore:

```text
c*p=r_{k-1}.
```

The complete transfer is:

```text
p*b_{k+1}=b_k
p*b_k=c
c!=b_{k-1}
c*p=r_{k-1}.
```

The return edge:

```text
b_k*r_{k-1}=b_{k+1}
```

is exactly the usual bad-cycle ladder.  Thus that ladder is the return side of
a shared-edge divergence diamond between rows `p` and `0`.

## Application To The Bad-Tail Occupied Row

In the bad-tail zero triangle:

```text
r*u=b_4.
```

If:

```text
u=b_5,
```

then row `r` shares the row-`0` edge:

```text
b_5 -> b_4.
```

Let:

```text
c=r*b_4.
```

The lemma gives:

```text
c!=b_3
c*r=r_3.
```

So the role `u=b_5` creates an explicit descent to the earlier tail `r_3`.

If additionally `r=b_j`, then:

```text
c*b_j=r_3.
```

## General Use

Whenever an active nonzero row acquires an edge:

```text
b_{k+1} -> b_k,
```

immediately add:

```text
the next output differs from b_{k-1};
its product with the active source row is r_{k-1}.
```

This is a reusable descent mechanism for future paired-chain and pivot-fan
hits.

# Zero-Tooth Bad-Cycle Return Lemma

Date: 2026-06-08.

Status:

```text
general proved / aligned occupied-return descent
```

## Setup

Assume a zero tooth:

```text
v*q=0.
```

Define its zero-column return:

```text
R=v*0.
```

The inverse edge chain gives:

```text
R*v=pred_0(q).
```

Assume:

```text
q=b_k
R=b_j
```

belong to the bad row-0 cycle. Then:

```text
pred_0(q)=b_{k+1},
```

so:

```text
b_j*v=b_{k+1}.
```

## Aligned Return

If:

```text
j=k,
```

then:

```text
b_k*v=b_{k+1}.
```

The bad-cycle predecessor ladder also gives:

```text
b_k*r_{k-1}=b_{k+1}.
```

By injectivity of row `b_k`:

```text
v=r_{k-1}.
```

Therefore:

```text
v*b_k=0
v*0=b_k
=>
v=r_{k-1}.
```

The zero tooth has returned to an already existing older tail.

## Non-Aligned Return

If:

```text
j!=k,
```

then row `b_j` contains:

```text
b_j*v=b_{k+1}
b_j*r_{j-1}=b_{j+1}.
```

The outputs are distinct:

```text
b_{k+1}!=b_{j+1}.
```

Thus the non-aligned role is extra occupied-row pressure, not an immediate
collision.

## Application To A Tip-Source Collision

The tip-source collision lemma gives:

```text
q*0=P
q*P=r
r*0=P
v=q*r
v*q=0.
```

Let:

```text
R=v*0.
```

Then:

```text
R*v=pred_0(q).
```

If:

```text
q=b_k
R=q,
```

the new point is exactly:

```text
v=r_{k-1}.
```

So the aligned return after a tip-source collision is completely classified.


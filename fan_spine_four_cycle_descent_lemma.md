# Fan-Spine Four-Cycle Descent Lemma

Date: 2026-06-08.

Status:

```text
general proved / closes the e=C first-hit in the minimal long-cycle setup
```

## Setup

Assume:

```text
0 is bad;
P*0=P;
C=P*P;
h=0*C=C*P;
a=0*P;
e=h*a;
P*e=h;
P*h=0.
```

Assume the four-cycle hit:

```text
e=C.
```

The points:

```text
P,C,h,0
```

are assumed distinct, as in the long bad-cycle role.

## Shared Row-0 Edge

Since:

```text
0*C=h
P*C=h,
```

rows `0` and `P` share the directed edge:

```text
C -> h.
```

Their next outputs are:

```text
0*h
P*h=0.
```

Shared-edge divergence gives:

```text
0*h!=0
(0*h)*0=0*P=a.
```

Thus `e=C` is not an unclassified closure. It is exactly a shared row-0 edge
and produces an explicit zero-column descent:

```text
(0*h)*0=a.
```

## Occupied Bad-Cycle Form

If:

```text
C=b_j,
```

then:

```text
h=b_{j-1}
0*h=b_{j-2}.
```

Therefore:

```text
r_{j-2}=b_{j-2}*0=a.
```

In the bad-tail role:

```text
P=b_2,
```

so:

```text
a=0*P=b_1.
```

Hence:

```text
e=C=b_j
=>
r_{j-2}=b_1.
```

This also follows by comparing:

```text
b_{j-1}*a=b_j
b_{j-1}*r_{j-2}=b_j
```

and using injectivity of row `b_{j-1}`.

## Badness Transfer

The row-`P` edges are:

```text
P -> C -> h -> 0 -> P.
```

Thus the orbit of `P` under its own left row `L_P` has length exactly four.

For a finite E677 magma, the fixed-point equivalence for E255 says that the
only possible solution of:

```text
P*(y*y)=y
```

is:

```text
y=L_P^{-4}(P).
```

On a four-cycle this candidate is `y=P`, but:

```text
P*(P*P)=P*C=h!=P.
```

Therefore E255 fails at `P`.

So:

```text
e=C
=>
P is a bad element whose own row cycle has length 4.
```

## Minimal-Bad-Cycle Corollary

Choose the original bad element `0` so that the length of its own row cycle is
minimal among all bad elements.

If that cycle has length greater than four, then:

```text
e=C
```

is impossible, because it creates the bad element `P` with a strictly shorter
own row cycle of length four.

Therefore, in the minimal long-cycle setup used by the `u=b_3` fan:

```text
e!=C.
```

The only base cases left outside this descent are bad own-row cycles of length
three or four.

## Size-9 Diagnostic

The normalized size-9 `u=b_3` role was checked only as confirmation:

```text
C=b_6, e=C -> immediate contradiction;
C=b_7, e=C -> status none, 12.44s, 61 nodes.
```

For `C=b_6`, the symbolic occupied-cycle formula already explains the
contradiction:

```text
r_4=P=b_2
```

but the four-cycle descent would require:

```text
r_4=b_1.
```

No finite diagnostic is used in the general proof above.


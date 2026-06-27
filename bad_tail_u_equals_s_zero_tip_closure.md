# Bad-Tail u=s Zero-Tip Closure

Date: 2026-06-07.

Status:

```text
proved for the long bad-cycle role
```

Purpose:

```text
Close all three possible zero tips in the three-source fan created by u=b_3.
```

## Setup

Use the role from:

```text
bad_tail_u_equals_s_fan_lemma.md
```

Write:

```text
P=b_2
s=b_3
B=b_4
A=0*0.
```

The proved relations are:

```text
P*0=P
B*0=P
A*0=P

s*P=B
s*B=s
s*s=0.
```

The common-edge fan over:

```text
0 -> P
```

has tips:

```text
C=P*P
D=B*P
E=A*P.
```

They are pairwise distinct and none equals `P`.

Assume the bad row-`0` cycle is long enough that:

```text
A=0*0!=P=b_2.
```

This includes the full size-9 cycle and the current long-cycle frontier.

## Zero Tip C=0

Assume:

```text
P*P=0.
```

Together with:

```text
P*0=P,
```

row `P` swaps:

```text
0 <-> P.
```

Apply E677 with:

```text
x=0
y=P.
```

It gives:

```text
0=P*(0*((P*0)*P))
 =P*(0*(P*P))
 =P*(0*0)
 =P*A.
```

But row `P` already has:

```text
P*P=0.
```

Injectivity gives:

```text
A=P,
```

contrary to the long-cycle assumption.

Therefore:

```text
C!=0.
```

## Zero Tip D=0

Assume:

```text
B*P=0.
```

Since:

```text
B*0=P,
```

the unique preimage of `0` in row `B` is `P`.

Apply E677 with:

```text
x=0
y=B.
```

It gives:

```text
0=B*(0*((B*0)*B))
 =B*(0*(P*B)).
```

Therefore:

```text
0*(P*B)=P.
```

The predecessor of `P=b_2` in row `0` is `s=b_3`, so:

```text
P*B=s.
```

The fan return hub is:

```text
H=D*B=0*B=s.
```

Since:

```text
P*H=0,
```

we get:

```text
P*s=0.
```

Now rows `P` and `s` both contain:

```text
B -> s -> 0:

P*B=s
P*s=0

s*B=s
s*s=0.
```

Two-step source reconstruction forces:

```text
P=s,
```

impossible.

Therefore:

```text
D!=0.
```

## Zero Tip E=0

Assume:

```text
A*P=0.
```

Since:

```text
A*0=P,
```

the unique preimage of `0` in row `A` is `P`.

Apply E677 with:

```text
x=0
y=A.
```

It gives:

```text
0=A*(0*((A*0)*A))
 =A*(0*(P*A)).
```

Therefore:

```text
0*(P*A)=P.
```

Again using the row-`0` predecessor of `P`:

```text
P*A=s.
```

Let:

```text
b_1=pred_0(0)
r_1=b_1*0.
```

The bad-cycle ladder in row `P=b_2` gives:

```text
P*r_1=s.
```

Since also:

```text
P*A=s,
```

row-`P` injectivity gives:

```text
r_1=A.
```

Thus:

```text
b_1*0=A
0*0=A.
```

Rows `b_1` and `0` share:

```text
0 -> A.
```

Their next outputs are:

```text
b_1*A=P
0*A.
```

The first equality is the bad-cycle ladder:

```text
b_1*r_0=P
r_0=0*0=A.
```

The shared-edge divergence hub is:

```text
pred_A(0)=P,
```

because:

```text
A*P=0.
```

Therefore:

```text
P*b_1=P.
```

But:

```text
P*0=P.
```

Row-`P` injectivity forces:

```text
b_1=0,
```

impossible in a nontrivial bad cycle.

Therefore:

```text
E!=0.
```

## Escape Consequence

All three tips:

```text
C,D,E
```

are:

```text
pairwise distinct;
nonzero;
different from P.
```

The source set is:

```text
S={P,B,A},
```

and contains the middle value `P`.

By the self-containing fan escape lemma, at least one tip lies outside:

```text
{0,P,B,A}.
```

Thus the role `u=s` cannot close locally.  It must transfer pressure to a new
point.

In a full row-`0` cycle, that new point is another occupied bad-cycle element,
so its return edge to the common hub becomes a new occupied-row pressure edge.

## Computational Check

The three normalized size-9 zero-tip nodes:

```text
7*7=0
5*7=0
1*7=0
```

closed respectively in:

```text
0.93s
7.94s
8.68s.
```

The symbolic arguments above explain all three closures, so these checks are
certificates only, not the proof.

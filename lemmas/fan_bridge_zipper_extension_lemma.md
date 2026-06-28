# Fan-Bridge Zipper Extension Lemma

Date: 2026-06-08.

Status:

```text
general proved / classifies the next step after every bridge
```

## Setup

Use one fan-tip bridge:

```text
T*w=P.
```

Define the next right-column value:

```text
V=T*P.
```

## Bridge Zipper

The row-`T` interval is:

```text
w -> P -> V.
```

The source-orbit zipper gives:

```text
P*(V*T)=w.
```

Define:

```text
z=V*T.
```

Then:

```text
z=pred_P(w)
P*z=w.
```

Thus every bridge has the forced square:

```text
row T:
  w -> P -> V

row P:
  z -> w

with:
  z=V*T=pred_P(w).
```

The bridge cannot be free from the row-`P` geometry: its predecessor in row
`P` is explicitly the return `V*T`.

## Hit On A Known Row-P Cycle

Suppose row `P` has a known cycle and:

```text
w
```

hits one of its points. Then:

```text
z=pred_P(w)
```

is the previous known cycle point.

For the exact six-cycle:

```text
P -> C -> f -> e -> h -> 0 -> P,
```

the bridge roles are:

```text
w=P -> z=0
w=C -> z=P
w=f -> z=C
w=e -> z=f
w=h -> z=e
w=0 -> z=h.
```

In every role:

```text
V*T=z.
```

## Self-Bridge Corollary

For the self source:

```text
q=P
T=C
w=k=f*P
V=C*P=h.
```

Therefore:

```text
z=h*C=pred_P(k)
P*(h*C)=k.
```

If:

```text
k=C,
```

then:

```text
h*C=P.
```

But good `P` gives:

```text
h*P=P.
```

Since:

```text
C!=P,
```

row `h` would send two distinct columns to `P`.

Thus:

```text
k!=C.
```

Together with the earlier restriction:

```text
k!=P,
```

the self bridge avoids both:

```text
P and C.
```

## Bridge-Source Hit

If a bridge equals another original source:

```text
w=r,
```

then:

```text
T*r=P
V*T=pred_P(r).
```

So a bridge-source collision does not remain an unstructured equality. It
forces a return to the predecessor of that source in row `P`.

If `r` is already on the known row-`P` cycle, this return is explicit.

## Bridge-Tip Hit

If:

```text
w=U
```

for another fan tip `U`, then:

```text
T*U=P
V*T=pred_P(U).
```

Again the overlap immediately creates a known row-`P` predecessor when `U`
lies on the active spine.

## Significance

The bridge expansion and the bridge zipper combine into:

```text
q -> T=q*P
T -> V=T*P

T*w=P
V*T=pred_P(w).
```

So each step of the right-column orbit creates a coupled predecessor step in
row `P`.

This is the precise double-interval recursion needed for the No-Free-Tail
termination argument.


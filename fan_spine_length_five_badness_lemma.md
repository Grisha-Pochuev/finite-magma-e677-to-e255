# Fan-Spine Length-Five Badness Lemma

Date: 2026-06-08.

Status:

```text
general proved / closes the good-P role for a five-cycle spine
```

## Setup

Assume the fan-spine relations:

```text
P*P=C
C*P=h
P*h=0
P*0=P.
```

Assume row `P` closes with exact length five:

```text
P -> C -> e -> h -> 0 -> P.
```

Thus:

```text
P*C=e
P*e=h.
```

All five points are distinct.

## Claim

E255 fails at `P`.

## Proof

For a row-`P` cycle of length five:

```text
f=L_P^{-4}(P)=C
g=L_P^{-5}(P)=P.
```

The fourth-predecessor test says that E255 at `P` would force:

```text
f*f=g,
```

so:

```text
C*C=P.
```

Apply the inverse edge chain to:

```text
C*C=P.
```

It gives:

```text
C=P*((C*P)*C).
```

Since:

```text
C*P=h,
```

we get:

```text
C=P*(h*C).
```

But:

```text
P*P=C.
```

Row `P` is injective, hence:

```text
h*C=P.
```

E255 at `P` also has the direct form:

```text
h*P=P.
```

Therefore row `h` would satisfy:

```text
h*C=P
h*P=P.
```

Since:

```text
C!=P,
```

this contradicts injectivity of row `h`.

Thus E255 cannot hold at `P`.

## Minimal-Bad-Cycle Corollary

Choose the original bad element with minimal own-row cycle length `m`.

If:

```text
m>5,
```

then the fan spine cannot close as a row-`P` cycle of length five, because
that would create a bad element `P` with a shorter own-row cycle.

Together with the four-cycle descent:

```text
minimal bad cycle length >=6
=>
row-P spine cannot close at length 4 or 5.
```

## New Boundary

The first potentially good shorter closure is now length six.

For a length-six row-`P` cycle:

```text
P -> C -> f -> e -> h -> 0 -> P,
```

the good-P test becomes:

```text
f*f=C
h*P=P.
```

This is the next exact longer-cycle role.


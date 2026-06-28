# Bad-Tail Repeat Self-Swap Relay

Date: 2026-06-07.

Status:

```text
proved relay for the occupied role r=b_3 / candidate recursive zero descent
```

Purpose:

```text
Show that the occupied self-swap role in the bad-tail repeat branch is not a
terminal boundary: it creates a second zero triangle.
```

## Setup

Use the repeat zero triangle:

```text
s=b_3
s*t=b_4
s*b_4=u
u*s=0
r=u*0
r*u=b_4.
```

Assume the occupied role:

```text
r=s.
```

Since:

```text
r*u=b_4
s*t=b_4,
```

row-`s` injectivity gives:

```text
u=t.
```

Therefore:

```text
s*t=b_4
s*b_4=t
t*s=0
t*0=s.
```

So row `s` swaps:

```text
t <-> b_4,
```

while row `t` has:

```text
0 -> s
s -> 0.
```

Thus row `t` swaps:

```text
0 <-> s.
```

## First Zero Relay

Apply the edge predecessor triangle to:

```text
t*s=0.
```

It gives:

```text
t*(s*(0*t))=s.
```

But:

```text
t*0=s.
```

Row-`t` injectivity therefore gives:

```text
s*(0*t)=0.
```

Let:

```text
rho=s*0=r_3.
```

Apply the inverse edge chain to:

```text
s*(0*t)=0.
```

Since `0*t` is the image of `t` in row `0`, row-`0` injectivity gives:

```text
rho*s=t.
```

So the first relay is:

```text
s*0=rho
rho*s=t.
```

The bad-cycle ladder also gives:

```text
b_4*rho=b_5.
```

## Distinctness In Row s

Row `s` contains:

```text
0     -> rho
t     -> b_4
b_4   -> t
0*t   -> 0.
```

The value `rho` cannot equal:

```text
0:
  because no y satisfies y*0=0;

b_4:
  because s*0=s*t=b_4 would force 0=t;

t:
  because s*0=s*b_4=t would force 0=b_4.
```

Hence:

```text
rho, b_4, t, 0
```

are four distinct outputs in row `s`, with four distinct columns:

```text
0,t,b_4,0*t.
```

## Second Zero Relay

Apply the inverse edge chain to:

```text
rho*s=t.
```

It gives:

```text
s=t*((rho*t)*rho).
```

But row `t` already has:

```text
t*0=s.
```

Therefore row-`t` injectivity gives:

```text
((rho*t)*rho)=0.
```

Define:

```text
m=rho*t.
```

Then:

```text
m*rho=0.
```

So the self-swap role creates a second zero triangle:

```text
s*0=rho
rho*s=t
rho*t=m
m*rho=0.
```

## Continuation

Define:

```text
n=m*0.
```

The inverse edge chain for:

```text
m*rho=0
```

gives:

```text
n*m=pred_0(rho).
```

Thus the self-swap role has a recursive zero-relay form:

```text
m*rho=0
n=m*0
n*m=pred_0(rho).
```

This is structurally parallel to the general source-row zero trap.

## Boundary Offsets

Two important offsets close immediately.

If:

```text
t=b_4,
```

then the repeat gives:

```text
b_4*0=b_4,
```

while `t*0=s` gives:

```text
b_4*0=b_3,
```

impossible.

If:

```text
t=b_5,
```

the repeat gives:

```text
b_4*0=b_5.
```

The bad-cycle ladder gives:

```text
b_4*r_3=b_5.
```

Thus:

```text
r_3=0,
```

contradicting badness of `0`.

Therefore the occupied self-swap role is closed for offsets:

```text
t in {b_4,b_5}.
```

For farther offsets it enters the second zero-relay chain above.

## Next Target

For farther offsets, classify:

```text
rho=r_3
m=rho*t
n=m*0
n*m=pred_0(rho).
```

The desired result is:

```text
the second zero triangle must hit the bad-cycle block, the original repeat
network, or a forbidden zero edge.
```

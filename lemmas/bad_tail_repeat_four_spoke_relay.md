# Bad-Tail Repeat Four-Spoke Relay

Date: 2026-06-07.

Status:

```text
proved four-spoke pressure / recursive occupied role r=b_4
```

Purpose:

```text
Strengthen the bad-tail repeat network and extract a second recursive
zero-triangle role besides r=b_3.
```

## Setup

Use:

```text
s=b_3
s*t=b_4
s*b_4=u
u*s=0
r=u*0
r*u=b_4.
```

Continue the row-`s` orbit:

```text
q=s*u
d=q*s.
```

The zipper gives:

```text
u*d=b_4.
```

The predecessor expansions give:

```text
e=s*(0*u)
u*e=s

f=d*(b_4*u)
u*f=d.
```

## Four Spokes In Row u

Row `u` contains:

```text
s -> 0
d -> b_4
e -> s
f -> d.
```

Thus its output set contains:

```text
0,b_4,s,d.
```

Known:

```text
d!=s.
```

If `d` is also distinct from `0,b_4`, then row `u` has four distinct forced
outputs and columns.

## Four Spokes In Row b_4

From:

```text
r*u=b_4,
```

the inverse edge chain gives:

```text
b_4*x_r=u
x_r=(r*b_4)*r.
```

From:

```text
u*d=b_4,
```

the inverse edge chain gives:

```text
b_4*x_u=d
x_u=(u*b_4)*u.
```

Together with the repeat and ladder edges:

```text
b_4*0=t
b_4*r_3=b_5,
```

row `b_4` contains:

```text
0   -> t
r_3 -> b_5
x_r -> u
x_u -> d.
```

So the repeat branch creates coupled four-spoke pressure in rows:

```text
u and b_4.
```

## Exact Role r=b_4

Recall:

```text
r=u*0.
```

Since:

```text
u*d=b_4,
```

row-`u` injectivity gives:

```text
r=b_4
<=>
u*0=b_4
<=>
d=0.
```

But:

```text
d=q*s.
```

Therefore:

```text
r=b_4
<=>
q*s=0.
```

This is a second zero-hit tooth, one source-orbit step after `u*s=0`.

## One-Step Zero-Triangle Relay

Assume:

```text
r=b_4,
```

equivalently:

```text
q*s=0.
```

Define:

```text
R=q*0.
```

The inverse edge chain for:

```text
q*s=0
```

gives:

```text
R*q=pred_0(s)=b_4.
```

Thus the role `r=b_4` reproduces the same zero-triangle shape:

```text
q*s=0
R=q*0
R*q=b_4.
```

Compare with the original:

```text
u*s=0
r=u*0
r*u=b_4.
```

So:

```text
(u,r)
```

is replaced by:

```text
(q,R).
```

This is a one-step relay inside the bad-tail repeat branch.

The wording "recursive" needs one qualification.  To force the next
row-`s` orbit point after `q` to hit zero, the required role is not again:

```text
R=b_4.
```

It is:

```text
R=u.
```

This shifted continuation role is impossible.  The proof is recorded in:

```text
bad_tail_double_zero_tooth_lemma.md
```

Thus the `r=b_4` relay produces exactly one additional consecutive zero tooth,
not an indefinitely repeatable chain.

## Consequence

Two occupied roles now have explicit continuation mechanisms:

```text
r=b_3:
  self-swap relay creates the second zero triangle m*r_3=0;

r=b_4:
  next source-orbit point q satisfies q*b_3=0 and creates R*q=b_4;
  a third consecutive zero tooth is impossible;
  R avoids 0,b_4,u.
```

The remaining occupied roles are:

```text
r=b_j, j notin {3,4},
```

and the fresh role.

## Updated Next Target

The `r=b_4` role is now structurally terminated.  Continue with the exit:

```text
R=q*0
R notin {0,b_4,u}.
```

Immediate roles:

```text
R=b_3  -> self-swap zero relay;
R=b_j  -> occupied bad-cycle row pressure;
R fresh -> new active return row.
```

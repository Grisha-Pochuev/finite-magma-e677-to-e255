# Double Interval Backward Extension Lemma

Date: 2026-06-05.

Status:

```text
proved consequence / candidate termination mechanism
```

Purpose:

```text
Show that the hard fresh-predecessor branch of the double interval is not
static: each fresh predecessor forces another predecessor one step farther
back.
```

## Setup

Use the double-interval pressure setup:

```text
t=r_2=b_2*0
t!=0
b_3*t=b_4
u_2=0*(t*b_2)
c_{-1}=t*(b_4*b_3).
```

Known interval edges:

```text
b_2*u_2=0
b_2*0=t

b_3*c_{-1}=t
b_3*t=b_4.
```

## Backward Extension In Row b_2

Apply the edge predecessor triangle to:

```text
b_2*u_2=0.
```

It gives:

```text
b_2*(u_2*(0*b_2))=u_2
0*((b_2*0)*b_2)=u_2.
```

The second identity is exactly:

```text
0*(t*b_2)=u_2.
```

Since:

```text
0*b_2=b_1,
```

define:

```text
e_2=u_2*b_1.
```

Then:

```text
b_2*e_2=u_2.
```

So row `b_2` actually contains:

```text
e_2 -> u_2 -> 0 -> t.
```

Since `u_2!=0`, the edge `b_2*u_2=0` is nontrivial, and the triangle
noncollision gives:

```text
e_2!=u_2.
```

If:

```text
e_2=0,
```

then row `b_2` sends:

```text
0 -> u_2
0 -> t,
```

so:

```text
u_2=t.
```

Thus, outside the origin self-swap role, the new predecessor `e_2` is neither
`0` nor `u_2`.

## Backward Extension In Row b_3

Apply the edge predecessor triangle to:

```text
b_3*c_{-1}=t.
```

It gives:

```text
b_3*(c_{-1}*(t*b_3))=c_{-1}
t*((b_3*t)*b_3)=c_{-1}.
```

The second identity is exactly:

```text
t*(b_4*b_3)=c_{-1}.
```

Define:

```text
e_3=c_{-1}*(t*b_3).
```

Then:

```text
b_3*e_3=c_{-1}.
```

So row `b_3` actually contains:

```text
e_3 -> c_{-1} -> t -> b_4.
```

If:

```text
c_{-1}=t,
```

then row `b_3` sends `t` to both:

```text
t
b_4,
```

so:

```text
t=b_4.
```

This is the old special offset self-return.

Outside that special role, the edge `b_3*c_{-1}=t` is nontrivial, and the
triangle noncollision gives:

```text
e_3!=c_{-1}.
```

## Hard Branch After Extension

The genuinely hard branch is now:

```text
u_2 fresh,
c_{-1} fresh,
e_2 fresh,
e_3 fresh,
no origin self-swap,
no offset self-return,
no row-t coincidence.
```

In that branch, the forced picture is:

```text
row b_2:
  e_2 -> u_2 -> 0 -> t

row b_3:
  e_3 -> c_{-1} -> t -> b_4
```

This is the key pressure-growth mechanism: a fully fresh double interval does
not merely persist; it extends backward in both active rows.

## Candidate Termination Form

A future proof can aim for:

```text
Repeated double backward extension cannot remain fresh in a finite E677 magma.
Eventually one of the new predecessors must hit:
  0;
  a bad-cycle element;
  the other interval;
  a row-t pressure column;
  or a self-swap/self-return role.
```

This would close the no-free-tail branch without broad enumeration.

# Bad-Tail Repeat Pressure Network

Date: 2026-06-07.

Status:

```text
proved pressure network / occupied-r role split / fresh-r candidate
```

Purpose:

```text
Continue the branch r_4=r_2 beyond the zero-triangle normal form and expose
the simultaneous pressure in rows u, r, and b_4.
```

## Setup

Assume:

```text
t=r_2!=0
s=b_3
s*t=b_4
s*b_4=u
u*s=0.
```

Define:

```text
r=u*0.
```

The zero-triangle lemma gives:

```text
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

Since:

```text
u*s=0
u*d=b_4,
```

and `0!=b_4`, row-`u` injectivity gives:

```text
d!=s.
```

## Three-Spoke Fan In Row u

Apply the edge triangle to:

```text
u*s=0.
```

Its first predecessor edge is:

```text
u*(s*(0*u))=s.
```

Define:

```text
e=s*(0*u).
```

Then row `u` has:

```text
s -> 0
d -> b_4
e -> s.
```

If:

```text
0,b_4,s
```

are distinct, then:

```text
s,d,e
```

are distinct columns.

Apply the triangle to:

```text
u*d=b_4.
```

Define:

```text
f=d*(b_4*u).
```

Then:

```text
u*f=d.
```

So row `u` contains the predecessor segments:

```text
e -> s -> 0
f -> d -> b_4.
```

This is a local double interval inside the repeat branch.

Special occupied source-orbit role:

```text
bad_tail_u_equals_s_fan_lemma.md
```

If:

```text
u=s=b_3,
```

then shared-edge divergence between rows `0` and `s` forces:

```text
t=b_2.
```

Row `s` contains:

```text
b_2 -> b_4 -> b_3 -> 0,
```

and the common edge `0 -> b_2` has at least the sources:

```text
b_2,b_4,0*0
```

in the full long-cycle role.

## Return Fan In Row b_4

Apply the inverse edge chain to:

```text
r*u=b_4.
```

It gives:

```text
u=b_4*((r*b_4)*r).
```

Define:

```text
x_r=(r*b_4)*r.
```

Then:

```text
b_4*x_r=u.
```

But the repeat assumption also gives:

```text
b_4*0=t,
```

and the bad-cycle ladder gives:

```text
b_4*r_3=b_5.
```

Therefore row `b_4` has:

```text
0   -> t
r_3 -> b_5
x_r -> u.
```

Immediate collision roles:

```text
u=t
  => x_r=0;

u=b_5
  => x_r=r_3;

u distinct from t,b_5
  => row b_4 has three distinct occupied outputs.
```

## General Restrictions On r

Because `0` is a bad element:

```text
y*0!=0
```

for every `y`.  Hence:

```text
r=u*0!=0.
```

The general forbidden zero edge also gives:

```text
u*0!=pred_0(u).
```

Therefore:

```text
r!=pred_0(u).
```

## Shared Row-0 Edge Role u=b_5

Use:

```text
bad_cycle_shared_edge_descent_lemma.md
```

If:

```text
u=b_5,
```

then:

```text
r*b_5=b_4
```

shares the row-`0` edge:

```text
0*b_5=b_4.
```

Let:

```text
c=r*b_4.
```

The shared-edge descent lemma gives:

```text
c!=b_3
c*r=r_3.
```

Thus the role `u=b_5` creates an explicit descent to the earlier tail `r_3`.
It is stronger than generic extra pressure in row `r`.

## Occupied Bad-Cycle Role

Suppose:

```text
r=b_j.
```

Then:

```text
b_j*u=b_4.
```

The bad-cycle ladder independently gives:

```text
b_j*r_{j-1}=b_{j+1}.
```

If:

```text
b_{j+1}=b_4,
```

then `j=3` on the bad-cycle indexing and row-`b_3` injectivity gives:

```text
u=r_2=t.
```

Consequently:

```text
s*t=b_4
s*b_4=t
t*s=0.
```

So row `s=b_3` swaps:

```text
t <-> b_4,
```

and row `t` has the zero edge:

```text
t*s=0.
```

This is the occupied self-swap role.

If:

```text
b_{j+1}!=b_4,
```

then row `b_j` has two distinct occupied outputs:

```text
b_j*u=b_4
b_j*r_{j-1}=b_{j+1}.
```

Applying the edge triangle to the first edge also yields:

```text
b_j*(u*(b_4*b_j))=u
b_4*((b_j*b_4)*b_j)=u.
```

Thus every occupied `r=b_j` adds:

```text
one predecessor edge in row b_j;
one new spoke in row b_4.
```

## Fresh-r Role

If `r` is fresh relative to the bad-cycle block, then:

```text
r*u=b_4
```

makes row `r` active.  Its triangle gives:

```text
r*(u*(b_4*r))=u
b_4*x_r=u.
```

So the fresh branch contains:

```text
row r:
  u -> b_4
  u*(b_4*r) -> u

row b_4:
  0 -> t
  r_3 -> b_5
  x_r -> u

row u:
  e -> s -> 0
  f -> d -> b_4.
```

This is a three-row pressure network, not a single free return row.

## Current Structural Split

The repeat branch now has:

```text
1. occupied r=b_3:
   explicit self-swap plus t*s=0;

2. occupied r=b_j, j!=3:
   row-b_j pressure plus an extra row-b_4 spoke;

3. fresh r:
   coupled pressure in rows r, b_4, and u.
```

The next useful computation should distinguish these three roles in the
normalized size-9 case, rather than enumerate arbitrary cells.

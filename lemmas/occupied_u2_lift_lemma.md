# Occupied u2 Lift Lemma

Date: 2026-06-05.

Status:

```text
proved consequence / role split candidate
```

Purpose:

```text
Classify what happens when the origin predecessor u_2 in the double interval
is not fresh but lies in the bad row-0 cycle.
```

## Setup

Use the nonzero-offset setup:

```text
t=r_2=b_k
t!=0
b_2*0=t
b_3*t=b_4
```

and:

```text
u_2=0*(t*b_2)
z_t=(b_2*t)*b_2
c_{-1}=t*(b_4*b_3).
```

Known pressure edges:

```text
b_2*u_2=0
b_2*0=t
t*z_t=0
t*(b_4*b_3)=c_{-1}.
```

## Lift From Row 0

Assume:

```text
u_2=b_j.
```

Since:

```text
u_2=0*(t*b_2)
```

and row `0` satisfies:

```text
0*b_{j+1}=b_j,
```

injectivity of row `0` gives:

```text
t*b_2=b_{j+1}.
```

Thus an occupied origin predecessor immediately lifts into row `t`.

## Row-t Pressure Form

If `t=b_k`, the bad-cycle ladder also gives:

```text
t*r_{k-1}=b_{k+1}.
```

So row `t` contains:

```text
t*z_t=0
t*(b_4*b_3)=c_{-1}
t*b_2=b_{j+1}
t*r_{k-1}=b_{k+1}.
```

This is stronger than merely saying that `u_2` is occupied: it gives a
four-edge pressure configuration in the row of the offset itself.

## Immediate Coincidence Roles

If:

```text
b_{j+1}=0,
```

then row `t` has:

```text
t*b_2=0
t*z_t=0,
```

so:

```text
b_2=z_t.
```

This is a row-`t` zero collision.

If:

```text
b_{j+1}=c_{-1},
```

then row `t` has:

```text
t*b_2=c_{-1}
t*(b_4*b_3)=c_{-1},
```

so:

```text
b_2=b_4*b_3.
```

This ties the origin predecessor interval directly to the offset predecessor
interval.

If:

```text
b_{j+1}=b_{k+1},
```

then row `t=b_k` has:

```text
t*b_2=b_{k+1}
t*r_{k-1}=b_{k+1},
```

so:

```text
b_2=r_{k-1}.
```

This is the bad-cycle descent role: an older tail value is forced to be the
fixed bad-cycle element `b_2`.

If none of these coincidences happens, row `t` has an extra occupied output
in addition to the zero edge, the backward-offset edge, and the bad-cycle
ladder edge.

## Consequence For The Main Lemma

The role:

```text
u_2=b_j
```

should no longer be treated as a broad occupied case.  It splits into:

```text
row-t zero collision;
origin/offset predecessor coupling;
bad-cycle descent;
or extra row-t pressure.
```

Thus the genuinely hard branch is narrower:

```text
u_2 fresh
and
c_{-1} fresh
and
no row-t coincidence.
```

That is the correct next fresh-interval target.

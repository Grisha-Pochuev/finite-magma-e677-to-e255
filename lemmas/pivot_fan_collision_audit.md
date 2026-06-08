# Pivot Fan Collision Audit

Date: 2026-06-07.

Status:

```text
complete ten-pair audit / one proved trap / bounded residual roles
```

Purpose:

```text
Classify all ten possible output coincidences in the five-spoke pivot fan
without treating a column equality as an automatic contradiction.
```

## Setup

Let:

```text
t=r_2=b_k
a=b_2
b=b_3
alpha=a*t
v=b*t=b_4.
```

The five-spoke fan in row `t` is:

```text
column z          -> output 0
column h          -> output c
column g_alpha    -> output w
column g_v        -> output p
column r_{k-1}    -> output d=b_{k+1},
```

where:

```text
z=(a*t)*a=alpha*a
h=(b*t)*b=v*b
c=pred_b(t)

w=(a*alpha)*a
alpha*w=t

p=(b*v)*b
v*p=t

g_alpha=(alpha*t)*alpha
g_v=(v*t)*v.
```

Since row `t` is injective, an equality of two outputs is equivalent to an
equality of their two columns.

There are exactly ten output pairs.

## Complete Collision Table

| # | Output collision | Forced column equality | Additional structural meaning | Status |
|---|---|---|---|---|
| 1 | `0=c` | `z=h` | The two source rows have the same predecessor of `t`: `pred_a(t)=pred_b(t)=0`. | **Known backward-zero trap.** |
| 2 | `0=w` | `z=g_alpha` | Since `alpha*w=t`, this gives `alpha*0=t`; both `a*0=t` and `alpha*0=t`. | Shared-zero-column coupling; not a contradiction by row injectivity. |
| 3 | `0=p` | `z=g_v` | Since `v*p=t` and `v=b_4`, this gives `b_4*0=t`, hence `r_4=r_2`. | Bad-tail repeat role; not yet closed generally. |
| 4 | `c=w` | `h=g_alpha` | Both `b*c=t` and `alpha*c=t`. | Common-column return coupling between rows `b_3` and `alpha`. |
| 5 | `c=p` | `h=g_v` | Both `b*c=t` and `v*c=t`. | Common-column return coupling between rows `b_3` and `b_4`. |
| 6 | `w=p` | `g_alpha=g_v` | Both `alpha*w=t` and `v*w=t`. | Common-column return coupling between successor rows `alpha` and `b_4`. |
| 7 | `0=d` | `z=r_{k-1}` | `b_{k+1}=0`; the ladder edge in row `t` is another zero edge. | Bad-cycle boundary/zero role; exact meaning depends on cycle length. |
| 8 | `c=d` | `h=r_{k-1}` | The predecessor `c=pred_b(t)` equals the next bad-cycle point `b_{k+1}`. | Direct source-cycle/bad-cycle coupling. |
| 9 | `w=d` | `g_alpha=r_{k-1}` | The row-`a` successor-return output is `b_{k+1}`. | A-side return meets the bad-cycle ladder. |
| 10 | `p=d` | `g_v=r_{k-1}` | The offset relay output `p` is `b_{k+1}`. | B-side return meets the bad-cycle ladder. |

## Verification Of The Additional Meanings

### Pair 2: `0=w`

Known:

```text
alpha*w=t.
```

Thus:

```text
w=0
=> alpha*0=t.
```

Together with:

```text
a*0=t,
```

this is a common-column coupling in column `0`.  It does not violate
injectivity because the equal outputs occur in different rows.

### Pair 3: `0=p`

Known:

```text
v*p=t
v=b_4.
```

Thus:

```text
p=0
=> b_4*0=t
=> r_4=t=r_2.
```

This is a genuine repeat among bad-tail values, but no general contradiction
has yet been proved from `r_4=r_2`.

### Pairs 4-6: Common-Column Returns

The defining return edges are:

```text
b*c=t
alpha*w=t
v*p=t.
```

Therefore:

```text
c=w => b*c=t and alpha*c=t;
c=p => b*c=t and v*c=t;
w=p => alpha*w=t and v*w=t.
```

These are cross-row common-column couplings.  They are not row collisions.

### Pairs 7-10: Ladder Collisions

These are exactly the four equivalences from the pivot ladder fan:

```text
d=0 <=> r_{k-1}=z
d=c <=> r_{k-1}=h
d=w <=> r_{k-1}=g_alpha
d=p <=> r_{k-1}=g_v.
```

They connect the old tail column `r_{k-1}` to one of the four explicit fan
columns.

## Session Result

The ten-pair audit is complete.

It proves:

```text
only 0=c is already the known backward-zero trap;
the other nine collisions are structured coupling roles, not automatic
contradictions.
```

The residual branches fall into three families:

```text
1. common-column return couplings:
   0=w, c=w, c=p, w=p;

2. bad-tail repeat:
   0=p => r_4=r_2;

3. ladder couplings:
   d in {0,c,w,p}.
```

## Next Single Frontier

The most promising next subproblem is:

```text
Bad-Tail Repeat Lemma:
under the nonzero-offset pressure diamond, prove that r_4=r_2 is impossible
or forces descent/self-swap.
```

Reason:

```text
it is the only nontrivial fan collision that immediately produces an equality
between two canonical bad-tail values, rather than only a cross-row coupling.
```

No broad computation is justified yet.  A future targeted check should test
the fixed symbolic hypothesis:

```text
r_2=t!=0
r_4=t.
```

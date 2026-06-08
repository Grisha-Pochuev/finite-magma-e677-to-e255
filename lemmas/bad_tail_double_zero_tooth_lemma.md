# Bad-Tail Double-Zero-Tooth Lemma

Date: 2026-06-07.

Status:

```text
proved termination of the r=b_4 relay
```

Purpose:

```text
Show that the apparent recursive r=b_4 zero relay cannot continue for a third
consecutive row-b_3 orbit point.
```

## Setup

Use:

```text
s=b_3
B=b_4=pred_0(s)
s*B=u
s*u=q
s*q=v.
```

Assume the bad-tail repeat zero tooth:

```text
u*s=0.
```

The source-orbit ladder for:

```text
B -> u -> q
```

gives:

```text
u*(q*s)=B.
```

Therefore:

```text
q*s=0
<=>
u*0=B.
```

This is exactly the occupied role:

```text
r=u*0=b_4.
```

## No Third Consecutive Zero Tooth

Assume:

```text
u*s=0
q*s=0.
```

Suppose, for contradiction, that the next orbit point also satisfies:

```text
v*s=0.
```

The ladder for:

```text
u -> q -> v
```

gives:

```text
q*(v*s)=u.
```

Hence:

```text
q*0=u.
```

Apply the inverse edge chain to:

```text
q*s=0.
```

Since:

```text
pred_0(s)=B,
```

we get:

```text
(q*0)*q=B.
```

Using `q*0=u`:

```text
u*q=B.
```

But the first ladder tooth already gave:

```text
u*0=B.
```

Row `u` is injective, so:

```text
q=0.
```

Then `q*s=0` becomes:

```text
0*s=0.
```

In the bad row-`0` cycle, the unique predecessor of `0` is `b_1`, while:

```text
s=b_3!=b_1.
```

This is impossible.

Therefore:

```text
v*s!=0.
```

So row `s=b_3` cannot have three consecutive orbit points:

```text
u,q,v
```

all mapping to `0` in column `s`.

## Exit Restrictions

Let:

```text
R=q*0.
```

The inverse edge chain for `q*s=0` gives:

```text
R*q=B.
```

The two-step source reconstruction lemma gives:

```text
R!=B.
```

Indeed, rows `u` and `q` both send:

```text
s -> 0,
```

and if both also sent:

```text
0 -> B,
```

they would be the same row.  But `u!=q`, because row `s` sends:

```text
B -> u -> q
```

with `B!=u`.

The no-third-zero argument also gives:

```text
R!=u.
```

For if `R=u`, then the ladder edge:

```text
q*(v*s)=u
```

and `q*0=R=u` would force `v*s=0`.

Finally, the general bad-zero restriction gives:

```text
R!=0.
```

Thus the relay exits into:

```text
R notin {0,B,u}.
```

## Correct Interpretation Of The r=b_4 Role

The role:

```text
u*0=B
```

does create a second zero source:

```text
q*s=0.
```

But it is not an indefinitely repeatable `r=B` recursion.  At the next orbit
step, the continuation condition shifts:

```text
v*s=0
<=>
q*0=u.
```

The theorem above rules this out.

Therefore the occupied role `r=b_4` has a finite structural outcome:

```text
one additional zero tooth is forced;
a third consecutive zero tooth is impossible;
the new return R=q*0 avoids 0,b_4,u.
```

If:

```text
R=s=b_3,
```

then:

```text
q=pred_s(B)=t,
t*s=0,
t*0=s,
```

so the branch enters the already identified self-swap zero relay and creates
the second zero triangle from `bad_tail_repeat_self_swap_relay.md`.

The remaining exits are:

```text
R=b_j, j notin {3,4},
or R fresh.
```

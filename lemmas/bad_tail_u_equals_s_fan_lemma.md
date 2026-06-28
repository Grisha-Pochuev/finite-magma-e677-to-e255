# Bad-Tail Role u=s Fan Lemma

Date: 2026-06-07.

Status:

```text
proved structural reduction / zero tips closed / external-tip role open
```

Purpose:

```text
Classify the occupied source-orbit role u=b_3 without continuing a blind
numeric split.
```

## Setup

Use:

```text
P=b_2
s=b_3
B=b_4
t=r_2=P*0

s*t=B
s*B=u
u*s=0
B*0=t.
```

Assume:

```text
u=s.
```

Then:

```text
s*B=s
s*s=0.
```

## Shared Edge With Row 0

Row `0` contains:

```text
0*B=s
0*s=P.
```

Row `s` contains:

```text
s*B=s
s*s=0.
```

Thus rows `0` and `s` share the edge:

```text
B -> s.
```

Their next outputs are:

```text
P and 0,
```

which are distinct.

The shared-edge divergence lemma gives the common return equality:

```text
P*0=0*s.
```

Since:

```text
0*s=P,
```

we obtain:

```text
t=P.
```

Therefore:

```text
r_2=b_2.
```

This is the exact occupied offset forced by `u=s`.

## Forced Row-s Segment

Substituting `t=P`, row `s` contains:

```text
s*P=B
s*B=s
s*s=0.
```

So row `s=b_3` has the consecutive segment:

```text
P -> B -> s -> 0.
```

The final zero edge gives the usual return:

```text
(s*0)*s=B.
```

Since:

```text
s*0=r_3,
```

this is:

```text
r_3*s=B.
```

## Common-Edge Fan Over 0 -> P

The bad-tail repeat gives:

```text
B*0=t=P.
```

The role above gives:

```text
P*0=P.
```

The universal row-`0` reduction gives:

```text
(0*0)*0=P.
```

Therefore the common-edge fiber:

```text
F(0,P)={x : x*0=P}
```

contains:

```text
P,
B,
0*0.
```

Whenever these source rows are distinct, the common-edge fan lemma gives three
pairwise distinct forward tips:

```text
P*P,
B*P,
(0*0)*P,
```

and one common return hub:

```text
(P*P)*P
=(B*P)*B
=((0*0)*P)*(0*0)
=pred_P(0).
```

In the full long bad cycle these are three distinct fan sources.

## Size-9 Diagnostic

For the normalized full 9-cycle, the role is:

```text
t=P=7
s=6
B=5
u=s=6.
```

The targeted requirements were:

```text
7*0=7
5*0=7
6*7=5
6*5=6
6*6=0.
```

One 60-second focused search timed out:

```text
status: timeout
nodes: 4785
dead ends: 4750
```

The closure layer forced:

```text
1*0=7
4*7=3
8*1=7.
```

These have structural interpretations:

```text
1*0=7  -> (0*0)*0=b_2;
4*7=3  -> bad-cycle ladder b_5*r_4=b_6;
8*1=7  -> bad-cycle ladder b_1*r_0=b_2.
```

No new numeric marker appeared, so the timeout is not a reason to raise the
limit.  The correct continuation is the three-source fan above `0 -> P`.

## Current Subfrontier

The role `u=s` is reduced to:

```text
r_2=b_2;
row b_3 contains b_2 -> b_4 -> b_3 -> 0;
the edge 0 -> b_2 has at least the sources b_2,b_4,0*0.
```

Further progress:

```text
bad_tail_u_equals_s_zero_tip_closure.md
```

All three possible zero tips of this fan are impossible in the long-cycle
role.  Therefore at least one pairwise distinct tip lies outside:

```text
{0,b_2,b_4,0*0}.
```

The next useful lemma should show that this fan must:

```text
transfer its external tip into a row-0 edge and descend;
create an aligned interval overlap;
or force a forbidden fixed point y*0=0.
```

Do not rerun the same size-9 node without a new fan invariant.

## Final Size-9 Split Before Stopping

For the normalized full 9-cycle:

```text
P=b_2=7
s=b_3=6
B=b_4=5
A=0*0=1.
```

The strongest fan tip is:

```text
C=P*P=7*7.
```

A row-domain diagnostic reduced it to:

```text
C in {1,2,3,5}
  = {A,b_7,b_6,B}.
```

The zero role:

```text
C=0
```

was already closed symbolically in:

```text
bad_tail_u_equals_s_zero_tip_closure.md
```

Two internal roles were then closed by complete targeted searches:

```text
C=A=1  -> status none, 18.47s, 205 nodes;
C=B=5  -> status none, 22.19s, 246 nodes.
```

Thus the entire size-9 role `u=s` is reduced to exactly:

```text
C=b_7=2
or
C=b_6=3.
```

Both far roles are now closed:

```text
C=b_7=2 -> status none, 46.31s, 640 nodes;
C=b_6=3 -> status none, 28.37s, 410 nodes.
```

Their common first mechanism is proved generally in:

```text
fixed_source_zero_descent_lemma.md
```

It gives:

```text
C*P=0*C
P*(0*C)=0.
```

Thus:

```text
C=b_7 -> P*b_6=0;
C=b_6 -> P*b_5=0.
```

Therefore the full normalized size-9 role `u=s=b_3` is closed.

The remaining mathematical task is to lift the fixed-source zero descent from
this size-9 certificate into the general long-cycle No-Free-Tail argument.

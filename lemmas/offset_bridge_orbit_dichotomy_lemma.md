# Offset Bridge-Orbit Dichotomy Lemma

Date: 2026-06-04.

Status:

```text
candidate structural lemma / not yet full main proof
```

Purpose:

```text
Replace the too-local occupied-block idea by a role split that survives
different offsets r_2=b_t.
```

This file follows:

```text
main_bad_cycle_no_free_tail_lemma.md
offset_relay_template_for_main_lemma.md
marker_bridge_transfer_lemma.md
row6_orbit_relay_lemma.md
long_cycle_r2_classification.md
```

## Setup

Let:

```text
b_j = L_0^{-j}(0)
r_j = b_j*0
```

Assume:

```text
r_2=b_t != 0.
```

The bad-cycle predecessor ladder gives:

```text
b_3*b_t=b_4.
```

Define:

```text
u=b_3*b_4
p=u*b_3=(b_3*b_4)*b_3.
```

The inverse-edge chain gives the universal offset relay:

```text
b_4*p=b_t.
```

## Bridge Transfer Lemma

Call a row `a` a bridge for this offset if:

```text
a*b_t=b_4
a*b_4=b_3.
```

Then the bridge forces:

```text
b_3*a=p.
```

Proof:

From:

```text
b_3*b_t=b_4
```

the inverse-edge chain gives:

```text
b_t=b_4*((b_3*b_4)*b_3)=b_4*p.
```

From the bridge:

```text
a*b_t=b_4
a*b_4=b_3
```

the same inverse-edge chain gives:

```text
b_t=b_4*((a*b_4)*a)=b_4*(b_3*a).
```

Since row `b_4` is injective:

```text
b_3*a=p.
```

So every bridge transfers the offset marker `p` back into row `b_3`.

## Bridge Uniqueness

There is at most one bridge row.

If `a` and `a'` are both bridges, then:

```text
b_3*a=p
b_3*a'=p
```

and row `b_3` is injective.  Hence:

```text
a=a'.
```

This makes bridge existence a controlled split, not a large family of cases.

## Special Offsets Explained

### Offset `r_2=b_4`

Here:

```text
b_3*b_4=b_4.
```

So:

```text
u=b_4
p=b_4*b_3
b_4*p=b_4.
```

This is the old local self-return:

```text
b_4*(b_4*b_3)=b_4.
```

In case45 numbers this was:

```text
7*0=5
6*5=5
5*(5*6)=5.
```

This explains why the local occupied-block exclusion was unusually sharp in
the `r_2=b_4` branch.

### Offset `r_2=b_5`

Here row `0` is automatically a bridge:

```text
0*b_5=b_4
0*b_4=b_3.
```

Therefore:

```text
b_3*0=p.
```

In case45 numbers this is:

```text
7*0=4
6*4=5
0*4=5
0*5=6
=> 6*0=(6*5)*6.
```

This explains why the old row-6 transfer in `7*0=4` worked: it was the bridge
case with bridge row `0`, not a universal reason to split by `b_3*0`.

### Ordinary Far Offsets

For offsets farther away, row `0` is no longer the same bridge.  In case45 this
was visible for:

```text
7*0=2
7*0=3
```

where row `0` has:

```text
0*2=3
0*3=4
```

instead of the bridge pattern:

```text
a*t=5
a*5=6.
```

Old diagnostics showed that bridge rows, when present, still close by the same
transfer:

```text
a*t=5
a*5=6
=> 6*a=(6*5)*6.
```

In the next two paragraphs, `t` is the numeric case45 value in `7*0=t`, not
the bad-cycle index in `b_t`.

For numeric `t=2` all bridge rows:

```text
a in {1,3,4,7,8}
```

closed under this split.

For numeric `t=3` all bridge rows:

```text
a in {1,2,4,7,8}
```

closed under the same split.

## No-Bridge Fallback

If no bridge exists, the old `b_3*0` marker is no longer the right invariant.
The stable fallback is the row-`b_3` orbit.

For any two consecutive row-`b_3` edges:

```text
b_3*z0=z1
b_3*z1=z2
```

the inverse-edge chain gives:

```text
z1*(z2*b_3)=z0.
```

This is the orbit relay.

In case45 the no-bridge fallback after `7*0=2,3` began with:

```text
z0=b_1=8
```

so the first marker was:

```text
6*8.
```

This matches the recorded diagnostics:

```text
no bridge -> split by b_3*b_1
```

not:

```text
no bridge -> split by b_3*0.
```

## Dichotomy Candidate

The current candidate lemma is:

```text
For an offset r_2=b_t, the next forced structure is either

1. an offset self-return, if b_t=b_4;
2. a unique bridge row a, forcing b_3*a=(b_3*b_4)*b_3;
3. no bridge, in which case the row-b_3 orbit relay from the nearest senior
   cycle point becomes the next invariant.
```

In all three cases, the branch is not free:

```text
the offset marker p must either be occupied by a bridge/self-return,
or the row-b_3 orbit produces return edges z1*(z2*b_3)=z0.
```

This is the strongest current candidate for the missing no-free-tail
termination mechanism.

## Remaining Gap

This is not yet the full No-Free-Tail Lemma.

What remains is to prove that the no-bridge orbit relay cannot keep moving
forever inside a finite bad-cycle tail.  The expected termination statement is:

```text
In the no-bridge branch, the row-b_3 orbit either hits 0, creates a short
cycle with a forced return edge, or descends to an already occupied lower
source row.
```

This is now a smaller target than the original problem, because bridge branches
and the special offset branches have a unified explanation.

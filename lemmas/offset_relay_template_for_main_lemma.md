# Offset Relay Template For Main Lemma

Date: 2026-06-04.

Status:

```text
symbolic offset template / main-lemma boundary
```

Purpose:

```text
Understand how the main No-Free-Tail Lemma must split by the offset
r_2=b_t.
```

This file follows:

```text
main_bad_cycle_no_free_tail_lemma.md
bad_cycle_descent_domain_template.md
```

## Setup

Let:

```text
b_j = L_0^{-j}(0)
r_j = b_j*0
```

Assume a counterexample, so:

```text
r_2 != 0.
```

Split by offset:

```text
r_2=b_t.
```

The bad-cycle predecessor ladder gives:

```text
b_3*r_2=b_4
```

so under the offset:

```text
b_3*b_t=b_4.
```

This is the basic offset edge.

## Universal Offset Relay

Apply the inverse-edge chain to:

```text
b_3*b_t=b_4.
```

It gives:

```text
b_t = b_4*((b_3*b_4)*b_3).
```

Define:

```text
u=b_3*b_4
p=u*b_3=(b_3*b_4)*b_3.
```

Then every offset has the row-`b_4` relay:

```text
b_4*p=b_t.
```

This is the correct general form behind the local `t=4` branch.

## The Special Offset `t=4`

If:

```text
t=4
```

then:

```text
b_3*b_4=b_4.
```

So:

```text
u=b_4
p=b_4*b_3.
```

Writing:

```text
w=b_4*b_3
```

the universal offset relay becomes:

```text
b_4*w=b_4.
```

This is exactly the local row-5 marker:

```text
5*6=w
5*w=5.
```

Therefore the strong local occupied-block exclusion in
`bad_cycle_descent_domain_template.md` depends on the fact that the offset edge
is a self-return:

```text
b_3*b_4=b_4.
```

## General Offset Behavior

For arbitrary `t`, the same reasoning gives only:

```text
b_4*p=b_t.
```

This is still useful, but it is weaker than:

```text
b_4*p=b_4.
```

Now let the row-`b_4` descent be:

```text
a=b_4*0
```

and use the bad-cycle predecessor ladder:

```text
b_4*r_3=b_5.
```

So row `b_4` has at least two forced outputs:

```text
b_4*p=b_t
b_4*r_3=b_5
```

plus:

```text
b_4*0=a.
```

Immediate collision exclusions now depend on whether:

```text
p != 0,
r_3 != 0,
p != r_3,
```

and on whether `a` equals one of:

```text
b_t, b_5.
```

Because `0` is bad:

```text
r_3 != 0.
```

So:

```text
a != b_5
```

remains a universal occupied-output exclusion.

But:

```text
a != b_t
```

requires:

```text
p != 0.
```

If `p=0`, then:

```text
b_t=b_4*0=a,
```

so the offset relay has folded into the descent value itself.  That is not the
same role as the `t=4` self-return.

## What Happens To `a=b_3`

In the special `t=4` branch, the exclusion:

```text
a != b_3
```

used:

```text
b_3*b_4=b_4.
```

For general `t`, assume:

```text
a=b_3.
```

E677 with:

```text
x=0
y=b_4
```

gives:

```text
0 = b_4*(0*((b_4*0)*b_4)).
```

Using:

```text
b_4*0=b_3
```

this becomes:

```text
0 = b_4*(0*(b_3*b_4)).
```

With:

```text
u=b_3*b_4
```

we get:

```text
b_4*succ0(u)=0.
```

So in a general offset, `a=b_3` does not immediately contradict.  It creates a
row-`b_4` zero-hit:

```text
b_4*succ0(u)=0.
```

In the special case `t=4`, `u=b_4`, so:

```text
succ0(u)=succ0(b_4)=b_3
```

and the zero-hit becomes:

```text
b_4*b_3=0.
```

But this is:

```text
w=0,
```

contradicting the residual assumption.  That is why the special branch closes
more sharply.

## Main-Lemma Consequence

The global no-free-tail proof should not expect the same occupied block for
every offset.

The correct offset split is:

```text
r_2=b_t
=> b_3*b_t=b_4
=> u=b_3*b_4
=> p=u*b_3
=> b_4*p=b_t.
```

Then:

```text
a=b_4*0
```

falls into one of three roles:

```text
1. occupied-output collision:
   a equals an already forced row-b_4 output, such as b_5 or b_t with p!=0;

2. zero-hit transfer:
   a=b_3 forces b_4*succ0(b_3*b_4)=0;

3. outside-role tail:
   a avoids the occupied outputs and must be handled by a source-row zero trap.
```

This is a better candidate for the main proof than the single local block:

```text
{0,b_2,b_3,b_4,b_5}.
```

## Next Work

Update 2026-06-04:

```text
offset_bridge_orbit_dichotomy_lemma.md
```

This comparison produced a better structural split than the original
vanish/collide/marker question.

The key new object is a bridge row:

```text
a*b_t=b_4
a*b_4=b_3.
```

Every such bridge satisfies:

```text
b_3*a=(b_3*b_4)*b_3=p.
```

There is at most one bridge row, because row `b_3` is injective.

This explains two old special cases:

```text
r_2=b_4:
  b_3*b_4=b_4
  so b_4*(b_4*b_3)=b_4
  the old occupied-block exclusion is a self-return case.

r_2=b_5:
  row 0 is a bridge:
    0*b_5=b_4
    0*b_4=b_3
  so b_3*0=p.
```

For farther offsets, row `0` is not automatically a bridge.  The current
dichotomy is:

```text
bridge exists:
  unique bridge row a transfers p into row b_3 by b_3*a=p;

no bridge:
  the next invariant is the row-b_3 orbit relay
    b_3*z0=z1, b_3*z1=z2 => z1*(z2*b_3)=z0.
```

Therefore the next main-lemma target is no longer:

```text
Does p vanish, collide, or create a usable row-b_4 marker?
```

It is:

```text
Prove that the no-bridge row-b_3 orbit relay cannot create an infinite
zero-avoiding free tail in a finite bad cycle.
```

Historical prompt before this update:

```text
Use this template to compare the offset branches already present in case45:

  r_2=b_2, b_3, b_4, b_5

corresponding to:

  7*0=7, 6, 5, 4

in the pure 9-cycle notation.

The key question for each offset:

  Does p=(b_3*b_4)*b_3 vanish, collide, or create a usable row-b_4 marker?

This is the next structural test for the main No-Free-Tail Lemma.
```

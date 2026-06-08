# Common-Edge Fan Lemma

Date: 2026-06-07.

Status:

```text
general proved
```

Purpose:

```text
Extend the shared-edge divergence diamond from two source rows to an arbitrary
fiber of source rows.
```

## Setup

Fix `a,b` and let:

```text
F(a,b)={p : p*a=b}.
```

For each:

```text
p in F(a,b),
```

define:

```text
c_p=p*b.
```

## Distinct Forward Tips

If:

```text
c_p=c_q,
```

then rows `p` and `q` contain the same interval:

```text
a -> b -> c_p.
```

The two-step source reconstruction lemma gives:

```text
p=q.
```

Therefore:

```text
p -> c_p
```

is injective on `F(a,b)`.

So all forward tips:

```text
{c_p : p in F(a,b)}
```

are pairwise distinct.

## Common Return Hub

The source-orbit ladder for:

```text
p*a=b
p*b=c_p
```

gives:

```text
b*(c_p*p)=a.
```

Since row `b` is injective, the column sending row `b` to `a` is unique:

```text
h=pred_b(a).
```

Hence every source in the fiber satisfies:

```text
c_p*p=h.
```

The full fan is:

```text
p*a=b
p*b=c_p
c_p*p=h
b*h=a,
```

where:

```text
h=pred_b(a)
```

is common and the values `c_p` are pairwise distinct.

## Reconstruction Form

Each source row is recovered from its own forward tip:

```text
p=pred_{c_p}(h).
```

Thus a common first edge creates:

```text
one distinct forward tip per source;
one common return hub for the whole fiber.
```

## Unavoidable Fan Above A Bad Zero Column

Let `0` be a bad element.  The standard bad-zero restriction says:

```text
p*0!=0
```

for every row `p`.

There are `n` rows but only `n-1` possible nonzero values of `p*0`.
Therefore some nonzero `b` has:

```text
|F(0,b)|>=2.
```

So every hypothetical finite counterexample contains an unavoidable
nontrivial common-edge fan above column `0`:

```text
p*0=b
q*0=b
p!=q.
```

Its distinct tips and common hub are:

```text
c_p=p*b
c_q=q*b
c_p!=c_q

c_p*p=c_q*q=pred_b(0).
```

This is a global structural consequence of badness, independent of a
particular size or bad-cycle offset.

## Bad-Tail Repeat Corollary

The collision:

```text
r_4=r_2=t
```

means:

```text
b_2*0=t
b_4*0=t.
```

Thus rows `b_2` and `b_4` belong to the same fan `F(0,t)`.

Define:

```text
alpha=b_2*t
delta=b_4*t.
```

Then:

```text
alpha!=delta
alpha*b_2=delta*b_4=pred_t(0).
```

This is the pivot zero column:

```text
t*pred_t(0)=0.
```

Therefore the bad-tail repeat is not only the zero triangle found earlier.  It
is also an unavoidable two-source subfan over the common edge:

```text
0 -> t.
```

## New Strategic Direction

The No-Free-Tail problem may be attacked by common-edge fans:

```text
1. a bad column 0 forces at least one nontrivial fan F(0,b);
2. every source in that fan creates a distinct forward tip;
3. all tips return to one common hub pred_b(0);
4. bad-cycle and pivot fans may force one of those tips or sources back into
   an occupied interval, where aligned-overlap or descent lemmas apply.
```

The remaining task is to connect the unavoidable global fan to the specific
fan containing:

```text
b_2*0=r_2.
```

For a fan whose middle value is itself a source, the connection to the
double-interval method is now explicit:

```text
self_containing_fan_spine_lemma.md
```

## Diagnostic Boundary

The known non-right-cancellative finite `E677` model of size `496` was checked
against this fan structure:

```text
all 496 right columns have collisions;
maximum common-edge fiber size is 16;
all 892800 tested collision pairs have distinct forward tips;
all 892800 have the common twisted return predicted above;
E255 still holds everywhere.
```

Therefore:

```text
large common-edge fans are not contradictions by themselves.
```

The proof must use the extra bad-element condition:

```text
no y satisfies y*0=0,
```

together with the bad-cycle and pivot structure.  Do not switch to a strategy
that tries to prove right cancellativity or to forbid common-edge fans
globally.

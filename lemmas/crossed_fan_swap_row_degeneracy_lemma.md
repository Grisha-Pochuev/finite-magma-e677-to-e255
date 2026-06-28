# Crossed-Fan Swap-Row Degeneracy Lemma

Date: 2026-06-17.

Status:

```text
general proved
```

## Statement

Fix distinct elements `a,b`.  Suppose a row `p` swaps them:

```text
p*a=b,
p*b=a.
```

Then `p` is the unique row with this ordered two-step interval.  In particular:

```text
q*a=b,
q*b=a
=> q=p.
```

Equivalently, in a crossed fan

```text
F(a,b)={x:x*a=b},
F(b,a)={x:x*b=a},
```

there is at most one row lying in the intersection in the swap form

```text
x*a=b,
x*b=a.
```

## Proof

This is exactly the two-step source reconstruction lemma applied to the
ordered interval:

```text
a -> b -> a.
```

If both rows `p` and `q` contain:

```text
p*a=b, p*b=a,
q*a=b, q*b=a,
```

then both contain the same ordered two-step interval `a -> b -> a`, so
`p=q`.

## Use In The Bad-Target Crossed-Fan Frontier

For a bad target `b`, a crossed fan around `a` may include a row that swaps
`a` and `b`.  Such a row is not an independent outgoing branch plus an
independent incoming return; it is a same-row two-cycle.

Thus the crossed-fan boundary should be split into:

```text
1. swap-row degenerate case:
   one shared row has x*a=b and x*b=a;

2. proper crossed-fan case:
   no selected source row swaps a and b.
```

If an outgoing source `p` has `p*b=a` and an incoming source `r` has
`r*a=b`, then either `p=r` or the configuration is impossible.  This removes
the false impression that two short returns can be independent.

The shared-row case is handled in:

```text
swap_row_target_advance_loop_lemma.md
```

It is a same-row target-advance loop, not a proper independent crossed fan.

## Diagnostics

The size-8 raw-label check with distinct rows forced to make the two short
returns:

```text
2*1=0, 2*0=1,
4*0=1, 4*1=0
```

inside the bad-target crossed-fan setup closed completely:

```text
status: none
time: 64.54s
nodes: 721
dead ends: 720
```

This finite check is only a sanity check; the proof above is the actual reason.

# A-Row Zero Trap Lemma

Date: 2026-06-04.

Status:

```text
candidate sublemma / row-3 and row-8 instances closed in current cascade
```

Scope:

```text
finite E677 magma
full bad row-0 cycle 0 -> 1 -> ... -> 8 -> 0
row-5 source orbit segment:
  5*0=a
  5*a=b
  c=b*5
```

## Statement

If:

```text
5*0=a
5*a=b
c=b*5
```

then the source-orbit ladder gives:

```text
a*c=0
```

where:

```text
c=b*5
```

This is the common form behind the late row-3 and row-8 traps in the L3
zero-hit transfer.

## Consequences

Let:

```text
d=a*0
```

Then the inverse-edge chain on:

```text
a*c=0
```

gives:

```text
d*a=pred0(c)
```

Also E677 with:

```text
x=c
y=a
```

gives:

```text
c = a*(c*((a*c)*a))
```

Since:

```text
a*c=0
0*a=succ0(a)
```

this becomes:

```text
c = a*(c*succ0(a))
```

So the reusable trap form is:

```text
a*c=0
d=a*0
d*a=pred0(c)
c=a*(c*succ0(a))
```

## Known Instances

### Row-3 Instance

For:

```text
a=3
```

we have:

```text
succ0(a)=4
```

so:

```text
3*c=0
d=3*0
d*3=pred0(c)
c=3*(c*4)
```

This is the previously closed row-3 late trap in:

```text
row3_late_trap_lemma.md
```

### Row-8 Instance

For:

```text
a=8
```

we have:

```text
succ0(a)=0
```

so:

```text
8*c=0
d=8*0
d*8=pred0(c)
c=8*(c*0)
```

This is the current live sublemma inside:

```text
l3_zero_hit_transfer_lemma.md
```

Current evidence:

```text
(a,b)=(8,3) closes by this trap.
(a,b)=(8,7), c=2 closes by this trap.
(a,b)=(8,7), c=3 is partially reduced; d=6 closes.
```

Additional extracted role:

```text
row-8 self-zero killer:
  8*8=0
  d=8*0
  d*8=7
  d in {2,3}
  both d=2 and d=3 close.
```

This role appears for both:

```text
(a,b,c)=(8,3,8)
(a,b,c)=(8,7,8)
```

Remaining work:

```text
The row-8 role split is closed in the current L3 representative cascade.
```

Final row-8 non-self closure:

```text
(a,b,c)=(8,7,3)
d=8*0 in {1,2,3,6,8}
all d-values close.
```

So the current row-8 instance is closed:

```text
(a,b)=(8,3) -> closed
(a,b)=(8,7) -> closed
```

## Process Rule

Do not treat this as a new broad search tree.  The point of this file is to
factor the repeated tail:

```text
row-5 orbit -> a*c=0 -> row-a zero trap
```

out of the L3 cascade.

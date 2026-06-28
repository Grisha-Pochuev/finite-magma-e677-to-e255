# Period-3 Shifted Hook Pair Implies Named Fan

Date: 2026-06-28.

Status:

```text
proved reduction / two db-supported shifted hooks imply Ib*h=c
```

## Purpose

The named middle-target fan was reduced to:

```text
Ib*h=c.
```

This file records a more structured sufficient condition.  Instead of trying
to prove `Ib*h=c` directly, it is enough to prove the single shifted input
identity:

```text
(Ib*c)*Ib=Ic.
```

A concrete db-supported way to get this identity is the shifted hook pair:

```text
Ib*c=z,
z*Ib=Ic.
```

Both identities hold in all currently cached strict public db period-3 cases,
but the proof below only uses E677 once after assuming them.

## Setup

Use the clean period-3 zipper:

```text
z*h=b,
b*h=c,
c*h=z.
```

The `H_h` zipper triangle has:

```text
z*alpha=h,
b*Ib=h,
c*Ic=h.
```

So:

```text
c*Ic=h.
```

## Lemma 1

Assume:

```text
(Ib*c)*Ib=Ic.
```

Then:

```text
Ib*h=c.
```

## Proof

Apply E677 with:

```text
x=c,
y=Ib.
```

Then:

```text
c = Ib*(c*((Ib*c)*Ib)).
```

Using:

```text
(Ib*c)*Ib=Ic,
c*Ic=h,
```

the right side becomes:

```text
Ib*(c*Ic)
= Ib*h.
```

Therefore:

```text
Ib*h=c.
```

## Lemma 2

The shifted hook pair:

```text
Ib*c=z,
z*Ib=Ic.
```

implies:

```text
(Ib*c)*Ib=Ic.
```

Therefore, by Lemma 1, it also implies:

```text
Ib*h=c.
```

## Proof

Using the two assumptions:

```text
Ib*c=z,
z*Ib=Ic,
```

we get immediately:

```text
(Ib*c)*Ib
= z*Ib
= Ic.
```

Then Lemma 1 gives:

```text
Ib*h=c.
```

By:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
```

this gives the named outgoing fan in `H_c`:

```text
row b:  h -> b*c,
row Ib: h -> Ib*c,
```

with distinct outputs in the clean residual.

## Diagnostic Status

The db identity scan confirms that all `6240` cached strict period-3 examples
have:

```text
Ib*c=z,
z*Ib=Ic,
Ib*h=c.
```

The local saturation check:

```text
tools\node-portable\node.exe tools\period3_zipper_saturation.js 5 16 1200000
```

still does not derive either shifted hook from the bare clean period-3 zipper.
It does derive only the ordinary zipper input shifts:

```text
alpha=(c*z)*c,
Ib=(z*b)*z,
Ic=(b*c)*b.
```

So the useful next target is not another one-step equality hunt for `Ib*h=c`.
It is to prove either the single shifted input identity:

```text
(Ib*c)*Ib=Ic,
```

or the stronger shifted hook pair:

```text
Ib*c=z,
z*Ib=Ic,
```

from global/minimality/core data, or show that failure reduces to the existing
clean V3 admissibility frontier.

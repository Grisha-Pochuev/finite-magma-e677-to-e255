# Period-3 Shifted Input Failure V3 Bridge Lemma

Date: 2026-06-28.

Status:

```text
proved reduction / failure of the shifted input identity becomes a V3 bridge
```

## Purpose

The direct named fan route is now:

```text
(Ib*c)*Ib=Ic  =>  Ib*h=c  =>  named fan in H_c.
```

This file records what happens if the shifted input identity fails cleanly.
The failure is not an unrelated local obstruction: it becomes a standard
same-input V3 bridge after target advance.

## Setup

Use the clean period-3 zipper:

```text
z*h=b,
b*h=c,
c*h=z.
```

The `H_h` zipper triangle has:

```text
b*Ib=h,
c*Ic=h.
```

In target `H_c`, row `b` already gives:

```text
row b: h -> BC,
BC=b*c.
```

Define:

```text
A=Ib*c,
K=A*Ib=(Ib*c)*Ib,
L=c*K.
```

## Forced Row-Ib Edge In H_c

Apply E677 with:

```text
x=c,
y=Ib.
```

Then:

```text
c = Ib*(c*((Ib*c)*Ib)).
```

Using the definitions of `K` and `L`, this is:

```text
Ib*L=c.
```

Since:

```text
Ib*c=A,
```

row `Ib` contributes an edge in `H_c`:

```text
row Ib: L -> A.
```

So `H_c` contains the pair:

```text
row b:  h -> BC,
row Ib: L -> A.
```

## Fan Case

If:

```text
K=Ic,
```

then:

```text
L=c*K=c*Ic=h.
```

Thus row `Ib` gives:

```text
Ib*h=c,
```

and the named fan follows from:

```text
period3_named_fan_reduces_to_Ibhc_lemma.md
period3_shifted_hook_pair_implies_named_fan_lemma.md
```

## Failure Case

Assume:

```text
K!=Ic.
```

Since row `c` is left-cancellative and:

```text
c*K=L,
c*Ic=h,
```

we get:

```text
L!=h.
```

Thus the two `H_c` edges above have distinct inputs.

If the pair has a local hit, it routes by the standard same-target roles:

```text
A=BC                         -> incoming merge in H_c;
L=BC or A=h                  -> input-output path hit;
L or A hits watched/core data -> ordinary attachment;
same full ported interval     -> source-row reconstruction.
```

## Clean Residual

If none of those hits occurs, the shifted-input failure is a clean same-target
pair in `H_c`:

```text
row b:  h -> BC,
row Ib: L -> A,
h!=L,
BC!=A.
```

Target-advance this pair.  Row `b` gives:

```text
H_BC: c -> b*BC.
```

Row `Ib` gives:

```text
H_A: c -> Ib*A.
```

Therefore the clean failure is a standard same-input V3 bridge with common
input:

```text
c.
```

## Consequence

The shifted input identity gives a sharper fan/V3 dichotomy:

```text
1. (Ib*c)*Ib=Ic
   -> Ib*h=c
   -> named H_c fan at h;

2. (Ib*c)*Ib!=Ic, clean
   -> same-target pair in H_c
   -> target-advanced V3 bridge at common input c.
```

So the period-3 residual now has two equivalent V3 exits:

```text
Ib*h!=c       -> V3 at common input h between rows b and Ib;
(Ib*c)*Ib!=Ic -> V3 at common input c after target advance from H_c.
```

The second version is often cleaner because it lives directly at the middle
target `H_c`, where the public db core-hook diagnostic sees the named fan.

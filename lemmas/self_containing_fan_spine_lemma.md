# Self-Containing Fan Spine Lemma

Date: 2026-06-08.

Status:

```text
general proved
```

Purpose:

```text
Connect the common-edge fan to the double-interval pressure mechanism.
```

## Setup

Assume:

```text
P*0=P.
```

Define:

```text
C=P*P
h=pred_P(0)
a=0*P.
```

## Central Zero Descent

The fixed-source zero descent lemma gives:

```text
h=C*P=0*C
P*h=0.
```

So row `P` already contains:

```text
h -> 0 -> P -> C.
```

## Backward Extension

Apply the edge-predecessor triangle to:

```text
P*h=0.
```

It gives:

```text
P*(h*(0*P))=h.
```

Define:

```text
e=h*a=h*(0*P).
```

Then row `P` contains the five-point spine:

```text
e -> h -> 0 -> P -> C.
```

## Fan Returns

Let:

```text
F(0,P)={q : q*0=P}.
```

For each source:

```text
q in F(0,P),
```

define its tip:

```text
T_q=q*P.
```

The common-edge fan lemma gives:

```text
T_q*q=h
```

for every `q` in the fiber.

Thus:

```text
all tips T_q are pairwise distinct;
all return to the same hub h;
the source P itself contributes T_P=C;
C*P=h;
row P extends backward through e=h*(0*P).
```

The complete structure is:

```text
row P:
  e -> h -> 0 -> P -> C

for every q with q*0=P:
  q*P=T_q
  T_q*q=h.
```

## Distinctness In A Bad-Cycle Role

Assume:

```text
P!=0
C and h=0*C are consecutive distinct points of the bad row-0 cycle.
```

Then:

```text
0,P,C,h
```

are distinct.

Row-`P` injectivity therefore implies:

```text
e,h,0,P
```

are distinct columns.

If `e=C`, then the row-`P` spine identifies:

```text
P*C=h
```

and closes a four-step source-row cycle:

```text
C -> h -> 0 -> P -> C.
```

Otherwise the spine contains five distinct points.

## Application To The u=b_3 Role

Use:

```text
P=b_2
s=b_3
B=b_4
A=0*0.
```

The fan sources include:

```text
P,B,A.
```

Their tips:

```text
C=P*P
D=B*P
E=A*P
```

are pairwise distinct and satisfy:

```text
C*P=D*B=E*A=h.
```

Together with the spine:

```text
e -> h -> 0 -> P -> C,
```

this is a double-interval pressure object:

```text
one long active interval in row P;
two additional distinct fan tips returning to its backward hub h.
```

## New Main Use

Future work on `u=b_3` should classify the first occupied hit among:

```text
e,h,C,D,E.
```

It should not branch independently on arbitrary cells of rows `P,B,A`.

The desired termination statement is:

```text
the fan spine cannot close in a finite bad-cycle block without:
  sharing a row-0 edge and descending;
  producing an aligned two-edge overlap;
  or forcing a zero-column fixed point.
```

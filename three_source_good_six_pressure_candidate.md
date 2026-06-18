# Three-Source Good-Six Pressure Candidate

Date: 2026-06-08.

Status:

```text
main candidate sublemma / not proved
```

## Setup

Assume:

```text
P*0=P
A*0=P
B*0=P
```

with three distinct sources:

```text
P,A,B.
```

Assume the self source `P` has the exact good six-cycle:

```text
P -> C -> f -> e -> h -> 0 -> P
```

and:

```text
h*P=P.
```

The three-source fan gives distinct tips:

```text
C=P*P
D=B*P
E=A*P,
```

with:

```text
C*P=D*B=E*A=h.
```

The source `A` is canonically anchored by:

```text
terminal_source_anchored_fan_lemma.md
```

If the bad row-0 cycle has length `m`, then:

```text
A=0*0=b_{m-1}
A*r_{m-2}=0
A*0=P
0*(P*A)=r_{m-2}.
```

Thus the three backward feet are:

```text
h
r_{m-2}
alpha_B=0*(P*B),
```

and they are pairwise distinct.

The bridge expansion gives:

```text
C*k=P
D*w_B=P
E*w_A=P,
```

where:

```text
k=(P*C)*P=f*P
w_B=(B*D)*B
w_A=(A*E)*A.
```

## Candidate Statement

The three-source fan cannot coexist with the exact good six-cycle while all:

```text
D,E,k,w_B,w_A
```

avoid:

```text
an internal source-tip collision;
a bridge collision;
a zero bridge;
the hub tip h;
an occupied bad-cycle descent;
an aligned two-edge overlap.
```

Equivalently, the bridge expansion of a three-source self-containing fan
cannot remain collision-free around a good six-cycle.

## Already Proved Parts

```text
D,E,C are pairwise distinct;
none of D,E,C equals P;

k,w_B,w_A differ from their own sources P,B,A;

bridge 0 <=> its tip is an internal source;
bridge P <=> its tip fixes P on the right;

under good P this is equivalent to tip h, by two-step source reconstruction
for the repeated interval P -> P -> P;

equal bridges create a second-generation common-edge fan;

distinct source tips cannot form a two-cycle;

internal source tips create zero teeth.
```

## Size-9 Diagnostic

Use the normalized row-0 9-cycle and:

```text
P=7
C=2
h=3.
```

Impose the good-P role:

```text
h*P=P.
```

For the exact fixed-point candidate:

```text
f=P*C
f*f=C,
```

all five possible `f` values close:

```text
f=1 -> immediate contradiction;
f=4 -> immediate contradiction;
f=5 -> 14 row-P candidates, all die after row P;
f=6 -> immediate contradiction;
f=8 -> 23 row-P candidates, all die after row P.
```

More importantly, for `f=5`:

```text
sources P,A only:
  5 row-P candidates survive the first row;

add only the third source B*0=P:
  14 row-P candidates exist and all die after row P.
```

No other `u=b_3` row constraints are needed for this closure.

Interpretation:

```text
the decisive finite pressure is the third common-edge source,
not the special continuation of row b_3.
```

This diagnostic is evidence for the candidate, not a general proof.

## Next Structural Split

Classify:

```text
k,w_A,w_B
```

by their first intersection with:

```text
the source set {P,A,B};
the tip set {C,D,E};
the six-cycle {P,C,f,e,h,0};
each other.
```

Bridge collisions and zero bridges are already classified. The next unresolved
overlap is:

```text
a bridge equals a different original source.
```

This overlap now has the exact transfer:

```text
fan_bridge_zipper_extension_lemma.md
```

If:

```text
T*w=P
V=T*P,
```

then:

```text
V*T=pred_P(w).
```

So a bridge-source or bridge-tip hit immediately returns to the predecessor of
that hit in row `P`.

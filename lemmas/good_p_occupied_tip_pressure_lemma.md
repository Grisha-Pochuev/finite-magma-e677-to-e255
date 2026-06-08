# Good-P Occupied-Tip Pressure Lemma

Date: 2026-06-08.

Status:

```text
general proved / pressure split for good-P with occupied C
```

## Setup

Use the fan spine and assume:

```text
C=b_j
h=0*C=b_{j-1}.
```

Assume `P` is good:

```text
h*P=P.
```

## Ladder Comparison

The bad-cycle predecessor ladder in row `h=b_{j-1}` gives:

```text
h*r_{j-2}=C.
```

The good-P condition gives:

```text
h*P=P.
```

If:

```text
r_{j-2}=P,
```

then row `h` would give:

```text
h*P=C
h*P=P,
```

so:

```text
C=P,
```

contradicting the fan-spine distinctness.

Therefore:

```text
good P and C=b_j
=>
r_{j-2}!=P.
```

In the remaining case, row `h` has two distinct forced occupied edges:

```text
h*P=P
h*r_{j-2}=C.
```

This is occupied-row pressure in `b_{j-1}`.

## Size-9 Interpretation

In the normalized size-9 `u=b_3` role:

```text
P=b_2
r_4=b_2.
```

Therefore:

```text
C=b_6
```

is impossible under `h*P=P`, because then:

```text
j=6
r_{j-2}=r_4=P.
```

This explains the immediate diagnostic contradiction:

```text
C=b_6, h*P=P -> contradiction.
```

For:

```text
C=b_7,
```

the lemma gives only:

```text
r_5!=P
```

and the row-`b_6` pressure:

```text
b_6*P=P
b_6*r_5=b_7.
```

The size-9 diagnostic still closes the branch after row `P`, but the general
symbolic reason for this second role is not yet extracted.

## Next Use

In the good-P length-six frontier:

```text
P -> C -> f -> e -> h -> 0 -> P
f*f=C
h*P=P,
```

if `C` is occupied, immediately split:

```text
r_{j-2}=P   -> contradiction;
r_{j-2}!=P -> occupied-row pressure in row b_{j-1}.
```


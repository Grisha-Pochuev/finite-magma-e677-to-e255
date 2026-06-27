# Cycle-Entry Hub Transport Lemma

Date: 2026-06-09.

Status:

```text
general proved / transports the orbit bridge into the new fan hub
```

## Setup

Use the first repeated point of a right-`P` orbit:

```text
q_j=q_k=Q
0<j<k.
```

Let:

```text
x=q_{j-1}
y=q_{k-1}.
```

Then:

```text
x!=y
x*P=Q
y*P=Q.
```

For every orbit point `q_i`, let `a_i` be the unique value with:

```text
q_i*a_i=P.
```

Since `q_j=q_k=Q`, uniqueness gives:

```text
a_j=a_k=a_Q,
```

where:

```text
Q*a_Q=P.
```

## New Fan

Rows `x,y` share:

```text
P -> Q.
```

Their backward feet are:

```text
a_{j-1}
a_{k-1},
```

and are distinct.

Define their forward tips:

```text
U=x*Q
V=y*Q.
```

The common-edge fan lemma gives:

```text
U!=V
U*x=V*y=pred_Q(P).
```

But `Q*a_Q=P`, so:

```text
pred_Q(P)=a_Q.
```

Therefore the complete cycle-entry relay box is:

```text
row x:
  a_{j-1} -> P -> Q -> U

row y:
  a_{k-1} -> P -> Q -> V

U*x=V*y=a_Q
Q*a_Q=P.
```

## Transport Meaning

The common hub of the new fan is exactly the bridge/predecessor label of the
repeated old-orbit state:

```text
old state bridge a_Q
=
new fan hub pred_Q(P).
```

Thus changing the common edge from:

```text
0 -> P
```

to:

```text
P -> Q
```

does not discard the old bridge recursion. Its current bridge becomes the
return hub of the new two-sided fan.

## Good-P Boundary

If the original orbit starts in `F(0,P)` and the repetition is external, then:

```text
a_Q!=0,
```

because `a_Q=0` would mean `Q*0=P`, a return to the source fiber.

If `P` is good, then:

```text
a_Q!=P,
```

because `Q*P=P` would make `Q` the unique right fixer `h`; the right-`P` orbit
would then move to `P` and return to the source fiber.

Hence every genuinely external cycle-entry fan has:

```text
a_Q notin {0,P}.
```

## Remaining Role

The next No-Free-Tail classifier is now the location of the transported hub:

```text
a_Q.
```

If it hits the bad cycle, the good-six spine, or an earlier transported hub,
the existing descent and collision lemmas apply. The only open branch is a
fresh nonzero hub accompanying a genuinely non-aligned edge `P -> Q`.


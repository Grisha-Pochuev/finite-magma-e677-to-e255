# Self-Containing Fan Escape Lemma

Date: 2026-06-07.

Status:

```text
general proved
```

Purpose:

```text
Show that a common-edge fan containing its own middle value cannot close only
on its source set.
```

## Statement

Fix:

```text
a!=b
```

and let:

```text
S subseteq F(a,b)={p : p*a=b}.
```

Assume:

```text
b in S.
```

For each `p in S`, define:

```text
c_p=p*b.
```

Then:

```text
all c_p are pairwise distinct;
no c_p equals b;
at least one c_p lies outside S.
```

More sharply:

```text
either some c_p=a,
or some c_p lies outside S union {a}.
```

## Proof

The common-edge fan lemma gives pairwise distinct values `c_p`.

Since:

```text
p*a=b
```

and:

```text
a!=b,
```

row-`p` injectivity gives:

```text
p*b!=b.
```

Thus:

```text
c_p!=b
```

for every `p in S`.

There are `|S|` distinct tips, but only `|S|-1` elements of `S` different from
`b`.  Therefore the tip set cannot be contained in `S`.

If no tip equals `a`, the escaping tip lies outside:

```text
S union {a}.
```

## Interpretation

A fan with its middle value among its own sources has only two outcomes:

```text
one tip returns to the initial input a;
or the fan creates a genuinely external tip.
```

This is a counting statement internal to one fan.  It does not assume right
cancellativity.

# Target-Advance Row-Orbit Lemma

Date: 2026-06-17.

Status:

```text
general proved / same-row recurrence normal form
```

## Statement

Fix a row `p`.  Suppose:

```text
p*x_i=x_{i+1}
```

along the row orbit of `p`.

Then the ported interval state with target `x_i` is exactly:

```text
(x_i, x_{i-1}, x_{i+1}).
```

After target advance, the same row `p` gives:

```text
(x_{i+1}, x_i, x_{i+2}).
```

Thus target advance for a fixed source row is just a one-step sliding window
along the row orbit of that source row.

## Proof

The ported interval:

```text
(x_i, x_{i-1}, x_{i+1})
```

means precisely:

```text
p*x_{i-1}=x_i,
p*x_i=x_{i+1}.
```

Changing the target from `x_i` to `x_{i+1}` keeps the same row `p` and uses
the next two cells:

```text
p*x_i=x_{i+1},
p*x_{i+1}=x_{i+2}.
```

So the next ported interval is:

```text
(x_{i+1}, x_i, x_{i+2}).
```

## Recurrence Classification

Because every row is a permutation in a finite E677 magma, the row orbit of
`p` is periodic.  A same-row repetition of a full ported interval is therefore
only a repetition of three consecutive positions on this row cycle.

It is not by itself a contradiction.

The contradiction appears only when the same full ported interval occurs in
two independent branch roles, because then two-step source reconstruction
forces the two branch rows to be the same.

## Use In No-Free-Tail

The remaining same-row recurrence boundary should be treated as:

```text
a row-orbit cycle interacting with another branch row,
```

not as a finished relay termination argument.

The next useful lemma should involve at least two source rows or a return to a
previous junction.  A one-row target-advance loop alone is too weak.

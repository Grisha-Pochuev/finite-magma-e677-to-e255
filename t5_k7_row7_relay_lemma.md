# T5 Layer `6*6=7`: Row-7 Relay

Date: 2026-05-25.

## Status

```text
local closed layer
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=7
```

This is the second closed layer inside the special top branch `t=5`, after the
closed zero-pass-through layer `6*6=0`.

## Structural Reason

The row-6 orbit relay says:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

Apply it to:

```text
z0=6
z1=7
z2=q
q=6*7
```

Then:

```text
6*6=7
6*7=q
h=q*6
=> 7*h=6
```

So the correct split is not a blind search over row `6`, but:

```text
q=6*7
h=q*6
7*h=6
```

## Coverage Certificate

Initial diagnostic:

```text
q=6*7 in {1,2,3,4}
```

The special value:

```text
q=1 -> status none, 48.55s, 1651 nodes
```

For:

```text
q in {2,3,4}
```

the direct checks timed out, so the relay split was used:

```text
h=q*6
7*h=6
```

### `q=2`

```text
h=1 -> status none, 11.79s, 21 nodes
h=2 -> status none, 18.18s, 392 nodes
h=3 -> status none, 28.19s, 824 nodes
h=4 -> status none, 29.76s, 921 nodes
h=5 -> status none, 13.18s, 64 nodes
h=8 -> timeout at 45s, then split by 8*8
```

The tail:

```text
q=2
h=8
```

closed by active-row split:

```text
8*8=2 -> status none, 15.59s, 93 nodes
8*8=3 -> status none, 23.63s, 153 nodes
8*8=4 -> status none, 19.67s, 133 nodes
8*8=5 -> status none, 18.19s, 40 nodes
```

### `q=3`

```text
h=1 -> status none, 14.22s, 49 nodes
h=2 -> status none, 14.17s, 364 nodes
h=3 -> status none, 18.16s, 397 nodes
h=4 -> status none, 26.56s, 895 nodes
h=5 -> status none, 12.88s, 72 nodes
h=8 -> timeout at 40s, then split by 8*8
```

The tail:

```text
q=3
h=8
```

closed by:

```text
8*8=2 -> status none, 6.35s, 1 node
8*8=3 -> status none, 15.29s, 91 nodes
8*8=4 -> status none, 20.19s, 132 nodes
8*8=5 -> status none, 18.59s, 40 nodes
```

### `q=4`

```text
h=1 -> status none, 14.01s, 49 nodes
h=2 -> status none, 28.31s, 867 nodes
h=3 -> status none, 7.73s, 1 node
h=4 -> status none, 18.49s, 400 nodes
h=5 -> status none, 7.97s, 1 node
h=8 -> timeout at 40s, then split by 8*8
```

The tail:

```text
q=4
h=8
```

closed by:

```text
8*8=2 -> status none, 23.89s, 131 nodes
8*8=3 -> status none, 6.80s, 1 node
8*8=4 -> status none, 19.87s, 91 nodes
8*8=5 -> status none, 20.54s, 37 nodes
```

Therefore:

```text
case45
7*0=5
6*5=5
6*6=7
status: closed
```

## Interpretation

The layer `6*6=7` is a clean example of the general row-6 orbit relay:

```text
6 -> 7 -> q
```

The relay transfers the problem to:

```text
row 7 at column h=q*6
```

When `h=8`, the active residue consistently moves to row `8` and closes by
the self-cell split:

```text
8*8 in {2,3,4,5}
```

This suggests a reusable rule for later `t=5` layers:

```text
follow the row-6 orbit first;
if the relay target is 8, switch to active row 8 and split by 8*8.
```

## Remaining Frontier

Special branch `t=5` now has:

```text
7*0=5
6*5=5
6*6 in {1,2,3,4,6,8}
```

Recommended next step:

```text
try k=1 next, because it is now the smallest remaining row-6 domain;
use the same orbit relay:
6*6=1
q=6*1
h=q*6
1*h=6
```

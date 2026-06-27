# A2 Row-5 Completion Trap Lemma

Date: 2026-06-04.

Status:

```text
candidate sublemma / diagnostic finite certificate
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=4
6*4=0
6*0=1
1*6=3
5*1=4
4*7=6
4*5=7
5*6=3
5*0=2
```

This file records the new branch factorization found while transferring the
L3 zero-hit cascade beyond the hard representative `w=2`.

## Structural Setup

The branch:

```text
w=5*6=3
a=5*0=2
```

has the row-5 orbit:

```text
5*6=3
5*3=5
```

The second edge is forced in the late `a=2` tails:

```text
5*2=b
b in {7,8}
=> 5*3=5
```

Now let:

```text
p=5*5
```

The source-orbit ladder on:

```text
5*6=3
5*3=5
```

gives:

```text
3*p=6
```

So the apparent row-5 completion problem is not a 15-case row enumeration.
It is controlled by the single marker:

```text
p=5*5
```

## Diagnostic Compression

For:

```text
5*2=7
```

the row-5 completion domain allows:

```text
p in {0,1,8}
```

For:

```text
5*2=8
```

the row-5 completion domain allows:

```text
p in {0,1}
```

All five marker nodes close immediately:

```text
5*2=7, p=0 -> contradiction, 1 node
5*2=7, p=1 -> contradiction, 1 node
5*2=7, p=8 -> contradiction, 1 node
5*2=8, p=0 -> contradiction, 1 node
5*2=8, p=1 -> contradiction, 1 node
```

Thus the `a=2` tail has a compact completion trap:

```text
a=2
late b in {7,8}
=> forced 5*3=5
=> p=5*5 is in a short list
=> every p-marker is contradictory
```

## Micro-Trap Signatures

The closure traces show three reusable signatures.

### `p=0`

For both `b=7` and `b=8`, closure forces:

```text
5*5=0
3*0=6
2*5=4
```

and the node contradicts immediately.

### `p=1`

For both `b=7` and `b=8`, closure forces:

```text
5*5=1
3*1=5
3*6=1
```

and the node contradicts immediately.

### `p=8`

This only appears for:

```text
5*2=7
```

Closure forces:

```text
5*5=8
3*8=6
8*5=6
2*0=2
```

and the node contradicts immediately.

## Interpretation

The `a=2` branch is not a new deep trap parallel to the row-3 and row-8
zero traps.  It folds back into row `5` itself:

```text
6 -> 3 -> 5 -> p
```

with the marker:

```text
3*p=6
```

This gives a third reusable role inside the L3 transfer cascade:

```text
a=3 -> row-3 zero trap
a=8 -> row-8 zero trap
a=2 -> row-5 completion trap via p=5*5
```

The next transfer step should use this as the closed role for residual
`w=3` and `w=8` cascades, instead of enumerating full row-5 completions again.

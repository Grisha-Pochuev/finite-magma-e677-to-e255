# K4 L3 A-Domain Restriction Lemma

Date: 2026-06-04.

Status:

```text
proved local restriction / transfer sublemma
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=4
6*4=0
6*0=r
r*6=3
5*r=4
4*7=6
4*5=7
w=5*6
5*w=5
a=5*0
4*a=3
```

This is the first fully symbolic transfer step above the representative
`w=2` cascade.  It explains why the next row-5 descent only has the already
known roles:

```text
a=1,2,3,8
```

with `a=w` excluded.

## Statement

In the `k=4` L3 zero-hit layer, after the row-5 bridge:

```text
w=5*6
a=5*0
```

and for a nonzero residual `w`, we have:

```text
a in {1,2,3,8} \ {w}
```

For the current `k=4` L3 transfer, the residual `w` values are:

```text
w in {1,2,3,8} \ {r}
```

after the separate quick-exit role:

```text
w=7
```

is removed.

## Proof Of The Exclusions

The known row-5 cells are:

```text
5*r=4
5*6=w
5*w=5
5*0=a
```

and the descent marker is:

```text
4*a=3
```

We exclude all values outside `{1,2,3,8}` and then exclude `a=w`.

### `a != 0`

Assume:

```text
5*0=0
```

Use E677 with:

```text
x=0
y=5
```

It gives:

```text
0 = 5*(0*((5*0)*5))
```

Using:

```text
5*0=0
0*5=6
0*6=7
```

this becomes:

```text
0 = 5*7
```

But row `5` already has:

```text
5*0=0
```

so row `5` would repeat the output `0` at columns `0` and `7`, impossible.

### `a != 4`

If:

```text
5*0=4
```

then row `5` repeats the output `4`, because:

```text
5*r=4
```

and in the L3 normal form:

```text
r != 0
```

### `a != 5`

If:

```text
5*0=5
```

then row `5` repeats the output `5`, because:

```text
5*w=5
```

and:

```text
w != 0
```

### `a != 6`

Assume:

```text
5*0=6
```

Again use E677 with:

```text
x=0
y=5
```

It gives:

```text
0 = 5*(0*((5*0)*5))
```

Now:

```text
(5*0)*5 = 6*5 = 5
0*5 = 6
```

so:

```text
0 = 5*6 = w
```

contradicting the residual assumption:

```text
w != 0
```

### `a != 7`

If:

```text
a=7
```

then the descent marker gives:

```text
4*7=3
```

but the L3 row-`k` marker for `k=4` already gives:

```text
4*7=6
```

contradiction.

### `a != w`

If:

```text
a=w
```

then:

```text
5*0=w
5*6=w
```

so row `5` repeats the output `w` at columns `0` and `6`, impossible.

## Diagnostic Sanity Checks

The symbolic restriction matches the current diagnostics.

For `r=1`:

```text
w=2 -> a in {1,3,8}
w=3 -> a in {1,2,8}
w=8 -> a in {1,2,3}
```

For `r=2`:

```text
w=1 -> a in {2,3,8}
w=3 -> a in {1,2,8}
w=8 -> a in {1,2,3}
```

Additional representatives:

```text
r=3,w=1 -> a in {2,3,8}
r=7,w=1 -> a in {2,3}
r=8,w=1 -> a in {2,3,8}
```

The `r=7,w=1` representative is narrower, but still satisfies the same
restriction.

## Interpretation

The k=4 L3 transfer now has a real finite role table above the late traps:

```text
w=7 -> quick exit
w in {1,2,3,8} \ {r}
  a=1 -> quick exit
  a=2 -> row-5 completion trap via p=5*5
  a=3 -> row-3 zero trap
  a=8 -> row-8 zero trap
```

The next gap is no longer the `a`-domain.  The next gap is to attach each
allowed `a` value to its corresponding already closed role uniformly across
the remaining `r` and `w` values.

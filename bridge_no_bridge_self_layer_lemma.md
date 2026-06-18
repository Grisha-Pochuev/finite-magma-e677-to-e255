# Bridge / No-Bridge Self-Layer Lemma

Date: 2026-05-25.

## Status

```text
candidate / local closed for t=2,3 self-layers in case45
```

This file summarizes the structural pattern that closed two neighboring
self-layers in `case45`.

## Setting

In `case45`, row `0` is the 9-cycle:

```text
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 0
```

The top branch is:

```text
7*0=t
```

The self-layer studied here is:

```text
6*t=5
6*6=6
6*5=t
```

The completed values are:

```text
t=2
t=3
```

## Bridge Split

A bridge row is a row `a` such that:

```text
a*t=5
a*5=6
```

The marker bridge transfer identity gives:

```text
6*a=t*6
```

So the bridge branch is cut by:

```text
u=t*6=6*a
```

For `t=2`, possible bridge rows were:

```text
a in {1,3,4,7,8}
```

All closed.

For `t=3`, possible bridge rows were:

```text
a in {1,2,4,7,8}
```

All closed.

## No-Bridge Split

If no bridge row exists, the senior marker remains active:

```text
6*8=m
```

The row-6 orbit relay gives:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

So the no-bridge branch is controlled by the orbit:

```text
8 -> m -> r -> ...
```

For `t=2`, all markers closed:

```text
6*8 in {1,3,4,7,8}
```

For `t=3`, all markers closed:

```text
6*8 in {1,2,4,7,8}
```

## Closed Local Result

The combined result is:

```text
case45
7*0=t
6*t=5
6*6=6
6*5=t
t in {2,3}
status: closed
```

Proof strategy:

```text
if bridge exists:
  use 6*a=t*6
  split by u=t*6=6*a

if no bridge exists:
  use senior orbit marker 6*8
  split by the row-6 orbit relay
```

## What Is Not Yet Proved

This is not yet a global lemma for all top branches.

The remaining special top branch:

```text
t=5
```

is different because:

```text
6*5=5
```

So the self-layer has a different shape.  It should not be assumed closed by
the same certificate without a separate check.

## Next Step

Test whether the bridge/no-bridge split has a meaningful analogue in the
special branch:

```text
case45
7*0=5
6*5=5
```

The first question should be structural:

```text
does the bridge notion a*5=5 and a*5=6 collapse immediately,
or does t=5 require a different active marker?
```

Do not start by enumerating all `6*8` markers for `t=5`.

# T5 Zero Pass-Through Layer

Date: 2026-05-25.

## Status

```text
local closed layer
```

This file records the first closed structural layer inside the special top
branch:

```text
case45
7*0=5
6*5=5
6*6=0
```

It is not a full closure of `t=5`. It is a closed sublayer and a useful
extension of the row-6 orbit relay.

## Structural Reason

Use the inverse edge chain:

```text
a*z=c  ==>  z=c*((a*c)*a)
```

With:

```text
a=6
z=6
c=0
```

we get:

```text
6=0*((6*0)*6)
```

In case45, row `0` is the fixed 9-cycle:

```text
0*5=6
```

Therefore, if:

```text
r=6*0
```

then:

```text
r*6=5
```

So the layer `6*6=0` is not a raw split. It forces the zero-pass-through relay:

```text
6 -> 0 -> r
r*6=5
```

## Coverage Certificate

In the base:

```text
7*0=5
6*5=5
6*6=0
```

the possible values are:

```text
r=6*0 in {1,2,3,4,8}
```

Checked sublayers:

```text
r=1, plus 1*6=5 -> status none, 33.51s, 2414 nodes
r=2, plus 2*6=5 -> status none, 48.32s, 11714 nodes
r=3, plus 3*6=5 -> status none, 42.56s, 5410 nodes
r=4, plus 4*6=5 -> status none, 57.95s, 3495 nodes
```

The only direct timeout was:

```text
r=8, plus 8*6=5 -> timeout at 75s
```

This timeout is not treated as a request for a bigger blind limit. The row-6
orbit continues:

```text
6 -> 0 -> 8 -> s
```

where:

```text
s=6*8 in {1,2,3,4,7}
```

Splitting by this next orbit edge closes the timeout:

```text
s=1 -> status none, 23.36s, 519 nodes
s=2 -> status none, 29.16s, 1680 nodes
s=3 -> status none, 32.49s, 1417 nodes
s=4 -> status none, 40.70s, 1781 nodes
s=7 -> status none, 34.67s, 1080 nodes
```

Therefore:

```text
case45
7*0=5
6*5=5
6*6=0
status: closed
```

## Interpretation

The special branch `t=5` does not follow the self-layer mechanism used for
`t=2,3`. It begins with row `5`, but the split `6*6=0` brings the problem back
to the row-6 orbit relay through a zero pass-through.

The useful pattern is:

```text
6*z0=0
6*0=z2
=> z2*6=pred0(z0)
```

For `z0=6`, this is:

```text
6*6=0
6*0=r
=> r*6=5
```

If the first zero-pass-through residue is still wide, continue along the same
row-6 orbit:

```text
6 -> 0 -> r -> s
```

instead of enumerating unrelated cells.

## Remaining Frontier

The special branch still has:

```text
7*0=5
6*5=5
6*6 in {1,2,3,4,6,7,8}
```

Earlier diagnostics gave row-6 domain sizes after fixing `6*6=k`:

```text
k=0 -> 366, now closed
k=1 -> 2554
k=2 -> 3079
k=3 -> 3036
k=4 -> 2878
k=6 -> 3645
k=7 -> 1595
k=8 -> 2836
```

Next recommended step:

```text
start with k=7, because it is the next smallest row-6 layer after k=0;
look for an orbit/role split before trying exact closure.
```

Do not return to the direct `p=5*5` split unless a new structural reason is
found. That split timed out too early and is currently considered a poor
frontier.

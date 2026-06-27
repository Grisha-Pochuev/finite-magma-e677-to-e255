# T5 Layer `6*6=1`: Row-1 Relay Progress

Date: 2026-05-25.

## Status

```text
closed layer
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=1
```

This layer is now closed.  It followed the previously closed layers:

```text
6*6=0
6*6=7
```

The historical progress notes below show how it was closed.

## Structural Rule

Use the row-6 orbit relay:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

For:

```text
6*6=1
q=6*1
h=q*6
```

the relay gives:

```text
1*h=6
```

So the intended split is:

```text
q=6*1
h=q*6
1*h=6
```

## Current Coverage

Diagnostic:

```text
q=6*1 in {0,2,3,4,6,7,8}
```

Closed immediately:

```text
q=0 -> h=0*6=7, plus 1*7=6 -> status none, 0.85s, 1 node
q=6 -> h=6*6=1, plus 1*1=6 -> status none, 0.89s, 1 node
```

The first wide q-layer:

```text
q=2
```

timed out directly:

```text
6*1=2 -> timeout at 50s, 4130 nodes
```

Using the relay split:

```text
h=2*6
1*h=6
```

closed all admissible h-values:

```text
h=1 -> status none, 12.44s, 101 nodes
h=2 -> status none, 19.61s, 300 nodes
h=3 -> status none, 24.00s, 1063 nodes
h=4 -> status none, 25.62s, 1015 nodes
h=5 -> status none, 16.37s, 303 nodes
h=7 -> status none, 14.46s, 174 nodes
h=8 -> status none, 28.08s, 854 nodes
```

Therefore:

```text
k=1, q=2
status: closed
```

## Remaining Frontier

Next wide q-layer:

```text
6*1=3 -> timeout at 35s, 1072 nodes
```

This should not be continued by simply raising the direct timeout. The correct
next layer is the relay:

```text
h=3*6
1*h=6
```

The diagnostic confirmed admissible relay values:

```text
h in {1,2,3,4,5,7,8}
```

The value `h=6` is not admissible because the diagnostic for `1*6` did not
include value `6`.

Using:

```text
h=3*6
1*h=6
```

closed all admissible h-values:

```text
h=1 -> status none, 14.47s, 191 nodes
h=2 -> status none, 14.55s, 413 nodes
h=3 -> status none, 21.24s, 335 nodes
h=4 -> status none, 35.90s, 2247 nodes
h=5 -> status none, 36.24s, 2673 nodes
h=7 -> status none, 15.21s, 233 nodes
h=8 -> status none, 40.03s, 1780 nodes
```

Therefore:

```text
k=1, q=3
status: closed
```

The next wide q-layer:

```text
6*1=4 -> timeout at 25s, 155 nodes
```

Again, the direct timeout was not extended.  The same relay split:

```text
h=4*6
1*h=6
```

closed all admissible h-values:

```text
h=1 -> status none, 15.11s, 183 nodes
h=2 -> status none, 19.20s, 1100 nodes
h=3 -> status none, 6.61s, 1 node
h=4 -> status none, 23.98s, 335 nodes
h=5 -> status none, 26.31s, 481 nodes
h=7 -> status none, 14.64s, 239 nodes
h=8 -> status none, 39.59s, 2125 nodes
```

Therefore:

```text
k=1, q=4
status: closed
```

The next q-layer:

```text
6*1=7 -> timeout at 25s, 325 nodes
```

Using:

```text
h=7*6
1*h=6
```

the admissible values are:

```text
h in {1,2,3,4,7,8}
```

Closed directly:

```text
h=1 -> status none, 18.13s, 157 nodes
h=2 -> status none, 25.81s, 988 nodes
h=4 -> status none, 44.15s, 1738 nodes
h=7 -> status none, 21.76s, 42 nodes
```

The two wider h-tails:

```text
h=3
h=8
```

closed by continuing the row-7 orbit.

For `h=3`, direct timeout:

```text
h=3 -> timeout at 35.97s, 1341 nodes
```

Then:

```text
7*7 in {0,1,2,4,7,8}
```

closed with:

```text
7*7=0 -> none, 14.96s, 31 nodes
7*7=1 -> none, 16.79s, 145 nodes
7*7=2 -> none, 33.81s, 582 nodes
7*7=4 -> none, 35.65s, 936 nodes
7*7=7 -> none, 31.92s, 1183 nodes
7*7=8 -> none, 36.66s, 914 nodes
```

For `h=8`, direct timeout:

```text
h=8 -> timeout at 45.98s, 1375 nodes
```

Then:

```text
7*7 in {0,1,2,3,4,7}
```

closed with:

```text
7*7=0 -> none, 17.34s, 71 nodes
7*7=1 -> none, 24.77s, 473 nodes
7*7=7 -> none, 36.30s, 1674 nodes
```

The sublayer `7*7=2` closed by continuing the row-7 orbit:

```text
7*2=0 -> none, 16.78s, 97 nodes
7*2=1 -> none, 17.61s, 73 nodes
7*2=3 -> none, 18.74s, 61 nodes
7*2=4 -> none, 18.36s, 73 nodes
7*2=6 -> none, 20.20s, 73 nodes
7*2=7 -> none, 0.80s, 1 node
```

The sublayer `7*7=3` closed by:

```text
7*3=0 -> none, 15.00s, 97 nodes
7*3=1 -> none, 16.44s, 73 nodes
7*3=2 -> none, 18.51s, 73 nodes
7*3=4 -> none, 17.72s, 73 nodes
7*3=6 -> none, 18.39s, 73 nodes
7*3=7 -> none, 1.25s, 1 node
```

The sublayer `7*7=4` closed by:

```text
7*4=0 -> none, 15.51s, 91 nodes
7*4=1 -> none, 17.71s, 67 nodes
7*4=2 -> none, 17.70s, 73 nodes
7*4=3 -> none, 17.34s, 73 nodes
7*4=6 -> none, 17.96s, 67 nodes
7*4=7 -> none, 0.86s, 1 node
```

Therefore:

```text
k=1, q=7
status: closed
```

Historical remaining point before the final q-layer:

```text
q=6*1 in {8}
```

Recommended next step:

```text
test q=8 using:
h=8*6
1*h=6
```

Stop raising direct timeouts for q-layers.  The direct `q=2` timeout was
resolved by the h-relay layer.

## Update 2026-05-26: q=8 started

For:

```text
6*6=1
q=6*1=8
```

direct run:

```text
6*1=8 -> timeout at 25s, 192 nodes
```

Using:

```text
h=8*6
1*h=6
```

closed directly:

```text
h=1 -> none, 22.02s, 171 nodes
h=2 -> none, 27.24s, 604 nodes
```

The first wide tail was:

```text
h=3
8*6=3
1*3=6
```

Direct check timed out:

```text
h=3 -> timeout at 35.26s, 1698 nodes
```

The active row was row `8`.  Splitting by:

```text
8*8 in {0,1,2,4,5,6,8}
```

gave:

```text
8*8=0 -> none, 15.80s, 70 nodes
8*8=6 -> none, 10.06s, 245 nodes
```

The non-self orbit tails closed by continuing the row-8 orbit:

```text
8*8=1:
  split by 8*7 in {2,4,5,6,8}
  all closed

8*8=2:
  split by 8*2 in {0,1,4,5,6,8}
  all closed

8*8=4:
  split by 8*4 in {0,1,2,5,6,8}
  all closed

8*8=5:
  split by 8*5 in {0,1,2,4,6,8}
  all closed
```

The self-tail:

```text
8*8=8
```

did not close by the first secondary row-8 split `8*7`; several values timed
out.  The useful structural switch was back to the original row-6 orbit:

```text
6*6=1
6*1=8
6*8=m
=> 8*(m*6)=1
```

Then:

```text
m=0 -> none, 10.29s, 1 node
m=4 -> none, 23.63s, 581 nodes
m=7 -> none, 25.92s, 642 nodes
```

The remaining `m=2,3` closed by the relay layer:

```text
m=2:
  k=2*6
  8*k=1
  k in {0,2,3,4,5,7}
  all closed

m=3:
  k=3*6
  8*k=1
  k in {0,2,3,4,5,7}
  all closed
```

Therefore:

```text
6*6=1
q=6*1=8
h=8*6=3
status: closed
```

Structural signal:

```text
If the active row-8 orbit is non-self, the next row-8 orbit edge closes it.
If row 8 hits a self-tail 8*8=8, control returns to the source row-6 orbit
through 6*8=m and 8*(m*6)=1.
```

Still open inside `q=8`:

```text
h=8*6 in {4,5,8}
```

For:

```text
h=4
8*6=4
1*4=6
```

direct check timed out:

```text
h=4 -> timeout at 30.11s, 1192 nodes
```

Diagnostics showed row `6` as the active compact row again.  The useful split
was:

```text
6*8=m
8*(m*6)=1
```

First layer:

```text
m=0 -> none, 14.13s, 34 nodes
m=4 -> none, 23.70s, 787 nodes
```

The wider values:

```text
m in {2,3,7}
```

closed by:

```text
k=m*6
8*k=1
k in {0,2,3,4,5,7,8}
```

Therefore:

```text
6*6=1
q=6*1=8
h=8*6=4
status: closed
```

Still open inside `q=8`:

```text
h=8*6 in {5,8}
```

For:

```text
h=5
8*6=5
1*5=6
```

direct check timed out:

```text
h=5 -> timeout at 30.97s, 576 nodes
```

Again row `6` was the useful compact row.  Splitting by:

```text
6*8=m
8*(m*6)=1
```

gave:

```text
m=0 -> none, 19.68s, 59 nodes
```

The wider values:

```text
m in {2,3,4,7}
```

all closed by:

```text
k=m*6
8*k=1
k in {0,2,3,4,5,7,8}
```

Therefore:

```text
6*6=1
q=6*1=8
h=8*6=5
status: closed
```

Still open inside `q=8`:

```text
h=8*6 in {8}
```

For:

```text
h=8
8*6=8
1*8=6
```

direct check timed out:

```text
h=8 -> timeout at 30.27s, 338 nodes
```

The same row-6 orbit split:

```text
6*8=m
8*(m*6)=1
```

closed:

```text
m=0 -> none, 18.09s, 13 nodes
m=2 -> none, 24.04s, 138 nodes
m=3 -> none, 24.76s, 122 nodes
m=4 -> none, 24.66s, 136 nodes
```

The remaining value:

```text
m=7
```

closed by:

```text
k=7*6
8*k=1
k in {2,3,4,5,7}
```

Therefore:

```text
6*6=1
q=6*1=8
h=8*6=8
status: closed
```

Final q=8 coverage:

```text
h=8*6 in {1,2,3,4,5,8}
all closed
```

Final layer result:

```text
case45
7*0=5
6*5=5
6*6=1
status: closed
```

Main structural mechanism:

```text
6*6=1
6*1=8
6*8=m
=> 8*(m*6)=1
```

This two-level return to the source row-6 orbit closed the difficult q=8
tails.

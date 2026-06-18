# Minimal Bad Short-Cycle Reduction

Date: 2026-06-08.

Status:

```text
general proved reduction / length-3 and length-4 base cases remain open
```

## Fixed-Point Criterion

For a finite E677 magma and a fixed element `x`, E255 at `x` is equivalent to:

```text
x*(y*y)=y
```

for the unique possible candidate:

```text
y=L_x^{-4}(x).
```

This gives a quick classification of very short own-row cycles.

## Length One

If:

```text
L_x(x)=x,
```

then:

```text
y=x
x*(x*x)=x.
```

So E255 holds at `x`.

## Length Two Is Impossible

If the own orbit of `x` had exact length two, then:

```text
L_x^{-4}(x)=x
L_x^2(x)=x.
```

Hence:

```text
x*(x*x)=x,
```

so the fixed-point criterion gives E255.

On the other hand, E677 with `y=x` gives:

```text
(x*x)*x=L_x^{-2}(x)=x.
```

Then the E255 left side is:

```text
((x*x)*x)*x=x*x!=x,
```

contradiction.

Therefore no element in a finite E677 magma has an exact own-row cycle of
length two.

## Length Four Is Bad

If the own orbit of `x` has exact length four, then:

```text
L_x^{-4}(x)=x,
```

but:

```text
x*(x*x)=L_x^2(x)!=x.
```

Thus E255 fails at `x`.

So every exact own-row four-cycle produces a bad element.

## Minimal Bad Element

Choose a bad element `0` whose own row cycle has minimal length `m`.

The previous cases show:

```text
m>=3.
```

The fan-spine four-cycle descent shows that a long-cycle role cannot close by
`e=C` when `m>4`, because that would create a bad element with cycle length
four.

Therefore the only short base cases not covered by strict minimal descent are:

```text
m=3
m=4.
```

## Base Case m=3

Write the row-`0` cycle:

```text
b_0=0
b_1
b_2=P.
```

Then:

```text
0*0=P.
```

Let:

```text
r_2=P*0.
```

The bad-cycle ladder at the wrapped index gives:

```text
0*r_2=b_1.
```

The unique input sent by row `0` to `b_1` is `P`, so:

```text
r_2=P.
```

Thus:

```text
P*0=P.
```

Define:

```text
C=P*P.
```

Then `C` cannot belong to the three-cycle:

```text
C!=P:
  row P already sends 0 to P;

C!=0:
  fixed-source zero descent would give 0*P=0*0,
  contradicting row-0 injectivity;

C!=b_1:
  then h=0*C=0 and P*h=0,
  but P*0=P.
```

Therefore:

```text
C outside {0,b_1,P}.
```

So every bad three-cycle forces the self-tip `P*P` to escape into another
row-`0` cycle.

This is the exact remaining length-3 base problem.

## Base Case m=4

Write:

```text
b_0=0
b_1
b_2=P
b_3=B.
```

Then:

```text
0*0=B.
```

Let:

```text
t=r_2=P*0.
```

The wrapped bad-cycle ladder gives:

```text
r_3=B*0=P.
```

The next ladder edge gives:

```text
B*t=0.
```

Thus row `B` contains the forced two-sided interval:

```text
t -> 0 -> P.
```

The bad condition gives:

```text
t!=0.
```

So the exact remaining length-4 base problem is already a double-interval
problem:

```text
P*0=t
B*t=0
B*0=P.
```

## Consequence For The Main Proof

After selecting a minimal bad element, the No-Free-Tail proof may be organized
as:

```text
m=3:
  prove that the forced external self-tip cannot close;

m=4:
  terminate the interval t -> 0 -> P in row B;

m>=5:
  use fan-spine minimal descent, where e=C is impossible.
```

This replaces an unspecified "small-cycle exception" with two exact base
configurations.


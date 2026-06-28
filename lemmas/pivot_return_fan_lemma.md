# Pivot Return Fan Lemma

Date: 2026-06-07.

Status:

```text
general proved construction / pressure amplification at r_2
```

Purpose:

```text
Propagate the cross-source predecessor fan one step forward in both source
cycles and return the resulting predecessor edges to the pivot row t.
```

## Setup

Let:

```text
t=r_2
a=b_2
b=b_3.
```

The two source-row cycles contain:

```text
row a:
  0 -> t -> alpha

row b:
  c -> t -> v
```

where:

```text
alpha=a*t=b_2*t
c=c_{-1}
v=b*t=b_4.
```

Define the next successors:

```text
alpha_2=a*alpha
v_2=b*v=b_3*b_4.
```

## First Predecessor Fan At t

The predecessor columns at `t` are:

```text
z=alpha*a=(b_2*t)*b_2
h=v*b=b_4*b_3.
```

The cross-source predecessor fan gives:

```text
t*z=0
t*h=c.
```

This is the original row-`t` pressure pair.

## Return Edges From The Successors

Apply the predecessor formula one step forward.

In row `a`, the predecessor of `alpha` is `t`, so:

```text
w=alpha_2*a=(b_2*alpha)*b_2
alpha*w=t.
```

In row `b`, the predecessor of `v=b_4` is `t`, so:

```text
p=v_2*b=(b_3*b_4)*b_3
v*p=t.
```

The second edge is the known offset relay:

```text
b_4*p=t.
```

## Lift Back Into Row t

Use the inverse edge chain:

```text
q*r=t
=> r=t*((q*t)*q).
```

From:

```text
alpha*w=t
```

we obtain:

```text
w=t*((alpha*t)*alpha).
```

From:

```text
v*p=t
```

we obtain:

```text
p=t*((v*t)*v).
```

Define:

```text
g_alpha=(alpha*t)*alpha
g_v=(v*t)*v.
```

Then row `t` has the four forced edges:

```text
t*z=0
t*h=c
t*g_alpha=w
t*g_v=p.
```

Explicitly:

```text
z=(b_2*t)*b_2
h=b_4*b_3
w=(b_2*(b_2*t))*b_2
p=(b_3*b_4)*b_3
g_alpha=((b_2*t)*t)*(b_2*t)
g_v=(b_4*t)*b_4.
```

## Collision Equivalences

Because row `t` is injective, every output coincidence is exactly a column
coincidence.  For example:

```text
w=p
<=>
g_alpha=g_v;

w=0
<=>
g_alpha=z;

w=c
<=>
g_alpha=h;

p=0
<=>
g_v=z;

p=c
<=>
g_v=h.
```

Thus a collision between either successor-return edge and the original
predecessor fan produces an explicit algebraic equality of columns in row
`t`.

If no collision occurs, row `t` has four distinct occupied outputs:

```text
0, c, w, p.
```

This is a genuine pressure amplification at the offset pivot.

## Strategic Meaning

The two source-row cycles cannot be studied independently.  Their first
forward steps return two new forced outputs to the common pivot row `t`.

The next target is:

```text
classify the five output-collision roles above and determine whether the
four-distinct-output branch can be extended once more without hitting the
bad-cycle ladder edge in row t.
```

This is a bounded symbolic layer, not a broad search.

# Right-Fixer To Balanced-Witness Lemma

Date: 2026-06-09.

Status:

```text
general proved
```

## Statement

Let a finite E677 magma be given. If:

```text
Y*b=b,
```

define successively:

```text
t=L_b^{-1}(Y),
z=L_b^{-1}(t).
```

Then:

```text
(b*z)*b=z.
```

Using the explicit inverse formula from Lemma 13.1(i), the witnesses may be
written without inverse notation:

```text
t=Y*((b*Y)*b),
z=t*b.
```

Thus every direct right fixer `Y` canonically gives a balanced witness `z`.

## Proof

By definition of `t`:

```text
b*t=Y.
```

Hence:

```text
(b*t)*b=Y*b=b.
```

Apply E677 in the form:

```text
x=y*(x*((y*x)*y))
```

with `x=t,y=b`. Since `(b*t)*b=b`, this gives:

```text
t=b*(t*b).
```

Now define `z` by:

```text
b*z=t.
```

Substitution into the previous equality gives:

```text
b*z=b*((b*z)*b).
```

Left multiplication by `b` is injective in every finite E677 magma.
Cancelling it yields:

```text
z=(b*z)*b.
```

Finally, Lemma 13.1(i) gives:

```text
t=L_b^{-1}(Y)=Y*((b*Y)*b).
```

Because `(b*t)*b=b`, applying the same inverse formula to `t` gives:

```text
z=L_b^{-1}(t)
 =t*((b*t)*b)
 =t*b.
```

## Consequence For The Current Frontier

For a directed path in `H_b`:

```text
p*a=b, p*b=v,
r*v=b, r*b=c,
u=p*v,
k=u*p,
v*k=b,
```

the model candidate is:

```text
Y=(b*c)*(u*k).
```

There is no need to synthesize `z` independently. It is enough to prove:

```text
((b*c)*(u*k))*b=b.
```

If this is established, the lemma above automatically supplies:

```text
t=Y*((b*Y)*b),
z=t*b,
(b*z)*b=z.
```

The unresolved mathematical step is therefore exactly the direct
right-fixer identity for `Y`, not term synthesis for `z`.

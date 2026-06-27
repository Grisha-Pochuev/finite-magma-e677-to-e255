# Period-3 Named Fan Reduces To `Ib*h=c`

Date: 2026-06-27.

Status:

```text
proved reduction / named middle-target fan needs only Ib*h=c
```

## Setup

Use the clean period-3 zipper residual:

```text
z*h=b,
b*h=c,
c*h=z.
```

The `H_h` zipper triangle contains:

```text
alpha -> b      carried by row z,
Ib    -> c      carried by row b,
Ic    -> z      carried by row c.
```

In particular:

```text
b*Ib=h,
b*h=c.
```

Target advance of the row-`b` zipper edge gives in `H_c`:

```text
row b: h -> b*c.
```

## Claim

Assume:

```text
Ib*h=c.
```

Then, unless the clean zipper has already routed by a local collision, `H_c`
has an outgoing fan at `h`:

```text
row b:  h -> b*c,
row Ib: h -> Ib*c,
b*c != Ib*c.
```

## Proof

The assumption:

```text
Ib*h=c
```

means that row `Ib` also gives an edge in `H_c` with input `h`:

```text
row Ib: h -> Ib*c.
```

If the two outputs were equal:

```text
Ib*c=b*c,
```

then rows `b` and `Ib` would realize the same full ported interval:

```text
(target,input,output)=(c,h,b*c).
```

By:

```text
ported_interval_state_lemma.md
```

the full ported interval reconstructs its source row.  Therefore:

```text
Ib=b.
```

But in the clean period-3 zipper this is already a routed local hit.  In
`H_h`, the edge:

```text
alpha -> b
```

would have output equal to the input of:

```text
Ib -> c,
```

giving an input-output path hit.  Thus the fully clean residual has:

```text
Ib!=b.
```

So, in the clean residual:

```text
Ib*c!=b*c.
```

Hence `Ib*h=c` alone creates the desired outgoing fan in `H_c` at the common
input `h`.

## Consequence

The named middle-target fan target is now only:

```text
Ib*h=c.
```

The stronger db identity:

```text
Ib*c=z
```

is useful evidence, but it is not needed to get the fan.  Once `Ib*h=c` is
proved, the output separation follows from full ported-interval
reconstruction and the clean condition.

The exact remaining negation is therefore:

```text
Ib*h!=c.
```

Equivalently, the db-supported named fan row `Ib` does not pass through the
middle target `c` at input `h`.

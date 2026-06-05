# Double-Fixed Self-Loop Lemma

Date: 2026-05-31.

Status:

```text
local closed / candidate role principle
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=6
```

## Structural Situation

This is the self-loop boundary left by the source-orbit zero-hit map.

Row `6` fixes two adjacent cycle elements:

```text
6*5=5
6*6=6
```

So the usual source-orbit route:

```text
6 -> k -> 0
```

does not start at `6*6`, because:

```text
6 -> 6
```

## Double-Fixed Exit

Use E677 with:

```text
x=5
y=6
```

E677 says:

```text
5 = 6 * (5 * ((6*5)*6))
```

Since:

```text
6*5=5
```

this becomes:

```text
5 = 6 * (5 * (5*6))
```

Because row `6` is a permutation and already sends `5` to `5`, the only
preimage of `5` under row `6` is `5`. Therefore:

```text
5*(5*6)=5
```

Let:

```text
u=5*6
```

Then the forced self-loop exit is:

```text
5*u=5
```

This is the correct replacement for the failed zero-hit route in the
`6*6=6` layer.

## Verification

Diagnostic under:

```text
case45
7*0=5
6*5=5
6*6=6
```

gave:

```text
u=5*6 in {1,2,3,7,8}
```

Targeted checks with:

```text
5*6=u
5*u=5
```

closed every value:

```text
u=1 -> closed
u=2 -> closed
u=3 -> closed
u=7 -> closed
u=8 -> closed
```

Therefore:

```text
case45
7*0=5
6*5=5
6*6=6
status: closed
```

## Relation To Source-Orbit Ladder

The source-orbit ladder covers layers where the row-6 source orbit reaches
`0`:

```text
6*6=k
6*k=0
```

and then row `0` gives a concrete predecessor condition.

The double-fixed layer is different:

```text
6*6=6
6*5=5
```

Here the useful exit comes from the fixed point `5` and the permutation
property of row `6`, not from an immediate zero-hit.

Working role split:

```text
source-orbit zero-hit:
  handles 6*6 in {2,3,4,8} representatives

double-fixed self-loop:
  handles 6*6=6
```

This gives a cleaner structural division for the special branch.

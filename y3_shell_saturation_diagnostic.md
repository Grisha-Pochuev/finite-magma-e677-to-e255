# Y3 Shell Saturation Diagnostic

Date: 2026-06-19.

Status:

```text
negative local diagnostic / no shallow named collapse
```

## Purpose

This records the first bounded diagnostic for:

```text
clean_external_bridge_eighth_stage_reduction_lemma.md
```

The diagnostic checks only the local Y3 shell equations:

```text
p*P=A,
p*A=S,
x*Beta=A,
x*A=b,
x*b=x1,
b*H=A,
b*A=D.
```

It closes these equations under E677 and left-row injectivity on a small
ground-term basis.

## Script

The reusable script is:

```text
tools/y3_shell_saturation.py
```

In the current Codex process, the normal Windows Python command resolves to
the WindowsApps placeholder and `py` is not visible.  Therefore the first run
was executed through the built-in Node REPL with the same bounded
ground-congruence logic.

## Result

For:

```text
depth=2, rounds=1
depth=3, rounds=1
```

the diagnostic closed in 4 iterations and produced:

```text
forced named equalities: none
```

among:

```text
A, p, x, b, P, Beta, H, S, D, x1.
```

After naming:

```text
U=p*S,
V=S*A,
```

the branch:

```text
U=V
```

was also checked at the same small bounded level.  It forced no further named
collapse beyond:

```text
U=V.
```

## Interpretation

The clean Y3/Z3 shell does not collapse by a very shallow local E677
congruence calculation.

So the next proof step should not expect an immediate equality such as:

```text
P=Beta, P=H, S=b, S=D, D=x1.
```

The useful next direction is structural:

```text
compare the left row-p cycle A -> S -> p*S -> ...
with the fixed-target source orbit p -> S -> S*A -> ...
and with the generated source orbit x -> b -> D -> ...
```

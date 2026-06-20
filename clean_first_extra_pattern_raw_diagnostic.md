# Clean First-Extra Pattern Raw Diagnostic

Date: 2026-06-20.

Status:

```text
diagnostic / targeted clean first-extra pattern check
```

## Purpose

This checks the local clean-disjoint branch left by:

```text
clean_first_extra_matching_bridge_alignment.md
m496_first_extra_intersection_roles_diagnostic.md
```

The diagnostic asks whether a small raw-label E677 model can realize the
simplest clean first-extra matching pattern.

## Pattern

Use labels:

```text
b=0,
z=1,
p=2,
q=3,
x_2=4,
y_2=5,
w=6,
S=7,
R=8.
```

Impose:

```text
2*0=1,
3*0=1,
2*1=4,
3*1=5,
2*4=6,
3*5=6,
2*6=7,
3*6=8.
```

This means rows `2` and `3` share:

```text
0 -> 1,
```

then meet again at:

```text
6,
```

but have different outputs after the first extra intersection:

```text
7 != 8.
```

So it is the clean-disjoint alternative to the M496 same-output pattern.

## Closure Diagnostic

Command shape:

```text
size 9, rawdiagnose, same requirements
```

Result:

```text
status: ok
row 2 domain: 94
row 3 domain: 94
forced cells: 8
domain checks: 2258160
```

Interpretation: short E677 propagation does not immediately contradict the
clean pattern.

## Raw Model Search

Command shape:

```text
size 9, 60 seconds, rawmodel, same requirements
```

Result:

```text
status: timeout
time: 67.77s
nodes: 249
dead ends: 241
forced rows: 0
forced cells: 1744
domain checks: 20018880
row-0 representative count: 362880
```

Interpretation: no model was found in the bounded run, but the search did not
complete.  This is weak evidence only.  It supports treating the clean
first-extra pattern as a serious residual rather than as a one-step local
contradiction.

## Tool Note

The search script now honors:

```text
globalThis.__searchCounterexampleArgv
```

inside the Codex JS runtime.  Ordinary command-line use is unchanged.

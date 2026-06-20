# Anchored Identity Negation Raw Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / targeted negation check for U*h=W*h
```

## Purpose

This checks the negation of the strong target from:

```text
shared_step_anchored_triangle_boundary.md
```

The strong target is:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q
=> U*h=W*h.
```

## Raw Pattern

Use labels:

```text
b=0,
z=1,
p=2,
q=3,
U=4,
W=5,
h=6,
T1=7,
T2=8.
```

Impose:

```text
2*0=1,
3*0=1,
2*1=4,
3*1=5,
4*2=6,
5*3=6,
1*6=0,
4*6=7,
5*6=8.
```

The last two cells force the negation:

```text
U*h != W*h
```

at the raw-label level.

## Closure Diagnostic

Command shape:

```text
tools/node-portable/node.exe tools/search_counterexample_strong.js 9 60 all rawdiagnose
```

with the requirements above.

Result:

```text
status: ok
row 1 domain: 21684, forcedCells=1, req=[6->0]
row 2 domain: 4032, forcedCells=2, req=[0->1, 1->4]
row 3 domain: 4032, forcedCells=2, req=[0->1, 1->5]
row 4 domain: 3121, forcedCells=2, req=[2->6, 6->7]
row 5 domain: 3121, forcedCells=2, req=[3->6, 6->8]
forced cells: 9
domain checks: 1349280
```

Interpretation: short E677 closure does not immediately contradict the
negation of the anchored identity.

## Raw Model Search

Command shape:

```text
tools/node-portable/node.exe tools/search_counterexample_strong.js 9 60 all rawmodel
```

with the same requirements.

Result:

```text
status: timeout
time: 60.43s
nodes: 576
dead ends: 566
forced rows: 0
forced cells: 4607
domain checks: 36389400
row-0 representative count: 362880
```

Interpretation: no size-9 arbitrary E677 model with the negated anchored
identity was found in the bounded run, but the search did not complete.

So this diagnostic supports the identity as a serious lemma target, but does
not prove it.

## Tool Note

This run used:

```text
tools/node-portable/node.exe
```

which is available in the project even when ordinary `node` is not on the
Codex process PATH.

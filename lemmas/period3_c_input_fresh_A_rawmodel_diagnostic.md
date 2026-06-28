# Period-3 c-Input Fresh A Rawmodel Diagnostic

Date: 2026-06-28.

Status:

```text
diagnostic / small raw-label search for fresh A=Ib*c
```

## Purpose

This checks whether the fresh-output side of:

```text
period3_c_input_v3_second_layer_boundary.md
```

is trivially realizable in very small arbitrary E677 models.

This is not a proof search for the whole theorem.  It only tests the partial
fresh `c`-input template:

```text
z*h=b,
b*h=c,
c*h=z,
b*Ib=h,
b*c=BC,
Ib*c=A,
```

with the labels:

```text
z=0,
h=1,
b=2,
c=3,
BC=4,
Ib=5,
A=6.
```

Thus `A` is forced distinct from the watched period-3 vertices and from `BC`.

## Runs

Size 7:

```text
tools\node-portable\node.exe tools\search_counterexample_strong.js 7 60 all rawmodel "0:1:2,2:1:3,3:1:0,2:5:1,2:3:4,5:3:6"
```

Result:

```text
status: none
time: 1.55s
nodes: 999
dead ends: 987
```

So there is no arbitrary size-7 E677 model realizing this weak fresh-A
template.

Size 8:

```text
tools\node-portable\node.exe tools\search_counterexample_strong.js 8 60 all rawmodel "0:1:2,2:1:3,3:1:0,2:5:1,2:3:4,5:3:6"
```

Result:

```text
status: timeout
time: 60.01s
nodes: 10256
dead ends: 10142
```

No model was found before timeout, but the size-8 case was not exhausted.

## Interpretation

The fresh branch:

```text
Ib*c=A fresh
```

is not immediately witnessed by the smallest raw-label arbitrary E677 search.
This supports continuing the structural route:

```text
prove Ib*c=z or another watched hit,
or reduce the fresh branch through the clean V3/fixed-target orbit machinery.
```

Do not treat this as evidence that the fresh branch is impossible in general.
The size-8 run timed out, and the template is only a partial version of the
full period-3 zipper residual.

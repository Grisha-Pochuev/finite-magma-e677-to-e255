# Period-3 Core Hook Diagnostic

Date: 2026-06-27.

Status:

```text
diagnostic / db evidence for a target-swap core hook in the period-3 residual
```

## Purpose

The shifted-window admissibility gap asks why the earlier bridge

```text
H_b: h -> z*b,
H_c: h -> b*c
```

should count as a smaller relay object.  A possible bridge-to-relay route is
that one of the target-advanced edges is not a fresh dangling edge, but lies in
the cycle core of its target graph.

For the period-3 triangle:

```text
z*h=b,
b*h=c,
c*h=z,
```

target advance gives:

```text
H_z: h -> c*z       carried by row c,
H_b: h -> z*b       carried by row z,
H_c: h -> b*c       carried by row b.
```

The diagnostic checks whether these three edges lie in the undirected 2-core
of their target graphs.

## Script

```text
tools/period3_core_hook_scan.js
```

It scans the cached public `eq677` db strict period-3 representatives and, for
each target graph `H_t`, repeatedly deletes degree `0` and `1` vertices to
compute the undirected 2-core.

It then records whether the three target-advanced period-3 hook rows lie in
the core:

```text
row z in H_b,
row b in H_c,
row c in H_z.
```

It also records the cyclomatic excess of the core component containing each
hook edge:

```text
excess = core_edges_in_component - core_vertices_in_component.
```

Excess `0` means a unicyclic core component.  Positive excess means the
component is already bicyclic or worse, hence it contains a fan/junction by
the existing graph lemmas.

## Run

```text
tools\node-portable\node.exe tools\period3_core_hook_scan.js
```

Result:

```text
totalStrictPeriod3: 6240
models: 77/65, 77/71, 77/72, 77/73

Hb(row z)=true; Hc(row b)=true; Hz(row c)=true: 6240

HbExcess(row z)=0;
HcExcess(row b)=9;
HzExcess(row c)=0: 6240

Hb hook component size: 10 edges / 10 vertices
Hc hook component size: 22 edges / 13 vertices
Hz hook component size: 20 edges / 20 vertices

HbTargetVertex=false; HbRightFixers=0;
HcTargetVertex=false; HcRightFixers=0;
HzTargetVertex=false; HzRightFixers=0: 6240

HcOutAtH=11; HcInAtBC=1: 6240

HbCoreEdges=77; HcCoreEdges=77; HzCoreEdges=77: 6240
misses: none
```

## Interpretation

The simple old-target hook:

```text
H_b: h -> z*b
```

is always a core edge in the public strict period-3 examples.  However its
core component has excess `0`, with size `10/10`, so this alone does not
force an old-target fan or a bicyclic relay component.  The `H_z` hook is
similar: it lies in an excess-`0` component of size `20/20`.

The middle shifted-window hook:

```text
H_c: h -> b*c
```

is stronger in the public examples.  It always lies in a core component with
size `22/13`, hence excess `9`.  This component contains neither the target
vertex `c` nor a right-fixer edge for `c` in the scan.  Thus in the db
models, the shifted-window bridge is attached to a genuine bicyclic core after
target swap to:

```text
c=b*h.
```

The endpoint profile is sharper still:

```text
HcOutAtH=11,
HcInAtBC=1.
```

So in every public strict period-3 example the middle hook is not merely in a
distant bicyclic component.  It is itself one edge of an outgoing fan at the
input `h` in `H_c`.  The edge carried by row `b` is unique for its output
`b*c`, but there are ten other rows `r` with:

```text
r*h=c.
```

Thus the db-supported candidate can be sharpened from "middle target core
hook" to:

```text
middle-target outgoing-fan-at-h.
```

This suggests that the next proof route should not rely only on:

```text
old target b contains the hook edge.
```

The sharper candidate is:

```text
Period-3 middle-target core-hook lemma:
in the clean period-3 residual, the edge H_c: h -> b*c is forced into a
bicyclic core component of H_c, or else the residual routes by a right fixer,
full ported interval collision, or old/core attachment.
```

## Boundary

This diagnostic is not a proof.  It uses public models only.  It does show
that the local shifted-window obstruction has a plausible global relay hook
not visible to bounded equality closure:

```text
the middle target c, not the old target b, may be the correct target for the
next relay step.
```

The next useful theoretical check is whether badness or no-right-fixer for
`b` transfers enough pressure to `c=b*h` to force the `H_c` component
containing row `b` to be bicyclic.  The public models suggest this is not a
right-fixer shortcut for `c`; it is genuine core pressure.

After the endpoint scan, an even sharper target is:

```text
Period-3 middle-target fan lemma:
in the clean period-3 residual, there is a row r!=b with r*h=c.
```

If additionally `r*c!=b*c`, then `H_c` has an outgoing fan at `h`.  In the db
examples `HcInAtBC=1`, so this output collision exception never occurs.

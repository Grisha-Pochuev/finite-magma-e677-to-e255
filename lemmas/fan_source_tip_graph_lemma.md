# Fan Source-Tip Graph Lemma

Date: 2026-06-08.

Status:

```text
general proved
```

## Setup

Use the self-containing common-edge fiber:

```text
F={q : q*0=P},
```

with:

```text
P in F.
```

For each source define:

```text
T_q=q*P.
```

The common-edge fan gives:

```text
T_q*q=h
```

for one common hub `h`, and the map:

```text
q -> T_q
```

is injective.

Draw a directed edge:

```text
q -> T_q
```

only when `T_q` also belongs to `F`.

## Basic Graph Restrictions

Every vertex has outdegree at most one and indegree at most one.

Also:

```text
T_q!=P
```

for every source `q`, because:

```text
q*0=P
q*P=T_q
```

and row `q` is injective.

Thus `P` has indegree zero in the internal source-tip graph.

Since the tip map is an injection from the finite set `F` and omits `P`, at
least one tip lies outside `F`.

## No Distinct Two-Cycle

Assume distinct sources `q,r` form:

```text
T_q=r
T_r=q.
```

The two fan returns are:

```text
r*q=h
q*r=h.
```

Apply the tip-source collision zero-tooth lemma to:

```text
T_q=r.
```

Since:

```text
q*r=h,
```

it gives:

```text
h*q=0.
```

Apply it to:

```text
T_r=q.
```

Since:

```text
r*q=h,
```

it gives:

```text
h*r=0.
```

Row `h` is injective, so:

```text
q=r,
```

contrary to the assumption.

Therefore distinct internal source tips cannot form a directed two-cycle.

## Self-Loop Form

If:

```text
T_q=q,
```

then:

```text
q*P=q
q*q=h.
```

The tip-source collision lemma gives:

```text
h*q=0.
```

Thus an internal self-loop is not harmless; it creates the explicit zero
tooth:

```text
q*q=h
h*q=0.
```

## Three-Source Corollary

In the `u=b_3` role, the source fiber contains:

```text
P,B,A.
```

Their three tips are distinct and none equals `P`.

Consequently:

```text
at least one of the three tips is outside {P,B,A};
B and A cannot exchange tips B -> A -> B.
```

The only entirely internal components allowed on `{B,A}` are self-loops.
Every such self-loop creates a zero tooth through the common hub `h`.

## Significance

The internal part of a common-edge fan is a partial permutation graph, but it
is not arbitrary:

```text
P has no incoming edge;
an external tip is unavoidable;
distinct two-cycles are impossible;
self-loops create zero teeth.
```

Thus the fan cannot close merely by pairing its source rows.

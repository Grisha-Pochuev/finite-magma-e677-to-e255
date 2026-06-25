# eq677 db Shared-Step Scan Diagnostic

Date: 2026-06-26.

Status:

```text
diagnostic / strong shared-step hypothesis downgraded
```

## Purpose

This follows the useful external-repository idea recorded in:

```text
eq677_repo_idea_notes.md
```

The check reuses the public `memoryleak47/eq677` `db/` models as known finite
E677/E255 examples.  It tests the current shared-step anchored triangle:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b.
```

The strong candidate was:

```text
U*h=W*h.
```

## Script

```text
tools/eq677_db_shared_step_scan.js
```

The script does not clone the external repository.  With `--refresh` it
downloads selected `db` model files into:

```text
cache/eq677-db/
```

The cache is local/generated and is ignored by git.

## Command Run

First smoke check:

```text
tools\node-portable\node.exe tools\eq677_db_shared_step_scan.js --refresh --sizes=5,7,9,11,13,16,19,21
```

Result: 19 small models, no shared-step pairs.  These models are therefore not
informative for the current hypothesis.

Full db check:

```text
tools\node-portable\node.exe tools\eq677_db_shared_step_scan.js --refresh --all --summary-only
tools\node-portable\node.exe tools\eq677_db_shared_step_scan.js --all --summary-only
tools\node-portable\node.exe tools\eq677_db_shared_step_scan.js --all --totals-only
```

The first full run downloaded the small public db cache.  The second full run
used the local cache.  The final command is the compact reproducible summary.

## Full db Result

The scanner covered:

```text
models:                 440
idempotent models:      182
non-idempotent models:  258
shared-step groups:     9657
shared-step pairs:      942388
```

Universal structural checks:

```text
h=U*p=W*q failures: 0
z*h=b failures:     0
```

Strong target check:

```text
U*h=W*h true pairs:      924040
U*h=W*h false pairs:      18348
```

The false pairs split as:

```text
all named terms distinct: 17040
with named collision:      1308
```

Anchored-X3 triple classification in `H_h`:

```text
clean triples p,q,alpha -> T,S,b: 17040
routed visible triples:             1308
```

Here:

```text
alpha = pred_z(h),
T=U*h,
S=W*h,
T!=S.
```

The clean-triple test requires distinct inputs `p,q,alpha`, distinct outputs
`T,S,b`, and no input-output cross hit.

Top collision profiles among false pairs:

```text
all-distinct:     17040
p=z:                504
q=z:                504
S=q;T=W=b:          150
S=U=b;T=p:          150
```

Top anchored-X3 triple profiles among false pairs:

```text
triple-clean:                                           17040
cross:alpha=T:                                            504
cross:alpha=S:                                            504
cross:alpha=S;cross:alpha=b;cross:p=T;output:S=b:         150
cross:alpha=T;cross:alpha=b;cross:q=S;output:T=b:         150
```

The known failing model families/sizes include:

```text
25/24: 300 false pairs, all with visible named collisions
49/18, 49/19, 49/27, 49/28: 882 false pairs each
77/65, 77/71, 77/72, 77/73: 3630 false pairs each
```

In the size-49 and size-77 failures, many false pairs are fully distinct in
the named set:

```text
b,z,p,q,U,W,h,T=U*h,S=W*h.
```

They are also clean as anchored-X3 triples.  Example shape from `77/65`:

```text
b=6, z=9, p=0, q=1,
U=64, W=52, h=8, alpha=5,
T=74, S=70,
triple=clean.
```

## Interpretation

The strong sentence:

```text
shared-step anchored triangle => U*h=W*h
```

is false as a general E677/E255 model identity.

This does not by itself refute the current proof route, because the live
research branch is not an arbitrary shared-step pair in an arbitrary model.
It is a minimal bad-target / clean-residual situation.  The diagnostic says
that any valid proof of `U*h=W*h` must use extra hypotheses such as:

```text
bad target b,
minimal G12 loop,
clean anchored-X3 residual,
watched/core avoidance,
or admissibility of the resulting V3 bridge.
```

Therefore the correct next step is not to promote `U*h=W*h` to a global lemma.
The false branch:

```text
T=U*h,
S=W*h,
T!=S
```

must remain active and should be routed through the anchored-X3/V3 machinery.

The diagnostic strengthens this point: in the external db, most false pairs
already are clean anchored-X3 triples at the visible `H_h` level.  So the
needed extra proof ingredient cannot be merely "the X3 triple is clean"; it
must use the stronger current assumptions:

```text
bad target,
minimality,
first-event/source-orbit rank,
or V3 admissibility.
```

## Next Use

Use the new db scanner for two narrower follow-up checks:

```text
1. classify false U*h!=W*h examples by V3 target-lift roles;
2. test whether the all-distinct db failures still survive the additional
   watched/core/minimal-clean exclusions that define the current G12 residual.
```

If the all-distinct db failures are eliminated by those extra exclusions, then
the strong hypothesis can be restated as a clean-minimal lemma.  If not, the
anchored-X3 route is the correct general branch.

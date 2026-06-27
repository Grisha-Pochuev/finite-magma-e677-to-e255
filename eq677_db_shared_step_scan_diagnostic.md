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

The clean-X3 triples were then expanded by the second triangle layer from:

```text
anchored_x3_second_triangle_pressure_lemma.md
```

For a clean false pair:

```text
T=U*h,
S=W*h,
T!=S,
```

the second layer in `H_h` is:

```text
row T: betaT=(U*T)*U -> T*h
row S: betaS=(W*S)*W -> S*h
row b: betaB=(z*b)*z -> b*h
```

Formula check:

```text
T*betaT=h,
S*betaS=h,
b*betaB=h
```

had zero failures in the db scan.

Second-layer endpoint classification:

```text
second layer routes by visible endpoint hit:  5928
second layer remains fully clean:           11112
```

The clean-X3 triples were also scanned as fixed-target source-successor
orbits in `H_h`, following:

```text
anchored_x3_source_orbit_boundary.md
anchored_m7_first_event_routing_lemma.md
```

The three source orbits are:

```text
U -> T -> T*h -> ...
W -> S -> S*h -> ...
z -> b -> b*h -> ...
```

The scanner stops at the first event among:

```text
cross-source hit,
output merge,
input repeat,
input-output hit,
same-orbit source repeat.
```

First-event result on the 17040 clean-X3 triples:

```text
routed first source-orbit event: 10800
clean same-orbit self-repeat:    6240
no finite event found:              0
```

First-event depth split:

```text
clean-self-repeat@3: 6240
routed@2:            5592
routed@1:            3528
routed@3:            1680
```

Clean self-repeat return signatures:

```text
z:3->0:          4320
W:3->0|z:3->0:  1050
U:3->0|z:3->0:   870
```

So every clean db self-repeat returns the `z` source orbit to its initial
source at depth 3:

```text
z -> b -> b*h -> z.
```

Target-advanced period-3 triangle profile:

```text
period3-advance-clean: 6240
```

Top first-event profiles:

```text
clean-self-repeat@3:self-source-repeat:z:                         4320
routed@2:input-output:z.input=z.output|input-repeat:W=U:           1512
routed@1:input-output:W.input=U.output|input-output:W.output=U.input: 1200
routed@1:input-output:z.input=z.output|input-output:z.output=z.input: 1200
routed@2:input-output:z.output=W.input:                           1143
routed@2:input-output:z.input=W.output:                           1098
clean-self-repeat@3:self-source-repeat:W|self-source-repeat:z:     1050
routed@3:cross-source:W=U|self-source-repeat:z:                    909
clean-self-repeat@3:self-source-repeat:U|self-source-repeat:z:      870
```

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

Top second-layer profiles among the clean anchored-X3 triples:

```text
second-layer-clean:                                      11112
cross:betaS=Sh:                                          1314
cross:betaS=Th;cross:betaT=Sh:                           1200
cross:betaT=Th:                                          1086
cross:alpha=bh;cross:betaB=b:                             960
cross:betaS=Th:                                           504
cross:betaT=Sh:                                           504
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

The second-layer scan sharpens this further.  The local two-layer pressure is
real and often routes, but it is not a universal local closure: many db
examples remain clean after both layers.  Therefore a proof should not try to
close anchored-X3 by endpoint comparison alone.  It should use the already
developed source-successor orbit route:

```text
anchored_x3_source_orbit_boundary.md
anchored_x3_rank_measure_candidate.md
anchored_m7_first_event_routing_lemma.md
```

or reduce the resulting clean cycle to V3 admissibility.

The first-source-orbit scan supports the current theoretical reduction even
more directly.  On the external db, every clean-X3 example reaches a finite
first event.  Most route by the already named first-event cases; the remaining
examples are exactly clean same-orbit self-repeats, which is the M7 residual
already developed in:

```text
anchored_x3_clean_self_repeat_normal_form.md
anchored_m7_cycle_zipper_lemma.md
anchored_m7_v3_necklace_measure_extension.md
```

Thus the db evidence no longer supports searching for a new local X3 closure.
It supports continuing the existing route:

```text
clean-X3
-> source-orbit first event
-> clean M7 self-repeat
-> zipper
-> clean V3 necklace
-> unified V3 admissibility.
```

The depth split adds one more useful boundary: all clean self-repeat residuals
in the public db occur first at depth 3.  So the external examples point toward
the short period-3 zipper window as the immediate obstruction shape, not toward
arbitrary long source cycles.

The signature split sharpens this again: every clean db self-repeat includes
the period-3 anchored `z`-orbit.  This is recorded as a working boundary in:

```text
fixed_target_period3_zipper_boundary.md
```

The target-advanced version of this period-3 triangle is also clean in all
`6240` db instances.  Thus the remaining object is not an endpoint collision
waiting to be named; it is a genuinely clean three-target same-input triangle:

```text
H_z: h -> (b*h)*z,
H_b: h -> z*b,
H_{b*h}: h -> b*(b*h).
```

The follow-up structural clarification is:

```text
period3_zipper_triangle_self_renewal_lemma.md
```

For this period-3 object, the X3-style triangle-pressure layer is the same
`H_h` zipper triangle shifted cyclically.  Therefore the db-supported residual
should not be attacked by merely adding another local pressure layer; that
does not create new independent structure.

## Next Use

Use the new db scanner for two narrower follow-up checks:

```text
1. classify the M7 clean-self-repeat examples by zipper/V3-necklace roles;
2. classify the second-layer-clean false examples by V3 target-lift roles;
3. test whether the all-distinct db failures still survive the additional
   watched/core/minimal-clean exclusions that define the current G12 residual.
```

If the all-distinct db failures are eliminated by those extra exclusions, then
the strong hypothesis can be restated as a clean-minimal lemma.  If not, the
anchored-X3 route is the correct general branch.

# V3 Admissibility Gap Audit

Date: 2026-06-27.

Status:

```text
boundary audit / local shifted-window closures exhausted, global admissibility remains
```

## Purpose

This file records the current exact shape of the remaining G12 obstacle after
the shared-step anchored triangle route:

```text
shared-step anchored false branch
-> anchored-X3
-> clean M7 self-repeat
-> fixed-target zipper
-> same-input V3 bridge necklace
```

The aim is to avoid repeating local equality and fingerprint checks that do not
address the real remaining issue.

## What Is Proved

The local M7 first-event analysis routes all first events except a clean
same-orbit right-`h` self-repeat:

```text
anchored_m7_first_event_routing_lemma.md
```

The clean self-repeat gives a target-independent fixed-target zipper:

```text
r_i*t=r_{i+1},
I_i=t*(r_{i+1}*r_i)=(r_{i-1}*r_i)*r_{i-1}.
```

This is recorded in:

```text
fixed_target_zipper_bridge_necklace_lemma.md
```

Target advance turns the zipper into a same-input V3 bridge necklace:

```text
H_{r_i}:     t -> A_i,
H_{r_{i+1}}: t -> A_{i+1},
A_i=r_{i-1}*r_i.
```

Every adjacent bridge is born before the terminal return:

```text
r_n=r_0.
```

So if such an adjacent V3 bridge is admissible as a measured relay object, it
is smaller than the terminal self-repeat.

Important caution:

```text
MZ<n is a chronological descent inside the current active source-orbit
timeline, not automatically a shorter autonomous source cycle.
```

If the same cycle is restarted at another row, its period may remain the same.
Therefore the proof cannot rely only on the abstract cycle length.  It must
show that the shifted window is already an active unresolved relay/ported
object born before the terminal event in the same minimal G12 loop, or else
explain why it creates one.

## What Is Only Conditional

The reduction currently depends on this admissibility sentence:

```text
A zipper-born clean adjacent V3 bridge is admissible under the same global
minimality measure as first-extra V3 bridges.
```

This sentence is not yet proved.  It is stronger than the first-extra V3
boundary because zipper-born bridges are not fresh four-edge V3 matchings.
Their second layer overlaps the existing zipper:

```text
zipper_born_v3_second_layer_shift_lemma.md
```

So the exact clean object is a shifted zipper window, not a generic V3 square.

## Period-3 Test Case

In the short period-3 residual:

```text
z*h=b,
b*h=c,
c*h=z.
```

The earlier bridge is explicit:

```text
H_b: h -> z*b,
H_c: h -> b*c.
```

Its target-lift in `H_h` is:

```text
alpha -> b,
Ib    -> c.
```

The terminal return is:

```text
c*h=z.
```

Thus this is the smallest concrete test of the global admissibility sentence:

```text
the shifted-window bridge H_b,H_c is born before the terminal return.
```

If it is admissible, the period-3 residual closes immediately by descent.

## Local Checks Now Exhausted

The diagnostic:

```text
tools/anchored_period3_saturation.js
anchored_period3_fingerprint_saturation_diagnostic.md
```

checks the anchored period-3 local theory with:

```text
E677,
left cancellation,
edge predecessor formula,
fixed-target source-successor formula,
anchored-X3 false branch,
period-3 zipper formulas.
```

Base closure does not derive:

```text
p*c=T,
q*c=S,
U*z=Ib,
W*z=Ib,
U*z=W*z,
E255(z), E255(b), E255(c), E255(h).
```

Even after assuming the db fingerprints:

```text
p*c=T,
q*c=S,
U*z=W*z=Ib,
```

the local closure still does not derive:

```text
T=S,
E255(z), E255(b), E255(c), E255(h),
or a clean endpoint collapse.
```

The sharper shifted-window and full period-3 triangle hit tests are also
negative.  They do not derive:

```text
ZB=BC,
ZB=CZ,
BC=CZ,
h=ZB,
h=BC,
h=CZ,
alpha=Ib,
alpha=Ic,
Ib=Ic,
alpha=c,
Ib=b,
other lift/source or lift cross hits,
ZB,BC,CZ hitting z,b,c.
```

So neither the shifted bridge `H_b,H_c` nor the full triangle `H_z,H_b,H_c`
closes by the ordinary local fan/path/core-hit roles in this bounded closure.

## Current Exact Gap

The current obstacle is not:

```text
a missing one-step equality,
an untested size-77 fingerprint,
or a generic clean four-edge V3 matching.
```

It is:

```text
a fully clean fixed-target zipper/V3 necklace whose adjacent shifted-window
V3 bridges are born earlier than the terminal return, but have not yet been
proved admissible under the global relay measure.
```

The period-3 case is now the sharpest visible form of this gap:

```text
a clean self-renewing three-target same-input triangle coupled to its own
H_h zipper triangle.
```

Reapplying the old X3 triangle-pressure step just shifts the same zipper
triangle; it does not create a new independent local layer.

## Next Useful Lemma

The next proof attempt should target the following precise statement:

```text
Shifted-window admissibility lemma:
in a minimal G12 relay loop, a clean adjacent V3 bridge born inside a
fixed-target zipper before the terminal self-repeat is either locally routed
or is a smaller admissible relay object.
```

The proof must explain one of these mechanisms:

```text
1. the shifted window attaches to old/core data;
2. the shifted window repeats a full ported interval in an independent role;
3. the shifted window regenerates a standard first-extra V3 object;
4. the whole zipper necklace forms a strict clean theta already excluded;
5. the global measure must be extended to accept shifted-window V3 bridges.
```

In particular, a valid proof must not merely say:

```text
the adjacent bridge occurs at i<n, hence it is smaller.
```

It must justify why this earlier occurrence belongs to the class of objects
being minimized.

Do not spend the next run on more isolated product equalities around
`p*c`, `q*c`, `U*z`, `W*z`, `h*h`, or db fingerprints unless a new structural
reason appears.

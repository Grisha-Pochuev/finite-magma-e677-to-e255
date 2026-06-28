# Anchored d-Term Strong-Branch Raw Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / d-term hint does not close from visible anchored data alone
```

## Purpose

This checks whether the M496 d-term pattern from:

```text
m496_anchored_d_term_scan_diagnostic.md
```

is forced by the visible strong anchored triangle alone.

The strong anchored branch is:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
U*h=W*h=T.
```

Use raw labels:

```text
b=0,
z=1,
p=2,
q=3,
U=4,
W=5,
h=6,
T=7.
```

## Raw Closure: `h*h != h`

Add:

```text
h*h=8
```

so `h*h!=h` at the raw-label level.

Command:

```text
tools/node-portable/node.exe tools/search_counterexample_strong.js 9 20 all rawclosure "2:0:1,3:0:1,2:1:4,3:1:5,4:2:6,5:3:6,1:6:0,4:6:7,5:6:7,6:6:8"
```

Result:

```text
status: ok
forced cells: 10
domain checks: 1062000
```

Interpretation: the visible strong anchored triangle does not immediately
force `h*h=h` by the raw closure rules.

## Raw Closure: `d(h) != h`

Add:

```text
h*h=8,
(h*h)*h=9.
```

so `d(h)!=h`.

Command:

```text
tools/node-portable/node.exe tools/search_counterexample_strong.js 10 20 all rawclosure "2:0:1,3:0:1,2:1:4,3:1:5,4:2:6,5:3:6,1:6:0,4:6:7,5:6:7,6:6:8,8:6:9"
```

Result:

```text
status: ok
forced cells: 11
domain checks: 10956960
```

Interpretation: the visible strong anchored triangle also does not immediately
force `d(h)=h`.

## Raw Closure: `z*d(h) != b`

The direct size-11 raw closure for:

```text
h*h=8,
(h*h)*h=9,
z*d(h)=10
```

was too expensive for this tool shape and ended with Node heap exhaustion.

Do not repeat the same size-11 raw closure without a narrower encoding.

## Raw Model Search: `h*h != h`

A 60-second raw model search was run for the size-9 `h*h!=h` pattern above.

Command:

```text
tools/node-portable/node.exe tools/search_counterexample_strong.js 9 60 all rawmodel "2:0:1,3:0:1,2:1:4,3:1:5,4:2:6,5:3:6,1:6:0,4:6:7,5:6:7,6:6:8"
```

Result:

```text
status: timeout
time: 61.03s
nodes: 1429
dead ends: 1413
forced rows: 0
forced cells: 10266
domain checks: 55768182
row-0 representative count: 362880
```

Interpretation: no size-9 model was found in 60 seconds, but the search did
not complete.  This supports caution, not a lemma.

## Correction To The M496 Hint

M496 is fully idempotent:

```text
x*x=x for all 496 elements.
```

Therefore in M496:

```text
d(x)=((x*x)*x)=x
```

for every element.  The observed relations:

```text
d(h)=h,
h*h=h,
d(z)=z,
z*z=z,
z*d(h)=b,
d(z)*h=b
```

are consequences of global idempotence plus the already known `z*h=b`.

So they are not currently a strong anchored-specific proof target.  They are
still useful as a warning: d-term scans on idempotent models can produce
misleadingly strong-looking patterns.

## Current Conclusion

The d-term route should be deprioritized unless a non-idempotent db model
shows the same pattern.

The active proof target should return to:

```text
anchored_m7_first_event_routing_lemma.md
anchored_x3_clean_self_repeat_normal_form.md
```

and use the cycle-end template for the clean same-orbit right-`h`
self-repeat.

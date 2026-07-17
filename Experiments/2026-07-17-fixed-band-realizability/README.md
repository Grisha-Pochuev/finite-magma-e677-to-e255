# Complete fixed-band realizability — 2026-07-17

## Mathematical purpose

The previous broad targets `ZB*A=Ib`, `(ZB*Ib)*ZB=c`, `b*(ZB*A)=h`, and direct `A=z` all timed out and are not repeated.

The new evidence is structural: an exact scan of 201,500 strict period-three anchors and 240 closed fibers found zero complete synchronized all-gamma-fixed eta bands. This run tests the complete band object rather than an isolated fixed page.

## Five targets

1. Complete eta cycle of length 2 is inconsistent.
2. Complete eta cycle of length 3 is inconsistent.
3. On the complete length-2 band, `P_0*(Ib*c)=V_0`.
4. On the complete length-3 band, `P_0*(Ib*c)=V_0`.
5. The same bridge from two adjacent synchronized positions, without closing the eta cycle.

The bridge and `P_0*z=V_0`, by left cancellation, imply `Ib*c=z`.

## Matrix and safety

Each target uses four previously validated profiles. The completed pilot used 1,800 seconds per job and the validated 12 GiB process-tree guard.


## Completed 30-minute pilot

Run: https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255/actions/runs/29538663524

The validation gate and all 20 matrix jobs completed. All five targets timed out in all four profiles; no proof, model, memory guard, OOM, or technical failure occurred. Peak tree RSS was 7915.8 MiB and the lowest MemAvailable was 7057.4 MiB.

The pilot is a negative search boundary: do not promote this unchanged matrix to 5h50. The next mathematical step must extract a global cyclic invariant or materially guide the encoding.

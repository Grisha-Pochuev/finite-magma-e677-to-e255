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

Each target uses four previously validated profiles:

- E auto schedule, 4 workers at 2500 MB;
- Vampire CASC, 4 workers at 2500 MB;
- Vampire CASC, 2 workers at 5000 MB;
- Vampire satisfiability intent, 4 workers at 2500 MB.

Full mode is 20 independent jobs, each with 21,000 seconds of useful search and a 360-minute job limit. The whole process tree is softly stopped after three consecutive samples at 12 GiB RSS or below 2.5 GiB MemAvailable.

The workflow has separate `smoke` and `full` dispatch modes. Full mode is allowed only after the smoke artifacts and logs have been reviewed.

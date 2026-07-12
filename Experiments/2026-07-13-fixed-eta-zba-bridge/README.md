# Fixed eta ZBA bridge run — 2026-07-13

## Purpose

This run tests the newest uncommitted 12 July fixed-eta frontier from the local research package.
The strict period-3 fixed eta-return base is:

```text
z*h=b, b*h=c, c*h=z,
b*Ib=h, c*Ic=h,
A=Ib*c, K=A*Ib, ZB=z*b,
r*b=z, r*z=U, U*r=h, U*Ib=r,
U*c=ZB, ZB*c=K.
```

The current shortest closing bridge is:

```text
ZB*A=Ib  =>  A=z.
```

The narrower structural subtarget is:

```text
(ZB*Ib)*ZB=c.
```

By E677 on row `ZB`, input `Ib`, that subtarget makes the predecessor term equal `A=Ib*c` and yields `ZB*A=Ib`.

## Problems

- `01-zba-bridge.p`: prove `ZB*A=Ib` from the fixed-eta relay package.
- `02-zbib-zb-c.p`: prove the smaller internal identity `(ZB*Ib)*ZB=c`.
- `03-b-zba-h.p`: prove the softer row-`b` form `b*(ZB*A)=h`.
- `04-direct-az.p`: control target, prove `A=z` from the same package.
- `05-zba-bad-target.p`: prove `ZB*A=Ib` with the additional bad-target condition `forall x, x*b != b`.

## Matrix

Each of the five problems is tested by four profiles, for 20 independent runners:

1. E prover, four-process auto schedule, 2500 MB per worker.
2. Vampire CASC, four workers, 2500 MB per worker.
3. Vampire CASC, two workers, 5000 MB per worker.
4. Vampire CASC with satisfiability intent, four workers, 2500 MB per worker.

The useful search limit in every matrix job is exactly 350 minutes (5 h 50 min). The GitHub job limit is 360 minutes, leaving up to ten minutes for setup and artifact upload.

## Safety

- The whole process tree is sampled every two seconds.
- The run is softly stopped if tree RSS remains above 12 GiB or available memory remains below 2.5 GiB for three samples.
- Solver logs, machine details, resource samples, exact commands and a result classification are uploaded even after a timeout or guarded stop.
- Expected time limits are recorded as a completed technical run, not disguised as a proof failure.
- Crashes, invalid arguments and malformed input remain red failures.

## Launch

The exact workflow is archived as `workflow-used.yml` and copied to:

```text
.github/workflows/fixed-eta-zba-bridge-2026-07-13.yml
```

The initial merge commit is the explicitly authorized launch event. Later ordinary edits do not relaunch it because the launch job also checks the exact commit message.

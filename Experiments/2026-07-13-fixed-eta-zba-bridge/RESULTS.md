# Results

Status: corrected retry launched; long-run results pending.

Initial launch commit:

```text
a130e97addde2060ea1596f757f180c0d20cdc92
```

The first attempt ended during the technical launch path. The GitHub connector did not expose the job logs directly, so the exact failing line could not be quoted. Inspection of the committed workflow found a concrete defect: the smoke test accepted only exit codes `0`, `1`, and `124`, although E prover and Vampire may use other ordinary nonzero codes when a short bounded search ends without a proof. Those normal endings could therefore be reported as red technical failures.

Corrected retry commit:

```text
9fd857118fbf6a7aafc73da53c3092b01a17c6d4
```

Correction PR:

```text
https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255/pull/9
```

Workflow page:

```text
https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255/actions/workflows/fixed-eta-zba-bridge-2026-07-13.yml
```

The corrected workflow now:

- validates all five TPTP inputs;
- runs short end-to-end checks through the same memory monitor and wrapper used by the long jobs;
- treats `Timeout`, `GaveUp`, `ResourceOut`, solver memory limits, and other ordinary bounded-search endings as technical completion rather than crashes;
- still fails on malformed input, invalid options, missing executables, fatal errors, segmentation faults, assertion failures, and signal-style exit codes;
- creates the result directory before the long search and preserves available output even after early failures.

The retry uses 20 independent jobs with a 350-minute (5 h 50 min) search limit per job. A timeout or lack of a proof is not a mathematical refutation. Final conclusions must be written here only after all artifacts and technical statuses have been checked.

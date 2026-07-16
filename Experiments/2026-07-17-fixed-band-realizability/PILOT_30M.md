# 30-minute pilot

This pilot was explicitly requested before any 5h50 full run.

- 5 structural targets × 4 validated profiles = 20 jobs.
- useful search time: 1,800 seconds per job.
- job timeout: 40 minutes.
- process-tree guard: 12 GiB RSS / 2.5 GiB MemAvailable, inherited from the validated wrapper.
- validate first parses all five inputs and exercises all four profiles through the real wrapper.
- final collect expects exactly 20 per-job summaries.

The pilot is launched once by the main-branch marker `.github/fixed-band-pilot-30m.launch`.

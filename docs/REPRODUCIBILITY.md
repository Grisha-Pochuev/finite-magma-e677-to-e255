# Reproducibility guide

This repository aims to make the mathematical work inspectable and the bounded
computational claims reproducible.

## Requirements

For the included scripts:

- Windows PowerShell, for `verify_size8_closed.ps1`;
- Node.js, for the JavaScript search tools in `tools/`.

No large solver toolchain is required for the included size-8 verification
script.

## Reproduce the size-8 closure

First, run the short smoke test:

```powershell
.\verify_smoke.ps1
```

If Windows blocks direct PowerShell script execution, use either:

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\verify_smoke.ps1
```

or double-click:

```text
verify_smoke.cmd
```

Expected runtime: usually under one minute on a normal laptop.

This checks:

```text
Node.js is available
the search script starts
one size-5 case closes
one size-8 base case closes
one size-8 split case closes
```

Then run the full size-8 verification:

From the repository root, run:

```powershell
.\verify_size8_closed.ps1
```

If direct script execution is blocked, use:

```powershell
powershell.exe -ExecutionPolicy Bypass -File .\verify_size8_closed.ps1
```

or double-click:

```text
verify_size8_closed.cmd
```

Expected behavior:

- the script checks all size-8 split cases used by the project;
- each subcase should end with `status: none`;
- the script writes a new timestamped log such as
  `logs/size8_rerun_20260605_203000.txt`;
- if a subcase does not close, the script stops and tells the user to send the
  log for inspection.

The recorded output from the previous successful run is kept at:

```text
logs/size8_verified_split_log.txt
```

The recorded log is not overwritten by reruns.

## Expected full runtime

The recorded successful size-8 run took about 7 minutes on the original
machine.  Runtime can vary by hardware and Node.js version.  The script has a
90-second per-subcase limit and checks 65 subcases, so the theoretical worst
case is much longer than the typical recorded run.

If the full run takes unexpectedly long, stop it and report the last printed
case label and the partial rerun log in `logs/`.

## Direct diagnostic command shape

The search tool can also be called directly.  For example:

```powershell
node .\tools\search_counterexample_strong.js 8 90 0 counterexample
```

Arguments:

```text
8              finite magma size
90             time limit in seconds
0              split index
counterexample search mode
```

Some later calls add an extra forced cell, such as:

```powershell
node .\tools\search_counterexample_strong.js 8 90 23 counterexample 4:0:1
```

meaning: in that split, also force row `4`, column `0`, value `1`.

## What counts as evidence here

The repository uses three evidence levels:

1. mathematical lemma files in `lemmas/`;
2. bounded computational scripts in `tools/`;
3. recorded logs in `logs/`.

The long-term goal is to move important lemmas from informal Markdown into a
formal proof assistant such as Lean.  That work has not yet replaced the
current notes and scripts.

## Preparation-environment note

During preparation of this public folder, Node.js was visible in the local
Codex desktop environment, but executing `node.exe` from the sandbox returned
`Access is denied`.  The size-8 command is therefore documented from the
existing project script and recorded successful log.

If a reviewer sees `Access is denied` while running inside Codex or another
sandbox, rerun the scripts in a normal terminal with a regular Node.js
installation.

An independent smoke test was run through the Node REPL environment on
2026-06-05:

```text
size 5, row-0 case 1: status none
size 8, row-0 case 1: status none
size 8, split case 24 with extra 4:0:1: status none
```

The full PowerShell script should still be rerun on a normal local clone before
claiming a fresh reproduction.

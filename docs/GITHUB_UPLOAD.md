# GitHub Upload Guide

This guide is for manually uploading the prepared public package to GitHub.

## Repository

Target repository:

```text
https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255
```

## What to upload

Upload the contents of the prepared public package folder:

```text
github_publish/finite-magma-e677-to-e255
```

Do not upload the outer `github_publish` folder itself.

The GitHub repository root should contain:

```text
README.md
CHANGELOG.md
LICENSE
docs/
lemmas/
tools/
logs/
formal/
verify_smoke.ps1
verify_smoke.cmd
verify_size8_closed.ps1
verify_size8_closed.cmd
```

## Suggested repository description

```text
Open reproducible research on the finite-magma implication E677 -> E255.
```

The broader umbrella name is:

```text
The Open Mathematics Project
```

## Important files

Make sure these files are present after upload:

```text
README.md
CHANGELOG.md
docs/CLOSED_CASES.md
docs/RESEARCH_UPDATE_2026-06-08.md
docs/REPRODUCIBILITY.md
docs/OPENAI_OSS_APPLICATION_NOTE.md
logs/size8_verified_split_log.txt
verify_smoke.ps1
verify_smoke.cmd
verify_size8_closed.ps1
verify_size8_closed.cmd
tools/search_counterexample_strong.js
formal/lean/README.md
```

Without these files, the repository will look like a set of private notes
rather than a reproducible public research project.

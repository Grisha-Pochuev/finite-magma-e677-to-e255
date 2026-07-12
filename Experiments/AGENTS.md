# Rules for the Experiments archive

This subtree stores historical GitHub Actions experiments and the web-chat handoff file.

## Web-only memory

`START_HERE_WEB.md` is written for ChatGPT in the web chat. It is not the mathematical source of truth for Codex and must not replace the project's normal frontier, status, or next-action files.

Codex should not read or update `START_HERE_WEB.md` during normal mathematical work unless the user explicitly asks it to work on web-chat continuity or experiment archiving.

## Historical runs

- Treat files inside dated run folders as historical records.
- Do not silently correct a historical script in place. Preserve the exact used version and record corrections in `RESULTS.md` or in a new dated run folder.
- Do not launch a workflow merely because files were reorganized or documented.
- A new full run requires explicit user approval.
- Before a new full run, perform a short end-to-end smoke test and verify logs, exit-code handling, memory monitoring, and artifact upload.

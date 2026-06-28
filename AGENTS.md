# Project Rule: E677 -> E255 Finite Magmas

This project is for working on the open problem:

`E677` for finite magmas:

`x = y * (x * ((y * x) * y))`

and whether it implies:

`E255`:

`x = ((x * x) * x) * x`

## Working Agreement

The assistant should use AI reasoning first. The preferred first moves are:

- derive algebraic consequences of `E677`;
- look for equivalent formulations of `E255`;
- search for structural obstructions to finite counterexamples;
- design smaller, smarter search spaces instead of brute force;
- translate promising ideas into checkable lemmas, scripts, or solver inputs;
- explain all steps in non-technical Russian, because the user is not a programmer.

The assistant should not ask the user to run computation just because computation is possible. It should ask only when CPU/solver work is genuinely the efficient next step.

## When To Stop And Ask For Local Computation

Stop reasoning and ask the user to run a local computation when one of these is true:

- a finite candidate search has been reduced to a small bounded case;
- a SAT/SMT/model-finder check can quickly reject or confirm a proposed structure;
- a script can verify a table, lemma, or counterexample candidate;
- continuing by pure reasoning would likely be slower or less reliable than a targeted solver run.

Do not ask the user to run long blind brute force. The user's laptop has an AMD Ryzen 3 3250U, so searches should be modest, resumable, and have clear stop conditions.

After the first size-8 run on 2026-05-12, strengthen this rule:

- Do not ask the user for another long run merely to "see what happens".
- Do not send a run expected to take more than 5 minutes unless there is a specific mathematical hypothesis being tested.
- A useful run must have a clear possible interpretation before it starts, such as "this will prove these exact cases impossible", "this will distinguish two structural hypotheses", or "this will produce a small object we can inspect".
- If a run only profiles performance or exposes where search gets stuck, the assistant should run it locally in short bursts, not delegate it to the user.
- The next serious user-side computation should happen only after the search space has been split by a new lemma, invariant, or independently meaningful case distinction.

## User-Friendly Computation Protocol

When asking the user to compute something locally, provide:

1. A plain-language goal: what the computation is checking.
2. A single simple action if possible, such as opening one file or running one command.
3. An expected runtime range for this laptop.
4. A clear stop rule, for example: "stop if it runs longer than 20 minutes".
5. The exact result to send back, preferably one small text block or generated file.
6. A reassurance that failure/no result is still useful information.

Prefer creating helper scripts with simple names such as:

- `run_small_search.ps1`
- `check_candidate.ps1`
- `verify_table.ps1`

The scripts should avoid requiring technical knowledge. They should print progress, explain what they are doing, and end with a short human-readable result.

## Computation Limits For This Project

Default local limits unless the user approves more:

- target runs under 5 minutes first;
- stretch runs may go up to 20 minutes;
- avoid all-core heavy computation unless necessary;
- avoid installing large toolchains unless there is a clear benefit;
- prefer Python or simple standalone executables over complex setups;
- keep intermediate files in this project folder.

Additional rule as of 2026-05-22:

- There is a difference between asking the user to run a computation and the
  assistant running a targeted local diagnostic itself.
- User-side computations should remain short and rare.
- Assistant-run diagnostics may use somewhat larger limits when they test a
  precise mathematical hypothesis, such as a fixed `(s,u,q)` node or a proposed
  lemma layer.
- A normal assistant-run diagnostic may run for 1-3 minutes.
- A harder assistant-run diagnostic may run for 5-10 minutes only when:
  - the branch is already sharply bounded;
  - the result has a clear interpretation;
  - it is not a blind brute-force search;
  - it uses one focused process rather than all-core heavy computation.
- If a targeted run times out twice without giving new structure, record that
  in `research_log.md` and switch to a different structural idea instead of
  only raising the timeout again.
- Do not ask the user to run those longer checks manually unless there is a
  strong reason and a simple stop rule.

## Long-Run Mode For This Chat

As of 2026-06-18, the user approved long research runs in this chat:

- do not stop after the first solved subtask or first local lemma;
- continue until a large mathematical milestone, a real blocker, or a clearly
  needed bounded computation is reached;
- assistant-run targeted local CPU checks may run up to 10 minutes when the
  hypothesis is precise, the run is not blind brute force, and the result has
  a clear interpretation;
- keep interim summaries and status rewrites sparse, so they do not consume the
  session budget;
- edit project files when it helps preserve reusable lemmas, scripts, or the
  next continuation point.

User wording to preserve the intended mode:

```text
Делай один длинный заход: не останавливайся после первой леммы, продолжай до
крупного рубежа. Можно делать целевые локальные проверки до 10 минут и
сохранять промежуточные леммы в файлы.
```

Infrastructure note: Git for Windows is installed at
`C:\Program Files\Git\cmd\git.exe`.  If plain `git` is not visible in the
current Codex process PATH, use the project wrapper `tools/git.cmd`.

## Current Research Stop Rule

As of 2026-05-14, the next phase is not to continue mechanical case-by-case
search. The assistant should keep working until one of these stopping points is
reached:

- a genuine general lemma is found that explains the repeated pattern
  `3*0 -> 2*0 -> 2*2 -> 2*3` around a bad 4-cycle;
- the remaining exploratory cases are finished and the assistant can clearly
  summarize what the exploration says about the depth of the problem;
- a precise, bounded computation is needed to confirm or reject a specific
  mathematical hypothesis.

The assistant should stop and summarize at that point. The desired output is a
plain Russian explanation of what was learned, whether the pattern became a
lemma, and what the next mathematically meaningful step is.

Until then, do not ask for another long run and do not merely continue to
record "case closed" results without extracting a structural reason.

## Loop Detection Rule

If the work becomes repetitive, such as closing several similar cases, hitting
similar timeouts, retrying the same split, or repeatedly rewriting the same
lemma, the assistant must pause briefly and check whether any new structural
information was gained.

If no new structure was gained, do not stop the research merely because the
pattern became repetitive. First record the repetition/blockage in
`research_log.md`, then switch strategy: reformulate the hypothesis, look for a
higher-level reason, test a different structural split, or derive a new lemma.
Only stop after the blockage and the attempted change of strategy have both
been saved clearly enough for a later chat to continue.

Keep this checkpoint short unless a longer summary is genuinely useful.

## Agent Workflow Rule

As of 2026-05-22, future work should follow `AGENT_WORKFLOW.md`.

The main process is:

- read `NEXT_ACTION.md` first, then `CURRENT_FRONTIER.md` only if more
  context is needed;
- do not read `CONTINUE_HERE.md`, `research_log.md`, `PROJECT_STATUS.md`, or
  old checkpoints at startup unless a specific past derivation needs auditing;
- work on one current frontier only;
- formulate one structural question before computing;
- run only 1-3 targeted checks at a time;
- immediately translate each computational result into a structural statement;
- after 3-5 similar closures, stop and decide whether a real lemma is emerging;
- if no new structure appears, record the blockage and change the split instead
  of continuing case-by-case.

The assistant should treat computation as support for lemma discovery, not as a
default way to make progress.

Status-writing rule: do not append routine progress to `research_log.md`.
Record only new proved lemmas, important boundary corrections, or meaningful
negative diagnostics.  Prefer updating `NEXT_ACTION.md`, `CURRENT_FRONTIER.md`,
or the exact lemma/boundary file that owns the result.

## Token And Agent Budget Rule

As of 2026-05-24, future work should use a token-saving role split:

- the main assistant is responsible for strategy, mathematical ideas, choosing
  the current frontier, deciding what is worth computing, and interpreting the
  result;
- subagents, when available, should be used only for narrow execution tasks:
  file checks, short diagnostics, bounded `(s,u,q)` verifications, or extracting
  compact facts from existing logs;
- do not ask a subagent to "look for the lemma", "think broadly", or continue
  open-ended research;
- subagent outputs should be compact, ideally 5-10 lines, and the main assistant
  must integrate or reject the result in `research_log.md` or the relevant lemma
  file;
- if the tool allows choosing model/reasoning level, reserve the highest level
  for the main strategic reasoning and use cheaper sufficient settings for
  narrow subagent checks.
- Update 2026-06-03: when the main assistant is running at `high` rather than
  `very high`, subagents should default to `gpt-5.5` with medium reasoning.
  In this mode the main assistant must shrink delegated tasks to medium-sized
  scopes: file/status extraction, checking a fixed derivation, verifying a
  short list of already specified nodes, or summarizing consequences from
  existing logs. Do not use high-reasoning subagents by default in a high-run.
- Update 2026-06-04: this is the current default mode unless the user explicitly
  says the main run is `very high`. The main assistant should assume it is
  running on `high`, keep strategic and lemma decisions in the main thread, and
  delegate only tasks that fit `gpt-5.5 medium`: narrow status audits, fixed
  derivation checks, compact domain/timeout tables, and 1-3 specified node
  checks. If a task would require a subagent to invent the next direction,
  judge whether a lemma is true, or explore broadly, it is too hard for the
  default subagent split and must be kept by the main assistant or rewritten as
  a smaller checklist first.
- for this mathematics project, use `gpt-5.5` subagents for anything that can
  affect mathematical status: whether a branch is closed, whether coverage is
  complete, whether a candidate lemma has enough representatives, or whether a
  relay argument is valid;
- use `gpt-5.5` medium for mathematical status/coverage audits;
- use `gpt-5.5` high only exceptionally for a very narrow mathematical check
  that is too subtle for medium and would otherwise block the main reasoning;
  record why high was needed before relying on it;
- use `gpt-5.5` low for non-mathematical mechanical tasks such as finding files,
  extracting exact log lines, listing domains/timeouts, checking file
  existence, or formatting a draft table. It must not decide "closed", "lemma",
  or "covered" by itself;
- do not use `gpt-5.4-mini` by default in this research project. Prefer keeping
  all subagents on `gpt-5.5` and saving cost through reasoning level (`low`,
  `medium`, `high`) rather than switching to a weaker model family;
- do not use very-high-level subagents by default. Reserve very high reasoning
  for the main assistant's strategy and key lemma decisions, unless the user
  explicitly asks otherwise or a short critical verification truly needs it.
- routine "dirty work" should be delegated by default when possible: repeated
  q-node checks, log/status extraction, domain tables, timeout lists, and
  checking several representatives under an already defined protocol;
- the main assistant should do dirty work directly only when it is one or two
  short steps, no subagent is available, or delegation overhead would exceed
  the work itself.

The goal is to spend the strongest reasoning on mathematical decisions, not on
routine enumeration or long status narration.

## Repository Hygiene And Commit Rule

As of 2026-06-29, repository structure must be protected before every commit
or publication step.

Allowed root files are only:

```text
README.md
AGENTS.md
CONTRIBUTING.md
LICENSE
CITATION.cff
.gitignore
.rgignore
verify_*.ps1
verify_*.cmd
```

All working research notes belong in `lemmas/`.  Status and navigation files
belong in `docs/`.  Historical checkpoints belong in `archive/`.  Logs belong
in `logs/`.  Scripts belong in `tools/`.  Do not leave new lemma, boundary,
candidate, diagnostic, frontier, period, orbit, bridge, fan, zipper, relay, or
row markdown files in the repository root.

`README.md` is a public front page, not a working scratchpad.  Do not rewrite
it from scratch.  Preserve the background, Equational Theories Project
references, Terence Tao quote, acknowledgements, and repository explanation.
Only update README in the narrow current-progress/status area or to fix links
after file moves.  If a README edit is needed, inspect the diff before commit
and reject accidental rewrites of the public introduction/background.

Before every commit, run a repository hygiene check:

```text
git status --short
git diff --stat
list root files
```

If unexpected root-level markdown files appear, move them first with `git mv`
when tracked.  If `README.md` is modified, inspect the README diff separately
and confirm that only the intended current-progress/link lines changed.

Commit protocol:

- keep cleanup commits separate from mathematical research commits;
- use one clear branch per publication task;
- fetch `origin` before comparing or publishing;
- never force push;
- if local history diverges from `origin/main`, create a safe branch from
  `origin/main` and publish through a pull request;
- before pushing, run `git diff --check` or `git diff --cached --check`;
- after pushing, report the branch, commit SHA, and PR link if one was created.

## Communication Style

Speak to the user in Russian by default.

Use friendly, non-technical explanations. Avoid assuming the user knows algebra software, SAT solvers, command lines, Git, or programming.

When mathematical notation is needed, introduce it gently and tie it back to the original problem.

The assistant should act like a research partner: think hard first, compute only when the computation has a purpose, and make every local task easy to run.

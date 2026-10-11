# Act 3 Opportunity Discovery — Environment Report

Date: 2026-10-09
Method: every claim below was verified by direct tool execution or by reading the installed
documentation. Nothing in this report is assumed. Assumptions, where unavoidable, are labeled.

## 1. Verified Open Research capabilities

OpenResearch is installed as the `orx` CLI, version 0.2.14, at `/home/codespace/.local/bin/orx`.
Source repository: `/workspaces/TEMPORARY/OpenResearch/` (openresearch-cli, Rust). The CLI's
bundled skill modules were read directly (`OpenResearch/agent-skills/orx-*/SKILL.md`) and key
capabilities were exercised end-to-end.

Verified by execution:

- `orx --version` → `orx 0.2.14`.
- `orx --help` → full command surface (projects, project, agent, runs, logs,
  create-experiment, compute, instance, exp, skill, skills, install-skills, discover,
  paper, version, update, delete, serve, supervise, up, telemetry, feedback).
- `orx discover keyword "clinician documentation burden" --limit 3` → returned structured JSON
  from alphaXiv with title, abstract, publicationDate, votes, and match snippets. Works with no
  login. `~/.config/openresearch/` contains settings and locks but NO credentials.json —
  confirming the documented split: literature retrieval is login-free, compute/account features
  require `orx login`.

Verified from the installed documentation (README.md, SKILL.md, agent-skills modules):

- **Discovery primitives** (all login-free, one public endpoint call each, structured JSON out):
  - `orx discover keyword "<query>"` — alphaXiv full-text with match snippets.
  - `orx discover embedding "<query>"` — alphaXiv semantic retrieval with reranking.
  - `orx discover openalex "<query>"` — cross-disciplinary OpenAlex scholarly graph.
  - `orx discover biorxiv "<query>"` — bioRxiv preprints via OpenAlex's bioRxiv index.
  - Date/ranking controls: `--published-after`, `--published-before`, `--prioritize
    default|recency|historical|popular`, `--limit`.
- **Paper reading**: `orx paper <id|url> [--full]` — alphaXiv report with full-text fallback, or
  OpenAlex/bioRxiv metadata+abstract. Source auto-detected.
- **Local experiment projects**: `orx up` (dashboard on 127.0.0.1:4791), `orx projects`,
  `orx project view`, `orx create-experiment`, `orx exp run/status/cancel/wait`, `orx logs`.
  Verified existing projects in the local store: t2v-t4-model-research, openedit-design-eval,
  typography-glow-research (leftovers from earlier work in this workspace).
- **Agent delegation**: `orx agent spawn "<task>" [--title ...] [--stdin] [--no-wake]` — spawns
  an independent helper session in the same project with its own worktree and transcript. Rules
  (from `orx-agent-delegation`): never delegate the literature retrieval loop; write standalone
  briefs; state which `orx exp run` calls are authorized.
- **Artifacts**: `orx-reports` module — durable outputs go in the project's artifacts directory;
  written files become project artifacts immediately.
- **Lit-review discipline** (from `orx-lit-review`): the retrieval loop is never delegated; the
  main agent ranks combined candidates; claim-level support only after reading a paper with
  `orx paper`; empty retrieval is not proof of absence; cap of ~2 loops per turn.

Not verified / not available:

- `orx login` has never been run (no credentials.json) → OpenResearch **managed compute** and
  instance provisioning are unavailable this session. Not needed: all research primitives are
  login-free.
- `orx serve` / `orx up` dashboards not started (not needed for this task).

## 2. Verified Hermes Agent capabilities

Verified from the live runtime environment:

- **Orchestration**: `delegate_task` — spawns subagents in isolated contexts (own conversation,
  terminal session, toolset), up to 10 in parallel; results return as child self-reports;
  `action=list/steer/stop` controls running children. Independent investigations batch into one
  call and run in parallel.
- **Execution**: `terminal` (persistent shell), `execute_code` (persistent Python kernel with
  Hermes tool helpers: web_search, web_extract, read_file, write_file, search_files, patch).
- **Persistence**: `memory` (cross-session facts), `skill_manage` (procedural skills), plus
  plain files in the workspace.
- **Retrieval**: `web_search`, `web_extract` (clean markdown, no LLM summarization), and a full
  browser stack (navigate, click, snapshot, console/JS evaluation, vision).
- **Task tracking**: `todo_list` (deferred, loadable via tool_search).

## 3. How information flows between Open Research and Hermes

- Open Research (`orx discover` / `orx paper`) is the **retrieval mechanism**: it executes the
  actual literature/source searches and returns structured JSON with URLs, abstracts, and
  snippets. Per `orx-lit-review`, the retrieval loop runs in the main session (never delegated
  to sub-agents).
- Hermes is the **orchestration, synthesis, and challenge layer**: it designs the research
  campaign, runs `orx discover`/`orx paper` calls, delegates independent investigations (domain
  context, red-team, competitive intelligence) to `delegate_task` sub-agents where the work is
  reasoning-heavy, consolidates all outputs into the persistent problem database, and produces
  the final ranked report.
- Handoff artifact: files under `/workspaces/TEMPORARY/act3-opportunity/` — sub-agents receive
  self-contained briefs pointing at these files and return structured findings that Hermes
  validates and merges.

## 4. Artifact storage structure

```
/workspaces/TEMPORARY/act3-opportunity/
  ENVIRONMENT-REPORT.md      (this file)
  research/                  (one structured report per research direction)
  problem-db/                (persistent problem intelligence database)
  opportunities/             (deep-dives and solution candidates)
  validation/                (red-team and judge assessments)
  FINAL-REPORT.md            (ranked shortlist + primary recommendation)
```

## 5. Missing capabilities and constraints

- No `orx` login → no OpenResearch managed compute (irrelevant to this research task).
- No Open Research "web search" primitive beyond scholarly corpora: `orx discover` covers
  alphaXiv/OpenAlex/bioRxiv. General web evidence (forums, reviews, issue trackers) uses Hermes
  `web_search`/`web_extract`/browser. This division follows the installed tool boundaries.
- Sub-agents cannot call `delegate_task`/`clarify`/`memory`; they return self-report summaries
  which are treated as claims to verify, not facts.
- Browser session has no residential proxies; bot-walled sources may fail (fallback:
  web_extract, or mark as unverifiable).

## 6. Exact execution procedure supported by the installed environment

1. Hermes establishes event constraints from authoritative sources (official event pages via
   web_extract/browser).
2. Hermes designs the research campaign (distinct directions, one structured brief each).
3. Retrieval loop runs in the main session via `orx discover` (alphaXiv/OpenAlex/bioRxiv) and
   Hermes `web_search`/`web_extract` for non-scholarly web evidence.
4. Reasoning-heavy independent investigations (domain deep-dives, red-team, competitive
   intelligence) run via `delegate_task` in parallel, each with a self-contained brief and a
   required output schema.
5. Hermes consolidates every structured report into `problem-db/` (SQLite-backed markdown
   inventory), merging duplicates while retaining sources.
6. Targeted follow-up research resolves material uncertainties (validated by re-reading sources).
7. Red team runs as independent sub-agents (problem investigator, competitive intelligence,
   technical, skeptical judge, user advocate, evidence auditor) — each submits its assessment
   before seeing the others.
8. Hermes scores survivors against the actual judging rubric and produces `FINAL-REPORT.md`.

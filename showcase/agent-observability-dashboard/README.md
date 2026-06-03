# Showcase: Agent Observability Dashboard

**The flagship real-world artifact built with Grok Build 0.1 + the skills and MCP patterns in this arsenal.**

A full-featured, self-hosted dashboard + CLI + Python library for deep analysis of AI coding agent sessions across Grok Build, Claude Code, Cursor, LangChain, CrewAI, and generic formats.

**Production package:** [`agent-failure-analyzer`](https://github.com/cobusgreyling/agent-failure-analyzer) on PyPI (`pip install agent-failure-analyzer`)

**Built entirely with Grok Build 0.1 (Plan Mode + subagents + custom MCPs + strict discipline).**

**Author:** Cobus Greyling

## The Prompt That Started It

"Build a production-grade, beautiful agent session analyzer and visualizer. It should ingest sessions from multiple vendors (Grok Build, Claude Code, Cursor, generic), classify failures using a living taxonomy, produce heatmaps, fingerprints, cost reports, and have both a web UI and strong CLI. Use Plan Mode. Create any MCPs or skills you need."

## How It Was Built (Transparency — The Arsenal Method in Action)
- Started strictly in Plan Mode using the `plan-mode-orchestrator` skill (see `skills/plan-mode-orchestrator/`).
- Used `subagent-arena` to explore three different storage + visualization strategies in parallel.
- Designed and implemented the `agent-session-analyzer` MCP (see `mcps/agent-session-analyzer/` and the minimal but functional `server.py`).
- Heavy use of `tdd-intelligence` — characterization tests written first for parsers (see full test suite in the package).
- Architecture decisions documented and reviewed with `architecture-reviewer`.
- Security surface (especially around untrusted session logs) reviewed with `security-audit`.
- UI validation performed with the `browser-qa` MCP pattern.
- Final git hygiene via `git-discipline` skill.
- Continuous validation with the `skill-validator` and the CI in this repo + the package repo.

**Result:** A complete, shipped, installable system (ingestion for 6+ formats, living failure taxonomy with 30+ subcategories, web dashboard, rich CLI/TUI, cost attribution, OTLP/Grafana export, GitHub Action, Docker) with clean history, high test coverage, benchmarks, and real user-facing docs.

## Where the Real Code Lives
The full implementation, sample logs, dashboard, parsers, exporters, and production polish live in the dedicated package repo (the arsenal keeps the *method* reusable and the MCP + build story):

- **GitHub:** https://github.com/cobusgreyling/agent-failure-analyzer
- **PyPI:** https://pypi.org/project/agent-failure-analyzer/
- **Quick install + demo:** `pip install agent-failure-analyzer && afa analyze --help`

The `mcps/agent-session-analyzer/` in this repo is the driving MCP definition + skeleton server that the agent used while building the real thing.

## Running / Exploring the Showcase
```bash
# The actual production tool (recommended)
pip install agent-failure-analyzer

# Analyze included samples (or your own logs)
afa analyze ./sample_logs/ --cost

# Launch the web dashboard
afa dashboard ./sample_logs/ --port 8080

# Or use the MCP directly inside a Grok Build session for agent-driven analysis
```

See the package README for the full CLI surface (tui, explain, check as CI gate, trend, notifications, LLM-assisted classification, etc.).

## What This Proves About grok-build-0.1 + Arsenal Discipline
- Excellent at long-horizon, multi-component, production-shipped projects when given Plan Mode + narrowly-scoped skills.
- Strong at meta-tooling (building high-quality tools *for* agents, while using agents).
- MCP design, taxonomy design, and packaging come naturally with the right harness.
- The combination produces artifacts you would actually depend on (PyPI package, GitHub Action, Docker, Grafana dashboards, PR comment workflows).

This is the concrete proof that the skills and patterns in `skills/` and `mcps/` are not theory — they ship real things.

**All original work by Cobus Greyling. Created and refined using Grok Build 0.1 in this exact disciplined style.**

# Showcase: Agent Observability Dashboard

**A full-featured, self-hosted dashboard + CLI for deep analysis of AI coding agent sessions.**

**Built entirely with Grok Build 0.1 (Plan Mode + subagents + custom MCPs).**

**Author:** Cobus Greyling

## The Prompt That Started It

"Build a production-grade, beautiful agent session analyzer and visualizer. It should ingest sessions from multiple vendors (Grok Build, Claude Code, Cursor, generic), classify failures using a living taxonomy, produce heatmaps, fingerprints, cost reports, and have both a web UI and strong CLI. Use Plan Mode. Create any MCPs or skills you need."

## How It Was Built (Transparency)

- Started strictly in Plan Mode using the `plan-mode-orchestrator` skill.
- Used `subagent-arena` to explore three different storage + visualization strategies in parallel.
- Designed and implemented the `agent-session-analyzer` MCP (see `mcps/agent-session-analyzer/`).
- Heavy use of `tdd-intelligence` — characterization tests were written first for parsers.
- Architecture decisions documented and reviewed with `architecture-reviewer`.
- Security surface (especially around untrusted session logs) reviewed with `security-audit`.
- UI validation performed with the `browser-qa` MCP (once it was ready).
- Final git hygiene via `git-discipline` skill.

**Result:** A complete, running system (ingestion, classification, web dashboard with Grafana panels, exporters, replay) with clean history and high test coverage on the core.

## Key Files

- `dashboard/app.py` — FastAPI + nice UI
- `agent_failure_analyzer/` — the core Python package (parsers, classifiers, exporters, TUI)
- `sample_logs/` — real-ish anonymized session examples from multiple frameworks
- `mcps/agent-session-analyzer/` — the MCP that powers agent-driven analysis

## Running the Showcase

```bash
cd showcase/agent-observability-dashboard
# (full setup instructions would go here — see the actual package README for now)
python -m agent_failure_analyzer.cli --help
```

## What This Proves About grok-build-0.1

- Excellent at long-horizon, multi-component projects when given Plan Mode + skills.
- Strong at meta-tooling (building tools for agents while being an agent).
- MCP design and integration comes naturally.
- With good skills and subagent patterns, it produces clean, reviewable, production-quality output.

This showcase is both a useful tool and a demonstration of the model's real capability.

**All original work by Cobus Greyling.**

# agent-session-analyzer MCP

**A powerful MCP server for ingesting, analyzing, and visualizing AI agent sessions (Grok Build, Claude Code, Cursor, custom harnesses).**

Part of the Grok Build Arsenal by Cobus Greyling.

## Why It Exists

Agent sessions are rich but hard to reason about at scale. This MCP gives agents (and humans) first-class tools to:

- Parse session logs and transcripts
- Classify failures using a living taxonomy
- Attribute cost and token usage
- Fingerprint similar failure modes across runs
- Generate heatmaps, reports, and replay artifacts
- Export to OTLP / Grafana / Markdown

## Capabilities (Tools)

- `ingest_session` — Load a session file or directory (supports multiple formats)
- `classify_failures` — Run the failure taxonomy classifier
- `generate_fingerprint` — Create a stable signature for a failure cluster
- `build_heatmap` — Produce time + category heatmaps
- `correlate_sessions` — Find related failures across many sessions
- `export_report` — Markdown, JSON, HTML, or OTLP
- `replay_session` — Step through key events with context

## Security Model

- Read-only by default on session files you explicitly point it at.
- No execution of code from sessions unless you enable a sandboxed replay mode.
- Never sends session content off-device unless you explicitly use an export target.

## Quick Setup (Python example)

```bash
cd mcps/agent-session-analyzer
python -m venv .venv
source .venv/bin/activate
pip install mcp pydantic "fastmcp>=0.1"
python server.py
```

Then configure in your `.grok/config.toml` or via Grok Build UI:

```toml
[mcp.agent-session-analyzer]
command = "python"
args = ["/absolute/path/to/mcps/agent-session-analyzer/server.py"]
```

## Driving Skill

See `skills/` in the root (or the mcp-orchestrator + dedicated usage patterns).

There is also a full showcase built around this MCP: `showcase/agent-observability-dashboard/`.

## Example Usage from an Agent

"Use the agent-session-analyzer MCP to ingest the last 20 sessions from the sample_logs directory, classify failures, and produce a markdown report of the top 3 recurring failure patterns with evidence."

## Status

Minimal but functional MCP server (illustrative implementation using the MCP SDK surface) + full production parsers, classifiers, exporters, and dashboard live in the shipped package.

See the flagship showcase `showcase/agent-observability-dashboard/` for the complete transparent build story and links to:
- https://github.com/cobusgreyling/agent-failure-analyzer (source)
- `pip install agent-failure-analyzer` (the real thing)

The MCP in this directory is what the agent used to help *build* the full tool.

**Author:** Cobus Greyling

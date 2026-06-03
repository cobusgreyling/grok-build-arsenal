# repo-graph MCP

Generates rich, actionable architecture and dependency graphs for codebases.

**Author:** Cobus Greyling — Grok Build Arsenal

## Tools

- `generate_module_graph` — Produces textual + (optionally) visual module dependency graph
- `identify_boundaries` — Detects logical boundaries and suggests hexagonal/clean architecture opportunities
- `find_hotspots` — High fan-in/fan-out modules, god classes, etc.
- `export_graph` — DOT, Mermaid, JSON, SVG (via graphviz if available)

## Value for Agents

Gives `grok-build-0.1` (and subagents) a structural map of the repo instead of relying only on file reads. Dramatically improves architecture reviews and large refactors.

## Setup Notes

Requires optional graphviz for visual exports. The server is intentionally small and focused.

Full usage examples and driving skill patterns are demonstrated in the `architecture-reviewer` skill and relevant showcases.

**This MCP was designed and prototyped using Grok Build 0.1 + Plan Mode.**

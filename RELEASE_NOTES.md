# Grok Build Arsenal v0.2.0 Release Notes

**Date:** June 2026  
**Sole author & maintainer:** Cobus Greyling

This release focuses on **substance + adoption + proof**. The arsenal now delivers runnable demos, more complete MCP implementations, a real one-command installer, and an interactive landing page — while being completely honest about where the production code lives.

## Highlights

### Runnable Demos & Prototypes
- New `showcase/arena-visualizer/arena_demo.py` — zero-dependency (rich optional) live simulation of the `subagent-arena` skill. Run it in 5 seconds after clone. Includes structured subagent output, side-by-side tradeoffs, synthesis, and fake cost/latency tracking.
- `mcps/test-intelligence/server.py` — full skeleton with `predict_tests_for_diff`, `run_minimal_test_set`, `detect_flaky_tests`, `coverage_guided_edit_plan`.
- `mcps/skill-validator/server.py` — frontmatter validation, MCP structure checks, safety audit for dangerous patterns, combined report generator.

### Frictionless Getting Started
- `scripts/install-skills.sh` — supports `--global`, `--target /path`, `--dry-run`. Now the recommended way in every Quick Start and template.
- Python FastAPI template is now a complete, copy-pasteable starter with `.grok/`, seeded skills, AGENTS.md, and .grokignore.

### Honesty & Navigation
- Flagship showcase and main docs now clearly distinguish "build story + MCP here" from "the real shipped PyPI package at agent-failure-analyzer".
- New "Related Projects & Proof" section (both README and landing page) that prominently surfaces the flagship + current runnable artifacts.
- All other showcases and MCPs updated with accurate status.

### Presentation & Interactivity
- Landing page (`docs/index.html`) is now alive:
  - Filterable + copyable skills grid.
  - Fully functional browser Subagent Arena simulator (same data shape as the Python demo).
- Better cross-links, updated tables, and "30 seconds to value" messaging everywhere.

### Meta / Dogfooding
- These improvements were planned and executed using the arsenal's own skills and patterns (Plan Mode discipline, subagent thinking for design tradeoffs, TDD on the demo, git discipline on changes, self-validation via the new skill-validator MCP, etc.).
- CI now also validates the installer and template structure.

## Upgrade / Try It
```bash
git clone https://github.com/cobusgreyling/grok-build-arsenal.git
cd grok-build-arsenal
bash scripts/install-skills.sh
python showcase/arena-visualizer/arena_demo.py   # <-- new!
grok inspect
```

Then open `docs/index.html` locally (or the GitHub Pages site) and play with the interactive arena widget.

## Full Details
See [CHANGELOG.md](CHANGELOG.md) for the complete list.

**All original work by Cobus Greyling. Built and refined with Grok Build 0.1 using the discipline documented in this repository.**

Next milestones will focus on completing more MCPs to production quality, adding one more runnable showcase component, and growing external signals.
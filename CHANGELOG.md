# Changelog

All notable changes to Grok Build Arsenal.

## [0.1.0] - 2026-06-03

### Added
- Initial release by Cobus Greyling
- 6 core production skills: plan-mode-orchestrator, subagent-arena, tdd-intelligence, mcp-orchestrator, git-discipline, architecture-reviewer
- 5 custom MCP server skeletons (agent-session-analyzer, repo-graph, test-intelligence, browser-qa, skill-validator) with examples
- 4 showcase directories with transparent build stories (agent-observability-dashboard as flagship)
- Project templates (Next.js, Python FastAPI, Rust CLI) pre-configured for Grok Build
- Exemplary AGENTS.md, .grok/ configuration, hooks, and .grokignore
- Public xAI API usage examples (`grok-build-0.1`)
- Skill validation CI + scripts
- Header image and professional README

**Sole author:** Cobus Greyling. Everything created using Grok Build 0.1.

## [0.2.0] - 2026-06 (Tier 1 + Tier 2 execution)

### Major Improvements — "Making the Arsenal More Amazing"
- **Substance delivered**: 
  - New runnable `showcase/arena-visualizer/arena_demo.py` (zero-dep Python simulation of subagent-arena with rich fallback, structured output, cost tracking, synthesis). Full build story in its README.
  - Implemented working `server.py` for `mcps/test-intelligence/` (predict_tests_for_diff, run_minimal_test_set, detect_flaky_tests, coverage_guided_edit_plan).
  - Implemented working `server.py` for `mcps/skill-validator/` (frontmatter validation, MCP structure checks, safety_audit, report generation).
- **Honesty & clarity**:
  - Complete rewrite of flagship showcase README + main README showcase descriptions to accurately point at the real shipped PyPI package while preserving transparent "arsenal method" stories.
  - New prominent "Related Projects & Proof" section (README + landing page) listing flagship + in-arsenal runnables.
- **Frictionless adoption**:
  - `scripts/install-skills.sh` (with --global / --target / --dry-run). Wired into all docs, templates, CI, and landing.
  - Python FastAPI template is now a real copy-paste starter (full .grok/ + seeded skills + AGENTS.md + .grokignore). Other templates refreshed.
- **Presentation & signals**:
  - Landing page (docs/index.html) now has interactive skills filter + per-skill "copy trigger" buttons + full browser-based Subagent Arena simulator widget (faithful to the Python demo).
  - Updated MCP tables, browser-qa README, and all cross-references.
  - Added Proof section and 30s flow callouts.
- **Release & CI**:
  - Extended CI to validate the installer and templates.
  - This changelog + release prep.

All changes executed while dogfooding the arsenal's own skills (plan-mode-orchestrator mindset, subagent-arena thinking for design choices, tdd-intelligence on demos, git-discipline on diffs).

**Sole author:** Cobus Greyling. Created and refined with Grok Build 0.1 + the exact patterns in this repo.

## [0.1.0] - 2026-06-03 (previous)

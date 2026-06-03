# Contributing to Grok Build Arsenal

**Sole original author and maintainer: Cobus Greyling**

This repository contains original work created by Cobus Greyling using Grok Build 0.1.

## Philosophy

- Extremely high quality bar. Only add things you would use in production.
- Every addition must have excellent documentation and clear value.
- New skills and MCPs must be narrowly scoped and come with driving instructions.

## How to Contribute

1. Open an issue or discussion first for anything non-trivial.
2. All original creative work remains attributed to Cobus Greyling.
3. Community contributions (bug fixes, improvements, new examples) are welcome and will be credited in commit messages / CHANGELOG.
4. Skills and MCPs added by contributors should still follow the strict frontmatter and safety standards defined in AGENTS.md.

## Adding a Skill

- Create `skills/<kebab-name>/SKILL.md`
- Excellent `name`, `description`, `when-to-use`
- Include Plan Mode guidance and verification steps
- Test it yourself with Grok Build

## Adding an MCP Server

- Keep it small and focused.
- Document security model clearly.
- Provide a driving skill pattern.
- Include a working (even if minimal) server implementation.

## Showcase Additions

Showcases must come with a transparent build story and must themselves be good examples of disciplined Grok Build usage.

## Concrete Ways to Help (Good First Contributions)

These are high-signal, narrowly scoped tasks that follow the project's standards. Open an issue first referencing one of these.

1. **Expand a failure taxonomy or add a new parser example** in the `agent-session-analyzer` MCP or the flagship package (see `mcps/agent-session-analyzer/` and the sister repo).
2. **Add a minimal runnable demo or example output** to `showcase/mcp-control-center/` or `showcase/smart-test-engine/` modeled after the new `arena-visualizer/arena_demo.py`.
3. **Implement the next MCP server skeleton** (e.g. finish `browser-qa/server.py` with screenshot + a11y tool surface) following the exact style of `test-intelligence/server.py`.
4. **Improve the browser arena simulator** in `docs/index.html` (more dynamic charters, export JSON button, better mobile layout) or port improvements back to the Python demo.
5. **Add one high-quality prompt + worked example** to `prompts/high-signal-examples.md` that has been battle-tested in a real Grok Build session.
6. **Portability notes**: Add a short worked example of using the `plan-mode-orchestrator` + `subagent-arena` patterns with Claude Code or Cursor (as a new file or section).

See existing issue templates in `.github/ISSUE_TEMPLATE/` (especially `skill_contribution.md` and `mcp_contribution.md`).

Before submitting, run:
- `python3 scripts/validate-skills.py`
- `bash scripts/install-skills.sh --dry-run`
- `python3 showcase/arena-visualizer/arena_demo.py --plain`

PRs should be small, reference the plan or skill used, and follow Conventional Commits.

## License

All contributions fall under the MIT license (see LICENSE). By contributing you agree that your changes may be used under those terms.

Thank you for helping make the Grok Build 0.1 ecosystem stronger.

— Cobus Greyling

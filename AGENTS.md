# AGENTS.md — Grok Build Arsenal

This file defines the contract for all work in this repository. Grok Build (and any agent using grok-build-0.1) must follow these rules without exception.

## Core Principles

- **Plan Mode first for anything non-trivial.** Never write code or make structural changes until a clear, approved plan exists.
- **Small, reviewable diffs.** Prefer many small, intentional commits over large ones.
- **Verification before declaration of done.** Tests, lint, type checks, and manual review where appropriate must pass.
- **Git discipline always.** Conventional Commits. Clean history. Feature branches. No direct commits to main.
- **Security and safety by default.** Treat hooks, MCP servers, and agent capabilities as high-risk. Explicitly call out risks.
- **Meta-awareness.** This repo exists to showcase and improve agentic workflows. When building tools for agents, dogfood them here.

## Project Identity

- **Sole author:** Cobus Greyling. All original creative and technical work is attributed to Cobus Greyling.
- **Tone:** Professional, precise, slightly irreverent where it serves clarity. No fluff.
- **Quality bar:** Production-grade or better. Every skill, MCP, and showcase must be something you would happily use in a real revenue-generating or high-visibility project.

## Workflow Rules

1. **Always begin complex work in Plan Mode.**
   - State the goal.
   - Decompose into the smallest safe steps.
   - Identify risks, files touched, and verification method.
   - Wait for explicit human approval before any write/edit.

2. **Use subagents deliberately.**
   - For investigation, research, or alternative approaches: spawn parallel subagents.
   - Synthesize results. Never blindly trust a single subagent path.
   - Document subagent usage in commit messages or PR descriptions when relevant.

3. **Skills are the primary mechanism for reusable workflows.**
   - Before writing custom instructions, check if an existing skill in `.grok/skills/` or `skills/` applies.
   - When a new repeatable workflow emerges, capture it with `/skillify` (or equivalent) into a new narrowly-scoped skill.
   - Skills must have excellent frontmatter (`name`, `description`, `when-to-use`).

4. **MCP servers are first-class citizens.**
   - New capabilities should be implemented as clean, narrowly-scoped MCP servers when they involve external state or tools.
   - Every MCP must have:
     - Clear security model
     - Manifest / tool list documented
     - A driving skill that knows how to use it effectively
     - Example usage in a showcase or prompt

5. **Testing and verification.**
   - For code changes: add or update tests that would have caught the change.
   - For skills and MCPs: include validation steps (frontmatter checks, safety review, example runs).
   - Run `grok inspect` after any structural change to configuration.

## Coding Standards

- **Python:** Modern (3.11+), type hints everywhere, pytest, ruff or black + isort.
- **TypeScript / JS (Next.js etc.):** Strict, App Router where applicable, proper server/client boundaries.
- **Rust (CLI/tools):** Strong error handling with thiserror/anyhow, comprehensive tests, clippy clean.
- **General:**
  - Prefer composition over inheritance.
  - Explicit over implicit.
  - No secrets in code or commits.
  - Maximum line length ~100 for most languages (120 acceptable for tests/docs).
  - Commit messages follow Conventional Commits.

## Git & Collaboration

- Branch naming: `feature/`, `fix/`, `chore/`, `docs/`
- Never push directly to main.
- Every PR must be small enough for a focused review.
- Update relevant skills, AGENTS.md, or docs when patterns change.
- `grok inspect` output or key decisions should be referenced in significant PRs.

## Showcase Rules

When adding or updating a showcase:
- Include a clear "Build Story" (prompts used, Plan Mode usage, subagents, skills/MCPs, approximate effort).
- All code must follow the standards above.
- The showcase must itself be a good citizen of this repo (uses skills from here where possible).
- Provide at least one "how to run / explore" command.

## Forbidden Patterns

- Large un-reviewed refactors.
- Adding frameworks or heavy dependencies without a plan that justifies them.
- Writing skills or MCPs that hide dangerous behavior.
- Committing generated or lockfile noise.
- Claiming authorship for work that is not yours (Cobus Greyling is the sole author of original material here).

## When in Doubt

Run `grok inspect`.

Then propose the smallest safe next step in Plan Mode.

---

This file is loaded automatically by Grok Build. It is the single source of truth for agent behavior in this repository.

Maintained by Cobus Greyling.

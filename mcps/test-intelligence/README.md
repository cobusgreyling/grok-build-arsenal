# test-intelligence MCP

Production-grade test selection, impact analysis, flakiness detection, and coverage-guided editing for large codebases.

**Sole author: Cobus Greyling**

Part of Grok Build Arsenal.

## Capabilities (Tools)
- `predict_tests_for_diff` — Given a diff or changed files, return the smallest high-signal test set.
- `run_minimal_test_set` — Execute only the predicted tests (with summary + failure capture).
- `detect_flaky_tests` — Surface tests with statistical flakiness signals from history.
- `coverage_guided_edit_plan` — Safe edit ordering + the tests that absolutely must stay green.

## Why It Matters
When used with `tdd-intelligence` and the `plan-mode-orchestrator`, this MCP lets agents make large refactors or feature additions with dramatically lower risk and much faster feedback loops.

See the `smart-test-engine` showcase for the vision and usage patterns.

A working skeleton server.py is included (same style as agent-session-analyzer). The real production version would integrate deeply with pytest coverage, git, and your CI history.

## Quick Setup (same pattern as other MCPs)
```bash
cd mcps/test-intelligence
python -m venv .venv && source .venv/bin/activate
pip install mcp
python server.py
```

Then register in your `.grok/config.toml` or via the MCP control center.

## Driving Skill
Pair with `tdd-intelligence` (write the test first) + `test-intelligence` MCP (run the *right* tests).

Example trigger:
"Use test-intelligence to predict the tests for this diff, then run the minimal set with tdd-intelligence discipline."

**This MCP was designed using Grok Build 0.1 + Plan Mode + subagent-arena exploration of test strategies.**

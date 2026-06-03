# Showcase: Subagent Arena Visualizer

**Interactive runner + visualizer for the `subagent-arena` skill pattern.**

**Sole author: Cobus Greyling**

## What This Is
A small, self-contained demo that shows exactly how the `subagent-arena` skill works in practice:

1. You give the arena a clear question.
2. You spawn 2–4 subagents with deliberately different charters (fast vs correct vs observable vs secure, etc.).
3. Each subagent returns structured output (Findings, Tradeoffs, Recommended Steps, Risks, Confidence).
4. You synthesize: extract the strongest ideas, build a hybrid recommendation, and usually hand off to `plan-mode-orchestrator`.

This is one of the highest-leverage patterns in the entire arsenal for any ambiguous or high-stakes design/architecture question.

## Run the Live Demo (Tier 1 deliverable)
```bash
# From the repo root
python showcase/arena-visualizer/arena_demo.py

# With rich (beautiful tables + markdown) — recommended
pip install rich
python showcase/arena-visualizer/arena_demo.py

# Custom question
python showcase/arena-visualizer/arena_demo.py --task "How should we add reversible architecture changes to a large legacy Python service?"

# Plain text (CI / no color)
python showcase/arena-visualizer/arena_demo.py --plain

# Machine readable
python showcase/arena-visualizer/arena_demo.py --json
```

The demo is deterministic (great for docs and tests) but uses realistic outputs that mirror what grok-build-0.1 actually produces when the skill is followed.

## How It Was Built (Transparency)
- Started with `plan-mode-orchestrator` on the question "Create a runnable, zero-to-hero demo of the subagent-arena skill that people can run in 10 seconds after cloning".
- Used the `subagent-arena` pattern itself while designing the output formats and synthesis logic.
- Followed `tdd-intelligence` for the core data models and printing paths (even in a demo).
- Kept it dependency-free with an optional rich path (the same "graceful degradation" philosophy used in many arsenal MCPs).
- Git hygiene via `git-discipline`.

**Result:** A single ~300 line file that is both a teaching tool and a working prototype you can point people at.

## The Driving Skill
See `skills/subagent-arena/SKILL.md` — this demo is the canonical "what good looks like" executable example.

Typical trigger in a real session:
> "Run a subagent arena on the best way to add persistent memory to the MCP control center. Use the arena-visualizer demo as the reference implementation for output shape."

## Next Steps (real usage)
After a good arena you almost always do:
```bash
# In your grok session
Use plan-mode-orchestrator. Take the synthesis from the arena above and produce the smallest safe first PR for Phase 1.
```

## Files
- `arena_demo.py` — the runnable visualizer (the actual value)
- `README.md` — this file (build story + usage)

This showcase proves that the `subagent-arena` skill is not just good advice — it produces clear, comparable, synthesizable artifacts that lead directly to better plans.

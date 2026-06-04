# Showcase: nemotron-think

**Visible Reasoning Agent Framework for NVIDIA Nemotron 3 Ultra**

**GitHub:** https://github.com/cobusgreyling/nemotron-think  
**Live landing + interactive trace demo:** https://cobusgreyling.github.io/nemotron-think/ (now public — served from `docs/`)

A clean, production-minded Python package and CLI that makes every internal step of a Nemotron 3 Ultra (or compatible LRM) agent **visible, logged, and replayable**.

- Streams reasoning (`enable_thinking`) in green, incremental tool call JSON building in orange, final answers cleanly.
- Full `AgentRun` / `AgentStep` traces persisted as rich JSON (every reasoning chunk, every delta.tool_call arg fragment, observations, token usage).
- `nemotron-think replay traces/xxx.json` — perfect deterministic offline replay for demos, evals, datasets, or talks (no API keys needed).
- Controllable `reasoning_budget`, `low_effort`, custom tools via simple decorator-style API.
- Batteries-included safe tools: math, time, python_exec (guarded), web_search.

**The point:** Most "agent" value lives in the harness and observability around the model. nemotron-think makes the model's thinking first-class output.

## Key Artifacts
- CLI + Python API (`pip install -e .` or published patterns)
- `docs/index.html` — self-contained, beautiful Tailwind landing page with live simulated trace, feature explanations, and one-click clone/run instructions.
- Example traces under `examples/traces/`
- Full docs in `docs/` (getting-started, traces, api, extending tools)

## How It Was Built (Grok Build Arsenal in Action)
- Started in Plan Mode (plan-mode-orchestrator) to design the trace model, streaming helpers, and CLI surface before any code.
- Subagent-arena used to explore alternative trace capture strategies and tool execution loop designs.
- tdd-intelligence for the execution + observation harness (characterization tests on streaming deltas and trace serialization).
- git-discipline + clean packaging (pyproject.toml entry points, .env.example, docs as first-class).
- The interactive showcase page (`docs/index.html`) itself was built with the same disciplined iteration + browser-qa style validation.

**Result:** A focused, installable, demo-ready framework whose primary output is *trustworthy, inspectable reasoning artifacts* — exactly what long-horizon reasoning models like Nemotron 3 Ultra are built for.

## Quick Demo (after making the repo public + `NVIDIA_API_KEY`)
```bash
git clone https://github.com/cobusgreyling/nemotron-think.git
cd nemotron-think
python -m venv .venv && source .venv/bin/activate
pip install -e .
nemotron-think run "A bat and a ball cost $1.10. The bat costs $1 more than the ball. How much does the ball cost?"
nemotron-think run "Research top open-source text-to-video models from the last 6 months." --budget 8192 --save-trace traces/video.json
nemotron-think replay traces/video.json
```

See the package README and `docs/` for the full surface, custom tools, and the philosophy.

**All original work by Cobus Greyling. Created using Grok Build 0.1 + the skills and patterns in this arsenal.**

---

See the main arsenal README for how this fits the larger story of shipping real things with disciplined agentic workflows.
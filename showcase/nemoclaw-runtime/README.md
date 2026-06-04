# Showcase: NemoClaw Runtime (nemoclaw-runtime)

**A secure, always-on runtime for autonomous agents.**

**GitHub:** https://github.com/cobusgreyling/nemoclaw-runtime  
**Control plane demo:** `nemoclaw serve` → http://127.0.0.1:8848 (serves the stdlib UI)

Reference implementation of the secure agent runtime blueprint: the model proposes actions; the runtime decides whether they actually happen.

- **Gateway** — single choke point that routes inference and adjudicates every action.
- **Policy engine** — explainable allow/deny rules over shell, fs, and network. Every decision logs the exact rule that matched.
- **OpenShell sandbox** — only executes what policy allowed; captures stdout/stderr, enforces timeout, records everything.
- **Hermes agent** — "gets better with use": captures successful goal → plan runs as durable, replayable *skills*. Next time the same intent matches, it replays without re-planning.
- **Zero hard dependencies** for the core runtime. Pure stdlib + optional local Ollama/Nemotron backends.
- Built-in control plane (single-file HTTP server + `ui/index.html`) showing live events, blocks, runs, and captured skills.

The architecture is deliberately small enough to read in one sitting yet production-minded: policy is plain JSON (reviewable, diffable, shippable), the sandbox interface is swappable for real container backends, and every layer is event-sourced.

## Quick Tour
```bash
git clone https://github.com/cobusgreyling/nemoclaw-runtime.git
cd nemoclaw-runtime
./nemoclaw.sh          # sets up the `nemoclaw` and `nemohermes` CLIs
nemoclaw onboard
nemoclaw run "check system disk health"
nemoclaw run "clean up everything on the host"   # watch policy block rm -rf patterns
nemohermes run "audit the system inventory"      # first time captures skill
nemohermes run "audit the system inventory"      # second time replays the skill
nemoclaw serve                                   # open the live dashboard
```

## How It Was Built (Grok Build Arsenal in Action)
- Heavy use of Plan Mode + plan-mode-orchestrator to design the layered architecture (gateway as the key abstraction) before writing the first line of the policy or sandbox.
- Architecture reviewer + subagent-arena on the policy model and the durable skills capture/replay strategy.
- tdd-intelligence and tight feedback loops on the sandbox executor and state machine (the thing that must never lie about what ran).
- git-discipline for the clean, minimal, stdlib-only structure (one `nemoclaw/` package, tiny installer script, docs as md + embedded ui).
- The control-plane dashboard was iterated with the browser-qa style patterns and kept dependency-free.

**The model is not the product. The runtime / harness is.**

This is the concrete, runnable counterpart to the "harness is where the intelligence lives" thesis that also powers nemotron-think and the Nemotron 3 Ultra showcase.

## Files of Note
- `nemoclaw/gateway.py`, `policy.py`, `sandbox.py`, `agent.py`, `skills.py`
- `nemoclaw/ui/index.html` — the live dashboard
- `policies/default.json` — the conservative starting guardrails
- `docs/` — architecture, policy writing, quickstart
- `BLOG.md` — the deep write-up

**All original work by Cobus Greyling. Created using Grok Build 0.1 + the skills and patterns in this arsenal.**

See the main README for context on why these runtime / harness projects matter for real agent deployments.
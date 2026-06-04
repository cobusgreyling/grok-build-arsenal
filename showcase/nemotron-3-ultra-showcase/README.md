# Showcase: Nemotron 3 Ultra Feature Showcase

**Live Gradio playground for NVIDIA Nemotron 3 Ultra (550B) capabilities**

**GitHub:** https://github.com/cobusgreyling/nemotron-3-ultra-showcase

A focused, styled-in-NVIDIA-green Gradio app that drives the live `NVIDIA-Nemotron-3-Ultra-550B-A55B` (and successor) endpoint to demonstrate exactly what the model was post-trained for: long-horizon agentic work inside harnesses.

## What It Demonstrates
| Tab / Area            | Feature exercised |
|-----------------------|-------------------|
| Reasoning Playground  | `enable_thinking` true/false, `low_effort` true, `reasoning_budget` slider, streamed reasoning tokens (green) + final answer |
| Tool Calling          | Streaming `delta.tool_calls` (watch args build live), local tool execution loop, re-injection of results |
| Model Card + Visuals  | Architecture (LatentMoE + Mamba2-Transformer hybrid), 1M context, benchmark charts (intelligence/speed, cost frontier) |

Includes high-fidelity screenshots of every mode in `assets/`.

## Why This Exists
Nemotron 3 Ultra is explicitly positioned as an *agent harness model*. This tiny app is the minimal harness needed to see its headline switches (reasoning mode + budget) and the reliable tool-call loop in action.

The same patterns (visible reasoning, tool loop, budget control) are productionized in the sibling `nemotron-think` framework.

## Run It
```bash
git clone https://github.com/cobusgreyling/nemotron-3-ultra-showcase.git
cd nemotron-3-ultra-showcase
pip install -r requirements.txt
export NVIDIA_API_KEY="nvapi-..."
python app.py
# open http://localhost:7860
```

## How It Was Built (Grok Build Arsenal in Action)
- Plan Mode for the overall Gradio surface + the extra_body construction for chat_template_kwargs (the non-standard reasoning controls live here).
- Subagent exploration of streaming accumulation strategies for tool call name+args (the model sometimes resends the tool name across deltas — a real foot-gun).
- tdd-intelligence on the tool loop and the mode switching logic.
- Heavy emphasis on visual QA of the screenshots + clean presentation (the `assets/` are first-class deliverables).
- The BLOG.md write-up was produced as part of the disciplined documentation step.

Small surface area, high signal: exactly the kind of focused artifact that proves model capabilities inside a real harness.

**All original work by Cobus Greyling. Created using Grok Build 0.1 + the skills and patterns in this arsenal.**

See `BLOG.md` for the full model + harness analysis and the other two Nemotron / NemoClaw showcases for the "production harness" counterparts.
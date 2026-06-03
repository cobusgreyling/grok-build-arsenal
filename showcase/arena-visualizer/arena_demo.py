#!/usr/bin/env python3
"""
Subagent Arena Visualizer — Runnable Demo
Part of Grok Build Arsenal (showcase/arena-visualizer)

Demonstrates the `subagent-arena` skill pattern:
- Define a clear question
- Spawn parallel subagents with distinct charters
- Collect structured outputs
- Synthesize the strongest ideas + produce a recommendation
- Track cost / latency (simulated)

Zero hard dependencies. Rich is used for beautiful output if installed:
    pip install rich

Otherwise falls back to clean ANSI/plain text.

Run:
    python showcase/arena-visualizer/arena_demo.py
    python showcase/arena-visualizer/arena_demo.py --task "Design a minimal persistent memory system for MCP servers"
    python showcase/arena-visualizer/arena_demo.py --plain

Built with the same discipline as the rest of the arsenal:
Plan Mode first, subagent-arena for exploration, then handoff to plan-mode-orchestrator.

Sole author: Cobus Greyling
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

# --- Optional rich for gorgeous output ----------------------------------------

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    Console = None  # type: ignore

# --- Data models --------------------------------------------------------------

@dataclass
class SubagentResult:
    charter: str
    approach_name: str
    findings: List[str]
    tradeoffs: List[str]
    recommended_steps: List[str]
    risks: List[str]
    confidence: str  # High / Medium / Low
    est_tokens: int
    est_latency_ms: int

@dataclass
class ArenaSynthesis:
    question: str
    winning_ideas: List[str]
    hybrid_recommendation: List[str]
    overall_confidence: str
    total_tokens: int
    total_latency_ms: int
    notes: str

# --- Sample task + realistic subagent outputs (deterministic for demo) --------

DEFAULT_QUESTION = (
    "Best way to add persistent memory / long-term recall to an MCP control center "
    "so that agents can remember previous sessions, user preferences, and past decisions "
    "across projects without leaking context or exploding token usage."
)

CHARTER_A = "Approach A: Minimal diff, ship fast (local JSON + simple vector store)"
CHARTER_B = "Approach B: Cleanest long-term architecture (proper embeddings + namespaced store + versioning)"
CHARTER_C = "Approach C: Best observability + testability + cost control (instrumented, evictable, cheap)"

# Fixed but realistic outputs so the demo is reproducible and educational
SUBAGENT_A: SubagentResult = SubagentResult(
    charter=CHARTER_A,
    approach_name="Fast local persistence (JSONL + sqlite-vec or faiss local)",
    findings=[
        "Store conversation summaries + key decisions as JSONL per project + global index.",
        "Use a tiny local vector DB (sqlite-vec or faiss) for semantic recall of past decisions.",
        "One file per MCP server + one global 'memory.db'. Easy to backup/rsync.",
        "Can be implemented in < 200 lines + one new MCP tool: remember() / recall().",
    ],
    tradeoffs=[
        "Very quick to ship (1-2 focused sessions).",
        "No external services, zero cost, works offline.",
        "Limited scalability and no easy multi-user / team sharing.",
        "Simple eviction policy needed or files will grow forever.",
    ],
    recommended_steps=[
        "Add a `memory` MCP server with tools: store_fact, semantic_recall, list_facts.",
        "Store only high-signal summaries (use the plan-mode-orchestrator output as source of truth).",
        "Add a .grok/memory/ directory that is gitignored by default.",
        "Expose a CLI command `grok memory search \"why did we choose X?\"`.",
    ],
    risks=[
        "Memory poisoning if bad summaries get stored.",
        "No encryption at rest by default (local machine risk).",
        "Will need migration path later when users want cloud or team sync.",
    ],
    confidence="Medium",
    est_tokens=1240,
    est_latency_ms=1850,
)

SUBAGENT_B: SubagentResult = SubagentResult(
    charter=CHARTER_B,
    approach_name="Production architecture (namespaced, versioned, pluggable backends)",
    findings=[
        "Introduce MemoryNamespace (project, user, global, team) + MemoryEntry with schema version.",
        "Pluggable storage: LocalJSON, SQLiteVec, Chroma (local), later S3 + pgvector.",
        "Store full provenance: which plan/subagent/session produced the memory + timestamp + confidence.",
        "Built-in compaction + summarization hooks using tdd-intelligence style tests.",
        "First-class support for 'forget' and TTL policies.",
    ],
    tradeoffs=[
        "Much higher quality and future-proof.",
        "More code (probably 800-1200 LOC across MCP + skill + tests).",
        "Steeper initial learning curve for contributors.",
        "Still starts local-first but the abstraction makes cloud later cheap.",
    ],
    recommended_steps=[
        "Define MemoryEntry pydantic model + versioned JSON schema first (TDD).",
        "Create memory-orchestrator skill that knows when to persist vs ephemeral.",
        "Implement local backend + one remote stub (Chroma or LanceDB).",
        "Add migration tests and a 'memory doctor' command.",
        "Update mcp-orchestrator skill to recommend the memory MCP on new projects.",
    ],
    risks=[
        "Scope creep — easy to turn into a whole second product.",
        "Over-engineering for users who just want 'remember the last decision'.",
        "Storage abstraction can hide real perf problems until you have data.",
    ],
    confidence="High",
    est_tokens=2180,
    est_latency_ms=3120,
)

SUBAGENT_C: SubagentResult = SubagentResult(
    charter=CHARTER_C,
    approach_name="Observable + measurable + cheap (instrument everything, cost guardrails)",
    findings=[
        "Every recall must log: query, retrieved facts, tokens saved vs cost, hit rate.",
        "Add a tiny 'memory health' dashboard (or export to the existing agent-observability tools).",
        "Aggressive summarization + embedding only of high-value items (use cost model).",
        "Budget guardrails: refuse to store if daily memory budget exceeded unless user approves.",
        "A/B test different compaction strategies using the subagent-arena pattern itself.",
    ],
    tradeoffs=[
        "Excellent for proving value and controlling spend.",
        "Requires the existing observability stack to be useful (or re-implements some).",
        "More moving parts = more surface for bugs in the memory layer itself.",
        "Users who don't care about metrics will see extra complexity.",
    ],
    recommended_steps=[
        "Extend agent-session-analyzer taxonomy with 'memory' failure modes.",
        "Add structured logging + OTLP spans for every memory operation.",
        "Build a tiny memory-specific Grafana panel (reuse existing dashboard).",
        "Implement a 'memory cost report' command that plugs into afa analyze style flows.",
        "Default to very conservative storage (only explicit 'remember this' from user or high-confidence plans).",
    ],
    risks=[
        "Analysis paralysis — you can spend forever measuring instead of shipping recall.",
        "Privacy surface increases (you are now deliberately keeping user data).",
        "The cost guardrails themselves can become annoying UX.",
    ],
    confidence="Medium",
    est_tokens=1670,
    est_latency_ms=2410,
)

# --- Core arena logic ---------------------------------------------------------

def run_arena(question: str, plain: bool = False) -> ArenaSynthesis:
    subagents = [SUBAGENT_A, SUBAGENT_B, SUBAGENT_C]
    total_tokens = sum(s.est_tokens for s in subagents)
    total_latency = max(s.est_latency_ms for s in subagents)  # parallel

    # Fake "thinking" delay for demo theater
    if not plain:
        print("\n[arena] Spawning 3 parallel subagents...")
        time.sleep(0.4)

    # Synthesis (the most important part of the skill)
    winning_ideas: List[str] = []
    for s in subagents:
        # Pick the strongest 1-2 ideas from each
        if "minimal" in s.approach_name.lower() or "fast" in s.approach_name.lower():
            winning_ideas.append("Start with a dead-simple local backend (JSONL + small vector index) so we can ship something this week.")
        if "pluggable" in s.approach_name.lower() or "versioned" in str(s.findings):
            winning_ideas.append("Define a clean MemoryEntry + Namespace model + provenance from day one (prevents future migrations).")
        if "observab" in s.approach_name.lower() or "cost" in str(s.findings):
            winning_ideas.append("Instrument every recall + store operation and tie it into the existing agent-observability pipeline.")

    hybrid: List[str] = [
        "Phase 1 (fast): local JSONL + sqlite-vec backend behind a tiny `memory` MCP (use the minimal approach).",
        "Phase 2 (architecture): introduce versioned MemoryEntry + namespaces + pluggable interface (pull the good ideas from B).",
        "Phase 3 (quality): add full tracing, cost accounting, compaction hooks, and health reporting (C).",
        "Driving skill: create a small `memory-orchestrator` skill that decides what is worth persisting.",
        "Safety: all memories are local by default, user must explicitly opt-in to any remote backend.",
        "Verification: add characterization tests + a tiny 'memory doctor' command before any real usage.",
    ]

    synthesis = ArenaSynthesis(
        question=question,
        winning_ideas=list(dict.fromkeys(winning_ideas)),  # dedupe preserve order
        hybrid_recommendation=hybrid,
        overall_confidence="High (strong consensus on phased approach)",
        total_tokens=total_tokens,
        total_latency_ms=total_latency,
        notes=(
            "All three subagents agreed that starting minimal + having a clear migration path to better architecture "
            "is the right move. The observability angle (C) is treated as a quality multiplier rather than the first deliverable."
        ),
    )
    return synthesis, subagents

# --- Pretty printing ----------------------------------------------------------

def print_header(text: str, plain: bool) -> None:
    if RICH_AVAILABLE and not plain:
        console = Console()
        console.print(Panel.fit(f"[bold cyan]{text}[/]", border_style="cyan"))
    else:
        print(f"\n=== {text} ===\n")

def print_subagent(result: SubagentResult, idx: int, plain: bool) -> None:
    if RICH_AVAILABLE and not plain:
        console = Console()
        md = f"""**Charter:** {result.charter}

**Approach:** {result.approach_name}

**Key Findings**
""" + "\n".join(f"- {f}" for f in result.findings) + """

**Tradeoffs**
""" + "\n".join(f"- {t}" for t in result.tradeoffs) + f"""

**Recommended Next Steps**
""" + "\n".join(f"{i+1}. {s}" for i, s in enumerate(result.recommended_steps)) + """

**Risks**
""" + "\n".join(f"- {r}" for r in result.risks) + f"""

**Confidence:** {result.confidence} | ~{result.est_tokens} tokens | ~{result.est_latency_ms}ms
"""
        console.print(Panel(Markdown(md), title=f"Subagent {idx}: {result.approach_name.split('(')[0].strip()}", border_style="blue"))
    else:
        print(f"\n--- Subagent {idx}: {result.approach_name} ---")
        print(f"Charter: {result.charter}")
        print("\nFindings:")
        for f in result.findings:
            print(f"  • {f}")
        print("\nTradeoffs:")
        for t in result.tradeoffs:
            print(f"  • {t}")
        print("\nRecommended steps:")
        for i, s in enumerate(result.recommended_steps, 1):
            print(f"  {i}. {s}")
        print("\nRisks:")
        for r in result.risks:
            print(f"  • {r}")
        print(f"\nConfidence: {result.confidence} | est. {result.est_tokens} tokens | {result.est_latency_ms}ms")

def print_synthesis(syn: ArenaSynthesis, plain: bool) -> None:
    if RICH_AVAILABLE and not plain:
        console = Console()
        content = f"""**Question:** {syn.question}

**Strongest ideas extracted from the arena**
""" + "\n".join(f"- {w}" for w in syn.winning_ideas) + """

**Recommended hybrid path (what you should actually do)**
""" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(syn.hybrid_recommendation)) + f"""

**Overall confidence:** {syn.overall_confidence}

**Arena cost:** ~{syn.total_tokens} tokens | ~{syn.total_latency_ms}ms (parallel)

**Notes:** {syn.notes}
"""
        console.print(Panel(Markdown(content), title="Arena Synthesis", border_style="green"))
    else:
        print("\n" + "=" * 60)
        print("ARENA SYNTHESIS")
        print("=" * 60)
        print(f"\nQuestion: {syn.question}\n")
        print("Strongest ideas extracted:")
        for w in syn.winning_ideas:
            print(f"  • {w}")
        print("\nRecommended hybrid path (execute this):")
        for i, h in enumerate(syn.hybrid_recommendation, 1):
            print(f"  {i}. {h}")
        print(f"\nOverall confidence: {syn.overall_confidence}")
        print(f"Arena cost: ~{syn.total_tokens} tokens | ~{syn.total_latency_ms}ms (executed in parallel)")
        print(f"\nNotes: {syn.notes}")
        print("=" * 60)

def print_cost_summary(subagents: List[SubagentResult], syn: ArenaSynthesis, plain: bool) -> None:
    if RICH_AVAILABLE and not plain:
        console = Console()
        table = Table(title="Arena Cost & Latency (simulated)", box=box.SIMPLE)
        table.add_column("Subagent", style="cyan")
        table.add_column("Tokens", justify="right")
        table.add_column("Latency (ms)", justify="right")
        for s in subagents:
            table.add_row(s.approach_name.split("(")[0].strip()[:35], f"{s.est_tokens}", f"{s.est_latency_ms}")
        table.add_row("[bold]TOTAL (parallel)[/]", f"[bold]{syn.total_tokens}[/]", f"[bold]{syn.total_latency_ms}[/]")
        console.print(table)
    else:
        print("\nArena cost breakdown (parallel execution):")
        for s in subagents:
            name = s.approach_name.split("(")[0].strip()
            print(f"  {name[:40]:<42} {s.est_tokens:>5} tokens  {s.est_latency_ms:>5}ms")
        print(f"  {'TOTAL (parallel)':<42} {syn.total_tokens:>5} tokens  {syn.total_latency_ms:>5}ms")

def print_next_steps(plain: bool) -> None:
    msg = (
        "\nNext in a real session:\n"
        "  1. Hand this synthesis to plan-mode-orchestrator\n"
        "  2. 'Plan the Phase 1 minimal memory MCP + skill using the arena output'\n"
        "  3. Use tdd-intelligence + git-discipline on the implementation\n\n"
        "This demo was produced by the exact patterns in skills/subagent-arena/SKILL.md\n"
    )
    if RICH_AVAILABLE and not plain:
        Console().print(Panel(msg.strip(), border_style="magenta"))
    else:
        print(msg)

# --- Main ---------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Subagent Arena Demo (Grok Build Arsenal)")
    parser.add_argument("--task", "-t", default=DEFAULT_QUESTION, help="Custom question to run the arena on")
    parser.add_argument("--plain", action="store_true", help="Force plain text output (no rich)")
    parser.add_argument("--json", action="store_true", help="Output raw structured results as JSON (for scripting)")
    args = parser.parse_args()

    plain = args.plain or not RICH_AVAILABLE

    if not RICH_AVAILABLE and not args.plain:
        print("(rich not installed — using plain text. `pip install rich` for beautiful tables & markdown)\n", file=sys.stderr)

    print_header("SUBAGENT ARENA VISUALIZER — LIVE DEMO", plain)
    print(f"Question: {args.task}\n")

    synthesis, subagents = run_arena(args.task, plain=plain)

    if args.json:
        payload = {
            "question": args.task,
            "subagents": [asdict(s) for s in subagents],
            "synthesis": asdict(synthesis),
        }
        print(json.dumps(payload, indent=2))
        return

    for i, sa in enumerate(subagents, 1):
        print_subagent(sa, i, plain)
        if not plain:
            time.sleep(0.15)

    print_cost_summary(subagents, synthesis, plain)
    print_synthesis(synthesis, plain)
    print_next_steps(plain)

    # Exit code 0 = success, as a real arena would
    sys.exit(0)

if __name__ == "__main__":
    main()
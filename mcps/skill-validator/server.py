#!/usr/bin/env python3
"""
skill-validator MCP Server
Validates skills (SKILL.md frontmatter + content) and MCP servers for safety, completeness, and arsenal conventions.

Used heavily by the CI in this repo and by agents when creating or reviewing new skills/MCPs.

Sole author: Cobus Greyling
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, List, Dict

try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    Server = object  # type: ignore
    stdio_server = lambda: None  # type: ignore
    Tool = dict  # type: ignore
    TextContent = dict  # type: ignore


server = Server("skill-validator")

REQUIRED_SKILL_FIELDS = {"name", "description", "version", "author"}
DANGEROUS_PATTERNS = [
    r"subprocess\.(run|call|Popen|check_output)",
    r"os\.system",
    r"eval\(",
    r"exec\(",
    r"__import__\s*\(",
    r"open\s*\([^)]*['\"][wa]['\"]",
]

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="validate_skill_frontmatter",
            description="Check that a SKILL.md has the required frontmatter fields and correct author (Cobus Greyling by default).",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Path to SKILL.md or skill directory"},
                },
                "required": ["path"],
            },
        ),
        Tool(
            name="validate_mcp_server",
            description="Basic sanity + security checks on an MCP server directory (README + server.py presence, dangerous code patterns).",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                },
                "required": ["path"],
            },
        ),
        Tool(
            name="safety_audit_skill",
            description="Scan a skill or MCP for risky patterns (shell execution, broad file writes, secret handling, etc.). Returns findings + severity.",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "strict": {"type": "boolean", "default": True},
                },
            },
        ),
        Tool(
            name="generate_skill_report",
            description="Produce a markdown validation report suitable for a PR or review.",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                },
            },
        ),
    ]


def _read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    path_str = arguments.get("path", ".")
    p = Path(path_str)

    if name == "validate_skill_frontmatter":
        if p.is_dir():
            p = p / "SKILL.md"
        content = _read_text(p)
        errors: List[str] = []
        if not content.startswith("---"):
            errors.append("Missing YAML frontmatter")
        else:
            # crude frontmatter extraction (same spirit as scripts/validate-skills.py)
            end = content.find("---", 3)
            if end == -1:
                errors.append("Malformed frontmatter")
            else:
                fm = content[3:end]
                data: Dict[str, Any] = {}
                for line in fm.splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        data[k.strip()] = v.strip().strip('"\'')
                for field in REQUIRED_SKILL_FIELDS:
                    if field not in data or not data[field]:
                        errors.append(f"Missing required field: {field}")
                if data.get("author") and data.get("author") != "Cobus Greyling":
                    errors.append("Author must be 'Cobus Greyling' per AGENTS.md policy (or update policy first)")
        return [TextContent(type="text", text=json.dumps({"path": str(p), "valid": len(errors) == 0, "errors": errors}, indent=2))]

    if name == "validate_mcp_server":
        errors = []
        if not (p / "README.md").exists():
            errors.append("Missing README.md")
        if not (p / "server.py").exists():
            errors.append("Missing server.py (or this MCP is intentionally docs-only)")
        return [TextContent(type="text", text=json.dumps({"path": str(p), "valid": len(errors) == 0, "errors": errors}, indent=2))]

    if name == "safety_audit_skill":
        content = _read_text(p if p.is_file() else p / "SKILL.md") + _read_text(p / "server.py" if p.is_dir() else Path())
        findings = []
        for pat in DANGEROUS_PATTERNS:
            if re.search(pat, content):
                findings.append({"pattern": pat, "severity": "high", "message": "Potential arbitrary execution or broad write — review with security-audit skill"})
        if "secret" in content.lower() or "password" in content.lower() or "api_key" in content.lower():
            findings.append({"pattern": "secret-like string", "severity": "medium", "message": "Mentions secrets — make sure they are never in code or committed memory"})
        return [TextContent(type="text", text=json.dumps({"path": str(p), "findings": findings, "passed": len(findings) == 0}, indent=2))]

    if name == "generate_skill_report":
        # Combine the other three for convenience
        fm = json.loads((await call_tool("validate_skill_frontmatter", {"path": path_str}))[0].text)
        mcp = json.loads((await call_tool("validate_mcp_server", {"path": path_str}))[0].text)
        safety = json.loads((await call_tool("safety_audit_skill", {"path": path_str}))[0].text)
        report = f"""# Skill / MCP Validation Report

**Path:** {path_str}

## Frontmatter
{'✅ Valid' if fm['valid'] else '❌ Issues'}
{chr(10).join('- ' + e for e in fm.get('errors', [])) or 'No errors'}

## MCP Structure
{'✅ OK' if mcp.get('valid', True) else '❌ Issues'}
{chr(10).join('- ' + e for e in mcp.get('errors', [])) or ''}

## Safety
{'✅ Clean' if safety.get('passed') else '⚠️ Findings'}
{chr(10).join('- ' + f['message'] for f in safety.get('findings', [])) or ''}

*Generated by skill-validator MCP (Grok Build Arsenal). Run with security-audit skill for deeper review.*
"""
        return [TextContent(type="text", text=report)]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

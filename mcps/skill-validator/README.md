# skill-validator MCP

Validates skills (frontmatter, structure, safety) and MCP servers. Used by CI and by agents when extending the arsenal.

**Sole author: Cobus Greyling**

## Tools
- `validate_skill_frontmatter` — required fields + author policy enforcement
- `validate_mcp_server` — README + server.py presence checks
- `safety_audit_skill` — scan for dangerous patterns (subprocess, eval, broad writes, secret mentions)
- `generate_skill_report` — combined markdown report perfect for PR descriptions

A working server.py skeleton is included. The real power comes when an agent calls this *during* skill/MCP creation (dogfooding).

## Example Use (inside a Grok session)
"Before I commit this new skill, use skill-validator on the directory and then run safety-audit with security-audit skill."

See `scripts/validate-skills.py` for the simpler CI version that this MCP generalizes.

This MCP was created as part of making the arsenal more self-validating (Tier 1 work).

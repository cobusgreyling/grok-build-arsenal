# Python FastAPI + Grok Build Starter

A high-quality, production-minded starting template pre-configured for Grok Build 0.1 / grok-build-0.1.

**Author:** Cobus Greyling (from grok-build-arsenal)

## What You Get
- `AGENTS.md` — strict rules for architecture, testing, security, and agent discipline on this stack
- `.grok/config.toml` — plan_mode_default on, skills paths configured
- `.grokignore` — tuned for Python + agent sessions (avoids logging large/sensitive traces)
- `.grok/skills/` — the highest-leverage skills pre-seeded (plan-mode-orchestrator, tdd-intelligence, git-discipline)
- Ready for `test-intelligence`, `repo-graph`, `security-audit` etc. MCPs (install via arsenal)

## Usage
```bash
# 1. Copy into your new project
cp -a /path/to/grok-build-arsenal/templates/python-fastapi-grok/. /path/to/my-new-service/

cd /path/to/my-new-service

# 2. (Optional but recommended) Pull in the full arsenal skills
bash /path/to/grok-build-arsenal/scripts/install-skills.sh

# 3. Let Grok discover everything
grok inspect

# 4. Start building (it will default to Plan Mode)
grok
```

Then use triggers like:
- "TDD this new endpoint with full auth"
- "Plan the addition of the payments service using plan-mode-orchestrator"
- "Security audit this diff"

This template + the skills in the arsenal are the exact starting point used for high-quality FastAPI services built with grok-build-0.1.

**All original template work by Cobus Greyling.**

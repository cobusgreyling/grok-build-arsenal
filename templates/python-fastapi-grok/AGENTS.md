# AGENTS.md — Python FastAPI + Grok Build

Sole author of the template: Cobus Greyling

## Stack Rules
- FastAPI + Pydantic v2 + SQLAlchemy 2.0 (or async equivalent)
- pytest + pytest-asyncio + factoryboy or similar for tests
- ruff for linting + formatting
- Type hints everywhere

## Architecture
- Routers in `app/routers/`
- Services / business logic in `app/services/`
- Models / schemas clearly separated
- No business logic in routers

## Grok Build Specific
- Always use Plan Mode for features larger than a single endpoint + test.
- Use `tdd-intelligence` skill.
- Prefer the `test-intelligence` MCP once available.
- Run `pytest -q` before considering work complete on any change.

## Security
- Never commit secrets.
- Use dependency injection for auth.
- Review all new MCP/hook usage with `security-audit` skill.

Copy this folder as a starting point for new Python services in the Grok ecosystem.

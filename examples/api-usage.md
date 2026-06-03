# Using grok-build-0.1 Directly via the xAI Public API

This repo demonstrates both the Grok Build CLI/TUI experience and direct use of the model (`grok-build-0.1`) through the public API for custom agents and harnesses.

**All examples by Cobus Greyling.**

## Python (OpenAI-compatible Responses API)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1",
)

response = client.responses.create(
    model="grok-build-0.1",
    input=[
        {
            "role": "user",
            "content": "Use the plan-mode-orchestrator pattern. Propose the smallest safe first step for adding a new MCP server to this project."
        }
    ],
)

print(response.output_text)
```

## With Tool Use / MCP-style Loops (Conceptual)

Because `grok-build-0.1` is trained for agentic tool use, you can drive it in a loop with your own MCP servers or function calling:

```python
# Pseudocode for a custom harness
while not done:
    resp = client.responses.create(
        model="grok-build-0.1",
        input=conversation,
        tools=your_mcp_tools,   # or OpenAI function calling format
    )
    # execute tools, append results, continue
```

See the official docs for the exact schema: https://docs.x.ai

## Headless + Structured Output

```bash
curl https://api.x.ai/v1/responses \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "grok-build-0.1",
    "input": "Run a subagent-arena on the best architecture for a session replay tool. Return structured JSON only."
  }'
```

## Why This Matters

The same model that powers the excellent Grok Build TUI is available at very attractive pricing ($1/M in, $2/M out) for anyone building custom agentic systems, IDE integrations, or specialized harnesses.

This arsenal provides the skills, MCP patterns, and prompt discipline that make the raw model dramatically more effective.

**Maintained by Cobus Greyling.**

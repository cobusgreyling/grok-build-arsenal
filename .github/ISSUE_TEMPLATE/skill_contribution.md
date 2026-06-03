---
name: New Skill Proposal / Contribution
about: Propose or contribute a new high-quality, reusable skill for the arsenal.
title: '[Skill] Short name: one-sentence purpose'
labels: enhancement, skill
assignees: ''
---

**Skill Name**
Proposed kebab-case name (e.g. `refactor-safely`)

**Description (for frontmatter)**
One or two sentences explaining exactly when Grok should auto-invoke this skill.

**Problem it solves**
Why is this useful for grok-build-0.1 users?

**Key features the skill should include**
- Plan Mode guidance?
- Subagent patterns?
- Specific verification steps?
- Integration with certain MCPs?

**Proposed trigger phrases**
List good natural language triggers.

**Example usage prompt**
A realistic prompt someone would type.

**Additional context**
Links to similar skills, references, or why it belongs in the core arsenal (vs user-local).

**Sole author / contribution note**
This repo's original skills and design are by Cobus Greyling. New skills contributed via PR are appreciated and will be credited in CHANGELOG / skill metadata where appropriate.

**Checklist for PR (if submitting code)**
- [ ] SKILL.md with excellent YAML frontmatter (name, description, version, author)
- [ ] Includes Plan Mode instructions and safety notes
- [ ] Tested with `grok` / `grok inspect`
- [ ] Follows patterns from existing skills (e.g. plan-mode-orchestrator)
- [ ] Added to README table if accepted

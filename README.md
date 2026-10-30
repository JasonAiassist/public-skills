# Public coding skills

Reusable instructions for AI coding agents, covering implementation standards and evidence-based code review.

| Skill | Purpose |
|---|---|
| [House coding rules](skills/house-coding-rules/SKILL.md) | Coding conventions, boundaries, error handling, security and testing, with references for 15 languages and configuration formats. |
| [Code audit](skills/code-audit/SKILL.md) | Assess coverage, test effectiveness, defects, missing implementation, cohesion and OWASP controls. Includes a reporting rubric and an 85% coverage warning threshold. |

## Use

Download or clone this repository, then copy the complete skill folders from `skills/` into the skill directory supported by your coding agent. Keep the supporting references and rubric alongside each `SKILL.md`.

For a repository using `.agents/skills/`, the resulting paths should be `.agents/skills/house-coding-rules/SKILL.md` and `.agents/skills/code-audit/SKILL.md`. Adopt the coding rules explicitly in your repository instructions. Agent-specific discovery and invocation support may vary.

Example requests:

- “Use house-coding-rules when implementing this change.”
- “Use code-audit to review this repository and save an evidence-based report.”

The skills complement each other. Coding rules guide implementation; code audit evaluates evidence. A passing coverage number does not establish correctness or security, and neither skill grants permission to install, deploy or publish.

## Source and licence

These skills were maintained in an AIS-OS workspace and exported for public reuse. This repository contains only the two skills and their supporting files, without personal workspace context or private repository history.

Published under the [MIT licence](LICENSE), retaining the source workspace's licence notice. The source workspace is based on [AIS-OS](https://github.com/nateherkai/AIS-OS). The licence's framework trademark notice is retained; that framework is not included here.

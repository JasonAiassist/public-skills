---
name: house-coding-rules
description: Apply before creating, changing, refactoring or testing project code, scripts, styles, markup or SQL. Load the reference for each language touched. Excludes prose-only knowledge edits.
---

# House coding rules

1. Read repository instructions, manifests and existing conventions before editing. Preserve established tooling; do not add dependencies or broadly reformat unrelated code without authorisation.
2. Load every applicable reference below before coding. For an unlisted language, first add a referenced language guide grounded in its canonical style, formatter/linter, error handling and testing idioms; mirror it with this skill.
3. Keep domain logic, presentation, transport and persistence separately testable. Use descriptive names, small cohesive functions and explicit boundaries. Format changed code for reading, not token compression.
4. Validate untrusted input at boundaries; enforce ownership where data is accessed. Encode output for its destination. Keep secrets out of source, fixtures and logs. Parameterise commands/queries; avoid dynamic execution.
5. Handle errors explicitly with actionable context, preserving causes without leaking secrets. Bound retries/timeouts, make repeatable side effects idempotent and clean up resources on success, failure and cancellation.
6. Implement only authorised requirements. Mark intentional simulations visibly; do not disguise missing behaviour behind successful dummy results. Preserve user data and compatibility; describe migrations and recovery before destructive changes.
7. Test observable behaviour, boundaries, failures and relevant security invariants. Add regression tests for fixes. Run repository-native checks; report commands, failures and untested paths. Follow the code-audit skill for audit gates: report unit line/statement and branch coverage separately, warn below 85%, identify unmeasured files, and sample test sensitivity safely.
8. Before handoff, review the diff for unrelated changes, record evidence and remaining gaps, and name changed outputs. Never claim a check passed unless it ran successfully.

## Language dispatch

| Files | Required reference |
|---|---|
| C# | [C#](references/csharp.md) |
| XML, MSBuild props/targets/project files | [XML](references/xml.md) |
| JS, JSX, CJS, MJS | [JavaScript](references/javascript.md) |
| QML | [QML](references/qml.md) |
| TS, TSX | [TypeScript](references/typescript.md) and JavaScript |
| Python | [Python](references/python.md) |
| Java | [Java](references/java.md) |
| Kotlin, Gradle Kotlin | [Kotlin](references/kotlin.md) |
| Shell scripts | [Shell](references/shell.md) |
| HTML | [HTML](references/html.md) |
| CSS | [CSS](references/css.md) |
| SQL | [SQL](references/sql.md) |
| YAML configuration | [YAML](references/yaml.md) |
| systemd unit and drop-in files | [systemd units](references/systemd.md) |
| GLSL shader files (.vert, .frag, .geom, .comp) | [GLSL](references/glsl.md) |

These rules do not grant execution, installation, publication or deployment permission. Higher-priority instructions win; document material project-specific exceptions. Workspace guidance requires this skill; other repositories must explicitly adopt it before claiming universal enforcement.

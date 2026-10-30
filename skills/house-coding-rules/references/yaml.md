# YAML configuration

Baseline: [YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/).
- Follow the repository's existing schema, indentation, quoting, and loader conventions.
- Use spaces for indentation and quote ambiguous scalar values. Keep executable loader tags only where the project explicitly supports them.
- Validate syntax and the effective merged configuration with the project's own loader before deployment.
- Keep secrets out of committed configuration; use the project's documented environment or credential references.

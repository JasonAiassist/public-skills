# Python
Baseline: [PEP 8](https://peps.python.org/pep-0008/), [PEP 257](https://peps.python.org/pep-0257/).
- Use snake_case functions/variables, PascalCase classes, four spaces and explicit imports. Follow configured Ruff/Black formatting; annotate public boundaries.
- Use pathlib and context managers for resources. Avoid mutable defaults and import-time I/O.
- Catch specific exceptions; chain with raise ... from ...; never silently swallow failures. Use subprocess argument lists without shell=True for variable commands.
- Keep logic independent of CLI/filesystem adapters. Use the project's pytest or unittest suite with temporary directories, deterministic fixtures, error/cleanup checks and coverage branch reporting.
- Run configured Ruff, type checker and formatter checks; do not install them without authorisation.

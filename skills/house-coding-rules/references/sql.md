# SQL
Baseline: chosen database documentation, e.g. [PostgreSQL](https://www.postgresql.org/docs/current/sql.html) or [SQLite](https://www.sqlite.org/lang.html). Record the dialect before changes.
- Use consistent snake_case identifiers and explicit column lists. Parameterise values; allowlist dynamic identifiers.
- Enforce required invariants through keys, uniqueness, nullability and checks. Apply tenant/ownership predicates consistently.
- Use transactions for atomic changes; define retry behaviour for contention without duplicating external effects.
- Version migrations with backup/recovery implications; do not assume all DDL is transactional. Avoid destructive migrations without authorisation.
- Test constraints, rollback, concurrency and migrations against the actual dialect. Inspect query plans for performance-sensitive queries; run the project's SQL lint checks.

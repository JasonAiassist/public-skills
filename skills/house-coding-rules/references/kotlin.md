# Kotlin
Baseline: [Kotlin coding conventions](https://kotlinlang.org/docs/coding-conventions.html), existing ktlint/detekt configuration.
- Prefer val, explicit nullability and sealed/data types for state. Avoid !! and casts that bypass validation.
- Use structured concurrency with lifecycle-owned scopes; propagate cancellation, avoid GlobalScope and do not block the UI dispatcher.
- Keep platform adapters outside domain logic. Close resources with use; preserve error causes; do not turn exceptions into silent nulls.
- Use project Kotlin/JUnit tests, coroutine virtual time where available, and instrumentation for UI/lifecycle contracts. Report coverage separately.
- Run configured formatter, detekt and Android lint; do not change Gradle/toolchain versions incidentally.

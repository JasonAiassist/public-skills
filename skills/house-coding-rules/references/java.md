# Java
Baseline: [Google Java Style](https://google.github.io/styleguide/javaguide.html), existing Gradle/Maven and formatter settings.
- Use PascalCase types, camelCase members, explicit visibility and immutable values where practical. Keep UI, domain and persistence responsibilities distinct.
- Validate external values; use enums/sealed states rather than magic strings where supported. Avoid unchecked casts and nullable contracts with unclear ownership.
- Use try-with-resources; preserve exception causes, catch narrowly and do not ignore interrupted status. Never block Android's main thread.
- Use repository JUnit tests and JaCoCo reports; distinguish JVM tests from Android instrumentation. Cover lifecycle, cancellation, persistence failure and duplicate events.
- Run configured Checkstyle/google-java-format and Android lint where applicable; honour the project's Java language level.

# C#
Baseline: [Microsoft C# coding conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) and the repository's `.editorconfig`.
- Use PascalCase for types and public members, camelCase for parameters and locals, and the repository's established private-field convention. Name asynchronous methods with an `Async` suffix.
- Enable and respect nullable reference analysis where the project supports it. Validate inputs at public and I/O boundaries; use typed exceptions with useful context and do not leak secrets.
- Use `async`/`await` for I/O, pass `CancellationToken` through cancellable work, and dispose streams, database connections and other owned resources with `using` or `await using`.
- Keep domain models separate from transport and UI. Prefer explicit immutable data for cross-boundary messages; preserve existing serialization formats and protocol compatibility.
- Use the repository's test framework for observable behavior, failure paths and cancellation. Build and test with the pinned SDK; use `dotnet format --verify-no-changes` only where the project already supports its formatting conventions.

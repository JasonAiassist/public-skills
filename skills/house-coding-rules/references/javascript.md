# JavaScript
Baseline: [MDN JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), repository ESLint/Prettier configuration.
- Use const by default, let for reassignment, strict equality, explicit return shapes and descriptive camelCase names. Prefer one statement per line; use the established module format.
- Separate deterministic transformations from DOM/I/O. Avoid global mutable state except a clearly bounded composition root.
- Throw Error objects, not strings; use stable codes for caller decisions. Await promises; catch only where recovery or context is added; release listeners, timers and handles.
- Render user text through textContent or context-correct escaping. Avoid eval and user-built HTML/URLs.
- Use the existing runner (Node test, Vitest or Jest); test errors, asynchronous ordering, duplicate events and cleanup. Test browser interactions in the real browser, separately from unit coverage.
- Run configured lint/format checks; do not introduce a new formatter solely for a small change.

# TypeScript
Baseline: [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html), project tsconfig and typescript-eslint.
- Apply JavaScript rules. Prefer strict checking; do not silently weaken compiler options.
- Use unknown at untrusted boundaries, narrow via validation, and model state transitions with discriminated unions. Avoid any, non-null assertions and casts that conceal invalid data.
- Define public contracts explicitly. Prefer readonly data where mutation is not required; avoid duplicating derived types.
- Return typed outcomes for expected failures; preserve Error causes for exceptional failures.
- Run project typecheck and behavioural tests; compile success is not behavioural evidence. Cover runtime validation and impossible-state rejection.

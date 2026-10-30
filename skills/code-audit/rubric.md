# Code-audit rubric

Use this minimum evidence standard.

| Gate | Pass | Fail | Unknown |
|---|---|---|---|
| Unit-test coverage | Measured production-code line/statement coverage is at least 85%; branch coverage is reported | Measured line/statement coverage is below 85%, or exclusions materially misrepresent it | No trustworthy coverage report |
| Test effectiveness | Sampled critical tests assert observable behavior and can detect controlled faults or mutations | Material tests only compile/import/smoke, assert tautologies, or cannot detect broken behavior | Tests cannot safely be inspected or exercised |
| Broken code | No confirmed defect in the exercised scope | At least one reproducible defect or failed required gate | Important paths were not executable |
| Missing/stub code | No required missing implementation found in inspected scope | Required behavior is stubbed, skipped, or absent | Contract or intended behavior is unclear |
| Cohesion | Inspected files have clear related responsibilities or explicit composition roles | Confirmed unrelated concerns share a file without a justified boundary | Architecture/sample is insufficient |
| Security | Applicable OWASP controls have evidence and no confirmed material weakness | Confirmed weakness or missing required mitigation | Important trust boundaries or deployment evidence unavailable |

## Severity

- **Critical:** practical compromise, destructive loss, broad unauthorized access, or secret exposure requiring immediate action.
- **High:** exploitable or user-impacting defect in an important path; major missing control.
- **Medium:** meaningful reliability, test, design, or defense-in-depth weakness.
- **Low:** limited impact, localized maintainability issue, or hardening opportunity.

## Coverage cautions

Report the metric exactly as produced. Do not average unrelated packages to hide weak components. Call out files or packages under 85% when the aggregate passes but risk is concentrated. Generated/vendor exclusions are acceptable only when identified. Test code must not inflate production coverage.

## Test-effectiveness sampling

Prioritize authentication/authorization, persistence, money or irreversible actions, external inputs, concurrency, parsers, error handling, and core domain behavior. Record how many tests and modules were manually inspected. Mutation testing is preferred where an existing safe runner is available; otherwise use reasoned assertion analysis and explicitly label the limitation.

## Security evidence

Separate source-code controls, tests, configuration, dependency metadata, and runtime/deployment evidence. A mitigation documented but not exercised is **documented, unverified**. A scanner clean result is not a security pass by itself.

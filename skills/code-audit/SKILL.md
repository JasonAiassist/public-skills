---
name: code-audit
description: Use when someone asks to audit, review, assess, or quality-check a codebase for unit-test coverage and effectiveness, broken or missing implementation, stubs, cohesion and file responsibilities, or OWASP-aligned security controls. Produces an evidence-based report and warns when measured unit-test coverage is below 85%.
---

# Code Audit

## Contents

- [Operating rules](#operating-rules)
- [1. Establish a trustworthy test baseline](#1-establish-a-trustworthy-test-baseline)
- [2. Verify that tests exercise functionality](#2-verify-that-tests-exercise-functionality)
- [3. Find broken code](#3-find-broken-code)
- [4. Find missing code and stubs](#4-find-missing-code-and-stubs)
- [5. Assess cohesion and file responsibility](#5-assess-cohesion-and-file-responsibility)
- [6. Review security and OWASP mitigations](#6-review-security-and-owasp-mitigations)
- [7. Report](#7-report)


Audit a codebase for demonstrable correctness, completeness, maintainability, and security. Report evidence, not impressions. Do not edit production code unless the user separately asks for remediation.

## Operating rules

- Read applicable `AGENTS.md`, `CLAUDE.md`, repository documentation, manifests, test configuration, CI configuration, and security policy before assessing the code.
- Establish the repository root, languages, frameworks, executable entry points, generated/vendor exclusions, and the commands CI actually runs.
- Prefer repository-native tools. Never install dependencies, access external services, run destructive commands, expose secrets, or execute untrusted fixtures without explicit authorization.
- Treat passing compilation, typechecking, linting, snapshots, or import tests as supporting evidence—not proof that behavior works.
- Mark each finding **confirmed**, **probable**, or **unverified**. Include file and line references, reproduction commands, observed output, impact, and a concrete remediation.
- Distinguish defects from intentional placeholders, abstract interfaces, examples, tests, generated code, and platform-specific branches.
- State audit scope and gaps. Do not claim exhaustive security assurance or absence of defects.
- Save completed reports as `audits/YYYY-MM-DD-code-audit.md` unless the user requests another location or no file write.

Read [rubric.md](rubric.md) before auditing.

## 1. Establish a trustworthy test baseline

1. Discover the test runner and coverage configuration from repository files; do not invent commands.
2. Run the narrowest safe baseline checks first, then the full unit-test suite when practical.
3. Generate a machine-readable coverage report if supported.
4. Measure unit-test statement/line coverage and branch coverage separately. Prefer coverage scoped to production code, excluding generated, vendor, fixtures, migrations, and test files only when the repository configuration justifies those exclusions.
5. Emit a prominent warning when measured line or statement coverage is **below 85%**. Also report branch coverage; do not disguise weak branches behind an aggregate percentage.
6. If coverage cannot be measured, report **coverage unknown**, not zero and not passing.
7. Identify untested production files, high-risk uncovered branches, and misleading exclusions.

Coverage is a signal, not evidence that assertions validate behavior.

## 2. Verify that tests exercise functionality

Sample tests across critical paths, changed code, boundary conditions, error paths, and security-sensitive behavior. Inspect what each selected test proves.

Flag tests that only:

- compile, import, instantiate, render without assertions, or assert that no exception occurred;
- assert constants, mocks, implementation details, or tautologies;
- mock the system under test so thoroughly that real behavior never runs;
- use snapshots without meaningful semantic assertions;
- cannot fail when the production behavior is deliberately perturbed.

Where safe and supported, validate test sensitivity with mutation testing or a controlled temporary fault that is fully reverted. Never leave mutations in the working tree. Report sampled scope and mutation score separately from coverage. A high coverage number does not pass this section when tests cannot detect broken behavior.

## 3. Find broken code

Use multiple forms of evidence:

- failing tests, typechecks, builds, linters, or runtime smoke tests;
- invalid imports, unresolved symbols, unreachable paths, inconsistent API contracts, broken error handling, and impossible state assumptions;
- incorrect async/resource lifecycle, unchecked return values, race conditions, platform/path errors, and dependency/API version drift;
- reproducible behavior that contradicts tests, docs, types, schemas, or callers.

Reproduce suspected defects when safe. Do not label dormant, optional, or platform-specific code broken without confirming its contract.

## 4. Find missing code and stubs

Search for explicit and implicit incompleteness:

- `TODO`, `FIXME`, `XXX`, `HACK`, `NotImplemented`, placeholder exceptions, `pass`, empty bodies, dummy returns, hard-coded sample data, disabled tests, skipped branches, and commented-out implementation;
- declared interfaces, routes, commands, configuration options, migrations, handlers, or documented features with no implementation;
- callers that expect behavior a callee does not supply;
- tests that are skipped or marked pending around required behavior.

Classify each candidate as required missing implementation, intentional extension point, deferred work, or false positive, with evidence.

## 5. Assess cohesion and file responsibility

Identify files that combine unrelated functions, features, classes, or architectural layers. Use semantic responsibility—not file length alone.

Flag a file when independently changing one concern is likely to affect unrelated concerns, or when it mixes areas such as transport, domain logic, persistence, UI, configuration, and process control without a clear coordinating role. Consider naming, imports, call graph, ownership, test boundaries, and reasons to change.

Do not penalize cohesive modules, small closely related helpers, schema/type collections, explicit composition roots, or generated files merely for containing multiple declarations. Recommend a proposed module boundary and dependency direction for each confirmed cohesion problem.

## 6. Review security and OWASP mitigations

Record the OWASP Top 10 edition used. Trace applicable risks through entry points, trust boundaries, sensitive data, authorization decisions, dependencies, and deployment configuration. At minimum inspect:

- access control and object/tenant ownership enforcement;
- authentication, session, token, password, and recovery handling;
- input validation and injection defenses for SQL, shell, templates, paths, URLs, headers, and deserialization;
- output encoding and browser controls where applicable;
- cryptography, secret storage, transport protection, and sensitive-data logging;
- secure defaults, error handling, debug/admin surfaces, CORS/CSRF, headers, file permissions, and exposed services;
- dependency pinning, provenance, update policy, CI integrity, and unsafe install/build scripts;
- threat modeling and insecure design risks;
- integrity checks for software, data, updates, and serialization;
- security logging, alerting, auditability, and exceptional-condition handling.

Map findings to an applicable OWASP category, but do not force irrelevant categories. Automated scanners are supporting evidence only. Never claim OWASP compliance solely because no scanner finding appeared.

## 7. Report

Lead with an executive outcome and ordered findings. Include:

1. scope, revision, environment, exclusions, and commands run;
2. quality gate table;
3. coverage results with the 85% threshold;
4. test-effectiveness evidence and sampling limits;
5. broken-code and missing/stub findings;
6. cohesion findings;
7. OWASP control matrix and security findings;
8. prioritized remediation: Critical, High, Medium, Low;
9. uncertainties and untested areas.

A gate passes only with evidence. Use **Fail**, **Pass**, or **Unknown**—never convert unknown into pass.

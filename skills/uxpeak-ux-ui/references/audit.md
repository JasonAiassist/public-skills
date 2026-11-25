# Interface evaluation

## Evidence and scope

Identify the task and user before judging the screen. Inspect the supplied interface at the states and viewport sizes relevant to that task. Label evidence **observed**, **inferred** or **unknown**. A screenshot supports findings about visible hierarchy and copy; it cannot establish keyboard behavior, responsiveness, latency or successful task completion.

Trace entry → decision → action → feedback → next step, including cancellation and recovery. For a multi-screen flow, inspect continuity of selections, data and navigation. When runtime access is unavailable, deliver a bounded visual review and a verification plan rather than invented results.

## Review dimensions

| Dimension | Questions |
|---|---|
| Information and hierarchy | Can users find what they need to make the next decision? Is essential information hidden? Does emphasis match task importance? |
| Navigation | Are destinations distinguishable from actions? Are location, back behavior and selected state clear? Does navigation remain predictable? |
| Inputs and choices | Does the control fit frequency and precision? Are units, constraints, defaults and validation understandable? Can unusual but valid input be entered? |
| Feedback and recovery | Are loading, empty, failed, pending and completed states distinguishable? Can users retry, correct, undo or leave safely? |
| Visual system | Are typography, spacing, colors, components and density coherent? Does imagery explain the product rather than compete with it? |
| Accessibility and inputs | Can applicable tasks be completed by keyboard and touch? Are labels, focus, contrast, state cues and alternatives to motion/dragging adequate? |
| Responsive behavior | Do content and actions survive narrow widths, long text, zoom, virtual keyboards and safe-area constraints? |
| Trust and commitment | Are total cost, recurring obligations, consent and reversibility explicit? Are social proof and scarcity substantiated? |

Use [patterns](patterns.md) for channel-derived heuristics and [delivery](delivery.md) for supplemental implementation checks. A heuristic is a prompt to investigate, not an automatic failure.

## Findings that lead to action

Use a compact table when useful:

`Location/state | Evidence | User consequence | Priority/confidence | Proposed change | Acceptance check`

Prioritize by impact, frequency, reach and recoverability:

- **Critical:** blocks an essential task or creates serious, difficult-to-reverse harm.
- **High:** prevents a common task, misleads a consequential decision or excludes an important input method.
- **Medium:** creates meaningful but recoverable confusion or extra work.
- **Low:** minor inconsistency or polish with limited task impact.

Keep confidence separate from severity. Unknown behavior is not a pass. Avoid arbitrary overall scores; if requested, define the rubric, evidence scope and weighting first. Separate genuine problems from stylistic preferences.

Example acceptance check: “At a narrow viewport with the keyboard open, the user can correct the invalid quantity and reach the purchase action without losing their selection.” This is more useful than “improve mobile UX.”

## Validation and experiments

For usability testing, choose representative tasks, relevant participants and neutral prompts. Observe completion, errors, hesitation and recovery; do not lead people toward the proposed design. Use the lowest fidelity that can answer the question. A prototype may answer comprehension questions while a working build is needed for performance or assistive-technology behavior.

For a proposed experiment, state the hypothesis, primary outcome, guardrails and decision rule. Account for mistaken purchases, cancellations and support burden as well as conversion. Do not import the channel's claimed uplift as an expected result. If no study ran, label the result a heuristic review or a proposed test.

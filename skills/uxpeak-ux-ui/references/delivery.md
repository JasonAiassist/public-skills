# Design and implementation

Contents: brief and flow; system and screens; working implementation; accessibility; verification. This is a delivery workflow combining the channel's principles with supplemental engineering and accessibility practices. See V08, V13, V14 and V21 in [sources](sources.md).

## Brief and flow

Capture the user's task, intended outcome, audience, constraints and known evidence. Mark inferred audience characteristics as assumptions. Research questions should resolve actual decisions rather than serve as a ritual. Use existing analytics, support issues and user research where available; do not invent them.

Map the primary path and meaningful alternatives before polishing screens. Include entry, selection, validation, commitment, result, back/cancel and recovery where relevant. Use low-fidelity sketches for structure and realistic interactive prototypes for questions that depend on behavior. Higher fidelity is not inherently better research.

## System and screens

Define a small coherent set of semantic colors, typography roles, spacing, surfaces, borders and interaction states. Reuse components for buttons, fields, navigation, cards and feedback. Derive variants from real needs, not a speculative catalog.

Start with realistic content and explain hierarchy. Specify responsive behavior rather than handing off a single fixed desktop frame: what wraps, resizes, reorders, collapses, scrolls or stays fixed? Check long labels, localization, large text, empty values and dense data. Preserve task-critical information at narrow widths.

For design-only work, deliver the flow, representative screens and behavior specifications needed to build them. Identify unresolved decisions rather than presenting decorative mockups as complete functionality.

## Working implementation

Inspect the repository and existing design system first. Use the requested framework and established components. Separate presentation, state and data access where it makes behavior understandable; avoid unnecessary architecture for small tasks.

Prefer semantic HTML or native controls and labels over custom replicas. Implement actual actions, validation, loading, failure and recovery behavior. If a backend is unavailable, clearly identify mock data and simulated actions. Guard against repeated submission and stale asynchronous responses when applicable. Keep useful input after recoverable failures.

Handle touch and keyboard, not hover alone. A virtual keyboard must not strand the active field or action. Give drag interactions an appropriate non-drag alternative. Account for fixed navigation, overlays, safe areas and scroll containers. Test the last item in clipped/scrolling content.

Performance is part of the experience. Use proportionate images and fonts, avoid blocking core tasks with decorative assets, and measure actual behavior before claiming speed improvements. A static fallback must preserve the task when optional 3D or animation is unavailable.

## Accessibility: supplemental checks

Consult the current [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/) for applicable web criteria. Check meaningful text alternatives, labels and instructions, keyboard operation, visible focus, contrast, non-color state cues, error identification, readable reflow and accessible status feedback. Evaluate target size and alternatives to dragging against the actual criterion and its exceptions. Respect reduced-motion preferences. Automated checks alone do not establish conformance.

For native applications, verify relevant requirements in [Apple's accessibility guidance](https://developer.apple.com/design/human-interface-guidelines/accessibility) or [Material interaction guidance](https://m3.material.io/foundations/interaction/gestures). These are verification pointers; their dynamic pages were not fully readable during this skill's source review. Never claim a platform guideline was verified without inspecting it.

Do not treat a tutorial's pixel value as a universal accessibility rule. Distinguish CSS pixels, physical pixels, points and dp. Where numeric thresholds matter, look up and cite the applicable current standard instead of combining incompatible conventions. Report accessibility checks performed, not unsupported certification.

## Verification and handoff

Use representative narrow and wide viewports, and actual device/input testing when available. Exercise:

- A primary task to its meaningful result, not just the first click.
- A plausible failure or invalid input and the recovery path.
- Back/cancel and preservation of relevant selections.
- Relevant keyboard focus, touch operation and reduced-motion behavior.
- Long/empty content, overflow and fixed-element collisions.

Inspect rendered screens, including states changed by interactions. Capture evidence where useful and deliver the actual runnable artifact or design file. State what was tested, what remains simulated and what requires real users or target devices. Do not describe build success as user validation.

For a small requested change, narrow these checks to the affected behavior. For a substantial flow, provide a compact acceptance checklist a reviewer can repeat.

# Task-focused patterns

Contents: hierarchy and information; inputs; search and filters; navigation; onboarding and commerce; feedback and personalization. Source IDs resolve in [sources](sources.md). Guardrails are this skill's critical synthesis, not claims that the channel endorsed them.

## Hierarchy and information — V01, V07, V12, V13

Make the primary decision legible: meaningful values and product details should not be visually subordinate to decorative labels. Use scale, weight, grouping, spacing and restrained color together. Keep related information close, and separate distinct decisions.

Show information people need to compare choices. Progressive disclosure helps when it removes secondary detail without concealing cost, consequences or necessary comparisons. Test whether hidden controls cause extra taps or memory demands. V01 supports this at description level only.

Use realistic content early: long names, empty values, multiple products and localized prices expose weak layouts. Product imagery should reveal what people receive or how they use it. Background overlays and shadows are optional techniques; readability and contrast decide whether they help.

## Inputs — V07, V09, V11

Choose controls using frequency, precision, range and discoverability:

- Frequent exact quantities: text entry or steppers may outperform a slider. Expose units and valid limits.
- Approximate bounded exploration: a slider can make a range understandable; retain an accessible precise alternative when needed.
- Small meaningful option sets: visible choices or cards can reduce recall, provided they do not create excessive scrolling.
- Open-ended categories: offer common choices plus a custom path rather than forcing incorrect data.

For money transfers or other consequential actions, make the amount, unit/currency, parties and consequences clear before confirmation. A novel control or more animation does not make a design more senior. Preserve valid input when validation fails.

## Search and filters — V01, V07

Avoid an unexplained blank search surface. Relevant recents, popular queries or examples can help, subject to privacy and relevance. Support no results, clearing, retry and loading states. Keep suggestions distinguishable from committed queries.

Expose active filters, a clear reset and the effect on results. Preserve selections when navigating back. For expensive queries, use an explicit apply step when useful; for cheap immediate filtering, live feedback may be preferable. Make any delayed or stale result state visible. These implementation details extend the channel's decision-focused principles; they are not verified specifics from V01's unavailable transcript.

## Navigation — V08, V11, V21, V22

For a mobile bottom bar, select a small set of frequent top-level destinations. Three to five is a starting heuristic, not a universal limit. Move infrequent settings, legal information and logout to appropriate secondary locations. Do not mix destinations and a prominent creation action without clear semantics.

Use understandable labels and consistent icons. Show selection through more than color alone, and retain readable inactive items. Badges should communicate actionable information without manufacturing urgency. Keep location predictable across personalized states.

Respect actual device safe areas and keyboard behavior. Avoid copying a tutorial's device-specific inset, label size or demonstration hitbox. Touch dimensions in native points/dp are not interchangeable with CSS pixels. Verify current platform guidance for the target device. Browser apps may need different navigation on wide screens; choose breakpoints around content needs.

## Onboarding and commerce — V02, V03, V04, V05

Let users understand value before demanding registration where the product allows it. Preserve work through sign-in. Represent genuinely completed steps as progress; never fabricate progress or threaten loss to force completion.

Use helpful defaults for reversible choices. Keep subscription enrollment, meaningful consent and optional charges explicit. Trial designs should explain when access begins, when billing starts, what it costs and how cancellation works. Promise reminders only when the product sends them.

Product pages should connect imagery, variants, quantity, reviews, delivery and price with the purchase decision. Keep a sticky action from obscuring content or errors. For bookings, clarify dates, duration, total cost and cancellation conditions. Retain price ranges or estimate labels when the underlying amount is uncertain.

Use authentic reviews, supported product claims and real inventory/activity. Compare prices on a consistent basis; do not portray a monthly charge as a tiny fraction of a one-time purchase while hiding the recurring cost. Show a credible discount baseline. Do not preselect a paid subscription merely because the channel example did.

V02's detailed treatment is based on its description, not a full transcript. V03–V05 contain conversion-oriented suggestions that this skill deliberately rejects where they mislead or pressure users.

## Feedback and personalization — V07, V11

Empty states should explain why no content exists and offer an appropriate action the application actually supports. Error messages should identify what happened and the available recovery path. Tracking screens should surface useful status, time windows, destination and contact options without pretending uncertain estimates are exact.

Adapt content to observed needs or explicit preferences while preserving navigational stability and user control. Familiar, legitimate visual cues can aid recognition; random decoration cannot substitute for clear names. Avoid inferring sensitive characteristics or ability from demographic assumptions.

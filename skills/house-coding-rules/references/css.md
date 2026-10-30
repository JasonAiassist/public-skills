# CSS
Baseline: [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), project Stylelint/formatter conventions.
- Use shared custom properties for colours, spacing and typography. Scope component rules; avoid specificity escalation and unexplained !important.
- Preserve readable contrast, visible focus and usable targets in light/dark themes. Respect reduced motion and zoom; do not communicate status by colour alone.
- Prefer flexible layouts and content-driven sizing. Test narrow screens, long text, overflow and 200% zoom rather than fixing only a screenshot.
- Keep styles separate from state/business logic. Run configured lint and browser visual/interaction checks; document viewport/theme evidence.

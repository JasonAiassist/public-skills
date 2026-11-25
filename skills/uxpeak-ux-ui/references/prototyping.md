# Figma, motion and visual storytelling

Source IDs refer to [sources](sources.md). These lessons describe techniques, not requirements to use Figma or a particular vendor.

## Reusable structure — V13, V17, V20

Use shared styles/tokens and components with meaningful names. Auto layout and constraints should express how content adapts. Use realistic text and assets before finalizing spacing. Preserve layer identity across related states where animation depends on matching layers.

Batch editing, reusable image fills, calculations and property copying can improve consistency. Verify present-day tool controls rather than prescribing historical shortcuts. Do not duplicate components solely to make a demonstration easier when a reusable variant would serve production better.

AI-generated assets can explore a coherent visual direction, but require appropriate rights, consistent framing and review for misleading details. Do not render essential interface text inside raster imagery or present generated product details as factual. Upscaling does not recover missing truth.

## Scroll, state and motion — V18, V19, V21, V22

Define each state and the transition between them. Distinguish a selected destination, an action in progress and a completed action. A navigation prototype should support every relevant destination and return transition, not just the showcased forward path.

Smart Animate can interpolate matched properties between frames. Rotation, position and color can create the impression of 3D without a real 3D scene. Test both directions, repeated clicks and interrupted transitions; matching only the showcase sequence can conceal broken behavior.

Scrolling requires content larger than its viewport, a defined viewport and the right overflow/clip behavior. Check horizontal and vertical regions separately. Fixed navigation must not obscure the final item or action. Provide alternatives when horizontal content is hard to discover or operate.

Tutorial durations around 600–1000 ms demonstrate effects; they are not recommended defaults for frequent navigation. Shorten or remove motion when it delays the task. Honor reduced-motion preferences and preserve information in the static state. Do not inherit V22's small demonstration hitbox as a production target.

## 3D and expressive websites — V06, V10, V15, V16, V23

Choose expressive motion when it clarifies a product, tells a relevant story or serves a justified brand experience. A visually impressive portfolio does not prove a booking or checkout flow usable. Assess performance, distraction, reading order, input compatibility and motion sensitivity.

For imported designs and 3D assets, check alignment, camera framing, responsive constraints and loading behavior. Import/export does not guarantee a production-ready responsive page. Keep essential content and actions available without the effect. Test target hardware rather than assuming the designer's machine represents visitors.

V16 discusses historical trends, including a 2023 context; do not label them current trends without fresh evidence. V06 was reviewed only through metadata/description and V23 through visual samples, so neither supports claims about exact implementation steps or usability outcomes.

## Prototype handoff

Document the purpose of the prototype, tested states, intended motion behavior and omitted production concerns. Distinguish simulated interactions from implemented data flows. Include a static/reduced-motion specification where animation carries meaning. Verify the final prototype through the same paths a reviewer will use.

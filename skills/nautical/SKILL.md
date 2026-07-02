---
name: nautical
description: Dithered nautical interface system for maritime products, fishing tools, coastal commerce, and ocean-facing dashboards.
license: MIT
metadata:
  author: typeui.sh
---

<!-- TYPEUI_SH_MANAGED_START -->
# nautical Design System Skill (Universal)

## Mission
You are an expert design-system guideline author for nautical.
Create practical, implementation-ready guidance that can be directly used by engineers and designers.

## Brand
Nautical blends crisp maritime utility with dithered coastal texture: deep water blues, sailcloth surfaces, brass accents, tide-chart rhythm, and high-contrast oceanic illustration patterns. It should make interfaces feel seaworthy and precise without changing what the product does.

## Style Foundations
- Visual style: maritime, dithered, utilitarian, calm
- Typography scale: 14/16/18/24/32/40 | Fonts: primary=Open Sans, display=Space Grotesk, mono=IBM Plex Mono | weights=400, 500, 600, 700, 800
- Color palette: primary, secondary, neutral, success, warning, danger, surface, text | Tokens: primary=#063B5B, secondary=#0F6B7A, accent=#D8A24A, success=#16825D, warning=#B86E16, danger=#B42318, surface=#F7F3E8, text=#102A36, neutral=#FFFFFF
- Spacing scale: 4/8/12/16/24/32
- Texture rule: dithered dots, wave hatching, chart-grid lines, and rope-like dividers are allowed only as supporting surfaces, never as text backgrounds below AA contrast.

## Interaction Preservation
- Preserve every existing route, form submission, link target, button action, keyboard shortcut, tracking hook, and API call.
- Retheme labels, surfaces, icon choices, spacing, and state styling without changing component names, event handlers, disabled logic, validation behavior, or loading behavior.
- When a nautical treatment conflicts with established behavior, keep the behavior and simplify the visual treatment.

## Accessibility
WCAG 2.2 AA, keyboard-first interactions, visible focus states, reduced-motion support, and non-color cues for status.

## Writing Tone
clear, concise, practical, lightly maritime when it helps meaning

## Rules: Do
- use deep-water primary surfaces with sailcloth or foam surfaces for content areas
- keep dithered patterns subtle and bounded to decorative bands, empty states, cards, and illustrations
- use brass accents for primary calls to action, selection rings, and important numeric highlights
- preserve visual hierarchy with type weight, spacing, and contrast before using texture
- keep interaction states explicit: hover, focus-visible, active, disabled, loading, success, warning, error
- design for empty/loading/error states with concise copy and stable layout
- ensure responsive behavior by default, especially for dense dashboards and mobile toolbars

## Rules: Don't
- do not replace working controls with decorative nautical props
- do not put dithered texture behind body text, form inputs, or small buttons
- do not use novelty labels when direct labels are clearer
- do not rely on blue alone for selection, safety, or error status
- do not reduce hit areas below 44px on touch targets
- do not introduce decorative motion that delays task completion

## Expected Behavior
- Follow the foundations first, then component consistency.
- When uncertain, prioritize accessibility and functional preservation over nautical novelty.
- Provide concrete defaults and explain trade-offs when alternatives are possible.
- Keep guidance opinionated, concise, and implementation-focused.

## Guideline Authoring Workflow
1. Restate the design intent in one sentence before proposing rules.
2. Define tokens, texture constraints, and behavioral preservation requirements before component-level guidance.
3. Specify component anatomy, states, variants, and interaction behavior.
4. Include accessibility acceptance criteria and content-writing expectations.
5. Add anti-patterns and migration notes for existing inconsistent UI.
6. End with a QA checklist that can be executed in code review.

## Required Output Structure
When generating design-system guidance, use this structure:
- Context and goals
- Design tokens and foundations
- Component-level rules (anatomy, variants, states, responsive behavior)
- Accessibility requirements and testable acceptance criteria
- Content and tone standards with examples
- Anti-patterns and prohibited implementations
- Migration notes for preserving existing behavior
- QA checklist

## Component Rule Expectations
- Define required states: default, hover, focus-visible, active, disabled, loading, error (as relevant).
- Describe interaction behavior for keyboard, pointer, and touch.
- State spacing, typography, color-token usage, and texture rules explicitly.
- Include responsive behavior and edge cases (long labels, empty states, overflow).
- Confirm that event handlers, route destinations, form behavior, and button actions stay unchanged unless a product requirement explicitly says otherwise.

## Quality Gates
- No rule should depend on ambiguous adjectives alone; anchor each rule to a token, threshold, or example.
- Every accessibility statement must be testable in implementation.
- Prefer system consistency over one-off local optimizations.
- Flag conflicts between aesthetics and accessibility, then prioritize accessibility.
- Treat broken button behavior, changed form semantics, or lost keyboard operation as release blockers.

## Example Constraint Language
- Use "must" for non-negotiable rules and "should" for recommendations.
- Pair every do-rule with at least one concrete don't-example.
- If introducing a new pattern, include migration guidance for existing components.

<!-- TYPEUI_SH_MANAGED_END -->

---
name: global-design
description: Portable design operating system for AI-assisted product work. Use for landing pages, SaaS apps, admin panels, dashboards, forms, design systems, and frontend handoff specs.
license: MIT
metadata:
  author: Staurus
---

<!-- TYPEUI_SH_MANAGED_START -->
# Global Design Skill (Universal)

## Mission
You are an expert design-system and frontend handoff guide for AI-assisted product work.
Create implementation-ready UI direction that reduces generic output and makes design decisions explicit.

## Brand
Global Design Skill is a portable design operating system for AI coding agents.
It prioritizes clear hierarchy, explicit states, accessible interaction, reusable tokens, and developer handoff clarity.

## Style Foundations
- Visual style: structured, product-focused, editorial-tech, high-clarity
- Typography scale: mobile-first, compact, with strong hierarchy
- Color palette: semantic tokens over raw values, OKLCH preferred
- Spacing scale: 4px grid, calm density, consistent rhythm
- Component families: marketing sections, product UI, admin UI, forms, navigation, tables, cards
- Motion: purposeful transitions only, never decorative by default

## Accessibility
WCAG 2.2 AA, keyboard-first interactions, visible focus states, semantic HTML, and testable ARIA where needed.

## Writing Tone
Concise, direct, implementation-focused, and specific.
Avoid generic "make it nicer" language.

## Rules: Do
- define user, goal, layout, states, and handoff before visual polish
- specify responsive behavior for mobile, tablet, and desktop
- require loading, empty, error, disabled, and success states where relevant
- prefer design tokens and reusable patterns
- include acceptance criteria for developers

## Rules: Don't
- do not rely on vague adjectives alone
- do not omit accessibility or keyboard behavior
- do not ship one-state-only components
- do not hide edge cases
- do not overuse effects, gradients, or novelty for its own sake

## Quality Gates
- Every recommendation must be concrete enough to implement
- Every interactive component must define states and behavior
- Every layout must name its breakpoints and hierarchy
- Every handoff must be understandable without clarification
- Every accessibility statement must be testable

## Expected Output Structure
When generating guidance, use this order:
1. Context and goal
2. Layout and hierarchy
3. Tokens and foundations
4. Component rules and states
5. Responsive behavior
6. Accessibility requirements
7. Developer handoff notes
8. QA checklist

## Example Constraint Language
- Use "must" for non-negotiable rules and "should" for recommendations
- Pair every do-rule with at least one concrete don't-example
- If introducing a new pattern, include migration guidance for existing components
- Keep the result opinionated, but not theatrical

## Anti-Patterns
- generic centered hero with vague CTA
- cards without states
- forms without labels, errors, or focus handling
- dashboards with decorative density instead of useful density
- motion that adds noise instead of comprehension

<!-- TYPEUI_SH_MANAGED_END -->

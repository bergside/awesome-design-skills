---
name: Nautical
colors:
  primary: "#063B5B"
  secondary: "#0F6B7A"
  accent: "#D8A24A"
  success: "#16825D"
  warning: "#B86E16"
  danger: "#B42318"
  surface: "#F7F3E8"
  text: "#102A36"
  neutral: "#FFFFFF"
typography:
  h1:
    fontFamily: "Space Grotesk"
    fontSize: 2.5rem
  body-md:
    fontFamily: "Open Sans"
    fontSize: 1rem
  label-caps:
    fontFamily: "IBM Plex Mono"
    fontSize: 0.875rem
  sourceScale: "14/16/18/24/32/40"
  weights: "400, 500, 600, 700, 800"
rounded:
  sm: 4px
  md: 8px
spacing:
  sm: 4px
  md: 8px
  sourceScale: "4/8/12/16/24/32"
---

## Overview

Dithered nautical interface system for maritime products, fishing tools, coastal commerce, and ocean-facing dashboards.

## Style Foundations

- **Visual style:** maritime, dithered, utilitarian, calm
- **Typography scale:** 14/16/18/24/32/40
- **Typography fonts:** primary=Open Sans, display=Space Grotesk, mono=IBM Plex Mono
- **Typography weights:** 400, 500, 600, 700, 800
- **Color palette:** primary, secondary, accent, neutral, success, warning, danger, surface, text
- **Spacing scale:** 4/8/12/16/24/32
- **Texture system:** dithered dots, wave hatching, chart-grid lines, and rope-like dividers

## Colors

- **Primary (#063B5B):** Deep harbor blue for navigation, headers, and major surfaces.
- **Secondary (#0F6B7A):** Teal waterline accent for secondary controls and data highlights.
- **Accent (#D8A24A):** Brass highlight for primary calls to action, selection, and key metrics.
- **Success (#16825D):** Navigational green for successful states and confirmed actions.
- **Warning (#B86E16):** Buoy orange for warnings and reversible risk.
- **Danger (#B42318):** Signal red for destructive or blocking errors.
- **Surface (#F7F3E8):** Sailcloth base for content and form surfaces.
- **Text (#102A36):** Ink-blue foreground for readable text on light surfaces.
- **Neutral (#FFFFFF):** Foam white for inset cards, menus, and raised controls.

## UI/UX Direction

Use nautical style as a visual language, not as a replacement for product behavior. Existing routes, form submissions, button handlers, validation flows, loading states, and disabled logic must remain intact. Retheme components with token changes, spacing refinements, icon updates, and dithered support surfaces.

## Component Guidance

- **Buttons:** Primary buttons use brass fill with ink-blue text; secondary buttons use sailcloth fill with harbor-blue border. Keep existing click handlers, submit types, disabled states, and loading states unchanged.
- **Navigation:** Use deep harbor surfaces, clear active indicators, and chart-line separators. Do not rename destinations unless product copy explicitly changes.
- **Cards and panels:** Prefer sailcloth or foam surfaces with 1px blue-gray borders. Add dithered corner shading only when it does not compete with data.
- **Forms:** Inputs stay plain and legible. Use strong focus rings, clear error messages, and avoid texture inside input fields.
- **Tables and dashboards:** Use compact spacing, sticky headers when useful, and teal/brass highlights for active filters or key values. Preserve sorting, filtering, pagination, and row actions.
- **Empty states:** Use small dithered nautical illustrations or chart-grid backgrounds with direct next-action copy.

## Accessibility

- Text and controls must meet WCAG 2.2 AA contrast.
- Focus-visible rings must be at least 2px and visible on both sailcloth and harbor surfaces.
- Status cannot be communicated by color alone; pair status colors with text, icons, or shape.
- Touch targets must be at least 44px in either dimension.
- Dithered patterns must not reduce text readability or pointer target clarity.

## Content Tone

Use clear product language first. Maritime terms are acceptable when they clarify orientation or state, such as "current route", "trip log", "harbor", "signal", or "bearing". Avoid novelty copy that hides the action, such as replacing "Save" with "Anchor it".

## Anti-Patterns

- Replacing working controls with decorative wheels, ropes, anchors, or map props.
- Applying dithered texture behind body copy, form fields, or dense table cells.
- Making the interface a single blue palette with no warm accent or neutral relief.
- Changing button behavior, form submission semantics, routes, or keyboard operation during a visual retheme.

## QA Checklist

- All existing buttons, links, forms, and shortcuts still trigger the same actions.
- Primary, secondary, disabled, loading, hover, active, focus-visible, success, warning, and error states are visually distinct.
- Dithered pattern usage is decorative, bounded, and never behind small text.
- Mobile layouts preserve hit targets and do not clip labels.
- Color contrast passes WCAG 2.2 AA for text and interactive states.

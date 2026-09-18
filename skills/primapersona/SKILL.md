---
name: primapersona
description: Swiss-editorial portfolio design. A strict four-column grid, monochrome neutrals with one reserved green accent, small utilitarian labels, hairline rules instead of cards, and true light/dark mode. Use when building personal sites, portfolios, CVs and typographic index pages that should feel restrained and precise.
license: MIT
metadata:
  author: Lexington Themes
  source: https://lexingtonthemes.com/templates/primapersona
  demo: https://lexingtonthemes.com/viewports/primapersona
---

# Prima Persona design system

Prima Persona is a one-page portfolio for a creative technologist or designer
with a Swiss-editorial feel: a strict 4-column grid, monochrome colour, small
utilitarian labels, hairline rules between entries, and real light/dark mode.
The page is essentially a typographic index. Rows of year / title /
description / category, separated by 1px lines. Anything you add must be
indistinguishable from what is already there.

This skill is written from a shipped theme, not generated from a
questionnaire. Every rule below is what the theme actually does.

## Mission

Produce UI that reads as one continuous editorial document: hierarchy through
position and weight rather than size, colour used almost nowhere, no boxes.
When in doubt, remove the decoration and let the grid do the work.

## Design personality

- Editorial and restrained. Content sits directly on the page background.
- Monochrome by default. The neutral scale does everything; the green accent
  appears only on hover and on an explicit button.
- Hierarchy through position and weight, not size. Section headings are
  smaller than the row titles beneath them.
- Dark mode is a first-class citizen driven by `prefers-color-scheme`; every
  colour has a dark twin.

## Style foundations

### Typography

One typeface: **Inter**. No serif, no mono, no second sans, no extra
OpenType feature settings.

Use the low end of the scale. The theme never shouts.

| Role | Size (mobile to desktop) | Weight and tracking |
| --- | --- | --- |
| Hero title (h1) | 30px, 36px from `md`, 48px from `lg`; `leading-snug` | semibold, `tracking-tighter` |
| Section heading (h2) | 18px, 20px from `sm`, 24px from `md`; `leading-snug` | semibold, `tracking-tighter` |
| Row title (h3), image rows | 24px, 30px from `sm`; `leading-tight` | semibold |
| Row title (h3), text rows | 16px, 18px from `sm`, 20px from `md`; `leading-tight` | semibold |
| Body and descriptions | 14px | regular |
| Meta labels (years, categories) | 12px, uppercase | regular, `tracking-tight` |
| Nav and footer links | 12px | regular, `tracking-tight` |

Rules:

- Headings are `font-semibold` with `tracking-tighter`. Never `font-bold`.
- No `text-balance`, no `max-w-*` clamps on headings. The grid column
  controls line length.
- Section eyebrow labels are two short lines (for example "Featured Work" /
  "2026 - Now").

### Colour

Two scales only, both defined in oklch. No default framework palettes, no hex
values in markup.

`base` is a pure gray (chroma 0):

| Step | oklch | approx hex |
| --- | --- | --- |
| 50 | `oklch(0.985 0 0)` | #FBFBFB |
| 100 | `oklch(0.970 0 0)` | #F5F5F5 |
| 200 | `oklch(0.922 0 0)` | #E5E5E5 |
| 300 | `oklch(0.870 0 0)` | #D4D4D4 |
| 400 | `oklch(0.708 0 0)` | #A3A3A3 |
| 500 | `oklch(0.556 0 0)` | #737373 |
| 600 | `oklch(0.439 0 0)` | #525252 |
| 700 | `oklch(0.371 0 0)` | #404040 |
| 800 | `oklch(0.269 0 0)` | #262626 |
| 900 | `oklch(0.205 0 0)` | #171717 |
| 950 | `oklch(0.145 0 0)` | #0A0A0A |

`accent` is a vivid green (hue 135):

| Step | oklch | approx hex |
| --- | --- | --- |
| 500 | `oklch(0.744 0.209 135)` | #6CC71C |
| 600 | `oklch(0.628 0.180 135.7)` | #519F11 |

(The full accent ramp runs 50 to 950 along the same hue; 500 and 600 are the
only steps the page uses.)

Usage, light / dark:

- Page background: `white` / `base-950`, set once on `body`.
- Headings and emphasised text: `base-900` / `white`.
- Body and meta text: `base-600` / `base-300`.
- Hairline rules: `base-200` / `base-800`.
- Default button: `base-800` fill with white text. Muted button: `base-100`.
- `accent` is reserved for `hover:text-accent-600` on links and for the
  accent button variant. Never on surfaces, headings, or section
  backgrounds.
- No tinted panels, no gradients, no coloured section backgrounds.

### Spacing and layout

- One page container: full width, `max-w-[90rem]` from 1536px up, `px-8`.
- Section vertical padding `py-12 lg:py-24`. The hero uses a large top pad
  (`pt-40 lg:pt-80`) because the nav is fixed. Nav and footer use `py-2`.
- Every section gets an `id` and `scroll-mt-32` so the fixed nav's anchor
  links land cleanly.
- **Everything sits on the same grid**: `grid grid-cols-1 lg:grid-cols-4
  items-start gap-4`. Signature placements:
  - Hero h1: `lg:col-span-2 lg:col-start-3` (the right half).
  - Section header: eyebrow label at `lg:col-start-2`, then the h2 spanning
    `lg:col-span-2`.
  - List row: col 1 year, col 2 title, col 3 description, col 4 category
    right-aligned (`lg:ml-auto lg:col-start-4`).
- Lists are `flex flex-col gap-12 mt-8`. Each entry is an `article` with
  `py-12 border-t` in the hairline colour. The top border is the only
  separator.
- Images run the full column width: `aspect-4/2 rounded-4xl object-cover`,
  with explicit width and height and lazy loading.

### Corners, borders, shadows

- Radius is binary: `rounded-4xl` (2rem) on large images, `rounded-full` on
  buttons. Nothing else is rounded. There are no cards to round.
- Borders are 1px `border-t` hairlines used as row separators, never as
  boxes or rings around content.
- Zero shadows. Not one `shadow-*` in the theme.

## Component families

- **Text**: one component owns the type scale (`display6XL` down to
  `displayXS`, `textXL` down to `textXS`). Headings go through it; never
  hand-size a heading.
- **Button**: pill (`rounded-full` baked in). Variants `default`
  (base-800), `accent` (accent-500), `muted` (base-100), `none`. Sizes
  `xxs` to `xl` with fixed heights (1.875rem to 3.25rem). Renders an anchor
  when given `href`. Icon-only buttons are square. Note that the landing page
  itself uses no buttons: real CTAs are plain 12px anchors, or an sr-only
  link wrapping a `size-4` arrow icon. Match that restraint.
- **Wrapper**: the single page-width container described above.
- **Logo**: a plain text span (for example `alessandro.p`) at 12px,
  `tracking-tight`.
- **Icons**: individual components in one stroke style (the theme ships only
  `ArrowRight` and `Plus`). Add new ones in the same style rather than
  importing an icon pack. Icon links pair an sr-only label with the icon.

## Accessibility

- Every colour utility has a `dark:` twin following the pairs above, so
  contrast holds in both schemes (body text base-600 on white and base-300
  on base-950 both clear WCAG AA).
- Icon-only links and buttons always carry an sr-only text label.
- Sections have ids; anchor navigation works with keyboard and screen
  readers.
- Focus states are visible; do not remove outlines.
- Images have explicit dimensions and alt text.

## Writing tone

Terse, declarative, systems-minded. Fragments over sentences ("Code. Design.
Strategy. Digital products with intent."). Constraint vocabulary
("trade-offs", "failure modes", "under real-world pressure"). Meta labels are
Title Case in source and uppercased by CSS. No exclamation marks, no emoji, no
marketing superlatives.

## Rules: Do

- Copy an existing row's structure (image row or text row) before inventing
  a new layout.
- Keep every new block on the `lg:grid-cols-4` grid and pick placements from
  the signature set above.
- Pair every colour utility with its `dark:` twin.
- Give new sections an `id` and `scroll-mt-32`.
- Use the `Text` and `Button` components (or their equivalents) rather than
  raw tags with ad-hoc sizes.

## Rules: Don't

- Don't add cards, panels, tinted backgrounds, gradients, or shadows.
- Don't use `accent` for anything but hover states or an explicit button.
- Don't round anything except large images (`rounded-4xl`); buttons handle
  their own `rounded-full`.
- Don't use default `gray`/`slate`/`zinc` classes; the neutral scale is
  `base-*`.
- Don't reach for big display sizes. Section headings top out at 24px and
  the hero at 48px.
- Don't introduce a second typeface.

## Quality gates

1. Fonts, colours and spacing all come from the tokens above and match a
   sibling section.
2. Layout holds on the 4-column grid and collapses to one column below `lg`.
3. Every colour class has a `dark:` counterpart; check both schemes.
4. Headings use the type scale; any buttons use the button variants.
5. No new dependencies, no unused imports, minimal diff.

## About this skill

Prima Persona is a free Astro and Tailwind CSS theme by
[Lexington Themes](https://lexingtonthemes.com/templates/primapersona).
This file is the same design skill that ships inside the theme. The finished
sections it describes are served to coding agents over
[Lexington MCP](https://lexingtonthemes.com/mcp), where Prima Persona is the
free tier.

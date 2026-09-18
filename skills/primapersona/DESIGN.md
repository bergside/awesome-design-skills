---
name: Prima Persona
colors:
  primary: "#171717"
  secondary: "#525252"
  accent: "#6CC71C"
  accent-hover: "#519F11"
  surface: "#FFFFFF"
  surface-dark: "#0A0A0A"
  text: "#171717"
  text-muted: "#525252"
  border: "#E5E5E5"
  border-dark: "#262626"
  neutral: "#F5F5F5"
typography:
  h1:
    fontFamily: "Inter"
    fontSize: 3rem
    fontWeight: 600
    letterSpacing: -0.05em
  h2:
    fontFamily: "Inter"
    fontSize: 1.5rem
    fontWeight: 600
    letterSpacing: -0.05em
  h3:
    fontFamily: "Inter"
    fontSize: 1.875rem
    fontWeight: 600
  body-md:
    fontFamily: "Inter"
    fontSize: 0.875rem
  label-caps:
    fontFamily: "Inter"
    fontSize: 0.75rem
    textTransform: uppercase
  sourceScale: "low end of a display/text scale; hierarchy by weight and position"
  weights: "400, 600"
rounded:
  image: 2rem
  button: 9999px
spacing:
  section: "3rem mobile, 6rem desktop"
  row: "3rem"
  grid-gap: "1rem"
  sourceScale: "Tailwind 4/8/12/16/24/32/48"
---

## Overview

Prima Persona is a one-page portfolio for a creative technologist or designer.
Swiss-editorial: a strict four-column grid, monochrome neutrals, one green
accent that almost never appears, small uppercase labels, and hairline rules
between entries instead of cards. It ships with real light and dark mode.

Live demo: [primapersona-astro.pages.dev](https://primapersona-astro.pages.dev)

## Design intent

The page is a typographic index. Each entry is a row: year, title,
description, category. Rows are separated by a 1px line and nothing else.
The reader scans down a column, not across a grid of boxes.

Three decisions carry the whole look:

1. **Hierarchy through position and weight, not size.** Section headings are
   smaller than the row titles beneath them. What matters is where a thing
   sits on the grid and whether it is semibold, not how big it is.
2. **Colour is reserved.** The landing page is pure gray. The green accent
   exists only as a link hover and an optional button variant. If you find
   yourself painting a surface green, stop.
3. **No containers.** No cards, panels, tinted backgrounds, gradients or
   shadows. Content sits directly on the page. The only borders are top
   hairlines on rows.

## Style foundations

- **Typeface:** Inter, and only Inter.
- **Weights:** 400 for text and labels, 600 for every heading. No bold.
- **Tracking:** `tracking-tighter` on headings, `tracking-tight` on 12px
  text.
- **Colour scales:** a pure-gray `base` scale (oklch, chroma 0, 50 to 950)
  and a vivid green `accent` scale (oklch hue 135).
- **Grid:** `grid-cols-1 lg:grid-cols-4`, `gap-4`, `items-start`. Every
  section, including the hero, sits on it.
- **Container:** full width, capped at 90rem from 1536px, `px-8`.
- **Section rhythm:** `py-12 lg:py-24`. Rows inside lists are `py-12` with a
  top hairline and `gap-12` between them.

## Colours

| Token | Light | Dark | Used for |
| --- | --- | --- | --- |
| Page | white | base-950 `#0A0A0A` | body background, set once |
| Heading | base-900 `#171717` | white | h1, h2, h3, emphasised text |
| Body | base-600 `#525252` | base-300 `#D4D4D4` | descriptions, meta labels |
| Rule | base-200 `#E5E5E5` | base-800 `#262626` | 1px row separators |
| Button | base-800 `#262626` | base-800 | default pill button |
| Accent | accent-600 `#519F11` on hover, accent-500 `#6CC71C` on buttons | same | link hover, accent button only |

Dark mode follows `prefers-color-scheme`. Every colour utility is written
with its `dark:` twin; there is no class toggle to forget.

## Typography

| Role | Mobile to desktop | Notes |
| --- | --- | --- |
| Hero h1 | 30px, 36px at `md`, 48px at `lg` | semibold, `leading-snug`, sits in the right half of the grid |
| Section h2 | 18px, 20px at `sm`, 24px at `md` | semibold, spans two columns |
| Row h3, image rows | 24px, 30px at `sm` | semibold, `leading-tight` |
| Row h3, text rows | 16px, 18px at `sm`, 20px at `md` | semibold |
| Body | 14px | descriptions, eyebrow labels |
| Meta | 12px, uppercase | years, categories |
| Nav, footer | 12px | plain anchors, `tracking-tight` |

Headings never get `max-w-*` or `text-balance`; the grid column measures the
line.

## Layout signatures

- **Hero:** h1 at `lg:col-span-2 lg:col-start-3`. The left half is empty on
  purpose.
- **Section header:** eyebrow label (two short lines) at `lg:col-start-2`,
  then the h2 spanning `lg:col-span-2`.
- **List row:** year in column 1, title in column 2, description in column
  3, category right-aligned in column 4.
- **Images:** full column width, `aspect-4/2`, `rounded-4xl`, `object-cover`.

## Components

- **Text:** one component owns the type scale. Headings go through it.
- **Button:** a pill. Variants default (base-800), accent (accent-500), muted
  (base-100), none. Fixed heights from 1.875rem to 3.25rem. The landing page
  itself uses none; its calls to action are 12px anchors or an arrow icon
  with an sr-only label.
- **Icons:** hand-drawn stroke icons, one per file. The theme ships only
  `ArrowRight` and `Plus`.

## Corners, borders, shadows

- Radius: `rounded-4xl` on large images, `rounded-full` on buttons. Nothing
  else.
- Borders: 1px top hairlines on rows. Never boxes, never rings.
- Shadows: none anywhere.

## Voice

Terse, declarative, systems-minded. "Code. Design. Strategy. Digital
products with intent." Constraint vocabulary over hype. No exclamation marks,
no emoji, no superlatives.

## Implementation notes

- Give every section an `id` and `scroll-mt-32`; the fixed nav links to
  them.
- New rows should copy an existing row's markup rather than invent a layout.
- When porting to another stack, keep the two oklch scales as CSS variables
  and map the semantic pairs in the colour table to them. Everything else is
  spacing and weight.

## Source

Prima Persona is a free Astro and Tailwind CSS theme by
[Lexington Themes](https://lexingtonthemes.com/templates/primapersona).
This design file and its companion skill ship inside the theme. The finished
sections are also served to coding agents through
[Lexington MCP](https://lexingtonthemes.com/mcp), where Prima Persona is the
free tier.

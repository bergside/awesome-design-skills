---
name: cronduit
description: Pure black × neon cyan system-monitor aesthetic. Dark-only, IBM Plex Mono-first, glow-not-shadow. Built for solo-operator storefronts and data dashboards.
license: MIT
metadata:
  author: Cronduit / AyeThoHaney
---

<!-- TYPEUI_SH_MANAGED_START -->
# Cronduit Design System Skill (Universal)

## Mission
You are an expert design-system guideline author for the Cronduit design system.
Create practical, implementation-ready guidance that engineers can drop directly into HTML/CSS, Liquid, or React. Every decision reinforces a single signal: precision, speed, and transparency — the aesthetic of a system monitor at 2 AM. Pure black backgrounds. Neon cyan accents. Monospace headers. Glow effects that feel earned, not decorative.

## Brand
Solo-operator, direct-sale aesthetic. The brand communicates that one person built something real, fast, with exact tools and exact numbers. No vague benefit statements. No decorative gradients. No light mode. Products are priced precisely. Build receipts are specific. The visual language borrows from order-book trading terminals and dark-mode IDEs: ultra-dense layouts, hairline borders, mono numerics, and a single brand-cyan accent driving every interactive element.

## Style Foundations
- **Visual style:** dark-only system-monitor. No light mode. No near-blacks — use `#000000` for page backgrounds, `#060A1A` for card/panel surfaces only.
- **Typography scale:** 9/11/12/13/14/16/20/24/32/40/56 | Fonts: display=IBM Plex Mono, body=IBM Plex Sans, mono=IBM Plex Mono | weights=400, 500, 600, 700
- **Color palette:** accent=`#00D9FF`, secondary=`#FF6B00`, success=`#00FF88`, muted=`#5A6370`, dim=`#8A95A5`, foreground=`#FFFFFF`, background=`#000000`, panel=`#060A1A`, surface=`#0A0E1F`
- **Glow tokens:**
  - `glow-1`: `0 0 10px rgba(0,217,255,0.4)`
  - `glow-2`: `0 0 22px rgba(0,217,255,0.55), 0 0 44px rgba(0,217,255,0.2)`
  - `glow-soft`: `0 0 32px rgba(0,217,255,0.12)`
  - `glow-orange`: `0 0 12px rgba(255,107,0,0.4)`
- **Spacing scale:** 4/8/12/16/20/24/32/40/48/56/64/96
- **Border radius:** 2–4px. No value above 4px except pill-shaped tags/badges (999px). Rounded corners above 4px are prohibited in all other contexts.

## Accessibility
WCAG 2.2 AA. `#00D9FF` on `#000000` passes at large text — always verify contrast at body text sizes with a checker. All interactive elements must have visible `box-shadow` focus states using the cyan glow token. Never suppress glow focus rings on dark backgrounds.

## Writing Tone
First-person, specific numbers, transparent about constraints. Direct. No hedging. Forbidden words: "revolutionary," "disrupting," "game-changing," "innovative," "cutting-edge." Prices always exact ($149, $99, $499 — never "~$100"). Build claims always specific ("2,117 leads," "5 days," "$149 entry").

## Rules: Do
- Use `#000000` pure black for all page backgrounds
- Use `#060A1A` for card/panel fill — never a random dark hex
- Apply IBM Plex Mono to all headers, navigation, labels, prices, stat numbers, CTA button text, tags, and eyebrows
- Apply IBM Plex Sans to all body copy and long-form text
- Replace all `box-shadow` elevation with glow: `box-shadow: 0 0 22px rgba(0,217,255,0.55), 0 0 44px rgba(0,217,255,0.2)`
- Use `letter-spacing: 2–4px` + `text-transform: uppercase` on all IBM Plex Mono labels and eyebrows
- Use `border-left: 2px solid #00D9FF` as the active/selected state indicator on cards and list items
- Use L-shaped corner bracket pseudo-elements (`::before`/`::after`) to decorate featured cards — top-left and bottom-right cyan corners
- Use scan-line animations (1px cyan gradient line keyframed top→100%) on product cards to signal live data
- Use `radial-gradient(ellipse ... rgba(0,217,255,0.06))` on `body::before` for ambient background bloom
- Sticky nav: `background: rgba(0,0,0,0.65); backdrop-filter: blur(20px); border-bottom: 1px solid rgba(0,217,255,0.08)`
- Primary CTA: `background: #00D9FF; color: #000; font-family: IBM Plex Mono; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; box-shadow: 0 0 32px rgba(0,217,255,0.45)`
- Secondary CTA: `border: 1px solid rgba(0,217,255,0.35); background: rgba(0,217,255,0.03); color: #00D9FF`
- Tag/eyebrow: `font-family: IBM Plex Mono; font-size: 9px; letter-spacing: 3px; text-transform: uppercase; color: #00D9FF; padding: 3px 8px; border: 1px solid rgba(0,217,255,0.3); background: rgba(0,217,255,0.04)`
- Stat numbers (prices, counts): IBM Plex Mono bold ≥18px + `glow-1`; use IntersectionObserver count-up animation on scroll entry
- Featured product cards: `border: 1px solid rgba(0,217,255,0.18)` + corner brackets + scan-line animation + pulsing green live dot

## Rules: Don't
- Never use light mode or any background lighter than `#060A1A`
- Never use color gradients for decoration — radial bloom and scan-line animations only
- Never use `border-radius` above 4px except approved pill badges
- Never use standard `box-shadow` for elevation — cyan glow only
- Never use font families other than IBM Plex Mono and IBM Plex Sans in UI chrome
- Never use `#FF6B00` orange as a primary action color — it is reserved for secondary lane differentiation
- Never write forbidden words: "revolutionary," "disrupting," "game-changing," "innovative"
- Never approximate prices — always exact numeric values
- Never add gradient color fills to text (gradient text effect) — all text is solid
- Never use white text on surfaces lighter than `#030609`

## Expected Behavior
- Default to `#000000` background + `#00D9FF` accent when in doubt
- Use `glow-1` on stat numbers and prices; `glow-2` on hovered interactive cards
- Keep copy receipt-style: first-person, specific numbers, no vague benefit claims
- Product cards always include: uppercase mono SKU tag, pulsing live indicator, price in IBM Plex Mono bold, corner bracket decoration
- Navigation always includes: CRONDUIT wordmark in IBM Plex Mono 700 + sticky blur + right-side cyan CTA button

## Guideline Authoring Workflow
1. Confirm pure-black background constraint before anything else
2. Map required colors to defined palette tokens — no new color introductions
3. Confirm IBM Plex Mono on all headers, labels, and stat numbers
4. Assign glow tokens (glow-1, glow-2, glow-soft) instead of arbitrary rgba shadows
5. Verify no border-radius exceeds 4px outside approved pill badges
6. Define card anatomy with corner brackets, scan-line animation, and pulsing live dot
7. QA checklist: black background ✓ cyan primary ✓ no light mode ✓ IBM Plex Mono on all labels ✓

## Required Output Structure
- Context and design intent (one sentence)
- Design tokens in use (colors, typography, glow)
- Component anatomy (HTML structure + CSS class names)
- Interaction states: default, hover (`translateY(-3px)` + glow-2), active (`border-left: 2px solid #00D9FF`), focus (cyan glow ring), disabled (opacity 0.4)
- Copy rules (tone, forbidden words, number format)
- Anti-patterns specific to this component
- QA checklist (background check, font check, glow check, radius check)

## Component Rule Expectations
- Cards: default → hover (`translateY(-3–4px)` + glow-2) → active (left cyan border) → disabled (opacity 0.4)
- Navigation: sticky, blur(20px), 1px cyan bottom border, IBM Plex Mono wordmark, right CTA
- Stat numbers: IBM Plex Mono bold, glow-1, IntersectionObserver count-up
- Product cards: L-corner brackets, scan-line animation, pulsing green live dot, SKU uppercase mono
- CTA buttons: IBM Plex Mono bold uppercase, 2px letter-spacing, glow box-shadow, translateY(-2px) on hover
- Section eyebrows: 9px IBM Plex Mono uppercase, 3px letter-spacing, cyan tag style
- Prices: IBM Plex Mono bold, cyan, glow-1, ≥18px in card context

## Quality Gates
- Background must be `#000000` — fail if any container uses a non-approved dark value
- All stat numbers and prices must use IBM Plex Mono bold with glow-1
- No border-radius above 4px (pill badges at 999px are exempt)
- Card hover must use glow, not standard box-shadow
- No color gradients except radial bloom and scan-line animations
- Copy regex check: `/revolutionary|disrupting|game.changing|innovative|cutting.edge/i` must return 0 matches

## Example Constraint Language
- "must" = non-negotiable canon rule (e.g., `background: #000000`, IBM Plex Mono on labels)
- "should" = strong recommendation with edge-case exceptions
- Every color rule anchored to an exact hex value — no ambiguous adjectives
- Every spacing rule anchored to the 4pt scale (4/8/12/16/24/32...)

<!-- TYPEUI_SH_MANAGED_END -->

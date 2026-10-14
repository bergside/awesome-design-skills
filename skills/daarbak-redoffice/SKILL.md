# Daarbak Redoffice Design Skill

> Danish B2B brand system for Daarbak Redoffice — advisory-led office
> supply and facility solutions. Warm, trustworthy, distinctly Nordic.
> "Et 100% danskejet valg."

## Mission

Generate interfaces that feel like a trusted Danish business partner:
calm, competent, and human. Daarbak Redoffice sells advice as much as
products ("Rådgivning. Kontorforsyning. Helhedsløsning."). UI should
prioritize clarity, generous whitespace, and quiet confidence over flash.
Never sterile, never loud — approachable professionalism.

## Brand

- **Group:** Daarbak. Divisions: Daarbak Redoffice, Daarbak Design,
  Daarbak Bop Recycle, Daarbak Plant.
- **This system targets the Redoffice division.**
- **Group tagline:** Rådgivning. Ansvarlighed. Helhedsløsning.
- **Redoffice tagline:** Rådgivning. Kontorforsyning. Helhedsløsning.
- **Suffix / signature:** Et 100% danskejet valg.
- **Logo lockup:** DAARBAK REDOFFICE — "DAARBAK" set bold, "REDOFFICE"
  set regular weight, same size, uppercase.
- **Signature detail:** A full stop after each word in headlines and
  taglines is a deliberate brand element (e.g. "Rådgivning. Helhed.").
  Use it in display headlines, never in body copy.

## Style Foundations

### Color palette
| Token | Hex | Role |
|---|---|---|
| `--color-primary` | `#D5494B` | Redoffice brand red — accents; preserve official value |
| `--color-action` | `#CE4447` | Accessibility variant — primary controls with white text |
| `--color-navy` | `#1E2B41` | Design navy — headings, dark UI, footers |
| `--color-gray` | `#5F5A57` | Daarbak warm gray — body text, borders |
| `--color-green` | `#618769` | Bop Recycle green — success, sustainability |
| `--color-forest` | `#465A45` | Plant dark green — secondary accent |
| `--color-surface` | `#EFEAE4` | Beige — page background, cards |
| `--color-white` | `#FFFFFF` | Surfaces, inverted text |

Default page background is beige `#EFEAE4`, not pure white — this warmth
is core to the brand. Red is used sparingly as an accent, not a fill for
large areas.

`--color-action` is a UI contrast variant, not an official brand color.
Keep `--color-primary` unchanged for brand assets and decorative accents.
Do not use the action variant to recolor logos.

### Typography
- **Office surfaces (docs, email, slides):** Calibri.
- **Web / digital:** Sofia Pro (primary); use Poppins only when Sofia Pro
  cannot be used in the target environment.
- **Print / design:** Sofia Pro.
- For web UI, default to **Sofia Pro**. Load the available, licensed font
  faces with their actual family names and weights. If unavailable or not
  permitted for the delivery, use Poppins and document the substitution.
  System sans is a technical last resort, not a brand font. Do not claim
  Sofia Pro is rendered based on a CSS family name alone; verify loading
  and actual rendering. Do not publish proprietary font files in this repo.
- Type scale (web): 12 / 14 / 16 (base) / 20 / 24 / 32 / 44.
- Headings: navy `#1E2B41`, semibold, tight leading.
- Body: warm gray `#5F5A57`, 16px, 1.6 line-height.

### Spacing & radius
- Spacing scale (px): 4, 8, 12, 16, 24, 32, 48, 64.
- Border radius: 8px default, 12px for cards, 999px for pills/buttons.
- Generous padding inside cards (24–32px). Let content breathe.

### Elevation
- Soft, low shadows only: `0 2px 8px rgba(30,43,65,0.08)`.
- No harsh borders; use 1px `#5F5A57` at 15% opacity when needed.

## Component Families

- **Buttons:** Primary = action red `#CE4447` fill, white text, pill radius.
  Use these opaque colors for default, hover, active, and focus states;
  do not lighten the fill or reduce opacity on enabled controls.
  Secondary = navy outline on beige. Ghost = navy text, no border.
  Min height 44px, 16–24px horizontal padding. Apply the same action
  pairing to CTA links styled as buttons, submit controls, and selected
  toggles/chips with white labels. Use navy, underlined text for inline
  links on white/beige; do not use action red for small text on beige.
- **Inputs:** White surface, 1px gray border, 8px radius, navy focus
  ring. Labels in navy, helper text in gray. 44px min height.
- **Cards:** White or beige surface, 12px radius, soft shadow, 24–32px
  padding. Optional 4px red top-accent bar for emphasis.
- **Navigation:** Navy bar, white logo lockup left, links using the chosen
  web font (Sofia Pro first, documented Poppins alternative) with white text.
  Active link underlined in red.
- **Modals:** Beige surface, navy heading with brand full-stop, action-red
  primary action bottom-right using the same button colors and states.
- **Tables/data:** Common for B2B (orders, pricing, spend). Navy header
  row, alternating beige/white rows, right-aligned numerics, gray rules.

## Accessibility Rules

- Target WCAG 2.2 AA: text ≥4.5:1 (large text ≥3:1); required control
  boundaries, state indicators, and meaningful icons ≥3:1 against adjacent
  colors. Compare unrounded ratios using actual rendered colors, including
  opacity, overlays, and every enabled state.
- White on brand red `#D5494B` is only 4.29989:1: never use this pairing
  for ordinary button labels. White on action red `#CE4447` is 4.62331:1.
- Use navy `#1E2B41` for ordinary text/inline links on beige `#EFEAE4`.
  Neither brand red nor action red passes 4.5:1 on beige. Green `#618769`
  also fails with small white text; use navy text on a light surface with
  green as an icon/accent, rather than inventing another variant.
- Keyboard-first: logical tab order; visible 2px navy focus outline with 2px offset on
  white/beige surfaces. On navy surfaces use a white outline. Keep the
  outline visible and unclipped; never suppress it without a replacement.
- Disabled controls are exempt from contrast minima; never use disabled
  styling for enabled, loading, or selected controls.
- All interactive targets ≥44×44px.
- Don't rely on color alone — pair the recycle green with an icon/label.

## Writing Tone

- Language: **Danish by default** for customer-facing UI copy.
- Warm but professional; direct, concise, no filler. Advisory, not salesy.
- Use the brand full-stop cadence in headlines: short, declarative.
- Microcopy is helpful and human, never corporate-stiff.
- Sign-off / brand line: "Et 100% danskejet valg."

## Do / Don't

**Do**
- Use beige `#EFEAE4` as the default canvas.
- Reserve red for accents and primary actions.
- Apply the full-stop styling in display headlines.
- Keep layouts spacious, calm, and content-led.
- Use navy for structure and hierarchy.

**Don't**
- Don't flood large areas with red — it's an accent, not a background.
- Don't put red text on beige (fails contrast).
- Don't mix in unrelated bright colors outside the palette.
- Don't use the full-stop element in body paragraphs.
- Don't make it loud, trendy, or gimmicky — quiet confidence wins.

## Quality Gates

- [ ] Page background defaults to beige `#EFEAE4`, not white.
- [ ] Red used only for accents/primary actions, never as large fill.
- [ ] Headings navy, body warm gray, all text passes WCAG 2.2 AA.
- [ ] Web type uses Sofia Pro; Poppins is used only when Sofia Pro cannot
      be used, with the reason documented. Verify loaded faces, weights,
      and rendered Danish characters (æ/ø/å); report any technical fallback.
- [ ] Primary buttons/CTA links/selected controls use opaque action red
      `#CE4447` + white in default, hover, active, and focus states.
- [ ] Inline links on white/beige use navy text and a visible underline.
- [ ] Buttons ≥44px, pill radius, correct primary/secondary roles.
- [ ] Display headlines use the brand full-stop; body copy does not.
- [ ] Logo rendered as DAARBAK (bold) REDOFFICE (regular), uppercase.
- [ ] All interactive targets ≥44×44px with visible focus rings.
- [ ] Official brand tokens preserved; only the documented action contrast
      variant added, never substituted into logos.
- [ ] Run `python3 skills/daarbak-redoffice/scripts/check_contrast.py` from
      the repository root; reject failed token contrast checks.
- [ ] Check the generated UI's computed colors in every enabled state,
      including control boundaries/icons and focus outlines; the token
      check alone does not certify a rendered portal or dashboard.

### Contrast checks

Use this table as the machine-checked minimums for opaque default tokens.
The same primary pairing must apply to every enabled interaction state.

| Foreground token | Background token | Minimum ratio |
|---|---|---|
| `--color-white` | `--color-action` | 4.5 |
| `--color-navy` | `--color-white` | 4.5 |
| `--color-navy` | `--color-surface` | 4.5 |
| `--color-gray` | `--color-white` | 4.5 |
| `--color-gray` | `--color-surface` | 4.5 |
| `--color-action` | `--color-white` | 3 |
| `--color-action` | `--color-surface` | 3 |
| `--color-primary` | `--color-navy` | 3 |

For focus outlines use navy against white/beige and white against navy;
these pairs are covered above. The offset separates the outline from the
control fill. Test other surfaces separately.

WCAG references: [text contrast (1.4.3)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
and [non-text contrast (1.4.11)](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

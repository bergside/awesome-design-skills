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
| `--color-primary` | `#D5494B` | Redoffice red — primary action, accents |
| `--color-navy` | `#1E2B41` | Design navy — headings, dark UI, footers |
| `--color-gray` | `#5F5A57` | Daarbak warm gray — body text, borders |
| `--color-green` | `#618769` | Bop Recycle green — success, sustainability |
| `--color-forest` | `#465A45` | Plant dark green — secondary accent |
| `--color-surface` | `#EFEAE4` | Beige — page background, cards |
| `--color-white` | `#FFFFFF` | Surfaces, inverted text |

Default page background is beige `#EFEAE4`, not pure white — this warmth
is core to the brand. Red is used sparingly as an accent, not a fill for
large areas.

### Typography
- **Office surfaces (docs, email, slides):** Calibri.
- **Web / digital:** Poppins (primary web font).
- **Print / design:** Sofia Pro.
- For web UI, default to **Poppins**; fall back to system sans.
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

- **Buttons:** Primary = red `#D5494B` fill, white text, pill radius.
  Secondary = navy outline on beige. Ghost = navy text, no border.
  Min height 44px, 16–24px horizontal padding.
- **Inputs:** White surface, 1px gray border, 8px radius, navy focus
  ring. Labels in navy, helper text in gray. 44px min height.
- **Cards:** White or beige surface, 12px radius, soft shadow, 24–32px
  padding. Optional 4px red top-accent bar for emphasis.
- **Navigation:** Navy bar, white logo lockup left, Poppins links.
  Active link underlined in red.
- **Modals:** Beige surface, navy heading with brand full-stop, red
  primary action bottom-right.
- **Tables/data:** Common for B2B (orders, pricing, spend). Navy header
  row, alternating beige/white rows, right-aligned numerics, gray rules.

## Accessibility Rules

- Target WCAG 2.2 AA. Red `#D5494B` on white passes AA for large text
  and UI components, but for body-size text on red, use white and verify
  4.5:1. Never put red text on beige (insufficient contrast).
- Navy `#1E2B41` on beige `#EFEAE4` is the safe default text pairing.
- Keyboard-first: visible focus rings (2px navy), logical tab order.
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
- [ ] Web type uses Poppins (or documented fallback).
- [ ] Buttons ≥44px, pill radius, correct primary/secondary roles.
- [ ] Display headlines use the brand full-stop; body copy does not.
- [ ] Logo rendered as DAARBAK (bold) REDOFFICE (regular), uppercase.
- [ ] All interactive targets ≥44×44px with visible focus rings.
- [ ] No off-palette colors introduced.

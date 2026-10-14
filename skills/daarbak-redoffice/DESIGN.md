# Daarbak Redoffice — Design Overview

Daarbak Redoffice is the office-supply and facility division of the
Danish group Daarbak. The visual identity centers on a warm beige
canvas, a confident red accent, and a deep navy for structure —
projecting trust, Danish ownership, and advisory expertise rather than
discount-retail energy.

## Design Direction

Calm, spacious, B2B-professional. The system leans on warmth (beige
ground, warm gray text) to soften an otherwise corporate palette. Red
is precious — used only where attention is earned. The full-stop in
headlines ("Rådgivning. Kontorforsyning. Helhedsløsning.") is the
signature rhythmic device of the brand voice.

## Rationale & References

- Colors and fonts follow Daarbak Designmanual v1.0 (Dec 2025).
- Multi-division group: shared palette tokens let sibling divisions
  (Design, Bop Recycle, Plant) reuse the system while Redoffice owns red.
- Use Sofia Pro as the primary font for web/digital and print/design.
  Use Poppins as the documented web alternative only when Sofia Pro
  cannot be used. Calibri remains the Office-suite standard.
  Verify actual font loading and rendering; do not distribute proprietary
  font files with this repository.

## Maintenance Notes

- Keep red as an accent — resist requests to fill hero sections with it.
- Preserve the existing official brand-red token `#D5494B`.
- Use the UI-only contrast variant `--color-action: #CE4447` with white
  labels for primary buttons, button-like CTA links, and selected controls.
  Keep the same opaque pairing in all enabled states (4.62331:1).
  This is an accessibility implementation addition, not a manual color.
- Use navy for ordinary inline links/text on white or beige; underline
  links. White on brand red fails normal-text AA (4.29989:1), and action
  red on beige also fails normal-text AA (3.86587:1).
- Use offset navy focus outlines on light surfaces and white on navy.
  Verify ≥4.5:1 for ordinary text and ≥3:1 for required non-text indicators
  in the rendered UI. Run the token check linked in SKILL.md; GitHub
  Actions checks these token pairs on changes to this skill.
- New components should inherit the beige canvas and soft elevation.
- Preserve the full-stop headline element; it is brand, not punctuation.

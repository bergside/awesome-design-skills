---
name: cronduit
description: Pure black × neon cyan system-monitor aesthetic. Dark-only, IBM Plex Mono-first, glow-not-shadow.
license: MIT
metadata:
  author: Cronduit / AyeThoHaney
---

# Cronduit Design System

## Configuration

The design system includes:
- **Color palette:** Accent `#00D9FF` (neon cyan), Secondary `#FF6B00` (hot orange), Success `#00FF88` (neon green), Background `#000000` (pure black), Panel `#060A1A` (deep navy), Surface `#0A0E1F`, Muted `#5A6370`, Dim `#8A95A5`, Foreground `#FFFFFF`
- **Typography:** IBM Plex Mono for all headers, labels, prices, CTAs, and monospace elements; IBM Plex Sans for body copy
- **Scale values:** Font sizes (9/11/12/13/14/16/20/24/32/40/56), spacing (4/8/12/16/20/24/32/40/48/56/64/96), border radius (2–4px; 999px for pill badges only)
- **Font weights:** 400, 500, 600, 700
- **Glow tokens:** `glow-1` (subtle, stat numbers), `glow-2` (card hover/focus), `glow-soft` (ambient), `glow-orange` (secondary lane)

## Design Approach

The system employs "pure black × neon cyan with system-monitor precision." Page backgrounds are always `#000000`. Card surfaces use `#060A1A`. The single accent color `#00D9FF` drives all interactive states — hover glows, active indicators, CTA buttons, and focus rings. IBM Plex Mono governs all mechanical UI text; IBM Plex Sans handles reading-weight body copy. Rounded corners are prohibited above 4px. Shadows are replaced entirely with radial glow effects. Scan-line animations and L-shaped corner bracket decorations signal live, data-driven products.

## Key Characteristics

- **Dark-only:** No light mode exists. No near-black surfaces except the approved panel value `#060A1A`.
- **Monospace-first:** IBM Plex Mono is the display typeface — all prices, stats, labels, and CTAs are monospace uppercase.
- **Glow over shadow:** Every elevation signal uses `box-shadow` with `rgba(0,217,255,...)` — no standard drop-shadows.
- **Precision copy:** Prices are exact ($149, $99, $499). Build claims are specific (2,117 leads, 5 days). Forbidden words: revolutionary, disrupting, game-changing.
- **Receipt aesthetic:** Products are sold as documented artifacts, not features. Copy reads like a build log, not a landing page.

#!/usr/bin/env python3
"""Validate the skill's opaque sRGB token pairs; not a rendered-UI audit."""
import re
from pathlib import Path


def luminance(hex_color):
    rgb = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
              for v in rgb]
    return sum(v * w for v, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(first, second):
    dark, light = sorted((luminance(first), luminance(second)))
    return (light + 0.05) / (dark + 0.05)


def main():
    text = (Path(__file__).resolve().parents[1] / 'SKILL.md').read_text()
    tokens = dict(re.findall(r'\| `(--color-[\w-]+)` \| `(#\w{6})` \|', text))
    checks = re.findall(
        r'\| `(--color-[\w-]+)` \| `(--color-[\w-]+)` \| ([\d.]+) \|', text)
    if len(checks) < 8:
        raise SystemExit('Missing contrast checks')
    if tokens.get('--color-primary') != '#D5494B':
        raise SystemExit('Official brand red changed')
    failed = False
    for foreground, background, minimum in checks:
        ratio = contrast(tokens[foreground], tokens[background])
        passed = ratio >= float(minimum)  # Never round for pass/fail.
        print(f'{"PASS" if passed else "FAIL"} {foreground} / {background}: '
              f'{ratio:.5f}:1 (minimum {minimum}:1)')
        failed |= not passed
    raise SystemExit(1 if failed else 0)


if __name__ == '__main__':
    main()

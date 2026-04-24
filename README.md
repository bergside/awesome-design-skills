# Awesome Design Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated registry of design system skill files for AI-powered agentic tools like [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), [Cursor](https://www.cursor.com/), [Codex](https://openai.com/index/codex/), and others. Pull any skill into your project with a single command.

Each skill now ships as a folder with:
- `SKILL.md` for AI-agent instructions (tokens, component rules, accessibility constraints, quality gates)
- `DESIGN.md` for human-readable design intent, rationale, and implementation notes

**[Preview all design skills on typeui.sh](https://typeui.sh/design-skills)**

Built and maintained by [Bergside](https://github.com/bergside). Powered by [typeui.sh](https://github.com/bergside/typeui.sh).

## Contents

- [Quick Start](#quick-start)
- [What is a Design Skill?](#what-is-a-design-skill)
- [Design Skills](#design-skills)
- [Usage](#usage)
- [Registry Structure](#registry-structure)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

Pull any design skill directly into your project using [typeui.sh](https://github.com/bergside/typeui.sh):

```bash
npx typeui.sh pull <slug>
```

For example, to pull the Glassmorphism design skill:

```bash
npx typeui.sh pull glassmorphism
```

Or browse all available skills interactively:

```bash
npx typeui.sh list
```

## What is a Design Skill?

A design skill is a folder containing `SKILL.md` and `DESIGN.md`.

`SKILL.md` acts as the instruction source for AI agents and LLMs. It contains:

- **Brand & mission** — the design philosophy and visual identity
- **Style foundations** — typography scale, color palette, spacing system
- **Component families** — buttons, inputs, cards, modals, navigation, and more
- **Accessibility rules** — WCAG 2.2 AA compliance, keyboard-first interactions
- **Writing tone** — content and voice guidelines
- **Do/Don't rules** — explicit patterns and anti-patterns
- **Quality gates** — testable acceptance criteria for code review

`DESIGN.md` is a companion document for human readers and maintainers. It captures:

- **Design overview** — concise summary of the visual direction
- **Rationale and references** — context for why patterns/tokens exist
- **Maintenance notes** — guidance for keeping design decisions aligned over time

When an AI agent reads a skill file, it follows the `SKILL.md` guidelines to generate UI code that is consistent, accessible, and true to the design system.

## Design Skills

Browse and preview all design skills at [typeui.sh/design-skills](https://typeui.sh/design-skills) before pulling them into your project.

| Skill | Category | Preview | Pull Command |
|-------|----------|---------|-------------|
| **Agentic** | Themed & Unique | [Preview](https://typeui.sh/design-skills/agentic) | `npx typeui.sh pull agentic` |
| **Ant** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/ant) | `npx typeui.sh pull ant` |
| **Application** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/application) | `npx typeui.sh pull application` |
| **Artistic** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/artistic) | `npx typeui.sh pull artistic` |
| **Bento** | Layout & Structure | [Preview](https://typeui.sh/design-skills/bento) | `npx typeui.sh pull bento` |
| **Bold** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/bold) | `npx typeui.sh pull bold` |
| **Brutalism** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/brutalism) | `npx typeui.sh pull brutalism` |
| **Cafe** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/cafe) | `npx typeui.sh pull cafe` |
| **Claymorphism** | Morphism & Effects | [Preview](https://typeui.sh/design-skills/claymorphism) | `npx typeui.sh pull claymorphism` |
| **Clean** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/clean) | `npx typeui.sh pull clean` |
| **Colorful** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/colorful) | `npx typeui.sh pull colorful` |
| **Contemporary** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/contemporary) | `npx typeui.sh pull contemporary` |
| **Corporate** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/corporate) | `npx typeui.sh pull corporate` |
| **Cosmic** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/cosmic) | `npx typeui.sh pull cosmic` |
| **Creative** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/creative) | `npx typeui.sh pull creative` |
| **Dashboard** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/dashboard) | `npx typeui.sh pull dashboard` |
| **Dithered** | Retro & Nostalgic | [Preview](https://typeui.sh/design-skills/dithered) | `npx typeui.sh pull dithered` |
| **Doodle** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/doodle) | `npx typeui.sh pull doodle` |
| **Dramatic** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/dramatic) | `npx typeui.sh pull dramatic` |
| **Editorial** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/editorial) | `npx typeui.sh pull editorial` |
| **Elegant** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/elegant) | `npx typeui.sh pull elegant` |
| **Energetic** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/energetic) | `npx typeui.sh pull energetic` |
| **Enterprise** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/enterprise) | `npx typeui.sh pull enterprise` |
| **Expressive** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/expressive) | `npx typeui.sh pull expressive` |
| **Fantasy** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/fantasy) | `npx typeui.sh pull fantasy` |
| **Flat** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/flat) | `npx typeui.sh pull flat` |
| **Friendly** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/friendly) | `npx typeui.sh pull friendly` |
| **Futuristic** | Themed & Unique | [Preview](https://typeui.sh/design-skills/futuristic) | `npx typeui.sh pull futuristic` |
| **Glassmorphism** | Morphism & Effects | [Preview](https://typeui.sh/design-skills/glassmorphism) | `npx typeui.sh pull glassmorphism` |
| **Gradient** | Morphism & Effects | [Preview](https://typeui.sh/design-skills/gradient) | `npx typeui.sh pull gradient` |
| **Levels** | Layout & Structure | [Preview](https://typeui.sh/design-skills/levels) | `npx typeui.sh pull levels` |
| **Lingo** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/lingo) | `npx typeui.sh pull lingo` |
| **Luxury** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/luxury) | `npx typeui.sh pull luxury` |
| **Material** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/material) | `npx typeui.sh pull material` |
| **Minimal** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/minimal) | `npx typeui.sh pull minimal` |
| **Modern** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/modern) | `npx typeui.sh pull modern` |
| **Mono** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/mono) | `npx typeui.sh pull mono` |
| **Neon** | Morphism & Effects | [Preview](https://typeui.sh/design-skills/neon) | `npx typeui.sh pull neon` |
| **Neobrutalism** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/neobrutalism) | `npx typeui.sh pull neobrutalism` |
| **Neumorphism** | Morphism & Effects | [Preview](https://typeui.sh/design-skills/neumorphism) | `npx typeui.sh pull neumorphism` |
| **Pacman** | Themed & Unique | [Preview](https://typeui.sh/design-skills/pacman) | `npx typeui.sh pull pacman` |
| **Paper** | Retro & Nostalgic | [Preview](https://typeui.sh/design-skills/paper) | `npx typeui.sh pull paper` |
| **Perspective** | Layout & Structure | [Preview](https://typeui.sh/design-skills/perspective) | `npx typeui.sh pull perspective` |
| **Premium** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/premium) | `npx typeui.sh pull premium` |
| **Professional** | Professional & Corporate | [Preview](https://typeui.sh/design-skills/professional) | `npx typeui.sh pull professional` |
| **Publication** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/publication) | `npx typeui.sh pull publication` |
| **Refined** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/refined) | `npx typeui.sh pull refined` |
| **Retro** | Retro & Nostalgic | [Preview](https://typeui.sh/design-skills/retro) | `npx typeui.sh pull retro` |
| **Shadcn** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/shadcn) | `npx typeui.sh pull shadcn` |
| **Simple** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/simple) | `npx typeui.sh pull simple` |
| **Skeumorphism** | Morphism & Effects | [Preview](https://typeui.sh/design-skills/skeumorphism) | `npx typeui.sh pull skeumorphism` |
| **Sleek** | Modern & Minimal | [Preview](https://typeui.sh/design-skills/sleek) | `npx typeui.sh pull sleek` |
| **Spacious** | Layout & Structure | [Preview](https://typeui.sh/design-skills/spacious) | `npx typeui.sh pull spacious` |
| **Storytelling** | Creative & Artistic | [Preview](https://typeui.sh/design-skills/storytelling) | `npx typeui.sh pull storytelling` |
| **Tetris** | Themed & Unique | [Preview](https://typeui.sh/design-skills/tetris) | `npx typeui.sh pull tetris` |
| **Vibrant** | Bold & Expressive | [Preview](https://typeui.sh/design-skills/vibrant) | `npx typeui.sh pull vibrant` |
| **Vintage** | Retro & Nostalgic | [Preview](https://typeui.sh/design-skills/vintage) | `npx typeui.sh pull vintage` |

## Usage

### Pull a skill into your project

Use the [typeui.sh CLI](https://github.com/bergside/typeui.sh) to pull any skill by its slug:

```bash
npx typeui.sh pull <slug>
```

The CLI will fetch the `SKILL.md` file from this registry and write it to your configured provider paths (e.g., `.cursor/skills/`, `.claude/`, etc.). The companion `DESIGN.md` remains in this repo alongside each skill for reference and maintenance.

### Specify providers

Target specific agentic tools when pulling:

```bash
npx typeui.sh pull glassmorphism -p cursor,claude
```

### Preview before writing

Use `--dry-run` to see what would be written without making changes:

```bash
npx typeui.sh pull glassmorphism --dry-run
```

### Browse and pull interactively

List all available skills with preview links, then pull one:

```bash
npx typeui.sh list
```

### Generate a custom skill

Run the interactive prompts to create your own design system skill:

```bash
npx typeui.sh generate
```

## Registry Structure

Each skill lives in its own folder under `skills/`:

```
skills/
├── index.json          # Slug-keyed map for fast CLI lookups
├── glassmorphism/
│   ├── SKILL.md        # AI-agent instruction file
│   └── DESIGN.md       # Human-readable design companion
├── brutalism/
│   ├── SKILL.md
│   └── DESIGN.md
├── minimal/
│   ├── SKILL.md
│   └── DESIGN.md
└── ...
```

The `index.json` file maps each slug to its skill path:

```json
{
  "glassmorphism": {
    "slug": "glassmorphism",
    "name": "Glassmorphism",
    "skillPath": "skills/glassmorphism/SKILL.md"
  }
}
```

When you run `npx typeui.sh pull <slug>`, the CLI reads this index, resolves the skill path, and fetches the corresponding `SKILL.md` file. `DESIGN.md` is stored next to each skill for human-facing documentation.

## Contributing

Contributions are welcome! If you'd like to add a new design skill to the registry:

1. Create a new folder under `skills/` with your slug name
2. Add a `SKILL.md` file following the existing format
3. Add a companion `DESIGN.md` file in the same folder
4. Add an entry to `skills/index.json`
5. Submit a pull request

Please ensure your skill file includes all required sections: mission, brand, style foundations, component families, accessibility rules, writing tone, do/don't rules, and quality gates.

## License

[MIT](LICENSE) &copy; [Bergside](https://github.com/bergside)

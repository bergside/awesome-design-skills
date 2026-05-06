# Awesome Design Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<img width="1200" height="630" alt="og-awesome-design-skills" src="https://github.com/user-attachments/assets/d392937a-a0a3-408d-b3f8-4d8920f836f9" />

<br>

> A curated registry of 67 design system skill files for AI-powered agentic tools like [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), [Cursor](https://www.cursor.com/), [Codex](https://openai.com/index/codex/), and others. Pull any skill into your project with a single command.

Each skill now ships as a folder with:
- `SKILL.md` for AI-agent instructions (tokens, component rules, accessibility constraints, quality gates)
- `DESIGN.md` for human-readable design intent, rationale, and implementation notes

**[Preview all design skills on typeui.sh](https://typeui.sh/design-skills)**

Built and maintained by [Bergside](https://github.com/bergside). Powered by [TypeUI](https://github.com/bergside/typeui.sh).

## Contents

- [Quick Start](#quick-start)
- [What is a Design Skill?](#what-is-a-design-skill)
- [Design Skills](#design-skills)
- [Usage](#usage)
- [Registry Structure](#registry-structure)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

Pull any design skill directly into your project using the [TypeUI CLI](https://github.com/bergside/typeui.sh):

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

**Total skills:** 67

| Skill | Thumbnail | Preview | Pull Command |
|-------|-----------|---------|-------------|
| **Agentic** | [<img src="https://www.typeui.sh/registry-examples/agentic.png" alt="Agentic thumbnail" width="280" />](https://typeui.sh/design-skills/agentic) | [Preview](https://typeui.sh/design-skills/agentic) | `npx typeui.sh pull agentic` |
| **Ant** | [<img src="https://www.typeui.sh/registry-examples/ant.png" alt="Ant thumbnail" width="280" />](https://typeui.sh/design-skills/ant) | [Preview](https://typeui.sh/design-skills/ant) | `npx typeui.sh pull ant` |
| **Application** | [<img src="https://www.typeui.sh/registry-examples/application.png" alt="Application thumbnail" width="280" />](https://typeui.sh/design-skills/application) | [Preview](https://typeui.sh/design-skills/application) | `npx typeui.sh pull application` |
| **Artistic** | [<img src="https://www.typeui.sh/registry-examples/artistic.png" alt="Artistic thumbnail" width="280" />](https://typeui.sh/design-skills/artistic) | [Preview](https://typeui.sh/design-skills/artistic) | `npx typeui.sh pull artistic` |
| **Bento** | [<img src="https://www.typeui.sh/registry-examples/bento.png" alt="Bento thumbnail" width="280" />](https://typeui.sh/design-skills/bento) | [Preview](https://typeui.sh/design-skills/bento) | `npx typeui.sh pull bento` |
| **Bold** | [<img src="https://www.typeui.sh/registry-examples/bold.png" alt="Bold thumbnail" width="280" />](https://typeui.sh/design-skills/bold) | [Preview](https://typeui.sh/design-skills/bold) | `npx typeui.sh pull bold` |
| **Brutalism** | [<img src="https://www.typeui.sh/registry-examples/brutalism.png" alt="Brutalism thumbnail" width="280" />](https://typeui.sh/design-skills/brutalism) | [Preview](https://typeui.sh/design-skills/brutalism) | `npx typeui.sh pull brutalism` |
| **Cafe** | [<img src="https://www.typeui.sh/registry-examples/cafe.png" alt="Cafe thumbnail" width="280" />](https://typeui.sh/design-skills/cafe) | [Preview](https://typeui.sh/design-skills/cafe) | `npx typeui.sh pull cafe` |
| **Claymorphism** | [<img src="https://www.typeui.sh/registry-examples/claymorphism.png" alt="Claymorphism thumbnail" width="280" />](https://typeui.sh/design-skills/claymorphism) | [Preview](https://typeui.sh/design-skills/claymorphism) | `npx typeui.sh pull claymorphism` |
| **Claude** | [<img src="https://www.typeui.sh/registry-examples/claude.png" alt="Claude thumbnail" width="280" />](https://typeui.sh/design-skills/claude) | [Preview](https://typeui.sh/design-skills/claude) | `npx typeui.sh pull claude` |
| **Clean** | [<img src="https://www.typeui.sh/registry-examples/clean.png" alt="Clean thumbnail" width="280" />](https://typeui.sh/design-skills/clean) | [Preview](https://typeui.sh/design-skills/clean) | `npx typeui.sh pull clean` |
| **Codex** | [<img src="https://www.typeui.sh/registry-examples/open.png" alt="Codex thumbnail" width="280" />](https://typeui.sh/design-skills/codex) | [Preview](https://typeui.sh/design-skills/codex) | `npx typeui.sh pull codex` |
| **Colorful** | [<img src="https://www.typeui.sh/registry-examples/colorful.png" alt="Colorful thumbnail" width="280" />](https://typeui.sh/design-skills/colorful) | [Preview](https://typeui.sh/design-skills/colorful) | `npx typeui.sh pull colorful` |
| **Contemporary** | [<img src="https://www.typeui.sh/registry-examples/contemporary.png" alt="Contemporary thumbnail" width="280" />](https://typeui.sh/design-skills/contemporary) | [Preview](https://typeui.sh/design-skills/contemporary) | `npx typeui.sh pull contemporary` |
| **Corporate** | [<img src="https://www.typeui.sh/registry-examples/corporate.png" alt="Corporate thumbnail" width="280" />](https://typeui.sh/design-skills/corporate) | [Preview](https://typeui.sh/design-skills/corporate) | `npx typeui.sh pull corporate` |
| **Cosmic** | [<img src="https://www.typeui.sh/registry-examples/cosmic.png" alt="Cosmic thumbnail" width="280" />](https://typeui.sh/design-skills/cosmic) | [Preview](https://typeui.sh/design-skills/cosmic) | `npx typeui.sh pull cosmic` |
| **Creative** | [<img src="https://www.typeui.sh/registry-examples/creative.png" alt="Creative thumbnail" width="280" />](https://typeui.sh/design-skills/creative) | [Preview](https://typeui.sh/design-skills/creative) | `npx typeui.sh pull creative` |
| **Dashboard** | [<img src="https://www.typeui.sh/registry-examples/dashboard.png" alt="Dashboard thumbnail" width="280" />](https://typeui.sh/design-skills/dashboard) | [Preview](https://typeui.sh/design-skills/dashboard) | `npx typeui.sh pull dashboard` |
| **Dithered** | [<img src="https://www.typeui.sh/registry-examples/dithered.png" alt="Dithered thumbnail" width="280" />](https://typeui.sh/design-skills/dithered) | [Preview](https://typeui.sh/design-skills/dithered) | `npx typeui.sh pull dithered` |
| **Doodle** | [<img src="https://www.typeui.sh/registry-examples/hand-drawn.png" alt="Doodle thumbnail" width="280" />](https://typeui.sh/design-skills/doodle) | [Preview](https://typeui.sh/design-skills/doodle) | `npx typeui.sh pull doodle` |
| **Dramatic** | [<img src="https://www.typeui.sh/registry-examples/dramatic.png" alt="Dramatic thumbnail" width="280" />](https://typeui.sh/design-skills/dramatic) | [Preview](https://typeui.sh/design-skills/dramatic) | `npx typeui.sh pull dramatic` |
| **Editorial** | [<img src="https://www.typeui.sh/registry-examples/editorial.png" alt="Editorial thumbnail" width="280" />](https://typeui.sh/design-skills/editorial) | [Preview](https://typeui.sh/design-skills/editorial) | `npx typeui.sh pull editorial` |
| **Elegant** | [<img src="https://www.typeui.sh/registry-examples/elegant.png" alt="Elegant thumbnail" width="280" />](https://typeui.sh/design-skills/elegant) | [Preview](https://typeui.sh/design-skills/elegant) | `npx typeui.sh pull elegant` |
| **Energetic** | [<img src="https://www.typeui.sh/registry-examples/energetic.png" alt="Energetic thumbnail" width="280" />](https://typeui.sh/design-skills/energetic) | [Preview](https://typeui.sh/design-skills/energetic) | `npx typeui.sh pull energetic` |
| **Enterprise** | [<img src="https://www.typeui.sh/registry-examples/enterprise.png" alt="Enterprise thumbnail" width="280" />](https://typeui.sh/design-skills/enterprise) | [Preview](https://typeui.sh/design-skills/enterprise) | `npx typeui.sh pull enterprise` |
| **Expressive** | [<img src="https://www.typeui.sh/registry-examples/expressive.png" alt="Expressive thumbnail" width="280" />](https://typeui.sh/design-skills/expressive) | [Preview](https://typeui.sh/design-skills/expressive) | `npx typeui.sh pull expressive` |
| **Fantasy** | [<img src="https://www.typeui.sh/registry-examples/fantasy.png" alt="Fantasy thumbnail" width="280" />](https://typeui.sh/design-skills/fantasy) | [Preview](https://typeui.sh/design-skills/fantasy) | `npx typeui.sh pull fantasy` |
| **Fiction** | [<img src="https://www.typeui.sh/registry-examples/fiction.png" alt="Fiction thumbnail" width="280" />](https://typeui.sh/design-skills/fiction) | [Preview](https://typeui.sh/design-skills/fiction) | `npx typeui.sh pull fiction` |
| **Flat** | [<img src="https://www.typeui.sh/registry-examples/flat.png" alt="Flat thumbnail" width="280" />](https://typeui.sh/design-skills/flat) | [Preview](https://typeui.sh/design-skills/flat) | `npx typeui.sh pull flat` |
| **Friendly** | [<img src="https://www.typeui.sh/registry-examples/friendly.png" alt="Friendly thumbnail" width="280" />](https://typeui.sh/design-skills/friendly) | [Preview](https://typeui.sh/design-skills/friendly) | `npx typeui.sh pull friendly` |
| **Futuristic** | [<img src="https://www.typeui.sh/registry-examples/futuristic.png" alt="Futuristic thumbnail" width="280" />](https://typeui.sh/design-skills/futuristic) | [Preview](https://typeui.sh/design-skills/futuristic) | `npx typeui.sh pull futuristic` |
| **Glassmorphism** | [<img src="https://www.typeui.sh/registry-examples/glassmorphism.png" alt="Glassmorphism thumbnail" width="280" />](https://typeui.sh/design-skills/glassmorphism) | [Preview](https://typeui.sh/design-skills/glassmorphism) | `npx typeui.sh pull glassmorphism` |
| **Gradient** | [<img src="https://www.typeui.sh/registry-examples/gradient.png" alt="Gradient thumbnail" width="280" />](https://typeui.sh/design-skills/gradient) | [Preview](https://typeui.sh/design-skills/gradient) | `npx typeui.sh pull gradient` |
| **Immersive** | [<img src="https://www.typeui.sh/registry-examples/immersive.png" alt="Immersive thumbnail" width="280" />](https://typeui.sh/design-skills/immersive) | [Preview](https://typeui.sh/design-skills/immersive) | `npx typeui.sh pull immersive` |
| **Impeccable** | [<img src="https://www.typeui.sh/registry-examples/impeccable.png" alt="Impeccable thumbnail" width="280" />](https://typeui.sh/design-skills/impeccable) | [Preview](https://typeui.sh/design-skills/impeccable) | `npx typeui.sh pull impeccable` |
| **Levels** | [<img src="https://www.typeui.sh/registry-examples/levels.png" alt="Levels thumbnail" width="280" />](https://typeui.sh/design-skills/levels) | [Preview](https://typeui.sh/design-skills/levels) | `npx typeui.sh pull levels` |
| **Lingo** | [<img src="https://www.typeui.sh/registry-examples/lingo.png" alt="Lingo thumbnail" width="280" />](https://typeui.sh/design-skills/lingo) | [Preview](https://typeui.sh/design-skills/lingo) | `npx typeui.sh pull lingo` |
| **Luxury** | [<img src="https://www.typeui.sh/registry-examples/luxury.png" alt="Luxury thumbnail" width="280" />](https://typeui.sh/design-skills/luxury) | [Preview](https://typeui.sh/design-skills/luxury) | `npx typeui.sh pull luxury` |
| **Material** | [<img src="https://www.typeui.sh/registry-examples/material.png" alt="Material thumbnail" width="280" />](https://typeui.sh/design-skills/material) | [Preview](https://typeui.sh/design-skills/material) | `npx typeui.sh pull material` |
| **Matrix** | [<img src="https://www.typeui.sh/registry-examples/matrix.png" alt="Matrix thumbnail" width="280" />](https://typeui.sh/design-skills/matrix) | [Preview](https://typeui.sh/design-skills/matrix) | `npx typeui.sh pull matrix` |
| **Minimal** | [<img src="https://www.typeui.sh/registry-examples/minimal.png" alt="Minimal thumbnail" width="280" />](https://typeui.sh/design-skills/minimal) | [Preview](https://typeui.sh/design-skills/minimal) | `npx typeui.sh pull minimal` |
| **Modern** | [<img src="https://www.typeui.sh/registry-examples/modern.png" alt="Modern thumbnail" width="280" />](https://typeui.sh/design-skills/modern) | [Preview](https://typeui.sh/design-skills/modern) | `npx typeui.sh pull modern` |
| **Mono** | [<img src="https://www.typeui.sh/registry-examples/mono.png" alt="Mono thumbnail" width="280" />](https://typeui.sh/design-skills/mono) | [Preview](https://typeui.sh/design-skills/mono) | `npx typeui.sh pull mono` |
| **Neon** | [<img src="https://www.typeui.sh/registry-examples/neon.png" alt="Neon thumbnail" width="280" />](https://typeui.sh/design-skills/neon) | [Preview](https://typeui.sh/design-skills/neon) | `npx typeui.sh pull neon` |
| **Neobrutalism** | [<img src="https://www.typeui.sh/registry-examples/neobrutalism.png" alt="Neobrutalism thumbnail" width="280" />](https://typeui.sh/design-skills/neobrutalism) | [Preview](https://typeui.sh/design-skills/neobrutalism) | `npx typeui.sh pull neobrutalism` |
| **Neumorphism** | [<img src="https://www.typeui.sh/registry-examples/neumorphism.png" alt="Neumorphism thumbnail" width="280" />](https://typeui.sh/design-skills/neumorphism) | [Preview](https://typeui.sh/design-skills/neumorphism) | `npx typeui.sh pull neumorphism` |
| **Pacman** | [<img src="https://www.typeui.sh/registry-examples/pacman.png" alt="Pacman thumbnail" width="280" />](https://typeui.sh/design-skills/pacman) | [Preview](https://typeui.sh/design-skills/pacman) | `npx typeui.sh pull pacman` |
| **Paper** | [<img src="https://www.typeui.sh/registry-examples/paper.png" alt="Paper thumbnail" width="280" />](https://typeui.sh/design-skills/paper) | [Preview](https://typeui.sh/design-skills/paper) | `npx typeui.sh pull paper` |
| **Perspective** | [<img src="https://www.typeui.sh/registry-examples/perspective.png" alt="Perspective thumbnail" width="280" />](https://typeui.sh/design-skills/perspective) | [Preview](https://typeui.sh/design-skills/perspective) | `npx typeui.sh pull perspective` |
| **Premium** | [<img src="https://www.typeui.sh/registry-examples/premium.png" alt="Premium thumbnail" width="280" />](https://typeui.sh/design-skills/premium) | [Preview](https://typeui.sh/design-skills/premium) | `npx typeui.sh pull premium` |
| **Professional** | [<img src="https://www.typeui.sh/registry-examples/professional.png" alt="Professional thumbnail" width="280" />](https://typeui.sh/design-skills/professional) | [Preview](https://typeui.sh/design-skills/professional) | `npx typeui.sh pull professional` |
| **Publication** | [<img src="https://www.typeui.sh/registry-examples/publication.png" alt="Publication thumbnail" width="280" />](https://typeui.sh/design-skills/publication) | [Preview](https://typeui.sh/design-skills/publication) | `npx typeui.sh pull publication` |
| **Refined** | [<img src="https://www.typeui.sh/registry-examples/refined.png" alt="Refined thumbnail" width="280" />](https://typeui.sh/design-skills/refined) | [Preview](https://typeui.sh/design-skills/refined) | `npx typeui.sh pull refined` |
| **Retro** | [<img src="https://www.typeui.sh/registry-examples/retro.png" alt="Retro thumbnail" width="280" />](https://typeui.sh/design-skills/retro) | [Preview](https://typeui.sh/design-skills/retro) | `npx typeui.sh pull retro` |
| **Riso** | [<img src="https://www.typeui.sh/registry-examples/riso.png" alt="Riso thumbnail" width="280" />](https://typeui.sh/design-skills/riso) | [Preview](https://typeui.sh/design-skills/riso) | `npx typeui.sh pull riso` |
| **Sega** | [<img src="https://www.typeui.sh/registry-examples/sega.png" alt="Sega thumbnail" width="280" />](https://typeui.sh/design-skills/sega) | [Preview](https://typeui.sh/design-skills/sega) | `npx typeui.sh pull sega` |
| **Shadcn** | [<img src="https://www.typeui.sh/registry-examples/shadcn.png" alt="Shadcn thumbnail" width="280" />](https://typeui.sh/design-skills/shadcn) | [Preview](https://typeui.sh/design-skills/shadcn) | `npx typeui.sh pull shadcn` |
| **Simple** | [<img src="https://www.typeui.sh/registry-examples/simple.png" alt="Simple thumbnail" width="280" />](https://typeui.sh/design-skills/simple) | [Preview](https://typeui.sh/design-skills/simple) | `npx typeui.sh pull simple` |
| **Sketch** | [<img src="https://www.typeui.sh/registry-examples/sketch.png" alt="Sketch thumbnail" width="280" />](https://typeui.sh/design-skills/sketch) | [Preview](https://typeui.sh/design-skills/sketch) | `npx typeui.sh pull sketch` |
| **Skeumorphism** | [<img src="https://www.typeui.sh/registry-examples/skeumorphism.png" alt="Skeumorphism thumbnail" width="280" />](https://typeui.sh/design-skills/skeumorphism) | [Preview](https://typeui.sh/design-skills/skeumorphism) | `npx typeui.sh pull skeumorphism` |
| **Sleek** | [<img src="https://www.typeui.sh/registry-examples/sleek.png" alt="Sleek thumbnail" width="280" />](https://typeui.sh/design-skills/sleek) | [Preview](https://typeui.sh/design-skills/sleek) | `npx typeui.sh pull sleek` |
| **Spacious** | [<img src="https://www.typeui.sh/registry-examples/spacious.png" alt="Spacious thumbnail" width="280" />](https://typeui.sh/design-skills/spacious) | [Preview](https://typeui.sh/design-skills/spacious) | `npx typeui.sh pull spacious` |
| **Storytelling** | [<img src="https://www.typeui.sh/registry-examples/storytelling.png" alt="Storytelling thumbnail" width="280" />](https://typeui.sh/design-skills/storytelling) | [Preview](https://typeui.sh/design-skills/storytelling) | `npx typeui.sh pull storytelling` |
| **Terracotta** | [<img src="https://www.typeui.sh/registry-examples/terracotta.png" alt="Terracotta thumbnail" width="280" />](https://typeui.sh/design-skills/terracotta) | [Preview](https://typeui.sh/design-skills/terracotta) | `npx typeui.sh pull terracotta` |
| **Tetris** | [<img src="https://www.typeui.sh/registry-examples/tetris.png" alt="Tetris thumbnail" width="280" />](https://typeui.sh/design-skills/tetris) | [Preview](https://typeui.sh/design-skills/tetris) | `npx typeui.sh pull tetris` |
| **Vibrant** | [<img src="https://www.typeui.sh/registry-examples/vibrant.png" alt="Vibrant thumbnail" width="280" />](https://typeui.sh/design-skills/vibrant) | [Preview](https://typeui.sh/design-skills/vibrant) | `npx typeui.sh pull vibrant` |
| **Vintage** | [<img src="https://www.typeui.sh/registry-examples/vintage.png" alt="Vintage thumbnail" width="280" />](https://typeui.sh/design-skills/vintage) | [Preview](https://typeui.sh/design-skills/vintage) | `npx typeui.sh pull vintage` |

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

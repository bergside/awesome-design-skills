# Awesome Design Skills Registry

This repository is an open-source design system skill registry based on https://typeui.sh/design-systems.

Each skill is organized by a unique folder name equal to its slug:

- `skills/<slug>/SKILL.md`
- `skills/index.json`

## Registry Structure

`skills/index.json` is a slug-keyed map for fast lookups from CLI tools.

Example entry:

```json
{
  "paper": {
    "slug": "paper",
    "name": "Paper",
    "skillPath": "skills/paper/SKILL.md"
  }
}
```

## CLI Pull Pattern

A CLI command like `npx typeui.sh pull <slug>` can:

1. Read `skills/index.json`
2. Resolve `index[slug].skillPath`
3. Fetch and return the matching `SKILL.md`

## Included Data

The current registry is generated from the provided source dataset and includes:

- `37` design-system skills
- one `SKILL.md` file per slug

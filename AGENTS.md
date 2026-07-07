# AGENTS.md

Instructions for AI coding agents working on the Make Me Unicorn codebase.
(For *your* project, generate one of these with `mmu agents` — see README.)

## What this is

An open-source launch checklist + CLI (`mmu`) for solo SaaS builders.
Python 3.10+, zero runtime dependencies in the core CLI. Optional extras:
`[llm]` (Anthropic), `[mcp]` (FastMCP server), `[validate]` (HN/Reddit idea
validation).

## Layout

- `src/mmu_cli/` — the CLI. `cli.py` (argparse + commands), `display.py`
  (dashboard/badges/cards), `vibecheck.py` (AI-code blind-spot scanner),
  `agents_md.py` (AGENTS.md generator), `scan.py`, `llm.py`, `mcp_server.py`,
  `validators/` (HN + Reddit + VADER).
- `docs/blueprints/` — the checklists themselves (markdown, the product).
- `src/mmu_cli/data/` — wheel-bundled copy of blueprints/prompts. **Never edit
  directly**; run `python scripts/sync_packaged_data.py` after changing
  `docs/blueprints/` or `prompts/`.
- `tests/` — stdlib `unittest`, no pytest.
- `action.yml` — the composite GitHub Action (vibecheck on PRs).
- `.pre-commit-hooks.yaml` — pre-commit hook definitions.

## Before you commit

Run exactly what CI runs:

```bash
ruff check src tests scripts
mypy src/mmu_cli
python scripts/sync_packaged_data.py --check
python -m unittest discover -s tests -p "test_*.py"
```

## Conventions

- Core CLI stays zero-dependency: stdlib only in `cli.py`, `display.py`,
  `vibecheck.py`, `agents_md.py`, `scan.py`. Optional deps import lazily
  inside functions and degrade with a friendly message.
- Commands return a `Result` (dict subclass) with `exit_code` + `messages`;
  `render_result` handles `--json`. Follow that pattern for new subcommands.
- Line length 120 (ruff). Type hints throughout; `from __future__ import
  annotations` in new modules.
- Paid/API calls are always opt-in with an explicit cost prompt.
- New user-facing features need: tests, README section (English at minimum),
  CHANGELOG entry under `[Unreleased]`, and a ROADMAP tick when applicable.
- READMEs exist in en/ko/ja/zh-CN/es. If you change README.md structurally,
  note which translations still need a sync pass in your PR description.

"""`mmu agents` — generate/update AGENTS.md, the open agent-instructions standard.

AGENTS.md (https://agents.md) is the convention Claude Code, OpenAI Codex,
Cursor, Gemini CLI, and most coding agents read on session start. MMU writes a
managed block into it so every agent session opens with the project's launch
context — score, stage, open gates, top next actions — instead of re-deriving
it (or ignoring it) each time.

Everything outside the marker comments is user-owned and never touched;
re-running `mmu agents` only regenerates the block between the markers.
"""

from __future__ import annotations

from pathlib import Path

BEGIN_MARKER = "<!-- mmu:agents:begin — managed by `mmu agents`; edits inside are overwritten -->"
END_MARKER = "<!-- mmu:agents:end -->"

_PRIORITY_TAGS = {0: "P0", 1: "P1", 2: "P2"}

_TEMPLATE_HEADER = """\
# AGENTS.md

Instructions for AI coding agents working in this repository.

Add your own project conventions above or below the managed block —
`mmu agents` regenerates only the content between the markers.

"""


def render_block(root: Path) -> str:
    """Render the managed AGENTS.md block from current project state."""
    from mmu_cli.cli import load_config, load_feature_flags
    from mmu_cli.display import (
        _collect_unchecked_items,
        scan_all_blueprints,
        scan_gates,
        unicorn_art,
    )

    flags = load_feature_flags(root)
    cfg = load_config(root)

    blueprints = scan_all_blueprints(root, flags)
    gates = scan_gates(root)
    bp_done = sum(d for _, d, _, _ in blueprints)
    bp_total = sum(t for _, _, t, _ in blueprints)
    gate_done = sum(d for _, d, _ in gates)
    gate_total = sum(t for _, _, t in gates)
    all_done = bp_done + gate_done
    all_total = bp_total + gate_total
    pct = int(all_done / all_total * 100) if all_total else 0
    stage_name, _ = unicorn_art(pct / 100)

    project = cfg.get("project", {}).get("name", "") or root.resolve().name
    framework = cfg.get("architecture", {}).get("framework", "")

    lines: list[str] = [BEGIN_MARKER, ""]
    lines.append("## Launch context (Make Me Unicorn)")
    lines.append("")
    stack = f" · stack: {framework}" if framework else ""
    lines.append(
        f"**{project}** — launch readiness **{pct}%** ({all_done}/{all_total} items), "
        f"stage **{stage_name.upper()}**{stack}."
    )
    lines.append("")

    if gates:
        lines.append("### Launch gates")
        lines.append("")
        for label, done, total in gates:
            status = "PASS" if total and done == total else "OPEN"
            lines.append(f"- {label}: {done}/{total} {status}")
        lines.append("")

    items = _collect_unchecked_items(root, flags)
    items.sort(key=lambda x: (x[1], x[3]))
    if items:
        lines.append("### Top next actions")
        lines.append("")
        for label, pri, text, _ in items[:5]:
            tag = _PRIORITY_TAGS.get(pri, "P2")
            lines.append(f"- [{tag}] {text} _({label})_")
        if len(items) > 5:
            lines.append(f"- … and {len(items) - 5} more — run `mmu next`")
        lines.append("")

    lines += [
        "### How to work in this project",
        "",
        "- `mmu status --json` — machine-readable score, gates, and per-blueprint progress.",
        "- `mmu next` — prioritized unchecked items; do these before inventing new work.",
        "- `mmu show <blueprint>` / `mmu check <blueprint> <n>` — read a checklist, mark an item done "
        "when (and only when) you have actually shipped it.",
        "- `mmu vibecheck` — run before committing; it catches the gaps AI-generated code ships most "
        "(hardcoded secrets, unverified webhooks, f-string SQL, missing password reset, wildcard CORS).",
        "- `mmu start --mode <mode> --agent` — load only the docs relevant to this session "
        "(backend, billing, growth, …) instead of the whole repo.",
        "- On session end, record decisions with `[DECISION]`, `[DONE]`, `[ISSUE]`, `[NEXT]` tags "
        "via `mmu close` so the next session starts with context.",
        "",
        "Regenerate this block after checklist changes: `mmu agents`.",
        "",
        END_MARKER,
    ]
    return "\n".join(lines)


def merge(existing: str | None, block: str) -> str:
    """Insert or replace the managed block, preserving user content."""
    if existing is None:
        return _TEMPLATE_HEADER + block + "\n"
    begin = existing.find(BEGIN_MARKER)
    end = existing.find(END_MARKER)
    if begin != -1 and end != -1 and end >= begin:
        tail = existing[end + len(END_MARKER):]
        return existing[:begin] + block + tail
    # No markers yet: append the block, keep the user's file intact.
    sep = "" if existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
    return existing + sep + block + "\n"


def write_agents_md(root: Path) -> tuple[Path, bool]:
    """Write/refresh AGENTS.md at project root. Returns (path, created)."""
    path = root / "AGENTS.md"
    existing: str | None
    try:
        existing = path.read_text(encoding="utf-8")
    except OSError:
        existing = None
    path.write_text(merge(existing, render_block(root)), encoding="utf-8")
    return path, existing is None

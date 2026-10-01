"""Build the labelled tech-stack icon grids (light and dark) in assets/.

Logos live in scripts/icons/: skill-*.svg are skillicons tiles, the rest come
from @lobehub/icons and simple-icons and are drawn on a matching tile.
Edit BACKEND / AI below, then run:  python scripts/stack_icons_svg.py
"""
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TILE, COL_W, ROW_H, RADIUS, PAD = 256, 400, 360, 60, 40
LABEL_SIZE, LABEL_Y = 54, TILE + 66
SCALE = 56 / TILE  # rendered tile size: 56px
BG = "#242938"  # skillicons' dark tile colour
LABEL = {"light": "#1f2328", "dark": "#c9d1d9"}

# (label, icon file, override colour or None). "skill-*" files are complete tiles.
BACKEND = [
    ("Python", "skill-py", None), ("Django", "skill-django", None), ("FastAPI", "skill-fastapi", None),
    ("PostgreSQL", "skill-postgres", None), ("MySQL", "skill-mysql", None), ("SQLAlchemy", "sqlalchemy", "#F0613F"),
    ("Redis", "skill-redis", None),
    ("Docker", "skill-docker", None), ("AWS basics", "skill-aws", None), ("GH Actions", "skill-githubactions", None),
    ("Linux", "skill-linux", None), ("Grafana", "skill-grafana", None), ("Prometheus", "skill-prometheus", None),
]
AI = [
    ("LangChain", "langchain", None), ("LangGraph", "langgraph", "#FFFFFF"), ("LlamaIndex", "llamaindex", None),
    ("Pydantic AI", "pydantic", "#E92063"), ("MCP", "mcp", "#FFFFFF"), ("Claude Code", "claudecode", None),
    ("Anthropic", "anthropic", "#F0EEE6"), ("OpenAI", "openai", "#FFFFFF"), ("Hugging Face", "huggingface", None),
    ("pgvector", "postgresql", "#6E9FD8"), ("Ollama", "ollama", "#FFFFFF"), ("Langfuse", "langfuse", None),
    ("Temporal", "temporal", "#FFFFFF"),
]


def parse(svg: str, prefix: str, colour: str | None) -> tuple[str, str]:
    view_box = re.search(r'viewBox="([^"]+)"', svg).group(1)
    body = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", svg, flags=re.S)
    body = re.sub(r"<title>.*?</title>", "", body, flags=re.S)
    for old in set(re.findall(r'id="([^"]+)"', body)):  # unique gradient/clip ids per icon
        body = body.replace(f'id="{old}"', f'id="{prefix}{old}"').replace(f"#{old}", f"#{prefix}{old}")
    if colour:
        body = re.sub(r'fill="(?!none)[^"]*"', f'fill="{colour}"', body)
    return view_box, body


def tile(i: int, x: int, y: int, name: str, colour: str | None) -> str:
    svg = (HERE / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    view_box, body = parse(svg, f"t{i}-", colour)
    if name.startswith("skill-"):
        return f'<svg x="{x}" y="{y}" width="{TILE}" height="{TILE}" viewBox="{view_box}">{body}</svg>'
    fill = colour or "#FFFFFF"
    out = (f'<rect x="{x}" y="{y}" width="{TILE}" height="{TILE}" rx="{RADIUS}" fill="{BG}"/>'
           f'<svg x="{x + PAD}" y="{y + PAD}" width="{TILE - 2 * PAD}" height="{TILE - 2 * PAD}" '
           f'viewBox="{view_box}" fill="{fill}" color="{fill}">{body}</svg>')
    if name == "postgresql":  # pgvector: elephant plus a small vector arrow
        out += (f'<g transform="translate({x + 170} {y + 168})" stroke="#FFD43B" stroke-width="16" '
                f'stroke-linecap="round" fill="none"><path d="M0 52 L52 0"/><path d="M18 0 H52 V34"/></g>')
    return out


def build(items: list, per_row: int, theme: str) -> str:
    rows = -(-len(items) // per_row)
    w, h = per_row * COL_W, rows * ROW_H
    parts = []
    for i, (label, name, colour) in enumerate(items):
        row, col = divmod(i, per_row)
        in_row = min(per_row, len(items) - row * per_row)
        offset = (per_row - in_row) * COL_W / 2  # centre a shorter last row
        cx = offset + col * COL_W + COL_W / 2
        x, y = int(cx - TILE / 2), row * ROW_H
        parts.append(
            f'<g><title>{label}</title>{tile(i, x, y, name, colour)}'
            f'<text x="{cx}" y="{y + LABEL_Y}" text-anchor="middle" fill="{LABEL[theme]}" '
            f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
            f'font-size="{LABEL_SIZE}">{label}</text></g>'
        )
    names = ", ".join(label for label, _, _ in items)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{round(w * SCALE)}" height="{round(h * SCALE)}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{names}">' + "".join(parts) + "</svg>\n")


if __name__ == "__main__":
    # File names carry a content hash so browsers and GitHub's raw cache never
    # serve a stale image; README.md is rewritten to point at the new names.
    root = HERE.parent
    out = root / "assets"
    readme = (root / "README.md").read_text(encoding="utf-8")
    for group, items, per_row in (("backend", BACKEND, 7), ("ai", AI, 7)):
        for theme in LABEL:
            svg = build(items, per_row, theme)
            name = f"stack-{group}-{theme}.{hashlib.sha1(svg.encode()).hexdigest()[:8]}.svg"
            for old in out.glob(f"stack-{group}-{theme}*.svg"):
                old.unlink()
            (out / name).write_text(svg, encoding="utf-8")
            readme = re.sub(rf"assets/stack-{group}-{theme}[^\"']*\.svg(\?v=\d+)?", f"assets/{name}", readme)
            print("wrote", name)
    (root / "README.md").write_text(readme, encoding="utf-8", newline="\n")

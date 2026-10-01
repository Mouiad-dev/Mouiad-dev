"""Build assets/ai-stack.svg: a skillicons-style strip of AI tool logos.

Logos live in scripts/icons/ (from @lobehub/icons and simple-icons).
Edit ICONS below, then run:  python scripts/ai_icons_svg.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TILE, GAP, RADIUS, PAD = 256, 44, 60, 40
BG = "#242938"  # same tile colour as skillicons' dark theme

# (title, file, override colour or None to keep the logo's own colours)
ICONS = [
    ("LangChain", "langchain", None),
    ("LangGraph", "langgraph", "#FFFFFF"),
    ("LlamaIndex", "llamaindex", None),
    ("Pydantic AI", "pydantic", "#E92063"),
    ("Model Context Protocol", "mcp", "#FFFFFF"),
    ("Claude Code", "claudecode", None),
    ("Anthropic", "anthropic", "#F0EEE6"),
    ("OpenAI", "openai", "#FFFFFF"),
    ("Hugging Face", "huggingface", None),
    ("pgvector", "postgresql", "#6E9FD8"),
    ("Ollama", "ollama", "#FFFFFF"),
    ("Langfuse", "langfuse", None),
    ("Temporal", "temporal", "#FFFFFF"),
]


def inner(svg: str, prefix: str, colour: str | None) -> tuple[str, str]:
    view_box = re.search(r'viewBox="([^"]+)"', svg).group(1)
    body = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", svg, flags=re.S)
    body = re.sub(r"<title>.*?</title>", "", body, flags=re.S)
    # keep gradient ids unique across icons
    for old in set(re.findall(r'id="([^"]+)"', body)):
        body = body.replace(f'id="{old}"', f'id="{prefix}{old}"').replace(f"#{old}", f"#{prefix}{old}")
    if colour:
        body = re.sub(r'fill="(?!none)[^"]*"', f'fill="{colour}"', body)
    return view_box, body


def build(icons_per_row: int = 13) -> str:
    tiles = []
    for i, (title, name, colour) in enumerate(ICONS):
        row, col = divmod(i, icons_per_row)
        x, y = col * (TILE + GAP), row * (TILE + GAP)
        view_box, body = inner((HERE / "icons" / f"{name}.svg").read_text(encoding="utf-8"), f"i{i}-", colour)
        fill = colour or "#FFFFFF"
        extra = ""
        if name == "postgresql":  # pgvector: elephant plus a small vector arrow
            extra = (f'<g transform="translate({x + 170} {y + 168})" stroke="#FFD43B" stroke-width="16" '
                     f'stroke-linecap="round" fill="none"><path d="M0 52 L52 0"/><path d="M18 0 H52 V34"/></g>')
        tiles.append(
            f'<g><title>{title}</title>'
            f'<rect x="{x}" y="{y}" width="{TILE}" height="{TILE}" rx="{RADIUS}" fill="{BG}"/>'
            f'<svg x="{x + PAD}" y="{y + PAD}" width="{TILE - 2 * PAD}" height="{TILE - 2 * PAD}" '
            f'viewBox="{view_box}" fill="{fill}" color="{fill}">{body}</svg>{extra}</g>'
        )
    cols = min(len(ICONS), icons_per_row)
    rows = -(-len(ICONS) // icons_per_row)
    w, h = cols * TILE + (cols - 1) * GAP, rows * TILE + (rows - 1) * GAP
    scale = 48 / TILE
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{round(w * scale)}" height="{round(h * scale)}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{", ".join(t for t, _, _ in ICONS)}">'
            + "".join(tiles) + "</svg>\n")


if __name__ == "__main__":
    out = HERE.parent / "assets" / "ai-stack.svg"
    out.write_text(build(), encoding="utf-8")
    print("wrote", out)

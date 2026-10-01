"""Render the animated `git log` career terminal as light and dark SVGs.

Edit CAREER below, then run:  python scripts/career_svg.py
"""
from html import escape
from pathlib import Path

PROMPT = "git log --oneline --reverse career"
CAREER = [
    # (hash, year, company, role, impact, is_head)
    ("a1f3c02", "2018", "SCASE", "AI intern", "lane detection · Detectron2 object detection", False),
    ("4be91d7", "2020", "KUWAITNET", "Software developer", "Py2 → Py3 / Django 1.8 → 3.2, +45% perf", False),
    ("7c2e5a9", "2023", "tigerlab", "Software developer", "Claim Journey · −20% external API calls", False),
    ("9d04b11", "2025", "tigerlab", "Senior backend engineer", "−30% system load · SSO · scoped permissions", False),
    ("e5a7f30", "2025", "LLM systems", "AI engineering", "RAG · MCP · agents · evals, at work and in my lab", True),
]

THEMES = {
    "dark": dict(bg="#0d1117", bar="#161b22", border="#30363d", text="#c9d1d9", muted="#8b949e",
                 hash="#e3b341", company="#58a6ff", impact="#7ee787", head="#39c5cf", prompt="#7ee787"),
    "light": dict(bg="#ffffff", bar="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#656d76",
                  hash="#9a6700", company="#0969da", impact="#1a7f37", head="#1b7c83", prompt="#1a7f37"),
}

W, LINE_H, PAD_X, TOP = 900, 30, 24, 72
STEP = 0.55  # seconds between lines


def render(t: dict) -> str:
    rows = len(CAREER) + 2
    h = TOP + rows * LINE_H + 20
    lines = []

    def line(i: int, spans: str) -> None:
        y = TOP + i * LINE_H
        lines.append(f'<text class="l" x="{PAD_X}" y="{y}" style="animation-delay:{0.4 + i * STEP:.2f}s">{spans}</text>')

    line(0, f'<tspan fill="{t["prompt"]}">$</tspan> <tspan fill="{t["text"]}">{escape(PROMPT)}</tspan>')
    for i, (sha, year, company, role, impact, head) in enumerate(CAREER, start=1):
        spans = (
            f'<tspan fill="{t["hash"]}">{sha}</tspan>  '
            f'<tspan fill="{t["muted"]}">{year}</tspan>  '
            f'<tspan fill="{t["company"]}" font-weight="600">{escape(company)}</tspan>'
            f'<tspan fill="{t["text"]}"> · {escape(role)}</tspan>'
            f'<tspan fill="{t["muted"]}"> — </tspan>'
            f'<tspan fill="{t["impact"]}">{escape(impact)}</tspan>'
        )
        if head:
            spans += f' <tspan fill="{t["head"]}">(HEAD → now)</tspan>'
        line(i, spans)
    last = len(CAREER) + 1
    cursor_delay = 0.4 + last * STEP
    line(last, f'<tspan fill="{t["prompt"]}">$</tspan> <tspan class="c" fill="{t["text"]}">█</tspan>')

    dots = "".join(
        f'<circle cx="{24 + k * 20}" cy="22" r="6" fill="{c}"/>'
        for k, c in enumerate(("#ff5f57", "#febc2e", "#28c840"))
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="Career as a git log: {escape(", ".join(f"{c[1]} {c[2]} {c[3]}" for c in CAREER))}">
<style>
.l{{font:14.5px ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;opacity:0;animation:in .5s ease forwards}}
.c{{animation:blink 1s step-end infinite {cursor_delay:.2f}s}}
@keyframes in{{from{{opacity:0;transform:translateX(-6px)}}to{{opacity:1;transform:none}}}}
@keyframes blink{{50%{{opacity:0}}}}
@media (prefers-reduced-motion:reduce){{.l{{animation:none;opacity:1}}.c{{animation:none}}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="12" fill="{t["bg"]}" stroke="{t["border"]}"/>
<path d="M.5 44V12.5A12 12 0 0 1 12.5 .5h{W - 25}a12 12 0 0 1 12 12V44z" fill="{t["bar"]}"/>
<line x1="0" y1="44" x2="{W}" y2="44" stroke="{t["border"]}"/>
{dots}
<text x="{W / 2}" y="27" text-anchor="middle" fill="{t["muted"]}" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="13">mouiad@career: ~</text>
{chr(10).join(lines)}
</svg>
'''


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for name, theme in THEMES.items():
        (out / f"career-{name}.svg").write_text(render(theme), encoding="utf-8")
        print("wrote", out / f"career-{name}.svg")

<sub>[All previews](../README.md) · [1 Minimal](1-minimal.md) · **2 Code** · [3 AI lab](3-ai-lab.md) · [4 Modern](4-modern.md) · [5 Case studies](5-case-studies.md) · [6 Dashboard](6-dashboard.md)</sub>

---

```python
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Mouiad:
    role: str = "Backend Engineer → AI Engineer"
    since: int = 2020
    domain: str = "Insurance platforms: policies, quotations, payments"

    stack: dict = field(default_factory=lambda: {
        "core":  ["Python", "Django", "DRF", "PostgreSQL", "Redis", "Celery"],
        "ai":    ["RAG", "pgvector", "Ollama", "Anthropic API", "tiktoken"],
        "ops":   ["Docker", "GitHub Actions", "Linux"],
    })

    believes_in: tuple = (
        "fat models + a service layer, thin views",
        "select_related before it's a problem",
        "domain events over tangled side effects",
        "a number before an opinion",
    )

    building_now: dict = field(default_factory=lambda: {
        "RAG-Lab":                  "every RAG technique is a switch — flip it, measure it",
        "prompt-cache-benchmark":   "the real break-even point of prompt caching",
        "attention-cost-simulator": "why 100x more context costs 10,000x more attention",
        "token-economics-cli":      "why Arabic costs ~2–3x more tokens than English",
    })

    def contact(self) -> str:
        return "mouiad.ali.work@gmail.com"
```

<sub>Projects: [RAG-Lab](https://github.com/Mouiad-dev/RAG-Lab) · [prompt-cache-benchmark](https://github.com/Mouiad-dev/prompt-cache-benchmark) · [attention-cost-simulator](https://github.com/Mouiad-dev/attention-cost-simulator) · [token-economics-cli](https://github.com/Mouiad-dev/LLm) · older work on [Mouiad-JRA](https://github.com/Mouiad-JRA)</sub>

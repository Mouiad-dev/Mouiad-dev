<sub>[All previews](../README.md) · [1 Minimal](1-minimal.md) · [2 Code](2-code.md) · [3 AI lab](3-ai-lab.md) · [4 Modern](4-modern.md) · [5 Case studies](5-case-studies.md) · [6 Dashboard](6-dashboard.md) · **7 Combined**</sub>

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:0f172a,100:1e3a8a&text=Mouiad%20Ali&fontColor=e2e8f0&fontSize=52&fontAlignY=38&desc=Backend%20%E2%86%92%20AI%20Engineer&descAlignY=60&descSize=18">
  <img alt="Mouiad Ali — Backend to AI Engineer" src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:dbeafe,100:93c5fd&text=Mouiad%20Ali&fontColor=0f172a&fontSize=52&fontAlignY=38&desc=Backend%20%E2%86%92%20AI%20Engineer&descAlignY=60&descSize=18">
</picture>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=3500&pause=900&color=3B82F6&center=true&vCenter=true&width=600&lines=6+years+of+Python+and+Django+backends;1%2B+year+shipping+LLM+features;RAG+systems+you+can+measure;Clean+architecture%2C+zero+N%2B1+queries" alt="Typing intro"/>
</p>

I've spent six years building Python and Django backends, most of them for insurance platforms. For the past **year and a bit** I've been building with LLMs, both **in production at work** and **in my own lab**. Every lab project answers one question with a number.

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,django,fastapi,postgres,redis,docker,linux,githubactions&perline=8" alt="Python, Django, FastAPI, PostgreSQL, Redis, Docker, Linux, GitHub Actions"/>
  <br/>
  <img src="https://img.shields.io/badge/Anthropic_API-191919?style=flat-square&logo=anthropic&logoColor=white" alt="Anthropic API"/>
  <img src="https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=claude&logoColor=white" alt="Claude Code"/>
  <img src="https://img.shields.io/badge/MCP-0F172A?style=flat-square&logo=modelcontextprotocol&logoColor=white" alt="MCP"/>
  <img src="https://img.shields.io/badge/pgvector-336791?style=flat-square&logo=postgresql&logoColor=white" alt="pgvector"/>
  <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/RAG_%2B_evals-0C7A6A?style=flat-square" alt="RAG and evals"/>
</p>

### Lab notebook

| Question | Project | Answer |
|---|---|---|
| Which RAG technique actually helps, and by how much? | [**RAG-Lab**](https://github.com/Mouiad-dev/RAG-Lab) | 6 retrieval modes behind one switch, scored on recall@k, faithfulness, and latency |
| When does prompt caching start saving money? | [**prompt-cache-benchmark**](https://github.com/Mouiad-dev/prompt-cache-benchmark) | The write costs 1.25×, each read 0.1×. Break-even is measured from real API usage |
| Why is long context so expensive? | [**attention-cost-simulator**](https://github.com/Mouiad-dev/attention-cost-simulator) | 1k → 100k tokens means 10,000× the attention work |
| Does language change the bill? | [**token-economics-cli**](https://github.com/Mouiad-dev/LLm) | The same sentence in Arabic costs ~2–3× the tokens of English |

### Roadmap: backend → AI engineer

| | | |
|---|---|---|
| ✅ **00** · How LLMs work | 🔲 **01** · APIs and structured output | 🔲 **02** · Tool calling and MCP |
| 🔲 **03** · Coding agents | 🔄 **04** · Embeddings and RAG | 🔄 **05** · Context, memory, and caching |
| 🔲 **06** · Agents and durability | 🔲 **07** · Evals, safety, and approval | 🔲 **08** · Channels and voice |

<sub>✅ done · 🔄 in progress · 🔲 next. Each phase ends in a public, measured project.</sub>

### Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/profile-night-rainbow.svg">
    <img alt="3D contribution graph" width="100%" src="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/profile-green-animate.svg">
  </picture>
</p>

<table>
<tr>
<td width="50%" valign="top">

**Recently pushed**

<!-- RECENT:START -->
- [RAG-Lab](https://github.com/Mouiad-dev/RAG-Lab) — 2026-09-23
- [Async](https://github.com/Mouiad-dev/Async) — 2026-09-06
- [prompt-cache-benchmark](https://github.com/Mouiad-dev/prompt-cache-benchmark) — 2026-09-01
- [attention-cost-simulator](https://github.com/Mouiad-dev/attention-cost-simulator) — 2026-08-28
- [LLm](https://github.com/Mouiad-dev/LLm) — 2026-08-28
<!-- RECENT:END -->

</td>
<td width="50%" valign="top">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=Mouiad-dev&hide_border=true&background=0d1117&ring=3b82f6&fire=3b82f6&currStreakLabel=3b82f6&sideLabels=c9d1d9&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=8b949e&stroke=30363d">
  <img alt="Contribution streak" width="100%" src="https://streak-stats.demolab.com?user=Mouiad-dev&hide_border=true&ring=1d4ed8&fire=1d4ed8&currStreakLabel=1d4ed8">
</picture>

</td>
</tr>
</table>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/github-snake-dark.svg">
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/github-snake.svg">
  </picture>
</p>

### How I build

Service layer and thin views · constraints and indexes in the schema · domain events to decouple side effects · providers behind a `Protocol` so tests use fakes · a number before an opinion.

<p align="center">
  <a href="mailto:mouiad.ali.work@gmail.com"><img src="https://img.shields.io/badge/Email-mouiad.ali.work-1d4ed8?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/Mouiad-JRA"><img src="https://img.shields.io/badge/Older_work_2020--2022-Mouiad--JRA-374151?style=flat-square&logo=github&logoColor=white" alt="Older account"/></a>
</p>

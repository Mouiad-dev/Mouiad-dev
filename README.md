<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:0f172a,100:1e3a8a&text=Mouiad%20Ali&fontColor=e2e8f0&fontSize=52&fontAlignY=38&desc=Senior%20Backend%20Engineer%20%C2%B7%20AI%20Engineer&descAlignY=60&descSize=18">
  <img alt="Mouiad Ali — Senior Backend Engineer and AI Engineer" src="https://capsule-render.vercel.app/api?type=waving&height=180&color=0:dbeafe,100:93c5fd&text=Mouiad%20Ali&fontColor=0f172a&fontSize=52&fontAlignY=38&desc=Senior%20Backend%20Engineer%20%C2%B7%20AI%20Engineer&descAlignY=60&descSize=18">
</picture>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=18&duration=3500&pause=900&color=3B82F6&center=true&vCenter=true&width=620&lines=7%2B+years+of+Python+and+Django+in+fintech+and+insurance;1%2B+year+shipping+LLM+features;RAG%2C+agents%2C+and+evals+you+can+measure;Clean+architecture%2C+zero+N%2B1+queries" alt="Typing intro"/>
</p>

<p align="center">
  <a href="cv/Mouiad-Ali-CV.pdf"><img src="https://img.shields.io/badge/Download_CV-PDF-1d4ed8?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Download CV"/></a>
  <a href="https://www.linkedin.com/in/mouiad-ali-678a22230/"><img src="https://img.shields.io/badge/LinkedIn-Mouiad_Ali-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:mouiad.ali.work@gmail.com"><img src="https://img.shields.io/badge/Email-Get_in_touch-374151?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</p>

I'm a **Senior Backend Engineer at [tigerlab](https://www.tigerlab.com/)** with 7+ years building scalable Python and Django systems for fintech and insurance. My focus is performance, security hardening, and system architecture. For the past **year and a bit** I've also been building with LLMs, **in production at work and in my own lab**.

### Tech stack

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/stack-backend-dark.svg">
    <img alt="Python, Django, FastAPI, PostgreSQL, MySQL, SQLAlchemy, Redis, Docker, AWS (basics), GitHub Actions, Linux, Grafana, Prometheus" src="assets/stack-backend-light.svg">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/stack-ai-dark.svg">
    <img alt="LangChain, LangGraph, LlamaIndex, Pydantic AI, MCP, Claude Code, Anthropic, OpenAI, Hugging Face, pgvector, Ollama, Langfuse, Temporal" src="assets/stack-ai-light.svg">
  </picture>
</p>

<details>
<summary><b>Full toolbox, by concern</b></summary>

| Concern | Tools |
|---|---|
| LLM APIs and structured output | Anthropic SDK, OpenAI SDK, OpenRouter, Pydantic v2, instructor, LiteLLM |
| Tool calling and MCP | MCP SDK, FastMCP, Streamable HTTP, MCP Inspector, OAuth 2.1 |
| Coding agents | Claude Code (CLAUDE.md, hooks, subagents, plan mode) |
| RAG and data | PostgreSQL + pgvector, SQLAlchemy 2 + Alembic, LlamaIndex, BM25 hybrid search, BGE/Cohere rerankers, RAG vs CAG |
| Agents and orchestration | LangChain, LangGraph (checkpointers, human-in-the-loop), Pydantic AI, CrewAI, Temporal, n8n |
| Memory and context | Prompt caching, context compression, Mem0, Zep, Letta |
| Evals and observability | Langfuse, RAGAS, LangSmith, Arize Phoenix, Promptfoo, DeepEval, Logfire, Prometheus, Grafana |
| Safety | Guardrails AI, NeMo Guardrails, Presidio (PII), sandboxed execution (Docker, E2B) |
| Models and serving | Claude, OpenAI, Bedrock, Ollama, vLLM, llama.cpp, Hugging Face Transformers |
| Cloud (AWS, working knowledge) | S3 (private buckets, pre-signed URLs), IAM, Secrets Manager, EC2, RDS, VPC, EventBridge, QuickSight, Bedrock |

</details>

### Track record

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/career-dark.svg">
  <img alt="Career as a git log: 2018 SCASE AI intern, 2020 KUWAITNET, 2023 tigerlab developer, 2025 tigerlab senior backend engineer, 2025 LLM systems" width="100%" src="assets/career-light.svg">
</picture>

<table align="center">
<tr>
<td align="center" width="20%"><h2>7+</h2><sub>years&nbsp;of<br/>Python&nbsp;·&nbsp;Django</sub></td>
<td align="center" width="20%"><h2>−30%</h2><sub>system&nbsp;load<br/>N+1&nbsp;fixes</sub></td>
<td align="center" width="20%"><h2>+45%</h2><sub>faster&nbsp;after<br/>Py2&nbsp;→&nbsp;Py3</sub></td>
<td align="center" width="20%"><h2>−20%</h2><sub>external&nbsp;calls<br/>caching&nbsp;layer</sub></td>
<td align="center" width="20%"><h2>75%</h2><sub>test&nbsp;coverage<br/>core&nbsp;modules</sub></td>
</tr>
</table>

<details>
<summary><b>📁 CASE-001 · Private policy files were publicly reachable</b> → access locked down, zero downtime</summary>

**Symptom.** Private insurance policy documents could be reached by anyone with the URL.<br/>
**Root cause.** The files were served from a public bucket, and legacy code depended on public links.<br/>
**Fix.** Moved them to a private S3 bucket, revoked public access, and served them through short-lived pre-signed URLs. The legacy code was migrated in phases across UAT, hotfix, and production.<br/>
**Result.** Customer documents became private without a breaking release.

</details>

<details>
<summary><b>📁 CASE-002 · Services slowing down under load</b> → −30% system load</summary>

**Symptom.** Response times climbed across several services as the data grew.<br/>
**Root cause.** N+1 query patterns and legacy bottlenecks in hot paths.<br/>
**Fix.** Profiled the hot paths, rewrote access with `select_related` / `prefetch_related`, added indexes, and removed redundant work.<br/>
**Result.** System load fell by 30%, and response times improved across services.

</details>

<details>
<summary><b>📁 CASE-003 · Paying for the same third-party answer twice</b> → −20% external calls</summary>

**Symptom.** High latency and third-party costs on external API integrations.<br/>
**Root cause.** Identical requests hit the provider again and again.<br/>
**Fix.** Designed a middleware caching layer in front of the external calls.<br/>
**Result.** External API calls fell by 20%, lowering both latency and cost.

</details>

<details>
<summary><b>📁 CASE-004 · A platform stuck on Python 2 / Django 1.8</b> → +45% performance, EOL risk removed</summary>

**Symptom.** An end-of-life stack, with mounting security risk and slow pages.<br/>
**Fix.** Led the full migration to Python 3.9 / Django 3.2, adapted the third-party packages that blocked the upgrade, and backed it with 75% unit-test coverage and Cypress E2E tests.<br/>
**Result.** Performance improved by 45%, and the EOL security risk was gone.

</details>

<details>
<summary><b>📁 CASE-005 · One permission model for many regions</b> → scoped access from scratch</summary>

**Symptom.** Users needed different actions and different slices of data depending on their geography.<br/>
**Fix.** Architected a permission system from scratch that combines Django action permissions with geographic data scoping, and led a custom SSO integration with Django REST Auth end to end.<br/>
**Result.** Access rules became explicit, testable, and compliant.

</details>

### Where my AI work started

<table>
<tr>
<td width="50%" valign="top">

**[Lane-Line-Detection](https://github.com/Mouiad-dev/Lane-Line-Detection-using-Image-Processing-vs-Deep-Learning)** <sub>· Python · ⭐ 15 · 🍴 3</sub>

Detects lane lines on changing road surfaces, curves, and lighting. Classical image processing goes head to head with a deep-learning model.

</td>
<td width="50%" valign="top">

**[Object-Detection-Using-Detectron](https://github.com/Mouiad-dev/Object-Detection-Using-Detectron)** <sub>· Jupyter · ⭐ 2 · 🍴 1</sub>

Detectron2 object detection, benchmarked for speed on CPU vs VPU. It uses fine-tuned pretrained models instead of training from scratch.

</td>
</tr>
</table>

<sub>Built in 2018–2020 during my AI internship. That curiosity is now production LLM work.</sub>

### Activity

<p align="center">
  <a href="https://mouiad-dev.github.io/Mouiad-dev/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/profile-night-rainbow.svg">
    <img alt="3D contribution graph" width="100%" src="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/profile-green-animate.svg">
  </picture>
  </a>
  <br/>
  <a href="https://mouiad-dev.github.io/Mouiad-dev/"><b>▶ Open the interactive 3D version</b></a> <sub>· drag to rotate · pick any year since 2020</sub>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=Mouiad-dev&hide_border=true&background=0d1117&ring=3b82f6&fire=3b82f6&currStreakLabel=3b82f6&sideLabels=c9d1d9&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=8b949e&stroke=30363d">
  <img alt="Contribution streak" width="70%" src="https://streak-stats.demolab.com?user=Mouiad-dev&hide_border=true&ring=1d4ed8&fire=1d4ed8&currStreakLabel=1d4ed8">
</picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/github-snake-dark.svg">
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/Mouiad-dev/Mouiad-dev/output/github-snake.svg">
  </picture>
</p>

### Education

**B.S. in Information Technology · Tishreen University** · 2016 – 2021 · GPA 87.56%, among the top students in the faculty
Ranked **12th of 3,500** nationally in Syria's Unified National Exam (top 2%) · Al-Basel Award for academic excellence, 4 times

**Languages:** Arabic (native) · English (C2) · German (A2, in progress)

### How I build

Service layer and thin views · constraints and indexes in the schema · event-driven design, Strategy and Factory where they earn their place · providers behind a `Protocol` so tests use fakes · a number before an opinion.

<p align="center"><sub>Older projects (2020–2022) live on <a href="https://github.com/Mouiad-JRA">Mouiad-JRA</a></sub></p>

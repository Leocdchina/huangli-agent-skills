# Huangli Agent Skills

> Standalone public skill package for Chinese Lunar Calendar workflows.

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)

Chinese version: `README.md`

This repository is intentionally **skills-only**.

It includes:
- `SKILL.md` definitions
- executable scripts
- product docs (install, best practices, release notes)

It excludes:
- frontend application code
- backend service code

---

## What this package provides

`Huangli Agent Skills` enables skill-capable AI agents to:
- query one specific date
- query date ranges in batch
- perform keyword filtering across returned records

Core API endpoints:
- `GET /api/lunar/date/{YYYY-MM-DD}`
- `POST /api/lunar/batch`

---

## Skills

- `huangli-query-by-date`
- `huangli-query-batch`
- `huangli-search-by-keyword`

---

## Quick Start

### 1) Configure env

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

### 2) Run scripts

```bash
python3 huangli-query-by-date/query.py 2027-08-08
python3 huangli-query-batch/query.py 2027-08-01 2027-08-07 --filter 搬家
python3 huangli-search-by-keyword/search.py 甲子日 --year 2027
```

### 3) Install in your client

See `INSTALL.md`.

---

## Supported Skill-capable Agent Tools

Based on ecosystem listings and public client docs:

### Coding/CLI agents
- OpenClaw
- Cursor
- Claude Code
- Gemini CLI
- Codex CLI
- Amp
- Roo Code
- Goose
- OpenHands
- OpenCode
- Continue
- Trae Agent
- AutoHand Code CLI
- Factory CLI
- Command Code
- VTCode
- Mistral Vibe
- Kiro

### IDE/platform assistants
- GitHub Copilot Agents / VS Code Copilot Chat
- JetBrains Junie
- Spring AI
- Databricks Assistant
- Snowflake Cortex Code
- Laravel Boost
- Letta Code
- Firebender Multi-Agent
- ONA Agents.md skills
- Emdash

> Support behavior may vary by version and integration mode.

---

## Product-quality design choices

- trigger-focused skill descriptions
- clear skill boundaries (single vs batch vs keyword)
- true batch implementation with chunking
- progressive disclosure-friendly docs and structure
- deterministic script interfaces and errors

See `BEST_PRACTICES.md` for details.

---

## Release assets

- `README.md` / `README.en.md`
- `INSTALL.md`
- `BEST_PRACTICES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES_v1.0.0.md`
- `LICENSE`
- three production-ready skills

---

## Security and quota

- Do not commit real tokens.
- Default free quota: 10 unique dates/day.
- Repeated same-date query does not consume extra unique-date quota.

---

## License

MIT

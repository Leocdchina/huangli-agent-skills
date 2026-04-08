# Huangli Agent Skills

> Standalone public skill package for Chinese lunar calendar (黄历) workflows.

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)
[![English](https://img.shields.io/badge/lang-English-blue)](./README.en.md)

English version: `README.en.md`

This repository is **fully decoupled** from application code.

It contains only:
- `SKILL.md` definitions
- runnable scripts
- product docs (`README`, install guide, release notes, best practices)

It does **not** contain frontend/backend source code.

---

## Product Overview

`Huangli Agent Skills` provides reusable skills so AI coding/agent tools can:
- query one date’s 黄历
- query multiple dates in batch
- run keyword-based filtering across date ranges

Core API endpoints:
- `GET /api/lunar/date/{YYYY-MM-DD}`
- `POST /api/lunar/batch`

---

## Included Skills

- `huangli-query-by-date` — single-date lookup
- `huangli-query-batch` — multi-date/range lookup via batch endpoint
- `huangli-search-by-keyword` — local filtering by ganzhi/constellation/lunar day/activity

---

## Quick Start

### 1) Set env

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

### 2) Run scripts directly

```bash
python3 huangli-query-by-date/query.py 2027-08-08
python3 huangli-query-batch/query.py 2027-08-01 2027-08-07 --filter 搬家
python3 huangli-search-by-keyword/search.py 甲子日 --year 2027
```

### 3) Install into your agent tool

See `INSTALL.md`.

---

## Supported Agent Tools (Skill-capable)

Below is the consolidated compatibility list for tools that support skill-style workflows (`SKILL.md`/agent skills), based on public client docs and ecosystem listings.

### General-purpose coding/CLI agents
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

### IDE/platform assistants with skill support docs
- GitHub Copilot Agents / VS Code Copilot Chat
- JetBrains Junie
- Spring AI (agent skills support)
- Databricks Assistant
- Snowflake Cortex Code
- Laravel Boost
- Letta Code
- Firebender Multi-Agent
- ONA Agents.md skills
- Emdash

> Notes:
> - Support details vary by product/version (path, activation behavior, permissions).
> - Always use each tool’s latest official docs as source of truth for install/behavior.

---

## Why this package is production-ready

- Trigger-oriented skill descriptions (high activation precision)
- Clear skill boundary design (single vs batch vs keyword)
- Batch skill uses real `POST /api/lunar/batch` with chunking
- Progressive disclosure approach for maintainable context usage
- CLI scripts with deterministic I/O and explicit error semantics

See `BEST_PRACTICES.md` for the applied authoring standards.

---

## Release Contents

- `README.md` — product homepage and compatibility
- `README.en.md` — English product homepage
- `INSTALL.md` — multi-client install guidance
- `BEST_PRACTICES.md` — skill-writing standards
- `CHANGELOG.md`
- `RELEASE_NOTES_v1.0.0.md`
- `LICENSE`
- three standalone skills (each with `SKILL.md` + scripts)

---

## Security & quota notes

- Never commit real tokens.
- Default free quota: 10 unique dates/day.
- Same date queried repeatedly does not duplicate quota usage.

---

## License

MIT

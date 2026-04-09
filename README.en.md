# Huangli Agent Skills

> Standalone public **single-skill** package for Chinese Lunar Calendar workflows.

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)

## ⚡ ClawHub Quick Install (Copy & Run)

```bash
# 1) Login to ClawHub (if not already logged in)
clawhub login

# 2) Install the unified skill
clawhub install huangli-toolkit
```

After installation, configure `HUANGLI_TOKEN` (see "Website, Token, and Getting Started").

Chinese version: `README.md`

This repository is skills-only and excludes frontend/backend application code.

---

## Website, Token, and Getting Started

- Website: https://nongli.skill.4glz.com
- Register: https://nongli.skill.4glz.com/register
- Login: https://nongli.skill.4glz.com/login
- Dashboard (request/copy token): https://nongli.skill.4glz.com/dashboard
- API Base: `https://api.nongli.skill.4glz.com`

Set environment variables:

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

---

## Product Shape

The package now keeps one unified skill only:

- `huangli-toolkit`

Built-in modes:
- `by-date` (single date)
- `batch` (multi-date/range)
- `search` (keyword lookup across date ranges)

---

## Quick Usage

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

---

## Install in Agent Clients

See `INSTALL.md` for OpenClaw, Cursor, Claude Code and other skill-capable tools.

---

## Best-practice design choices

- trigger-first skill description
- natural-language time expansion before API calls
- batch-first strategy for range requests
- progressive disclosure for maintainable context size

See `BEST_PRACTICES.md`.

---

## Quota & security

1、默认免费额度：10 个唯一日期/天
2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
3、不限制重置次数。
- Never commit real tokens

---

## License

MIT

# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac (Auspicious & Inauspicious)

> Standalone public **single-skill** package for Chinese Lunar Calendar workflows.

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)

## ⚡ ClawHub Quick Install (Copy & Run)

```bash
# 1) Login to ClawHub (if not already logged in)
clawhub login

# 2) Install the unified skill (new searchable name)
clawhub install zhongguo-nongli-huangli-jixiong
```

After installation, you can either configure `HUANGLI_TOKEN` manually or use the secure CLI device authorization flow (see “Website, Token, and Getting Started”).

Chinese version: `README.md`

This repository contains only end-user skill assets and usage guides.

---

## Website, Token, and Getting Started

- Website: https://nongli.skill.4glz.com
- Register: https://nongli.skill.4glz.com/register
- Login: https://nongli.skill.4glz.com/login
- Dashboard (request/copy token): https://nongli.skill.4glz.com/dashboard
- GitHub repository (source): https://github.com/Leocdchina/huangli-agent-skills
- Publisher: Leocdchina
- API Base: `https://api.nongli.skill.4glz.com`

You can either copy a token from the dashboard or use secure CLI auth:

```bash
python3 huangli-toolkit/auth.py login
python3 huangli-toolkit/auth.py register
python3 huangli-toolkit/auth.py status
```

Then set environment variables:

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
clawhub install zhongguo-nongli-huangli-jixiong

# Secure CLI auth (recommended)
python3 huangli-toolkit/auth.py login
source ~/.huangli.env

python3 huangli-toolkit/toolkit.py by-date 2027-08-08
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

> For security reasons, logout and device unbinding must be done in the web dashboard, not from the local CLI.

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

## Keywords / 关键词 (for search)

中国农历, 黄历, 老黄历, 农历查询, 吉凶, 吉日, 宜忌, 择日, 搬家吉日, 结婚吉日, 开业吉日, Chinese lunar calendar, Chinese almanac, Huangli, Nongli, auspicious day, inauspicious day, lucky date, wedding date selection, move-in date selection, feng shui date, jixiong

---

## Quota & security

1、默认免费额度：10 个唯一日期/天
2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
3、不限制重置次数。

---

## License

MIT

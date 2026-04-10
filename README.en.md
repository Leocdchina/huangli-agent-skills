# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac

> A user-facing unified Huangli skill package for agents and CLI tools.

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)

## What this is

This repository provides one ready-to-use Huangli skill package for end users.

It ships one skill folder:
- `huangli-toolkit`

Supported usage modes:
- `by-date` — query one specific date
- `batch` — query a date range
- `search` — search by keyword across dates

---

## Quick start

### 1) Install the skill

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

If you use another client, see `INSTALL.md`.

### 2) Get a token

- Website: https://nongli.skill.4glz.com
- Register: https://nongli.skill.4glz.com/register
- Login: https://nongli.skill.4glz.com/login
- Dashboard: https://nongli.skill.4glz.com/dashboard

You can either:
- copy a token from the dashboard
- or use the included secure CLI auth helper:

```bash
python3 huangli-toolkit/auth.py login
source ~/.huangli.env
```

Also available:

```bash
python3 huangli-toolkit/auth.py register
python3 huangli-toolkit/auth.py status
```

### 3) Start using it

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

---

## Usage notes

### Environment variables

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

### Quota

1. Free tier: 10 unique dates per day  
2. Over quota returns 429 and requires dashboard reset  
3. Manual reset is not limited  

### Security

- `auth.py` is the recommended way to authorize CLI usage
- `python3 huangli-toolkit/auth.py status` checks whether your current token still works
- logout and device unbinding must be done in the web dashboard

---

## More

- Client install guide: `INSTALL.md`
- Unified skill definition: `huangli-toolkit/SKILL.md`
- Design notes: `BEST_PRACTICES.md`
- Changelog: `CHANGELOG.md`

## License

MIT

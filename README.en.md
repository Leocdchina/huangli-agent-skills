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

## Install the skill first

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

If you use another client, see `INSTALL.md`.

---

## Mode 1: Web mode

Best for users who want to:
- register and log in on the website
- copy a token manually
- manage CLI devices in the dashboard

### Full steps

#### Step 1: Open the website
- Website: https://nongli.skill.4glz.com

#### Step 2: Register or log in
- Register: https://nongli.skill.4glz.com/register
- Login: https://nongli.skill.4glz.com/login

#### Step 3: Open the dashboard
- Dashboard: https://nongli.skill.4glz.com/dashboard

From the dashboard you can:
- view today’s quota
- copy your token
- refresh your access token
- manage bound CLI devices
- log out

#### Step 4: Set environment variables

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

#### Step 5: Start using the toolkit

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

---

## Mode 2: CLI mode

Best for users who want to:
- authorize from the terminal
- avoid copying tokens manually
- let the CLI save local environment files automatically

### Full steps

#### Step 1: Make sure the skill is installed

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

#### Step 2: Start CLI authorization

If you already have an account:

```bash
python3 huangli-toolkit/auth.py login
```

If you are a new user:

```bash
python3 huangli-toolkit/auth.py register
```

#### Step 3: Complete approval in the browser

The CLI will:
- request a one-time authorization code
- open the browser automatically
- wait for you to log in or register and approve access

#### Step 4: Load local environment variables

After approval, run:

```bash
source ~/.huangli.env
```

To check status:

```bash
python3 huangli-toolkit/auth.py status
```

#### Step 5: Start using the toolkit

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

---

## Important notes

### Quota

1. Free tier: 10 unique dates per day  
2. Over quota returns 429 and requires dashboard reset  
3. Manual reset is not limited  

### Security

- `auth.py` is the recommended way to authorize CLI usage
- `python3 huangli-toolkit/auth.py status` checks whether the current token still works
- logout and device unbinding must be done in the web dashboard

## More

- Client install guide: `INSTALL.md`
- Unified skill definition: `huangli-toolkit/SKILL.md`

## License

MIT

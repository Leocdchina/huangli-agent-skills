# Release Notes — v1.1.1

## Summary

This release consolidates the previous 3-skill layout into one unified production skill: `zhongguo-nongli-huangli-jixiong` (alias folder: `huangli-toolkit`).

Quota description (public copy):
1、默认免费额度：10 个唯一日期/天
2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
3、不限制重置次数。

## Why this release

- easier installation (single folder)
- clearer user onboarding (official website, token application, usage examples)
- lower maintenance overhead while keeping full capability

## Official website & token

- Website: https://nongli.skill.4glz.com
- Register: https://nongli.skill.4glz.com/register
- Login: https://nongli.skill.4glz.com/login
- Dashboard (request/copy token): https://nongli.skill.4glz.com/dashboard

## What’s included

- `huangli-toolkit/SKILL.md`
- `huangli-toolkit/toolkit.py`
- `huangli-toolkit/toolkit.sh`
- `huangli-toolkit/references/reference.md`
- updated docs (`README`, `README.en`, `INSTALL`, `CHANGELOG`)

## 快速安装（ClawHub）

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

安装后配置：

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

## Unified usage

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2027-08-08
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py search 甲子日 --year 2027
```

## Clean-up policy

Previous split skills are cleaned up from this standalone package and replaced by the unified toolkit.

---

## v1.2.0

### New: Agent Mode — Fully Autonomous AI Authentication

AI Agent can now register an account and obtain a valid `HUANGLI_TOKEN` without any human intervention.

**How it works:**

Standard CLI flow requires browser confirmation (human-in-the-loop). Agent mode (`mode=agent`) skips browser confirmation entirely, using username+password as identity proof, and returns `access_token` in a single API call.

**Backend changes** (`/api/auth/cli/device/start`):
- New `mode=agent` parameter
- In agent mode: after validating credentials, the server returns `access_token` immediately
- No browser confirmation, no polling needed
- Supports both `action=login` and `action=register`

**auth.py changes:**
- New `--agent` flag
- New `HUANGLI_AUTO_AGENT=1` environment variable (auto-detect)
- New `cmd_agent()` function — one-step token acquisition
- Existing browser-based flow remains unchanged

**Usage for AI Agent:**
```bash
export HUANGLI_USERNAME="myuser"
export HUANGLI_PASSWORD="mypassword"
export HUANGLI_AUTO_AGENT=1

python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login
# → access_token returned immediately, no browser, no polling
```

```bash
# Or with explicit --agent flag:
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register --username=myuser --email=me@example.com --password=mypass --agent
```

**Published:** ClawHub v1.6.0

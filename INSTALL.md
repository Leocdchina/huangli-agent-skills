# Install Guide

This repository contains one **source** skill folder:
- `huangli-toolkit/`

Published production slug on ClawHub:
- `zhongguo-nongli-huangli-jixiong`

---

## Choose install method by client/location

### A) ClawHub clients (registry install)

Use this when your environment supports `clawhub`:

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

Installed folder will be:
- `skills/zhongguo-nongli-huangli-jixiong/`

### B) Cursor / Claude Code / OpenClaw (GitHub command install)

Use this when your client loads local `SKILL.md` folders directly.

#### Cursor

```bash
tmp="$(mktemp -d)" && \
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leocdchina/huangli-agent-skills.git "$tmp" && \
git -C "$tmp" sparse-checkout set huangli-toolkit && \
mkdir -p .cursor/skills/huangli && \
rm -rf .cursor/skills/huangli/zhongguo-nongli-huangli-jixiong && \
cp -R "$tmp/huangli-toolkit" .cursor/skills/huangli/zhongguo-nongli-huangli-jixiong && \
rm -rf "$tmp"
```

#### Claude Code

```bash
tmp="$(mktemp -d)" && \
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leocdchina/huangli-agent-skills.git "$tmp" && \
git -C "$tmp" sparse-checkout set huangli-toolkit && \
mkdir -p ~/.claude/skills/huangli && \
rm -rf ~/.claude/skills/huangli/zhongguo-nongli-huangli-jixiong && \
cp -R "$tmp/huangli-toolkit" ~/.claude/skills/huangli/zhongguo-nongli-huangli-jixiong && \
rm -rf "$tmp"
```

#### OpenClaw

```bash
tmp="$(mktemp -d)" && \
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leocdchina/huangli-agent-skills.git "$tmp" && \
git -C "$tmp" sparse-checkout set huangli-toolkit && \
mkdir -p ~/.openclaw/skills/huangli && \
rm -rf ~/.openclaw/skills/huangli/zhongguo-nongli-huangli-jixiong && \
cp -R "$tmp/huangli-toolkit" ~/.openclaw/skills/huangli/zhongguo-nongli-huangli-jixiong && \
rm -rf "$tmp"
```

#### Other skill-capable clients

Use the same command pattern:
1. Clone this GitHub repo with sparse-checkout (`huangli-toolkit` only)
2. Copy to client skill directory as `zhongguo-nongli-huangli-jixiong`
3. Restart client / refresh skill indexing

---

## Auth/query command rule (all clients)

Canonical commands (recommended from any project/root directory):

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --username=<name> --password=<password>
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register --username=<name> --email=<mail>
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py status

python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2027-08-08
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py search 甲子日 --year 2027
```

Short commands (`python3 auth.py`, `python3 toolkit.py`) are only for cases where current directory is already the installed skill folder.

---

## Modes (do not mix)

- 模式 A：网页模式
- 模式 B：CLI 模式（一切交给 Agent）

### 模式 A：网页模式

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2027-08-08
```

### 模式 B：CLI 模式

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --print-shell
# 或
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --username=<name> --password=<password>
# 或
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register --username=<name> --email=<mail>

source ~/.huangli.env
```

---

## Troubleshooting

- `401`: token missing/invalid
- `429`: daily quota exceeded; reset in dashboard
- Skill not triggering: confirm folder is in correct client skill directory
- Logout / device unbind must be done in web dashboard
# Install Guide

This package ships one skill folder:
- `huangli-toolkit`

## Option A: ClawHub

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

## Option B: Manual install

Copy `huangli-toolkit/` into your client’s skill directory.

### Cursor

```bash
mkdir -p .cursor/skills/huangli
cp -R huangli-toolkit .cursor/skills/huangli/
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/huangli
cp -R huangli-toolkit ~/.claude/skills/huangli/
```

### OpenClaw

```bash
mkdir -p ~/.openclaw/skills/huangli
cp -R huangli-toolkit ~/.openclaw/skills/huangli/
```

### Other skill-capable clients

1. Locate the client skill directory
2. Copy `huangli-toolkit/`
3. Restart the client or refresh skill indexing

---

## Get a token

- Website: https://nongli.skill.4glz.com
- Register: https://nongli.skill.4glz.com/register
- Login: https://nongli.skill.4glz.com/login
- Dashboard: https://nongli.skill.4glz.com/dashboard

### Recommended: secure CLI auth

```bash
python3 huangli-toolkit/auth.py login
source ~/.huangli.env
```

Other useful commands:

```bash
python3 huangli-toolkit/auth.py register
python3 huangli-toolkit/auth.py status
python3 huangli-toolkit/auth.py login --print-shell
python3 huangli-toolkit/auth.py login --append-zshrc
```

### Manual environment variables

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

> For security, logout and device unbinding must be done in the web dashboard.

---

## Verify installation

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
curl "$HUANGLI_BASE/api/quota" \
  -H "Authorization: Bearer $HUANGLI_TOKEN"
```

## Troubleshooting

- `401`: token missing, invalid, or expired
- `429`: daily quota exceeded; reset in dashboard
- Skill not triggering: confirm the folder was copied into the correct client skill directory

# Install Guide (Standalone Skill Package)

This package is client-agnostic and can be installed into any agent client that supports `SKILL.md` style skills.

## Prerequisites

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

---

## OpenClaw

```bash
mkdir -p ~/.openclaw/skills/huangli
cp -R huangli-query-by-date ~/.openclaw/skills/huangli/
cp -R huangli-query-batch ~/.openclaw/skills/huangli/
cp -R huangli-search-by-keyword ~/.openclaw/skills/huangli/
```

## Cursor

```bash
mkdir -p .cursor/skills/huangli
cp -R huangli-query-by-date .cursor/skills/huangli/
cp -R huangli-query-batch .cursor/skills/huangli/
cp -R huangli-search-by-keyword .cursor/skills/huangli/
```

## Claude Code

```bash
mkdir -p ~/.claude/skills/huangli
cp -R huangli-query-by-date ~/.claude/skills/huangli/
cp -R huangli-query-batch ~/.claude/skills/huangli/
cp -R huangli-search-by-keyword ~/.claude/skills/huangli/
```

## Gemini CLI / Codex CLI / Other skill-capable clients

Use the same pattern:
1. Find client skill directory in official docs
2. Copy each skill folder (with `SKILL.md` intact)
3. Restart client if required

---

## Verify Installation

### API sanity check

```bash
curl "$HUANGLI_BASE/api/quota" \
  -H "Authorization: Bearer $HUANGLI_TOKEN"
```

### Script sanity check

```bash
python3 huangli-query-by-date/query.py 2027-08-08
python3 huangli-query-batch/query.py 2027-08-01 2027-08-03
```

---

## Troubleshooting

- `401 Unauthorized`: invalid/expired token
- `429 Too Many Requests`: daily quota exceeded; reset via dashboard
- no skill triggering: make sure client scanned skill path and supports `SKILL.md`

# Contributing

Thanks for contributing to Huangli Agent Skills.

## Scope policy

This repository is skill-only.

Allowed:
- `SKILL.md` improvements
- script quality/performance fixes
- install/docs/release docs updates

Not allowed:
- frontend/backend app code
- unrelated product modules

## Development checklist

1. Keep each skill single-purpose and composable
2. Keep `description` trigger-oriented (when to use)
3. Prefer batch endpoint for date ranges
4. Preserve executable permissions for scripts
5. Ensure `name` matches parent directory

## Validation

- Verify scripts run with required env vars
- Check `SKILL.md` frontmatter format and limits
- Keep docs consistent with behavior

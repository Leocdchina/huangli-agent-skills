# Release Notes — v1.1.0

## Summary

This release consolidates the previous 3-skill layout into one unified production skill: `huangli-toolkit`.

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

## Unified usage

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

## Clean-up policy

Previous split skills are cleaned up from this standalone package and replaced by the unified toolkit.

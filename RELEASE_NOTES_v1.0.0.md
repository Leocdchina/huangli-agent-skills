# Release Notes — v1.0.0

## Summary

Huangli Agent Skills v1.0.0 is the first standalone public release.
This package is built for skill-capable agent clients and includes only reusable skill assets.

## What’s inside

- `huangli-query-by-date`
- `huangli-query-batch`
- `huangli-search-by-keyword`
- documentation: install guide + best practices + changelog

## Highlights

- clear trigger-oriented skill descriptions
- proper batch endpoint usage (`POST /api/lunar/batch`)
- tool-agnostic packaging for multi-client adoption

## Not included

- frontend UI code
- backend service code

## Compatibility

Designed for clients supporting `SKILL.md` style skills (OpenClaw, Cursor, Claude Code and other compatible clients listed in README).

## Operational notes

- required env: `HUANGLI_TOKEN`
- optional env: `HUANGLI_BASE` (default `https://api.nongli.skill.4glz.com`)
- free quota baseline: 10 unique dates/day

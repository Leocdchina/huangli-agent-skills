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

## Release process standard

Use this repository release order as the standard process.

### Mandatory metadata transparency rules (must pass before release)

For `huangli-toolkit/SKILL.md`, frontmatter must explicitly disclose runtime requirements and persistence behavior:

- `required_env` must include `HUANGLI_TOKEN`
- `optional_env` must include `HUANGLI_BASE`
- `config_paths` must include:
  - `~/.huangli_token.json`
  - `~/.huangli.env`
  - `~/.zshrc (only when --append-zshrc is used)`
- `outbound_hosts` must include `api.nongli.skill.4glz.com`

Do not publish if frontmatter/runtime behavior is inconsistent.

### 1) Prepare content

Before publishing, make sure all of the following are true:
- user-facing docs are updated first
- Web mode and CLI mode instructions are clear and separated
- `SKILL.md` matches actual behavior
- required env vars, local file writes, and optional shell changes are disclosed clearly
- no frontend/backend app code is added to this repo

### 2) Validate locally

Recommended checks before release:

```bash
python3 -m py_compile huangli-toolkit/auth.py
python3 -m py_compile huangli-toolkit/toolkit.py
```

Then review:
- `README.md`
- `README.en.md`
- `INSTALL.md`
- `huangli-toolkit/SKILL.md`

### 3) Push GitHub source first

Always push the final release content to GitHub before publishing to ClawHub.

```bash
git add .
git commit -m "<release message>"
git push origin main
```

### 4) Publish to ClawHub

ClawHub is the packaging/distribution release.

Example:

```bash
clawhub publish "./huangli-toolkit" \
  --version 1.2.2 \
  --name "中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac" \
  --slug zhongguo-nongli-huangli-jixiong \
  --changelog "<release summary>"
```

Rules:
- version must use semver
- changelog text must summarize user-visible changes
- if ClawHub content changes, GitHub source must be updated to match

### 5) Sync the same version back to GitHub tag/release

After ClawHub publish succeeds, create the same Git tag and GitHub Release.

Example:

```bash
git tag -a v1.2.2 -m "Release v1.2.2"
git push origin v1.2.2

gh release create v1.2.2 \
  --repo Leocdchina/huangli-agent-skills \
  --title "v1.2.2" \
  --notes "Standard release synchronized with ClawHub version 1.2.2."
```

Rules:
- ClawHub version and GitHub tag must match
- GitHub Release notes should summarize the same standard release
- GitHub is the source of truth for files; ClawHub is the packaged published version

### 6) Release checklist

Before marking a release complete, confirm:
- GitHub `main` contains the final content
- ClawHub publish succeeded
- Git tag exists
- GitHub Release exists
- version numbers match across all channels
- published ClawHub `SKILL.md` still contains required transparency fields (`required_env`, `optional_env`, `config_paths`, `outbound_hosts`)

Suggested post-publish verification commands:

```bash
clawhub inspect zhongguo-nongli-huangli-jixiong --version <x.y.z> --file SKILL.md
clawhub inspect zhongguo-nongli-huangli-jixiong --json
```

### 7) Versioning rules

- patch (`x.y.Z`): wording fixes, metadata fixes, small doc corrections, packaging fixes
- minor (`x.Y.0`): new user-visible capability, new script behavior, new auth flow, new usage mode
- major (`X.0.0`): breaking changes in usage model, packaging model, or compatibility expectations

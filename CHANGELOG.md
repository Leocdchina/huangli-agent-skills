# Changelog

## v1.1.1 - 2026-04-09

### Changed
- project/skill branding renamed for searchability: **中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac (Auspicious & Inauspicious)**
- ClawHub install slug updated to: `zhongguo-nongli-huangli-jixiong`
- docs now explicitly include Chinese + English + pinyin naming keywords (中国农历 / 黄历 / 吉凶 / nongli / huangli / jixiong)

## v1.1.0 - 2026-04-09

### Added
- new unified skill `huangli-toolkit` with three modes: `by-date`, `batch`, `search`
- one-command style toolkit scripts (`toolkit.py`, `toolkit.sh`)
- dedicated reference document for website/token/usage guidance

### Changed
- product docs now explicitly explain official website, token application path, and quick usage
- install guide simplified to single folder deployment (`huangli-toolkit`)

### Clean-up
- legacy split skills (`huangli-query-by-date`, `huangli-query-batch`, `huangli-search-by-keyword`) are removed from this standalone package and replaced by unified toolkit

## v1.0.0 - 2026-04-08

### Added
- standalone skill package structure for public distribution
- product-grade docs (`README.md`, `INSTALL.md`, `BEST_PRACTICES.md`)
- release note template for distribution channels

### Improved
- trigger-oriented `description` content in all `SKILL.md`
- batch skill implementation switched to `POST /api/lunar/batch` with chunking
- clearer usage boundaries for single-date vs range vs keyword workflows

### Scope
- includes only skill assets and docs
- excludes frontend/backend application code

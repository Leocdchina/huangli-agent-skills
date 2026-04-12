---
name: zhongguo-nongli-huangli-jixiong
license: MIT
homepage: https://nongli.skill.4glz.com
repository: https://github.com/Leocdchina/huangli-agent-skills
publisher: Leocdchina
compatibility: Requires Python 3.9+ or bash with curl. This skill uses included Python scripts (`toolkit.py`, `auth.py`) and requires HTTPS outbound access to api.nongli.skill.4glz.com. You must either set HUANGLI_TOKEN manually (recommended for web mode) or run canonical commands from any working directory: `python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --username=<name> --password=<password>` / `python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register --username=<name> --email=<mail>`. Short form `python3 auth.py ...` is only for cases where current directory is already the installed skill folder. `auth.py` writes tokens to `~/.huangli_token.json` and shell exports to `~/.huangli.env` by default; it only modifies `~/.zshrc` if you explicitly pass `--append-zshrc`. `HUANGLI_BASE` is optional.
required_env:
  - HUANGLI_TOKEN
optional_env:
  - HUANGLI_BASE
config_paths:
  - ~/.huangli_token.json
  - ~/.huangli.env
  - ~/.zshrc (only when --append-zshrc is used)
outbound_hosts:
  - api.nongli.skill.4glz.com
description: |
  中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac (Auspicious & Inauspicious).
  Runtime transparency (important):
  - Requires `HUANGLI_TOKEN` for API calls (`HUANGLI_BASE` optional)
  - CLI auth writes token files to user home by default: `~/.huangli_token.json` and `~/.huangli.env`
  - `~/.zshrc` is modified only when `--append-zshrc` is explicitly used
  Keywords / 关键词: 中国农历, 黄历, 老黄历, 农历查询, 吉凶, 吉日, 宜忌, 择日, 搬家吉日, 结婚吉日, 开业吉日, Chinese lunar calendar, Chinese almanac, Huangli, Nongli, auspicious day, inauspicious day, lucky date, wedding date selection, move-in date selection, feng shui date, jixiong.

  Unified Huangli skill for common workflows: single-date query, date-range batch query,
  and keyword search over a date range.

  Use this skill when users ask:
  - one specific date: “今天宜忌是什么 / 2027-08-08 吉时”
  - a period comparison: “下月哪天适合搬家”
  - keyword lookup: “2027年哪些日子是甲子日 / 哪些天宜开业”

  Convert natural-language time to concrete YYYY-MM-DD first.
  Prefer batch endpoint for multi-date requests.
  Keep ranges focused to reduce quota usage.

  1、默认免费额度：10 个唯一日期/天
  2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
  3、不限制重置次数。
---

# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac (Auspicious & Inauspicious)

## 安装路径与客户端分流（重要）

按客户端选择安装方式：
- **ClawHub 客户端**：`clawhub install zhongguo-nongli-huangli-jixiong`
- **Cursor / Claude Code / OpenClaw**：使用 GitHub 命令安装（稀疏克隆 `huangli-toolkit/` 后复制到本地 skills 目录，目录名为 `zhongguo-nongli-huangli-jixiong`）

对应命令请参考仓库根目录 `INSTALL.md`。

- 官网（注册/登录）：https://nongli.skill.4glz.com
- 控制台（获取 Token / 管理已绑定 CLI 设备 / logout）：https://nongli.skill.4glz.com/dashboard
- API Base：`https://api.nongli.skill.4glz.com`

## 两种模式

### 网页模式
- 在控制台复制 Token
- 手动设置 `HUANGLI_TOKEN`
- 不会写入本地 token 文件或 shell 配置

### CLI 模式
- 推荐从任意目录执行：`python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login` 或 `python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register`
- 若当前目录已在技能安装目录，才可使用短命令：`python3 auth.py ...`
- 默认写入 `~/.huangli_token.json` 与 `~/.huangli.env`
- 只有显式传入 `--append-zshrc` 时才会修改 `~/.zshrc`
- 可用 `python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --print-shell` 仅打印导出命令，减少持久化配置修改

可直接配置环境变量，或使用内置安全 CLI 授权：

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"

# 推荐：安全 CLI 设备授权（任意目录）
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py status
```

## 用法（统一入口）

```bash
# 1) 单日查询
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2027-08-08

# 2) 区间批量查询（支持筛选）
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家

# 3) 关键词搜索
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py search 甲子日 --year 2027
```

## 何时用哪种模式

- `by-date`：只问一个具体日期
- `batch`：比较多天、整周、整月
- `search`：关键词跨日期范围检索（甲子日/摩羯座/初一/搬家等）

## 关键实践

- 自然语言时间先展开为具体日期（YYYY-MM-DD）
- 多日期请求优先 `POST /api/lunar/batch`
- 关键词检索基于返回数据本地筛选（无服务端关键词搜索接口）
- logout 与“取消绑定设备”只能在网页控制台完成，避免本地 CLI 被滥用

## 配额说明

1、默认免费额度：10 个唯一日期/天
2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
3、不限制重置次数。

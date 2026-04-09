# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac (Auspicious & Inauspicious)

> Standalone public **single-skill** package for Chinese lunar calendar (黄历) workflows.

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)
[![English](https://img.shields.io/badge/lang-English-blue)](./README.en.md)

## ⚡ ClawHub 安装命令（复制即用）

```bash
# 1) 登录 ClawHub（若尚未登录）
clawhub login

# 2) 安装统一技能（新名称）
clawhub install zhongguo-nongli-huangli-jixiong
```

安装后，把 `HUANGLI_TOKEN` 配好即可使用（见下方“官网、Token 申请、使用入口”）。

English version: `README.en.md`

This repository is fully decoupled from app code and contains only skill assets.

---

## 🔔 最新状态总结（2026-04-09）

- 新品牌名已统一：`中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac (Auspicious & Inauspicious)`
- ClawHub 安装 slug 已切换：`zhongguo-nongli-huangli-jixiong`
- 中英文关键词已扩展并同步：
  - 中国农历 / 黄历 / 老黄历 / 农历查询 / 吉凶 / 吉日 / 宜忌 / 择日 / 搬家吉日 / 结婚吉日 / 开业吉日
  - Chinese lunar calendar / Chinese almanac / Huangli / Nongli / auspicious day / inauspicious day / lucky date / wedding date selection / move-in date selection / feng shui date / jixiong
- 元数据已补全：`homepage`、`repository`、`publisher`、`required_env`、`outbound_hosts`
- API Base（生产）：`https://api.nongli.skill.4glz.com`（已验证可访问）

---

## 官网、Token 申请、使用入口（最重要）

- 官网：https://nongli.skill.4glz.com
- 注册：https://nongli.skill.4glz.com/register
- 登录：https://nongli.skill.4glz.com/login
- 控制台（申请/复制 Token）：https://nongli.skill.4glz.com/dashboard
- GitHub 仓库（源码）：https://github.com/Leocdchina/huangli-agent-skills
- 发布者：Leocdchina
- API Base：`https://api.nongli.skill.4glz.com`

先在控制台拿到 Token，然后设置：

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

---

## 产品形态

本仓库现在只保留一个统一 Skill：

- `huangli-toolkit`

该 Skill 内含三种模式：
- `by-date`：单日查询
- `batch`：区间/多日期批量查询
- `search`：关键词跨日期检索

---

## 快速使用

```bash
clawhub install zhongguo-nongli-huangli-jixiong

# 单日
python3 huangli-toolkit/toolkit.py by-date 2027-08-08

# 批量（可选活动筛选）
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家

# 关键词检索
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

---

## 安装到 Agent 工具

见 `INSTALL.md`。

支持 skill-capable agent 工具（含 OpenClaw、Cursor、Claude Code、Gemini CLI、Codex CLI 等）与安装说明均在该文档中。

---

## 设计原则（最佳实践）

- 触发导向：Skill 描述优先说明“何时用”
- 时间先展开：自然语言时间先转具体日期
- 多日期优先 batch：避免逐日重复请求
- 渐进披露：核心逻辑放 `SKILL.md`，细节放 `references/` 与脚本

详见 `BEST_PRACTICES.md`。

---

## 关键词 / Keywords（用于搜索）

中国农历、黄历、老黄历、农历查询、吉凶、吉日、宜忌、择日、搬家吉日、结婚吉日、开业吉日、Chinese lunar calendar、Chinese almanac、Huangli、Nongli、auspicious day、inauspicious day、lucky date、wedding date selection、move-in date selection、feng shui date、jixiong

---

## 配额与安全

1、默认免费额度：10 个唯一日期/天
2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
3、不限制重置次数。
- 不要把真实 Token 提交到仓库

---

## License

MIT

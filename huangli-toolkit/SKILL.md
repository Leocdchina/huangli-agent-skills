---
name: huangli-toolkit
license: MIT
compatibility: Requires Python 3.9+ or bash with curl. Set HUANGLI_TOKEN env var (Bearer token from https://nongli.skill.4glz.com/dashboard). Needs HTTPS outbound access to api.nongli.skill.4glz.com.
description: |
  Unified Huangli skill for common workflows: single-date query, date-range batch query,
  and keyword search over a date range.

  Use this skill when users ask:
  - one specific date: “今天宜忌是什么 / 2027-08-08 吉时”
  - a period comparison: “下月哪天适合搬家”
  - keyword lookup: “2027年哪些日子是甲子日 / 哪些天宜开业”

  Convert natural-language time to concrete YYYY-MM-DD first.
  Prefer batch endpoint for multi-date requests.
  Keep ranges focused to reduce quota usage.
---

# Huangli Toolkit (Unified Skill)

## 官网与 Token

- 官网（注册/登录）：https://nongli.skill.4glz.com
- 控制台（获取 Token）：https://nongli.skill.4glz.com/dashboard
- API Base：`https://api.nongli.skill.4glz.com`

先配置环境变量：

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

## 用法（统一入口）

```bash
# 1) 单日查询
python3 toolkit.py by-date 2027-08-08

# 2) 区间批量查询（支持筛选）
python3 toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家

# 3) 关键词搜索
python3 toolkit.py search 甲子日 --year 2027
```

## 何时用哪种模式

- `by-date`：只问一个具体日期
- `batch`：比较多天、整周、整月
- `search`：关键词跨日期范围检索（甲子日/摩羯座/初一/搬家等）

## 关键实践

- 自然语言时间先展开为具体日期（YYYY-MM-DD）
- 多日期请求优先 `POST /api/lunar/batch`
- 关键词检索基于返回数据本地筛选（无服务端关键词搜索接口）

## 配额说明

1、默认免费额度：10 个唯一日期/天
2、超额返回429，并提醒手动重置，用户登陆控制台进行手动重置。
3、不限制重置次数。

# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong

> AI Agent 完全自主认证的黄历查询 Skill。配置用户名密码即可自动完成注册/登录并获取 token，全程无需人工干预。

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)

## 唯一亮点

**AI Agent 完全自主认证——无需任何人工干预。**

配置 `HUANGLI_USERNAME` + `HUANGLI_PASSWORD` + `HUANGLI_AUTO_AGENT=1`，调用 auth.py 即可一步获得 `HUANGLI_TOKEN`，直接查询黄历。

---

## 快速开始（AI Agent）

```bash
export HUANGLI_USERNAME="your_username"
export HUANGLI_PASSWORD="your_password"
export HUANGLI_AUTO_AGENT=1

# 登录（AI Agent 自动化，全程无需人工）
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login

# 输出示例：
# Agent mode authorization successful (mode=agent, one-step).
# Run in your current shell session:
# export HUANGLI_TOKEN='eyJhbGci...' && export HUANGLI_BASE='https://api.nongli.skill.4glz.com'
```

---

## 功能

| 命令 | 说明 |
|---|---|
| `toolkit.py by-date YYYY-MM-DD` | 单日黄历查询 |
| `toolkit.py batch START END` | 区间批量查询（支持 `--filter` 筛选） |
| `toolkit.py search KEYWORD` | 关键词跨日期检索 |

## 配额

- 默认免费额度：**10 个唯一日期/天**
- 超额返回 429，需登录控制台手动重置
- 不限重置次数

## 安装方式

- **ClawHub**：`clawhub install zhongguo-nongli-huangli-jixiong`
- **手动安装**：见 [INSTALL.md](./INSTALL.md)

## 更多信息

- 官网：https://nongli.skill.4glz.com
- API Base：`https://api.nongli.skill.4glz.com`
- 详细文档：https://github.com/Leocdchina/huangli-agent-skills

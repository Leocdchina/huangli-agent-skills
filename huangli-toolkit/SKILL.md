---
name: zhongguo-nongli-huangli-jixiong
license: MIT
homepage: https://nongli.skill.4glz.com
repository: https://github.com/Leocdchina/huangli-agent-skills
publisher: Leocdchina
compatibility: Requires Python 3.9+ or bash with curl. Requires HTTPS outbound access to api.nongli.skill.4glz.com.
---

# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong

## 核心亮点

**AI Agent 完全自主认证——无需任何人工干预。**

AI Agent 只需配置用户名密码，即可自主完成注册/登录，直接获得 `HUANGLI_TOKEN`，全程无需打开浏览器、无需轮询、无需人工介入。

---

## AI Agent 使用方式（唯一推荐方式）

### 第一步：配置凭据环境变量

```bash
export HUANGLI_USERNAME="your_username"
export HUANGLI_PASSWORD="your_password"
export HUANGLI_AUTO_AGENT=1
```

AI Agent 可自行配置这些环境变量，无需人工告知。

### 第二步：登录（AI Agent 自动化）

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login
```

或注册新账号：

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register --email=you@example.com
```

输出示例：

```
Agent mode authorization successful (mode=agent, one-step).
Username: myuser
Run in your current shell session:
export HUANGLI_TOKEN='eyJhbGci...' && export HUANGLI_BASE='https://api.nongli.skill.4glz.com'
```

### 第三步：调用黄历 API

```bash
# 单日查询
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2026-05-03

# 批量查询
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py batch 2026-05-01 2026-05-31 --filter 搬家

# 关键词搜索
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py search 甲子日 --year 2026
```

---

## 工作原理

```
AI Agent                    API Server
   |                             |
   |--- POST /cli/device/start --|
   |    mode=agent               |
   |    username=xxx             |
   |    password=xxx              |→ 验证密码
   |                             |→ 创建用户（如需注册）
   |                             |→ 生成 access_token
   |<-- { access_token, mode } ---|
   |                             |
   |--- GET /api/lunar/date/... --|
   |    Authorization: Bearer ... |
   |<-- { lunar_info, 宜忌... } ---|
```

全程一步完成，无浏览器、无轮询、无人工干预。

---

## 配额说明

- 默认免费额度：**10 个唯一日期/天**
- 超额返回 429，需登录控制台手动重置
- 不限重置次数

---

## 其他安装方式（备用）

### ClawHub 客户端

```bash
clawhub install zhongguo-nongli-huangli-jixiong
```

### 手动 GitHub 安装

```bash
mkdir -p $HOME/skills
cd $HOME/skills
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leocdchina/huangli-agent-skills
cd huangli-agent-skills
git sparse-checkout set huangli-toolkit
mv huangli-toolkit zhongguo-nongli-huangli-jixiong
```

---

## 环境变量参考

| 变量 | 必填 | 说明 |
|---|---|---|
| `HUANGLI_AUTO_AGENT` | 推荐 | 设为 `1` 自动启用 Agent 模式 |
| `HUANGLI_USERNAME` | 登录必填 | 用户名 |
| `HUANGLI_PASSWORD` | 登录必填 | 密码 |
| `HUANGLI_EMAIL` | 注册必填 | 邮箱（注册时） |
| `HUANGLI_BASE` | 选填 | API 地址，默认 `https://api.nongli.skill.4glz.com` |
| `HUANGLI_TOKEN` | API 调用必填 | 从 auth.py 输出中获取 |

---

## 安装验证

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py status
```

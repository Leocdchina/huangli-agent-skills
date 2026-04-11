# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac

> 面向使用者的统一黄历 Agent Skill 包。

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)
[![English](https://img.shields.io/badge/lang-English-blue)](./README.en.md)

## 这是什么

这是一个可直接提供给 Agent / CLI / Skill 客户端使用的统一黄历技能包。

它包含一个源码技能目录：
- `huangli-toolkit`（发布 slug：`zhongguo-nongli-huangli-jixiong`）

支持三种常见使用方式：
- `by-date`：查询某一天黄历
- `batch`：查询一段日期范围
- `search`：按关键词跨日期检索

---

## 安装方式（按客户端区分）

不同客户端安装方式不同：
- **ClawHub 客户端**：用 `clawhub install zhongguo-nongli-huangli-jixiong`
- **Cursor / Claude Code / OpenClaw**：使用 GitHub 命令安装（稀疏克隆 `huangli-toolkit/` 后复制到本地 skills 目录，目录名为 `zhongguo-nongli-huangli-jixiong`）

完整分流安装步骤见 `INSTALL.md`。

---

## 使用方式一：网页模式

适合人群：
- 想先在网页里注册、登录、查看配额的人
- 想手动复制 Token 给其他工具使用的人
- 想在网页里管理已绑定 CLI 设备的人

### 完整步骤

#### 第 1 步：打开官网
- 官网：https://nongli.skill.4glz.com

#### 第 2 步：注册或登录
- 注册：https://nongli.skill.4glz.com/register
- 登录：https://nongli.skill.4glz.com/login

#### 第 3 步：进入控制台
- 控制台：https://nongli.skill.4glz.com/dashboard

你可以在控制台完成：
- 查看今日配额
- 复制 Token
- 刷新访问凭证
- 管理已绑定 CLI 设备
- logout

#### 第 4 步：复制 Token 并设置环境变量

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

#### 第 5 步：开始使用

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2027-08-08
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py search 甲子日 --year 2027
```

---

## 使用方式二：CLI 模式（一切交给Agent）

适合人群：
- 希望直接在本地终端完成授权的人
- 不想手动复制 Token 的人
- 想让 CLI 自动保存本地环境变量的人

### 完整步骤

#### 第 1 步：确认已安装 Skill（按客户端任选其一）

**A. ClawHub 客户端**

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

**B. Cursor / Claude Code / OpenClaw（GitHub 命令安装）**

按 `INSTALL.md` 中对应客户端的一键命令执行（稀疏克隆 + 复制到本地 skills 目录）。

#### 第 2 步：了解 CLI 模式会写入哪些本地文件

默认情况下，CLI 模式会写入：
- `~/.huangli_token.json`
- `~/.huangli.env`

只有你显式使用 `--append-zshrc` 时，才会修改：
- `~/.zshrc`

如果你不希望改动 shell 配置，可优先使用：

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --print-shell
```

#### 第 3 步：在本地终端发起授权

已有账号：

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login
```

新用户：

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py register
```

#### 第 3 步：在浏览器中完成确认

运行命令后，CLI 会：
- 申请一次性授权码
- 自动打开浏览器授权页
- 等待你在网页里登录或注册并确认授权

#### 第 4 步：加载本地环境变量

授权成功后，CLI 会生成本地文件。执行：

```bash
source ~/.huangli.env
```

如果你想检查当前状态：

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/auth.py status
```

#### 第 5 步：开始使用

```bash
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2027-08-08
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家
python3 skills/zhongguo-nongli-huangli-jixiong/toolkit.py search 甲子日 --year 2027
```

---

## 重要说明

### 配额

1、默认免费额度：10 个唯一日期/天  
2、超额返回429，并提醒用户登录控制台手动重置  
3、不限制重置次数  

### 安全

- 推荐优先使用 `auth.py` 做 CLI 授权
- `python3 skills/zhongguo-nongli-huangli-jixiong/auth.py status` 可检查当前 token 是否仍可使用
- CLI 模式默认写入 `~/.huangli_token.json` 与 `~/.huangli.env`
- 只有显式使用 `--append-zshrc` 时才会修改 `~/.zshrc`
- 如果你不希望修改 shell 配置，优先使用网页模式，或使用 `python3 skills/zhongguo-nongli-huangli-jixiong/auth.py login --print-shell`
- logout 与“取消绑定设备”必须在网页控制台完成

## 更多内容

- 安装到不同客户端：`INSTALL.md`
- 统一技能定义（源码目录）：`huangli-toolkit/SKILL.md`
- 贡献与发布规范：`CONTRIBUTING.md`

## License

MIT

# Install Guide

This package ships one skill folder:
- `huangli-toolkit`

## Step 1: Install the skill

### ClawHub

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

### Manual install

Copy `huangli-toolkit/` into your client’s skill directory.

#### Cursor

```bash
mkdir -p .cursor/skills/huangli
cp -R huangli-toolkit .cursor/skills/huangli/
```

#### Claude Code

```bash
mkdir -p ~/.claude/skills/huangli
cp -R huangli-toolkit ~/.claude/skills/huangli/
```

#### OpenClaw

```bash
mkdir -p ~/.openclaw/skills/huangli
cp -R huangli-toolkit ~/.openclaw/skills/huangli/
```

#### Other skill-capable clients

1. Locate the client skill directory
2. Copy `huangli-toolkit/`
3. Restart the client or refresh skill indexing

---

## Step 2: Choose one mode only

下面两种模式请分开使用，不要混合：
- 模式 A：网页模式
- 模式 B：CLI 模式（一切交给Agent）

---

## 模式 A：网页模式

### 完整步骤

#### 1) 打开官网并登录
- 官网：https://nongli.skill.4glz.com
- 注册：https://nongli.skill.4glz.com/register
- 登录：https://nongli.skill.4glz.com/login
- 控制台：https://nongli.skill.4glz.com/dashboard

#### 2) 在控制台复制 Token

登录后，进入控制台复制你的 Token。

#### 3) 设置环境变量

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

#### 4) 验证是否可用

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
curl "$HUANGLI_BASE/api/quota" \
  -H "Authorization: Bearer $HUANGLI_TOKEN"
```

---

## 模式 B：CLI 模式（一切交给Agent）

### 完整步骤

#### 1) 先了解本地持久化行为

默认情况下，CLI 模式会写入：
- `~/.huangli_token.json`
- `~/.huangli.env`

只有你显式使用 `--append-zshrc` 时，才会修改：
- `~/.zshrc`

如果你不想改动 shell 配置，可使用：

```bash
python3 huangli-toolkit/auth.py login --print-shell
```

#### 2) 在终端发起授权

已有账号：

```bash
python3 huangli-toolkit/auth.py login
```

新用户：

```bash
python3 huangli-toolkit/auth.py register
```

#### 2) 在浏览器中完成确认

CLI 会自动打开浏览器，你只需要在网页中：
- 登录或注册
- 确认把当前账号授权给 CLI

#### 3) 加载本地环境变量

```bash
source ~/.huangli.env
```

#### 4) 检查当前状态

```bash
python3 huangli-toolkit/auth.py status
```

#### 5) 验证是否可用

```bash
python3 huangli-toolkit/toolkit.py by-date 2027-08-08
curl "$HUANGLI_BASE/api/quota" \
  -H "Authorization: Bearer $HUANGLI_TOKEN"
```

#### 6) 可选命令

```bash
python3 huangli-toolkit/auth.py login --print-shell
python3 huangli-toolkit/auth.py login --append-zshrc
```

---

## Troubleshooting

- `401`: token missing, invalid, or expired
- `429`: daily quota exceeded; reset in dashboard
- Skill not triggering: confirm the folder was copied into the correct client skill directory
- For security, logout and device unbinding must be done in the web dashboard

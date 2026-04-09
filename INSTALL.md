# Install Guide (Unified Skill)

This package now ships one unified skill folder:

- `huangli-toolkit`

## 1) 先申请 Token

1. 打开官网：https://nongli.skill.4glz.com
2. 注册：https://nongli.skill.4glz.com/register
3. 登录：https://nongli.skill.4glz.com/login
4. 控制台获取 Token：https://nongli.skill.4glz.com/dashboard

## 2) 配置环境变量

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

## 3) 安装到不同 Agent 客户端

### OpenClaw

```bash
mkdir -p ~/.openclaw/skills/huangli
cp -R huangli-toolkit ~/.openclaw/skills/huangli/
```

### Cursor

```bash
mkdir -p .cursor/skills/huangli
cp -R huangli-toolkit .cursor/skills/huangli/
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/huangli
cp -R huangli-toolkit ~/.claude/skills/huangli/
```

### Gemini CLI / Codex CLI / 其他支持 SKILL.md 的工具

同理：
1. 找到客户端技能目录
2. 复制 `huangli-toolkit/`
3. 重启客户端或刷新技能索引

## 4) 验证

```bash
curl "$HUANGLI_BASE/api/quota" \
  -H "Authorization: Bearer $HUANGLI_TOKEN"

python3 huangli-toolkit/toolkit.py by-date 2027-08-08
```

## 5) 故障排查

- `401`：Token 无效/过期
- `429`：当日额度超限，去控制台重置
- 不触发：确认客户端技能目录和 SKILL.md 支持状态

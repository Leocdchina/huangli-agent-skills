# 安装方式

## 方式一：ClawHub（推荐）

```bash
clawhub install zhongguo-nongli-huangli-jixiong
```

## 方式二：GitHub 手动安装（Cursor / Claude Code / OpenClaw）

### 1. 稀疏克隆

```bash
mkdir -p $HOME/skills
cd $HOME/skills
git clone --depth 1 --filter=blob:none --sparse https://github.com/Leocdchina/huangli-agent-skills
cd huangli-agent-skills
git sparse-checkout set huangli-toolkit
mv huangli-toolkit zhongguo-nongli-huangli-jixiong
```

### 2. AI Agent 自主认证

```bash
export HUANGLI_USERNAME="your_username"
export HUANGLI_PASSWORD="your_password"
export HUANGLI_AUTO_AGENT=1

python3 $HOME/skills/zhongguo-nongli-huangli-jixiong/auth.py login
```

注册：
```bash
export HUANGLI_AUTO_AGENT=1
python3 $HOME/skills/zhongguo-nongli-huangli-jixiong/auth.py register --email=you@example.com
```

### 3. 验证

```bash
python3 $HOME/skills/zhongguo-nongli-huangli-jixiong/toolkit.py by-date 2026-05-03
```

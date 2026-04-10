# 中国农历黄历吉凶 · Zhongguo Nongli Huangli Jixiong · China Lunar Almanac

> 面向使用者的统一黄历 Agent Skill 包。

[![Release](https://img.shields.io/github/v/release/Leocdchina/huangli-agent-skills?display_name=tag)](https://github.com/Leocdchina/huangli-agent-skills/releases)
[![License](https://img.shields.io/github/license/Leocdchina/huangli-agent-skills)](./LICENSE)
[![English](https://img.shields.io/badge/lang-English-blue)](./README.en.md)

## 这是什么

这是一个可直接提供给 Agent / CLI / Skill 客户端使用的统一黄历技能包。

它包含一个技能目录：
- `huangli-toolkit`

支持三种常见使用方式：
- `by-date`：查询某一天黄历
- `batch`：查询一段日期范围
- `search`：按关键词跨日期检索

---

## 最快开始

### 1) 安装 Skill

```bash
clawhub login
clawhub install zhongguo-nongli-huangli-jixiong
```

如果你不是用 ClawHub，请看 `INSTALL.md`。

### 2) 获取 Token

- 官网：https://nongli.skill.4glz.com
- 注册：https://nongli.skill.4glz.com/register
- 登录：https://nongli.skill.4glz.com/login
- 控制台：https://nongli.skill.4glz.com/dashboard

你可以：
- 直接在控制台复制 Token
- 或使用内置安全 CLI 授权：

```bash
python3 huangli-toolkit/auth.py login
source ~/.huangli.env
```

也可用：

```bash
python3 huangli-toolkit/auth.py register
python3 huangli-toolkit/auth.py status
```

### 3) 开始使用

```bash
# 单日查询
python3 huangli-toolkit/toolkit.py by-date 2027-08-08

# 批量查询
python3 huangli-toolkit/toolkit.py batch 2027-08-01 2027-08-31 --filter 搬家

# 关键词搜索
python3 huangli-toolkit/toolkit.py search 甲子日 --year 2027
```

---

## 使用说明

### 环境变量

```bash
export HUANGLI_TOKEN="your_token_here"
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"
```

### 配额

1、默认免费额度：10 个唯一日期/天  
2、超额返回429，并提醒用户登录控制台手动重置  
3、不限制重置次数  

### 安全说明

- 推荐优先使用 `auth.py` 做安全 CLI 授权
- `python3 huangli-toolkit/auth.py status` 可检查本地 token 是否仍可使用
- logout 与“取消绑定设备”必须在网页控制台完成

---

## 更多内容

- 安装到不同客户端：`INSTALL.md`
- 统一技能定义：`huangli-toolkit/SKILL.md`

## License

MIT

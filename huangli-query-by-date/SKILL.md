---
name: huangli-query-by-date
license: MIT
compatibility: Requires Python 3.7+ or bash with curl. Set HUANGLI_TOKEN env var (Bearer token from https://nongli.skill.4glz.com/dashboard). Needs HTTPS outbound access to api.nongli.skill.4glz.com. Daily quota is 10 unique dates/day with one manual reset after login.
description: |
  Use this skill when the user asks about one specific day’s 黄历 (宜忌、吉时、干支、农历等),
  including requests like “今天适合搬家吗” or “2027-08-08 的吉时”.

  Before calling the API, convert natural-language time into one concrete date (YYYY-MM-DD).
  Call GET /api/lunar/date/{YYYY-MM-DD} for single-date lookup.

  If the user asks for a range (本周/下月/未来7天), switch to huangli-query-batch instead.
  Daily quota is 10 unique dates/day; repeated same-date queries do not duplicate quota usage.
---

# 黄历日期查询 (Huangli Query by Date)

## Setup

```bash
export HUANGLI_TOKEN="your_token_here"          # required
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"   # optional, this is the default
```

Get your token at: https://nongli.skill.4glz.com/dashboard

## Quick Use

```bash
curl "$HUANGLI_BASE/api/lunar/date/2027-08-08" \
  -H "Authorization: Bearer $HUANGLI_TOKEN"
```

## Agent Pattern

When user asks: **「明天宜不宜搬家？」**

```python
from datetime import date, timedelta
import os, requests

HEADERS = {"Authorization": f"Bearer {os.environ['HUANGLI_TOKEN']}"}
BASE = os.environ.get("HUANGLI_BASE", "https://api.nongli.skill.4glz.com")

target = (date.today() + timedelta(days=1)).isoformat()
resp = requests.get(f"{BASE}/api/lunar/date/{target}", headers=HEADERS)
resp.raise_for_status()
data = resp.json()

is_good_for_moving = "搬家" in data.get("suitable_activities", [])
print(target, is_good_for_moving, data["lunar_info"])
```

## Key Response Fields

| Field | Description |
|-------|-------------|
| `solar_date` | Gregorian date, YYYY-MM-DD |
| `lunar_info` | Lunar date in Chinese, e.g. 二月初二 |
| `ganzhi_day` | Day ganzhi, e.g. 癸巳日 |
| `suitable_activities` | List of auspicious activities |
| `unsuitable_activities` | List of inauspicious activities |
| `auspicious_hours` | 12-period map with suitable activities per hour |
| `solar_term` | Solar term if applicable, else null |
| `_quota` | Current quota status |

## Error Handling

| Status | Meaning | Action |
|--------|---------|--------|
| 200 | OK | Use response data |
| 401 | Token missing or expired | Prompt user to check HUANGLI_TOKEN |
| 404 | Date not found in current dataset | Inform user to try another date |
| 429 | Daily quota exceeded | Inform user to reset in dashboard after login |

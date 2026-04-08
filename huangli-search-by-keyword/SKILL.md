---
name: huangli-search-by-keyword
license: MIT
compatibility: Requires Python 3.7+. Set HUANGLI_TOKEN env var (Bearer token from https://nongli.skill.4glz.com/dashboard). Needs HTTPS outbound access to api.nongli.skill.4glz.com. Daily quota is 10 unique dates/day with one manual reset after login.
description: |
  Use this skill when the user asks for keyword-based 黄历 search across a period,
  e.g. “2027年哪些日子是甲子日”, “摩羯座日期”, or “哪些天宜搬家”.

  There is no server-side search endpoint. Expand date range first,
  fetch records with huangli-query-batch (preferred) or single-date fallback,
  then filter locally by target field (ganzhi_day / constellation / lunar_day_cn / suitable_activities).

  Keep ranges tight to reduce quota usage (10 unique dates/day for free users).
---

# 黄历关键词搜索 (Huangli Search by Keyword)

## Setup

```bash
export HUANGLI_TOKEN="your_token_here"          # required
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"   # optional
```

Get your token at: https://nongli.skill.4glz.com/dashboard

## Quick Use

```bash
# Search within one month by pulling data in batch, then filter locally
python search.py 搬家 --start 2027-08-01 --end 2027-08-31
```

## Supported Keyword Types

| Keyword Pattern | Matches Field | Example |
|-----------------|---------------|---------|
| 3-char ganzhi + 日 | `ganzhi_day` | `甲子日`, `庚午日`, `壬寅日` |
| XX座 (constellation) | `constellation` | `摩羯座`, `天蝎座`, `狮子座` |
| 初X / 十X / 二十X (lunar day) | `lunar_day_cn` | `初一`, `十五`, `三十` |
| Other terms | `suitable_activities` | `搬家`, `结婚`, `开业` |

## Agent Pattern

When user asks: **「2027年 8 月哪些日子宜搬家？」**

```python
import os, requests
from datetime import date, timedelta

HEADERS = {
    "Authorization": f"Bearer {os.environ['HUANGLI_TOKEN']}",
    "Content-Type": "application/json",
}
BASE = os.environ.get("HUANGLI_BASE", "https://api.nongli.skill.4glz.com")

start = date(2027, 8, 1)
end = date(2027, 8, 31)
dates = []
current = start
while current <= end:
    dates.append(current.isoformat())
    current += timedelta(days=1)

resp = requests.post(
    f"{BASE}/api/lunar/batch",
    headers=HEADERS,
    json={"dates": dates},
)
resp.raise_for_status()
payload = resp.json()

matches = [
    item for item in payload["results"]
    if "搬家" in item.get("suitable_activities", [])
]
for item in matches:
    print(item["solar_date"], item["lunar_info"], item["ganzhi_day"])
```

## Quota Warning

Large date-range searches consume many unique dates.
- For small checks, query only the needed week/month
- For long ranges, split requests by smaller windows
- If quota is exceeded (429), reset in dashboard and continue

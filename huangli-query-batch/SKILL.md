---
name: huangli-query-batch
license: MIT
compatibility: Requires Python 3.7+ or bash with curl. Set HUANGLI_TOKEN env var (Bearer token from https://nongli.skill.4glz.com/dashboard). Needs HTTPS outbound access to api.nongli.skill.4glz.com. Daily quota is 10 unique dates/day with one manual reset after login.
description: |
  Use this skill when the user asks for multiple dates or a time range,
  such as “下月哪天适合搬家” or “本周每天宜忌”.

  First expand natural-language time to concrete YYYY-MM-DD date list,
  then call POST /api/lunar/batch (max 100 dates/request, chunk if needed).

  This skill is preferred over repeated single-date calls for ranges and comparisons.
  Daily quota is 10 unique dates/day; repeated same-date queries do not duplicate quota usage.
---

# 黄历批量查询 (Huangli Query Batch)

## Setup

```bash
export HUANGLI_TOKEN="your_token_here"          # required
export HUANGLI_BASE="https://api.nongli.skill.4glz.com"   # optional
```

Get your token at: https://nongli.skill.4glz.com/dashboard

## Quick Use

```bash
curl "$HUANGLI_BASE/api/lunar/batch" \
  -X POST \
  -H "Authorization: Bearer $HUANGLI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"dates":["2027-08-01","2027-08-02","2027-08-03"]}'
```

## Agent Pattern

When user asks: **「下月有哪些搬家吉日？」**

```python
import calendar, os, requests
from datetime import date

HEADERS = {
    "Authorization": f"Bearer {os.environ['HUANGLI_TOKEN']}",
    "Content-Type": "application/json",
}
BASE = os.environ.get("HUANGLI_BASE", "https://api.nongli.skill.4glz.com")

# 1. Expand "下月" into all dates of next month
now = date.today()
year = now.year + (1 if now.month == 12 else 0)
month = 1 if now.month == 12 else now.month + 1
_, days = calendar.monthrange(year, month)
dates = [date(year, month, day).isoformat() for day in range(1, days + 1)]

# 2. Call batch API once
resp = requests.post(
    f"{BASE}/api/lunar/batch",
    headers=HEADERS,
    json={"dates": dates},
)
resp.raise_for_status()
payload = resp.json()

# 3. Filter good moving days
good_days = [
    item for item in payload["results"]
    if "搬家" in item.get("suitable_activities", [])
]
print([item["solar_date"] for item in good_days])
```

## Key Response Fields

| Field | Description |
|-------|-------------|
| `results` | Array of daily 黄历 records |
| `requested_dates` | The normalized date list sent to the API |
| `returned_count` | Number of records successfully returned |
| `missing_dates` | Dates with no data in the available range |
| `_quota` | Current quota status after the batch request |

## Notes

- Request body must be `{ "dates": ["YYYY-MM-DD", ...] }`
- Maximum 100 dates per request
- Use batch after expanding natural-language time ranges
- Repeated dates do not consume extra quota
- Missing dates are returned in `missing_dates`

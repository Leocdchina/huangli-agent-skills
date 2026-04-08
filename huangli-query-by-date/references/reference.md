# Response Schema Reference — huangli-query-by-date

Full 29-field schema for `GET /api/lunar/date/{YYYY-MM-DD}`.

## Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `solar_date` | string | Gregorian date, format YYYY-MM-DD |
| `lunar_info` | string | Full lunar date in Chinese, e.g. `二月初二` |
| `lunar_month_cn` | string | Lunar month, e.g. `二月` |
| `lunar_day_cn` | string | Lunar day, e.g. `初二` |
| `is_leap_month` | bool | Whether this is a leap lunar month |
| `ganzhi_year` | string | Year ganzhi, e.g. `丙午年` |
| `ganzhi_month` | string | Month ganzhi, e.g. `丁卯月` |
| `ganzhi_day` | string | Day ganzhi, e.g. `癸巳日` |
| `heavenly_stem` | string | Heavenly stem (天干) of the day |
| `earthly_branch` | string | Earthly branch (地支) of the day |
| `day_element` | string | Five-element of the day: 金/木/水/火/土 |
| `constellation` | string | Western zodiac constellation, e.g. `双鱼座` |
| `zodiac` | string | Chinese zodiac animal, e.g. `马` |
| `suitable_activities` | array\<string\> | Activities that are auspicious today |
| `unsuitable_activities` | array\<string\> | Activities that are inauspicious today |
| `auspicious_hours` | object | Map of 12 time periods → hour detail (see below) |
| `solar_term` | string\|null | Solar term name if today is one, else null |
| `is_holiday` | bool | Whether today is a Chinese public holiday |
| `holiday_name` | string\|null | Name of the holiday, else null |
| `chongsha` | string | Conflicting zodiac and direction, e.g. `冲猪 丁亥 煞东` |
| `taishen` | string | Location of the fetal god (胎神) |
| `jishen` | string | Auspicious deities present today (吉神) |
| `xingshen` | string | Day officer / value deity (值神) |
| `xiongsha` | string | Inauspicious deities present today (凶煞) |
| `_quota` | object | Quota status appended to every response (see below) |

## auspicious_hours Object

Each key is a ganzhi hour name (e.g. `甲子时`). Value:

```json
{
  "甲子时": {
    "time": "23:00-0:59",
    "chongsha": "冲马 煞南",
    "suitable": ["祈福", "出行"],
    "unsuitable": []
  }
}
```

| Sub-field | Type | Description |
|-----------|------|-------------|
| `time` | string | Time range for this period, e.g. `23:00-0:59` |
| `chongsha` | string | Conflict/inauspicious direction for this hour |
| `suitable` | array\<string\> | Activities auspicious in this hour |
| `unsuitable` | array\<string\> | Activities inauspicious in this hour |

## _quota Object

Appended to every successful response. Does **not** consume quota itself.

```json
{
  "used_today": 1,
  "limit": 2,
  "is_paid": false,
  "resets_at": "2026-03-21"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `used_today` | int | Unique dates queried today |
| `limit` | int\|null | Daily limit; null for paid users (unlimited) |
| `is_paid` | bool | Whether the user has an active paid subscription |
| `resets_at` | string | Date when quota resets (next calendar day, UTC+8) |

## Data Range

- Coverage: **2026-01-01 to 2035-12-31** (3,652 days)
- Dates outside this range return HTTP 404

## Common suitable_activities Values

祈福、出行、搬家、装修、结婚、入宅、领证、理发、开业、开工、  
安葬、交易、动土、立券、栽种、纳畜、沐浴、破土、安床、嫁娶

#!/usr/bin/env python3
"""search.py — Search 黄历 data by keyword via client-side filtering.

Calls GET /api/lunar/date/{date} for each day in range and filters locally.
Does NOT use a server-side search endpoint.

Usage:
    python search.py KEYWORD
    python search.py KEYWORD --start 2027-01-01 --end 2027-12-31
    python search.py KEYWORD --year 2027
    python search.py 甲子日
    python search.py 摩羯座 --year 2027
    python search.py 初一 --start 2027-01-01 --end 2027-06-30
    python search.py 搬家 --year 2027

Env vars:
    HUANGLI_TOKEN  (required) Bearer token
    HUANGLI_BASE   (optional) API base URL, default: https://api.nongli.skill.4glz.com

Supported keyword types:
    ganzhi day  : 甲子日, 庚午日, 壬寅日, ... (3-char + 日)
    constellation: 摩羯座, 天蝎座, 狮子座, ...
    lunar day   : 初一, 十五, 三十, ...
    activity    : 搬家, 结婚, 开业, 理发, ...
"""
import sys
import os
import json
import urllib.request
import urllib.error
from datetime import date, timedelta

# ── Keyword classifier ───────────────────────────────────────────────────────

GANZHI_STEMS = set("甲乙丙丁戊己庚辛壬癸")
GANZHI_BRANCHES = set("子丑寅卯辰巳午未申酉戌亥")
CONSTELLATIONS = {
    "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
    "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座",
}
LUNAR_DAYS = {
    "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
    "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
    "二十一", "二十二", "二十三", "二十四", "二十五", "二十六", "二十七", "二十八", "二十九", "三十",
}


def classify_keyword(kw: str):
    """Return (field, value) tuple for filtering."""
    if kw in CONSTELLATIONS:
        return "constellation", kw
    if kw in LUNAR_DAYS:
        return "lunar_day_cn", kw
    # ganzhi day: exactly 3 chars, first is stem, second is branch, third is 日
    if len(kw) == 3 and kw[0] in GANZHI_STEMS and kw[1] in GANZHI_BRANCHES and kw[2] == "日":
        return "ganzhi_day", kw
    # Fallback: search in suitable_activities
    return "suitable_activities", kw


def matches(record: dict, field: str, value: str) -> bool:
    v = record.get(field)
    if v is None:
        return False
    if isinstance(v, list):
        return value in v
    return v == value


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python search.py KEYWORD [--start YYYY-MM-DD] [--end YYYY-MM-DD] [--year YYYY]",
              file=sys.stderr)
        sys.exit(1)

    keyword = args[0]

    # Parse optional flags
    start_str = end_str = year_str = None
    i = 1
    while i < len(args):
        if args[i] == "--start" and i + 1 < len(args):
            start_str = args[i + 1]; i += 2
        elif args[i] == "--end" and i + 1 < len(args):
            end_str = args[i + 1]; i += 2
        elif args[i] == "--year" and i + 1 < len(args):
            year_str = args[i + 1]; i += 2
        else:
            i += 1

    # Determine date range
    if year_str:
        start = date(int(year_str), 1, 1)
        end = date(int(year_str), 12, 31)
    elif start_str and end_str:
        start = date.fromisoformat(start_str)
        end = date.fromisoformat(end_str)
    else:
        # Default range: current year
        y = date.today().year
        start = date(y, 1, 1)
        end = date(y, 12, 31)

    # Clamp to available data range
    data_start = date(2026, 1, 1)
    data_end = date(2035, 12, 31)
    start = max(start, data_start)
    end = min(end, data_end)

    if start > end:
        print("Error: start date is after end date.", file=sys.stderr)
        sys.exit(1)

    base = os.environ.get("HUANGLI_BASE", "https://api.nongli.skill.4glz.com").rstrip("/")
    token = os.environ.get("HUANGLI_TOKEN", "")

    if not token:
        print("Error: HUANGLI_TOKEN is not set.", file=sys.stderr)
        print(f"Get your token at: {base}/dashboard", file=sys.stderr)
        sys.exit(1)

    field, value = classify_keyword(keyword)
    total_days = (end - start).days + 1

    print(f"# Searching '{keyword}' in field '{field}' across {total_days} days ({start} to {end})",
          file=sys.stderr)

    results = []
    quota_hit = False
    current = start

    while current <= end:
        url = f"{base}/api/lunar/date/{current.isoformat()}"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req) as resp:
                record = json.loads(resp.read())
            if matches(record, field, value):
                results.append(record)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(
                    f"\nQuota exceeded at {current} — stopping early.\n"
                    f"Reset once in dashboard, then continue: {base}/dashboard",
                    file=sys.stderr,
                )
                quota_hit = True
                break
            elif e.code == 404:
                pass  # date out of range, skip silently
            else:
                print(f"HTTP {e.code} for {current} — skipping", file=sys.stderr)
        except urllib.error.URLError as e:
            print(f"Connection error: {e.reason}", file=sys.stderr)
            sys.exit(1)
        current += timedelta(days=1)

    output = {"keyword": keyword, "field": field, "count": len(results), "data": results}
    if quota_hit:
        output["warning"] = "Results are incomplete — daily quota was exceeded."

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

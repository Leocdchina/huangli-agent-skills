#!/usr/bin/env python3
"""query.py — Batch query 黄历 via POST /api/lunar/batch.

Usage:
    python query.py START_DATE END_DATE
    python query.py 2027-08-01 2027-08-31
    python query.py 2027-08-01 2027-08-31 --filter 搬家

Env vars:
    HUANGLI_TOKEN  (required) Bearer token from https://nongli.skill.4glz.com/dashboard
    HUANGLI_BASE   (optional) API base URL, default: https://api.nongli.skill.4glz.com

Notes:
    - Uses POST /api/lunar/batch (max 100 dates/request), chunked automatically.
    - Daily quota: 10 unique dates/day for free users.
"""
import sys
import os
import json
import urllib.request
import urllib.error
from datetime import date, timedelta


def chunked(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def make_dates(start: date, end: date):
    out = []
    current = start
    while current <= end:
        out.append(current.isoformat())
        current += timedelta(days=1)
    return out


def post_batch(base: str, token: str, dates):
    body = json.dumps({"dates": dates}).encode("utf-8")
    req = urllib.request.Request(
        f"{base}/api/lunar/batch",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    if len(sys.argv) < 3:
        print("Usage: python query.py START_DATE END_DATE [--filter ACTIVITY]", file=sys.stderr)
        sys.exit(1)

    start = date.fromisoformat(sys.argv[1])
    end = date.fromisoformat(sys.argv[2])

    filter_activity = None
    if "--filter" in sys.argv:
        idx = sys.argv.index("--filter")
        if idx + 1 < len(sys.argv):
            filter_activity = sys.argv[idx + 1]

    base = os.environ.get("HUANGLI_BASE", "https://api.nongli.skill.4glz.com").rstrip("/")
    token = os.environ.get("HUANGLI_TOKEN", "")

    if not token:
        print("Error: HUANGLI_TOKEN is not set.", file=sys.stderr)
        print(f"Get your token at: {base}/dashboard", file=sys.stderr)
        sys.exit(1)

    if start > end:
        print("Error: start date is after end date", file=sys.stderr)
        sys.exit(1)

    if (end - start).days > 365:
        print("Error: date range too large (max 365 days)", file=sys.stderr)
        sys.exit(1)

    dates = make_dates(start, end)
    all_results = []
    requested_dates = []
    missing_dates = []
    quota = None

    try:
        for part in chunked(dates, 100):
            payload = post_batch(base, token, part)
            all_results.extend(payload.get("results", []))
            requested_dates.extend(payload.get("requested_dates", part))
            missing_dates.extend(payload.get("missing_dates", []))
            quota = payload.get("_quota", quota)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 401:
            print("Error: Unauthorized. Check your HUANGLI_TOKEN.", file=sys.stderr)
        elif e.code == 429:
            print(f"Error: Daily quota exceeded. Reset in dashboard: {base}/dashboard", file=sys.stderr)
            try:
                print(json.dumps(json.loads(body), ensure_ascii=False, indent=2), file=sys.stderr)
            except Exception:
                pass
        else:
            print(f"Error: HTTP {e.code}\n{body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Error: Cannot connect to {base}\n{e.reason}", file=sys.stderr)
        sys.exit(1)

    if filter_activity:
        all_results = [
            item for item in all_results
            if filter_activity in item.get("suitable_activities", [])
        ]

    output = {
        "count": len(all_results),
        "requested_dates": requested_dates,
        "missing_dates": missing_dates,
        "data": all_results,
    }
    if quota is not None:
        output["_quota"] = quota

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""query.py — Query 黄历 data for a specific date.

Usage:
    python query.py YYYY-MM-DD
    python query.py 2027-08-08

Env vars:
    HUANGLI_TOKEN  (required) Bearer token from https://nongli.skill.4glz.com/dashboard
    HUANGLI_BASE   (optional) API base URL, default: https://api.nongli.skill.4glz.com
"""
import sys
import os
import json
import urllib.request
import urllib.error
from datetime import date


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()
    base = os.environ.get("HUANGLI_BASE", "https://api.nongli.skill.4glz.com").rstrip("/")
    token = os.environ.get("HUANGLI_TOKEN", "")

    if not token:
        print("Error: HUANGLI_TOKEN is not set.", file=sys.stderr)
        print(f"Get your token at: {base}/dashboard", file=sys.stderr)
        sys.exit(1)

    url = f"{base}/api/lunar/date/{date_str}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
        print(json.dumps(data, ensure_ascii=False, indent=2))

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 401:
            print("Error: Unauthorized. Check your HUANGLI_TOKEN.", file=sys.stderr)
        elif e.code == 404:
            print(f"Error: No data for {date_str}. Data covers 2026-01-01 to 2035-12-31.", file=sys.stderr)
        elif e.code == 429:
            print(f"Error: Daily quota exceeded. Upgrade at {base}/dashboard", file=sys.stderr)
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


if __name__ == "__main__":
    main()

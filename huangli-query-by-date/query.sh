#!/usr/bin/env bash
# query.sh — Query 黄历 data for a specific date
# Usage:   ./query.sh YYYY-MM-DD
# Example: ./query.sh 2027-08-08
#
# Env vars:
#   HUANGLI_TOKEN  (required) Bearer token from https://nongli.skill.4glz.com/dashboard
#   HUANGLI_BASE   (optional) API base URL, default: https://api.nongli.skill.4glz.com

set -euo pipefail

DATE="${1:-$(date +%Y-%m-%d)}"
BASE="${HUANGLI_BASE:-https://api.nongli.skill.4glz.com}"
TOKEN="${HUANGLI_TOKEN:-}"

if [ -z "$TOKEN" ]; then
  echo "Error: HUANGLI_TOKEN is not set." >&2
  echo "Get your token at: $BASE/dashboard" >&2
  exit 1
fi

# Validate date format
if ! echo "$DATE" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'; then
  echo "Error: invalid date format '$DATE'. Expected YYYY-MM-DD." >&2
  exit 1
fi

HTTP_CODE=$(curl -s -o /tmp/huangli_response.json -w "%{http_code}" \
  -H "Authorization: Bearer $TOKEN" \
  "$BASE/api/lunar/date/$DATE")

case "$HTTP_CODE" in
  200)
    python3 -m json.tool /tmp/huangli_response.json
    ;;
  401)
    echo "Error: Unauthorized. Check your HUANGLI_TOKEN." >&2
    exit 1
    ;;
  404)
    echo "Error: No data for $DATE. Data covers 2026-01-01 to 2035-12-31." >&2
    exit 1
    ;;
  429)
    echo "Error: Daily quota exceeded. Upgrade at $BASE/dashboard" >&2
    python3 -m json.tool /tmp/huangli_response.json >&2 || true
    exit 1
    ;;
  *)
    echo "Error: HTTP $HTTP_CODE" >&2
    cat /tmp/huangli_response.json >&2
    exit 1
    ;;
esac

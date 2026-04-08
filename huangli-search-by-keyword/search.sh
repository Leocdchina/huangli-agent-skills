#!/usr/bin/env bash
# search.sh — Search 黄历 data by keyword via client-side filtering.
# Delegates to search.py which calls the single-date API for each day in range.
#
# Usage:
#   ./search.sh KEYWORD
#   ./search.sh KEYWORD --year 2026
#   ./search.sh KEYWORD --start 2026-01-01 --end 2026-06-30
#
# Examples:
#   ./search.sh 甲子日
#   ./search.sh 摩羯座 --year 2026
#   ./search.sh 初一 --year 2027
#   ./search.sh 搬家 --start 2026-01-01 --end 2026-12-31
#
# Env vars:
#   HUANGLI_TOKEN  (required) Bearer token — paid account recommended
#   HUANGLI_BASE   (optional) API base URL, default: https://api.nongli.skill.4glz.com

set -euo pipefail

KEYWORD="${1:?Usage: ./search.sh KEYWORD [--year YYYY | --start DATE --end DATE]}"
shift

BASE="${HUANGLI_BASE:-https://api.nongli.skill.4glz.com}"
TOKEN="${HUANGLI_TOKEN:-}"

if [ -z "$TOKEN" ]; then
  echo "Error: HUANGLI_TOKEN is not set." >&2
  echo "Get your token at: $BASE/dashboard" >&2
  exit 1
fi

# Delegate to search.py in the same directory
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$DIR/search.py" "$KEYWORD" "$@"

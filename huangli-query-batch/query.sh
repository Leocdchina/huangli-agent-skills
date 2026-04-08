#!/usr/bin/env bash
# query.sh — Batch query 黄历 via POST /api/lunar/batch
# Usage:   ./query.sh START_DATE END_DATE
# Example: ./query.sh 2027-08-01 2027-08-31
#
# Env vars:
#   HUANGLI_TOKEN  (required) Bearer token from https://nongli.skill.4glz.com/dashboard
#   HUANGLI_BASE   (optional) API base URL, default: https://api.nongli.skill.4glz.com

set -euo pipefail

START="${1:?Usage: ./query.sh START_DATE END_DATE}"
END="${2:?Usage: ./query.sh START_DATE END_DATE}"
BASE="${HUANGLI_BASE:-https://api.nongli.skill.4glz.com}"
TOKEN="${HUANGLI_TOKEN:-}"

if [ -z "$TOKEN" ]; then
  echo "Error: HUANGLI_TOKEN is not set." >&2
  echo "Get your token at: $BASE/dashboard" >&2
  exit 1
fi

DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$DIR/query.py" "$START" "$END"

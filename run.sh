#!/usr/bin/env bash
# run.sh — push vibestudio.py to an active Colab session and execute it.
# Usage: ./run.sh <notebook_id> [script_args]
#
# NOTEBOOK_ID: the alphanumeric ID from your Colab URL
#   https://colab.research.google.com/drive/<NOTEBOOK_ID>
#
# Requirements: colab-cli installed and authenticated (`colab auth login`)

set -euo pipefail

NOTEBOOK_ID="${1:?Usage: ./run.sh <notebook_id>}"

echo "📤 Pushing vibestudio.py to Colab runtime..."
colab-cli push "$NOTEBOOK_ID" vibestudio.py

echo "▶️  Executing on Colab..."
colab-cli exec "$NOTEBOOK_ID" "exec(open('vibestudio.py').read())"

echo "✅ Done — check Colab runtime + Google Drive for output."

#!/usr/bin/env bash
set -euo pipefail
set -x

echo "Testing 'edit' command..."
TEMP_DIR=$(mktemp -d)

export RUNBOOK_WORKING_DIR="$TEMP_DIR"

runbook init --skip-confirmation=true
runbook create test-notebook.ipynb
runbook edit runbooks/binder/test-notebook.ipynb

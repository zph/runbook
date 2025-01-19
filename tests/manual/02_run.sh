#!/usr/bin/env bash
set -euo pipefail

echo "Testing 'run' command..."
TEMP_DIR=$(mktemp -d)

export RUNBOOK_WORKING_DIR="$TEMP_DIR"

runbook init --skip-confirmation=true

# Test non-interactive run
echo "Testing non-interactive run..."
runbook run --no-interactive runbooks/binder/_template-deno.ipynb --output output.ipynb

# Verify output file exists
if [ -f "output.ipynb" ]; then
    echo "✅ Non-interactive run successful"
else
    echo "❌ Non-interactive run failed - output file not created"
    exit 1
fi

# Test interactive run
echo "Testing interactive run..."
runbook run runbooks/binder/_template-deno.ipynb

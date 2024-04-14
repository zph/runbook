#!/usr/bin/env bash

set -eou pipefail

export RUNBOOK_HELP="$(poetry run runbook --help)"

envsubst < ".config/README.md.template" > README.md

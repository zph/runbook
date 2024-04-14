#!/usr/bin/env bash

set -eou pipefail
set -x

export RUNBOOK_HELP="$(poetry run runbook --help)"

envsubst < ".config/README.md.template"

#!/usr/bin/env bash

set -eou pipefail

export RUNBOOK_HELP="$(runbook --help)"

envsubst < ".config/README.md.template" > README.md

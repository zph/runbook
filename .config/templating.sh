#!/usr/bin/env bash

set -eou pipefail

export RUNBOOK_HELP="$(runbook --help)"
export RUNBOOK_VERSION="$(runbook version | grep -i version | awk '{print $3}')"

envsubst < ".config/README.md.template" > README.md

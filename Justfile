plan NOTEBOOK NEW_NOTEBOOK *FLAGS:
  papermill {{NOTEBOOK}} {{NEW_NOTEBOOK}} --prepare-only {{FLAGS}}
  jupyter nbconvert --clear-output --inplace {{NEW_NOTEBOOK}}
  # TODO: make this SHA suffix the new notebook?

apply NOTEBOOK:
  open {{NOTEBOOK}}

new NAME:
  #!/usr/bin/env bash

  set -eou pipefail

  ts="$(date -Idate)"
  cp -v runbooks/_template.ipynb runbooks/${ts}-{{NAME}}.ipynb
  perl -p -i -e "s/DATE_REGEX/${ts}/" runbooks/${ts}-{{NAME}}.ipynb

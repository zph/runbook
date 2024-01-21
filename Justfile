open NOTEBOOK:
  poetry run jupyter notebook {{NOTEBOOK}}

plan NOTEBOOK NEW_NOTEBOOK *FLAGS:
  papermill {{NOTEBOOK}} {{NEW_NOTEBOOK}} --prepare-only {{FLAGS}}
  jupyter nbconvert --clear-output --inplace {{NEW_NOTEBOOK}}
  # TODO: make this SHA suffix the new notebook?

new NAME:
  #!/usr/bin/env bash

  set -eou pipefail

  ts="$(date -Idate)"
  cp -v runbooks/_template.ipynb runbooks/${ts}-{{NAME}}.ipynb
  perl -p -i -e "s/DATE_REGEX/${ts}/" runbooks/${ts}-{{NAME}}.ipynb

clear-binder-output:
  jupyter nbconvert --clear-output --inplace ./runbooks/binder/*.ipynb

clear-output *FILES:
  jupyter nbconvert --clear-output --inplace {{FILES}}

template-update:
  #!/usr/bin/env bash

  set -eou pipefail
  set -x
  f="./runbooks/binder/_template.ipynb"
  d="./runbook/template.py"
  echo 'TEMPLATE = """' > $d
  base64 < "$f" >> "$d"
  echo '"""' >> "$d"

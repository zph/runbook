open NOTEBOOK:
  poetry run runbook edit {{NOTEBOOK}}

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

profile:
  poetry run python3 -m cProfile runbook/cli/__init__.py

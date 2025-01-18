test:
  uv run pytest --disable-warnings -s

test-watch:
  watchexec -- pytest --disable-warnings -s

open NOTEBOOK:
  uv run runbook edit {{NOTEBOOK}}

clear-binder-output:
  jupyter nbconvert --clear-output --inplace ./runbooks/binder/*.ipynb

clear-output *FILES:
  jupyter nbconvert --clear-output --inplace {{FILES}}

lint:
  pre-commit run

lint-all:
  pre-commit run --all-files

profile:
  uv run python3 -m cProfile runbook/cli/__init__.py

release:
  release-it

clean:
  rm -rf ./dist

build:
  uv build

benchmark:
  hyperfine --export-markdown=PERFORMANCE.md -- runbook

template-update:
  #!/usr/bin/env bash

  set -eou pipefail

  readonly UPDATED_AT="$(date -Iseconds)"
  export UPDATED_AT
  # Base 64 to avoid corruption during parsing/exporting
  readonly TEMPLATE_DENO="$(uv run jupyter nbconvert --log-level='ERROR' runbooks/binder/_template-deno.ipynb --stdout --clear-output --ClearMetadataPreprocessor.enabled=True \
      --ClearMetadataPreprocessor.preserve_cell_metadata_mask='[("tags")]' "--ClearMetadataPreprocessor.clear_notebook_metadata=False"  | grep -E -v "^poetry-version-plugin" | base64)"
  export TEMPLATE_DENO
  readonly TEMPLATE_PYTHON="$(uv run jupyter nbconvert --log-level='ERROR' runbooks/binder/_template-python.ipynb --stdout --clear-output --ClearMetadataPreprocessor.enabled=True \
      --ClearMetadataPreprocessor.preserve_cell_metadata_mask='[("tags")]' "--ClearMetadataPreprocessor.clear_notebook_metadata=False"  | grep -E -v "^poetry-version-plugin" | base64)"
  export TEMPLATE_PYTHON
  envsubst < runbook/template_builder.py | tee runbook/template.py

readme:
  .config/templating.sh

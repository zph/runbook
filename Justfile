test:
  uv run pytest --disable-warnings -s
  deno test -A --reload https://raw.githubusercontent.com/zph/runbook/main/ext/deno/runbook/mod.ts --parallel tests/cli_test.ts

test-watch:
  watchexec -- just test

open NOTEBOOK:
  uv run runbook edit {{NOTEBOOK}}

clear-binder-output:
  jupyter nbconvert --clear-output --inplace ./runbook/data/*.ipynb

clear-output *FILES:
  jupyter nbconvert --clear-output --inplace {{FILES}}

lint:
  pre-commit run

lint-all:
  pre-commit run --all-files

profile:
  uv run python3 -m cProfile runbook/cli/__init__.py

release:
  deno run -A npm:release-it

clean:
  rm -rf ./dist

build:
  uv build

benchmark:
  hyperfine --export-markdown=docs/PERFORMANCE.md -- runbook

readme:
  .config/templating.sh

docs:
  cp -f README.md docs/
  uvx --with sphinx-click --with myst_parser --with . --from sphinx sphinx-build -b html docs/ site

docs-release:
  bash .hermit/bin/publish-docs

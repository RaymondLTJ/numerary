# AGENTS.md

Early-stage Python library for numerical methods (regression). There is **no**
packaging, test suite, linter, CI, or dependency manifest — don't go looking for
them, and don't scaffold them unless asked.

## Running

- Run scripts from the repo root: `python percobaan.py`. Imports are
  root-relative (`from src.base import NumericalMethod`) and only resolve there.
- The only third-party import is `numpy`, already installed in the local Python
  3.14. There is nothing to `pip install -e .`.
- `.vscode/settings.json` points at a conda env, but `conda` is not on PATH in
  this environment; use `python` directly.
- No test runner exists. Verify by running `percobaan.py` or a one-off
  `python -c "..."` from the root.

## Layout

- `src/` is the package; `src/base.py` defines `NumericalMethod` (ABC with a
  read-only `name` property) and the `Regressor` base (`fit`/`predict` abstract).
- `src/__init__.py` only re-exports `NumericalMethod`.
- `src/regressor/Regressor.py` is a separate, unrelated `Regressor` stub: it does
  not subclass `src.base.Regressor`, prints on import, and its directory has no
  `__init__.py`. Two `Regressor` definitions exist — confirm which one is
  current before editing either.
- `percobaan.py` (root) is the scratch/experiment entrypoint; root `__init__.py`
  is empty and unused.
- Names and debug strings are partly Indonesian (`percobaan`, "Ini jalan"); they
  are intentional, not typos.

## Gotchas

- `src/__pycache__/*.pyc` files are tracked in git. Ignore them in
  `git status`/diffs and never stage them.
- This is a hand-edited work in progress; the working tree often contains
  unfinished changes to `src/base.py`/`percobaan.py`. Read `git diff` before
  assuming HEAD reflects current behavior, and don't revert edits you didn't make.
- `NumericalMethod` has no abstract methods, so it is instantiable directly
  (as `percobaan.py` does); only `Regressor` enforces `fit`/`predict`.

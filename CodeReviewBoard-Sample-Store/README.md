# Code Review Board Sample Store

A deliberately imperfect Python sample repository for testing an automated code-review system. Do not use it in production.

## Contents
- `src/sample_store/pricing.py` — pricing and discount calculations
- `src/sample_store/catalog.py` — catalog search
- `tests/test_pricing.py` — partial unit coverage
- `pyproject.toml` — project configuration

## Run tests
```bash
python -m pip install -e ".[dev]"
python -m pytest -q
```

Some tests are expected to fail because the sample contains intentional bugs.

# Scripts Directory

This directory contains utility scripts for the sample-api project template.

## Validation Script

### `validate_template.py`

Validates that a project created from the educational API template follows the required structure and patterns.

**Usage:**
```bash
# Validate current directory (auto-detects backend/ if present)
python scripts/validate_template.py

# Validate specific project path
python scripts/validate_template.py /path/to/project

# Validate backend directory specifically
python scripts/validate_template.py backend/
```

**What it checks:**
- ✅ Required files exist (pyproject.toml, app.py, cli.py, src/, tests/)
- ✅ Business logic structure (functions, imports)
- ✅ API structure (FastAPI setup, business logic imports)
- ✅ CLI structure (argparse setup, business logic imports)
- ✅ Test structure (unit and integration test files)

**Output:**
- Lists found files and components
- Reports errors (must fix)
- Reports warnings (may be intentional)

## Code Quality Scripts (Not Included)

The template documentation mentions optional shell scripts for code quality:
- `check-all.sh` - Run all quality checks
- `format.sh` - Format code with black
- `lint.sh` - Run flake8 linting
- `typecheck.sh` - Run mypy type checking
- `sort-imports.sh` - Sort imports with isort

These are optional because you can use `uv` commands directly:

```bash
# Format code
uv run black .

# Sort imports
uv run isort .

# Type checking
uv run mypy src/

# Linting
uv run flake8 .

# Run tests
uv run python -m unittest discover -s tests -p "test_*.py" -v
```

If you want shell scripts, create them to wrap these `uv` commands.


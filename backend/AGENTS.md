# Backend Agent Instructions: Python API Template

## Overview

This directory contains a complete educational Python API project template with FastAPI. The template demonstrates business logic separation, where pure functions in `src/` are accessed via REST API (`app.py`) and CLI (`cli.py`).

**Key Principle:** Business logic is independent of interface. The same functions work for API, CLI, and any other interface.

## Project Structure

```
backend/
├── AGENTS.md            # This file
├── pyproject.toml       # Dependencies & tool configuration
├── src/
│   ├── __init__.py
│   └── math_operations.py    # Business logic functions
├── tests/
│   ├── unit/                 # Unit tests for business logic
│   └── integration/         # Integration tests for API/CLI
├── app.py                    # FastAPI REST API
└── cli.py                    # Command-line interface
```

## 1. Configuration: pyproject.toml

Create `pyproject.toml` with these dependencies and tool configurations:

```toml
[project]
name = "{project-name}"
version = "1.0.0"
description = "Educational Python API project demonstrating {domain} concepts"
readme = "README.md"
authors = [{name = "Sample Project", email = "example@example.com"}]
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "httpx>=0.25.0",  # Required for FastAPI TestClient
    "black>=23.0.0",
    "isort>=5.12.0",
    "mypy>=1.5.0",
    "flake8>=6.0.0",
]

[dependency-groups]
dev = [
    "black>=25.9.0",
    "flake8>=7.3.0",
    "httpx>=0.28.1",
    "isort>=7.0.0",
    "mypy>=1.18.2",
    "pytest>=8.4.2",
    "pytest-cov>=7.0.0",
]

[tool.black]
line-length = 88
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 88
known_first_party = ["src"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
strict_equality = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

Install: `uv sync --dev`

## 2. Business Logic: src/math_operations.py

**Key Principle:** Pure functions with no side effects. Easily testable and reusable.

Create `src/math_operations.py` with stubbed functions. See `docs/template/business-logic.md` for complete template with all 6 functions (square, power, factorial, fibonacci, is_prime, calculate_stats).

**Requirements:**
- Proper type hints
- Input validation with appropriate exceptions
- Clear docstrings
- TODO markers in stubbed implementations
- Pure functions (no side effects)

## 3. FastAPI API: app.py

**Key Principle:** API endpoints should never implement business logic directly. They only call functions from business logic module.

Create `app.py` with FastAPI application. See `docs/template/api-patterns.md` for complete template code.

**Required components:**
- FastAPI app initialization with metadata
- Optional CORS middleware (if serving frontend)
- Pydantic request models (PowerRequest, StatsRequest)
- Pydantic response models (all extending MathOperationResponse)
- API endpoints that call business logic functions
- Error handling with try/except blocks

**Required endpoints:**
- `GET /` - API information
- `GET /health` - Health check
- `GET /square/{number}` - Square calculation
- `GET /factorial/{number}` - Factorial calculation
- `GET /fibonacci/{count}` - Fibonacci sequence
- `GET /prime/{number}` - Prime check
- `POST /power` - Power calculation
- `POST /stats` - Statistics calculation

## 4. CLI Interface: cli.py

**Key Principle:** CLI commands call business logic functions, not reimplement logic.

Create `cli.py` with command-line interface. See `docs/template/cli-patterns.md` for complete template code.

**Required components:**
- Imports (argparse, sys, business logic functions)
- Result formatting function
- Command handlers (cmd_* functions)
- Argument parser setup with subparsers
- Main entry point

**Required commands:**
- `square <number>` - Calculate square
- `power <base> <exponent>` - Calculate power
- `factorial <number>` - Calculate factorial
- `fibonacci <count>` - Generate sequence
- `prime <number>` - Check if prime
- `stats <number> ...` - Calculate statistics

## 5. Testing

**Structure:**
- `tests/unit/test_math_operations.py` - Unit tests for business logic
- `tests/integration/test_api_integration.py` - API endpoint tests
- `tests/integration/test_cli_integration.py` - CLI command tests

**Run tests:**
```bash
uv run python -m unittest discover -s tests -p "test_*.py" -v
```

## 6. Code Quality

**Formatting:**
```bash
uv run black .
uv run isort .
uv run mypy src/
uv run flake8 .
```

## Customization Guide

### Replace Placeholders
- `{project-name}` → actual project name
- `{domain}` → domain name

### Update Business Logic
- Replace function logic inside `src/math_operations.py`
- Keep same function signatures initially
- Maintain error handling patterns
- Update docstrings for domain functionality

### Update API Endpoints
- Modify endpoint paths for domain terminology
- Update Pydantic model names and descriptions
- Keep same response structure patterns

### Update CLI Commands
- Rename commands to match domain functions
- Update help text and descriptions
- Maintain argument parsing patterns

### Domain Adaptation Examples

**Data Processing API:**
- `square()` → `normalize_value()`
- `power()` → `transform_data()`
- `factorial()` → `calculate_permissions()`
- `fibonacci()` → `generate_sequence()`
- `is_prime()` → `is_valid()`
- `calculate_stats()` → `analyze_dataset()`

**Validation Service API:**
- `square()` → `validate_format()`
- `power()` → `check_strength()`
- `is_prime()` → `meets_criteria()`
- `calculate_stats()` → `validation_report()`

## Key Reminders

1. Keep business logic in `src/`
2. Keep API thin (calls business logic)
3. Keep CLI calling business logic
4. Maintain test patterns
5. Update documentation

## Validation

Run validation script from project root:
```bash
python scripts/validate_template.py backend/
```

## Reference Files

For complete code templates, see:
- `docs/template/business-logic.md` - Full business logic template
- `docs/template/api-patterns.md` - Full FastAPI application template
- `docs/template/cli-patterns.md` - Full CLI template
- `docs/template/customization.md` - Domain adaptation guide


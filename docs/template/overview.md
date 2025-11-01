# Template Overview: Educational API Project

## Purpose

These instructions guide you to create a complete educational Python API project with the same structure and infrastructure as the sample-api project, but with stubbed-out business logic that can be customized for different domains.

## Project Structure Template

**Note:** The actual sample-api project uses a `backend/` directory structure. The template below shows the structure within the backend directory:

```
{project-name}/backend/
├── .github/
│   └── copilot-instructions.md        # Copilot workspace instructions (optional)
├── .gitignore                         # Python/uv gitignore
├── README.md                          # Comprehensive project documentation
├── pyproject.toml                     # Dependencies & tool configuration
├── src/
│   ├── __init__.py                    # Package initialization
│   └── math_operations.py              # Stubbed business functions (or business_logic.py)
├── tests/
│   ├── unit/
│   │   └── test_math_operations.py     # Unit tests for business functions
│   └── integration/
│       ├── test_api_integration.py    # API endpoint tests
│       └── test_cli_integration.py    # CLI command tests
├── scripts/                           # Code quality scripts (optional - can use uv commands directly)
│   ├── check-all.sh                   # Run all quality checks
│   ├── check-format.sh                # Check code formatting
│   ├── check-imports.sh               # Check import sorting
│   ├── fix-all.sh                     # Auto-fix formatting issues
│   ├── format.sh                      # Format code with black
│   ├── lint.sh                        # Run flake8 linting
│   ├── sort-imports.sh                # Sort imports with isort
│   └── typecheck.sh                   # Run mypy type checking
├── app.py                             # FastAPI application
└── cli.py                             # Command-line interface
```

## Key Principles to Maintain

1. **Separation of Concerns**: Keep business logic in `src/`, API in `app.py`, CLI in `cli.py`
2. **Pure Functions**: Business logic should have no side effects
3. **Comprehensive Testing**: Unit tests for business logic, integration tests for API/CLI
4. **Code Quality**: Use the same linting, formatting, and type checking setup
5. **Documentation**: Maintain extensive docstrings and README documentation
6. **Educational Focus**: Structure should teach API design principles

## Next Steps

- Review [Business Logic Patterns](business-logic.md) for function templates
- Review [API Patterns](api-patterns.md) for FastAPI structure
- Review [CLI Patterns](cli-patterns.md) for command-line interface
- Review [Customization Guide](customization.md) for domain adaptation


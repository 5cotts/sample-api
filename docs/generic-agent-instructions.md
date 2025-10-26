# Agent Instructions: Educational API Project Template

## Overview
These instructions guide you to create a complete educational Python API project with the same structure and infrastructure as the sample-api project, but with stubbed-out business logic that can be customized for different domains.

## Project Structure Template
Generate this exact directory structure:

```
{project-name}/
├── .github/
│   └── copilot-instructions.md        # Copilot workspace instructions
├── .gitignore                         # Python/uv gitignore
├── README.md                          # Comprehensive project documentation
├── pyproject.toml                     # Dependencies & tool configuration
├── src/
│   ├── __init__.py                    # Package initialization
│   └── business_logic.py              # Stubbed business functions
├── tests/
│   ├── unit/
│   │   └── test_business_logic.py     # Unit tests for business functions
│   └── integration/
│       ├── test_api_integration.py    # API endpoint tests
│       └── test_cli_integration.py    # CLI command tests
├── scripts/                           # Code quality scripts
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

## Core Files to Generate

### 1. pyproject.toml
Create with these exact dependencies and tool configurations:

```toml
[project]
name = "{project-name}"
version = "1.0.0"
description = "Educational Python API project demonstrating {domain} concepts"
readme = "README.md"
authors = [
    {name = "Sample Project", email = "example@example.com"}
]
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "requests>=2.31.0",
]

[project.optional-dependencies]
dev = [
    "httpx>=0.25.0",  # Required for FastAPI TestClient
    "black>=23.0.0",  # Code formatting
    "isort>=5.12.0",  # Import sorting
    "mypy>=1.5.0",    # Type checking
    "flake8>=6.0.0",  # Code style linting
]

# Include all tool configurations from sample-api pyproject.toml
```

### 2. src/math_operations.py
Create with stubbed math functions - replace logic with domain-specific implementations:

```python
"""
Business Logic Module for Mathematical Operations

This module contains pure business logic functions that can be used
independently of any API implementation. This demonstrates the important
principle of separating business logic from API infrastructure.

These functions are designed to be:
- Pure functions with no side effects
- Easily testable
- Reusable across different interfaces (API, CLI, etc.)

NOTE: These functions are stubbed with basic implementations.
Replace the logic inside each function with your domain-specific operations
while maintaining the same function signatures and error handling patterns.
"""

from typing import List, Union


def square(number: Union[int, float]) -> Union[int, float]:
    """
    Calculate the square of a number.
    
    STUB: Replace with your domain-specific logic that takes a single numeric input.
    Examples: validate_score(), normalize_value(), convert_units()
    
    Args:
        number: The number to square
        
    Returns:
        The square of the input number
        
    Raises:
        TypeError: If input is not a number
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    
    # TODO: Replace this basic square operation with your domain logic
    return number ** 2


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Calculate base raised to the power of exponent.
    
    STUB: Replace with your domain-specific logic that takes two numeric inputs.
    Examples: calculate_distance(), combine_values(), apply_transformation()
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        The result of base^exponent
        
    Raises:
        TypeError: If inputs are not numbers
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both base and exponent must be numbers")
    
    # TODO: Replace this basic power operation with your domain logic
    return base ** exponent


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    STUB: Replace with your domain-specific logic that takes an integer input.
    Examples: calculate_permissions(), generate_combinations(), process_sequence()
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    
    # TODO: Replace this basic factorial with your domain logic
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> List[int]:
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    STUB: Replace with your domain-specific logic that returns a list/sequence.
    Examples: generate_report_data(), create_timeline(), build_hierarchy()
    
    Args:
        n: Number of Fibonacci numbers to generate
        
    Returns:
        List of the first n Fibonacci numbers
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is not positive
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # TODO: Replace this basic Fibonacci sequence with your domain logic
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    STUB: Replace with your domain-specific logic that returns a boolean.
    Examples: is_valid(), has_permission(), meets_criteria()
    
    Args:
        n: The number to check
        
    Returns:
        True if the number is prime, False otherwise
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is less than 2
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Prime numbers are defined for integers >= 2")
    
    # TODO: Replace this basic prime check with your domain logic
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def calculate_stats(numbers: List[Union[int, float]]) -> dict:
    """
    Calculate basic statistics for a list of numbers.
    
    STUB: Replace with your domain-specific logic that processes a list.
    Examples: analyze_data(), process_batch(), aggregate_results()
    
    Args:
        numbers: List of numbers
        
    Returns:
        Dictionary containing mean, median, min, max, and count
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If the list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Validate all elements are numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")
    
    # TODO: Replace this basic statistics calculation with your domain logic
    sorted_numbers = sorted(numbers)
    count = len(numbers)
    mean = sum(numbers) / count
    
    if count % 2 == 0:
        median = (sorted_numbers[count // 2 - 1] + sorted_numbers[count // 2]) / 2
    else:
        median = sorted_numbers[count // 2]
    
    return {
        "count": count,
        "mean": mean,
        "median": median,
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
    }
```

### 3. app.py
Create FastAPI application with math operation endpoints (update descriptions for your domain):

```python
"""
FastAPI REST API for Mathematical Operations

This module provides a REST API interface to the mathematical operations
defined in the business logic module. It demonstrates how APIs can serve
as a thin layer over business logic, making functionality accessible
via HTTP endpoints.

NOTE: Update the API descriptions and endpoint names to match your domain
while keeping the same structure and patterns.
"""

from typing import List, Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from src.math_operations import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)

# Create FastAPI app with metadata
app = FastAPI(
    title="Mathematical Operations API",
    description="Educational Python API demonstrating business logic separation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Pydantic request models
class PowerRequest(BaseModel):
    """Request model for power calculation."""
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent")

class StatsRequest(BaseModel):
    """Request model for statistics calculation."""
    numbers: List[Union[int, float]] = Field(
        ..., description="List of numbers to calculate statistics for", min_length=1
    )

# Pydantic response models  
class MathOperationResponse(BaseModel):
    """Base response model for mathematical operations."""
    operation: str = Field(..., description="The operation that was performed")
    success: bool = Field(default=True, description="Whether the operation succeeded")

class SquareResponse(MathOperationResponse):
    """Response model for square operation."""
    input: Union[int, float] = Field(..., description="The input number")
    result: Union[int, float] = Field(..., description="The squared result")

class PowerResponse(MathOperationResponse):
    """Response model for power operation."""
    base: Union[int, float] = Field(..., description="The base number")
    exponent: Union[int, float] = Field(..., description="The exponent")
    result: Union[int, float] = Field(..., description="The power result")

class FactorialResponse(MathOperationResponse):
    """Response model for factorial operation."""
    input: int = Field(..., description="The input number")
    result: int = Field(..., description="The factorial result")

class FibonacciResponse(MathOperationResponse):
    """Response model for fibonacci operation."""
    count: int = Field(..., description="Number of Fibonacci numbers requested")
    sequence: List[int] = Field(..., description="The Fibonacci sequence")

class PrimeResponse(MathOperationResponse):
    """Response model for prime check operation."""
    input: int = Field(..., description="The input number to check")
    is_prime: bool = Field(..., description="Whether the number is prime")

class StatisticsData(BaseModel):
    """Model for statistical calculations."""
    count: int = Field(..., description="Number of values")
    mean: float = Field(..., description="Arithmetic mean")
    median: Union[int, float] = Field(..., description="Median value")
    min: Union[int, float] = Field(..., description="Minimum value")
    max: Union[int, float] = Field(..., description="Maximum value")
    sum: Union[int, float] = Field(..., description="Sum of all values")

class StatsResponse(MathOperationResponse):
    """Response model for statistics operation."""
    input_numbers: List[Union[int, float]] = Field(..., description="The input numbers")
    statistics: StatisticsData = Field(..., description="Calculated statistics")

# API endpoints
@app.get("/")
async def root():
    """API root endpoint providing information about available endpoints."""
    return {
        "message": "Mathematical Operations API",
        "version": "1.0.0",
        "docs_url": "/docs",
        "endpoints": {
            "GET /": "API information",
            "GET /health": "Health check",
            "GET /docs": "Interactive API documentation (Swagger UI)",
            "GET /redoc": "Alternative API documentation (ReDoc)",
            "GET /square/{number}": "Calculate square of a number",
            "GET /factorial/{number}": "Calculate factorial of a number",
            "GET /fibonacci/{count}": "Generate Fibonacci sequence",
            "GET /prime/{number}": "Check if number is prime",
            "POST /power": "Calculate base^exponent",
            "POST /stats": "Calculate statistics for a list of numbers",
        },
    }

@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running."""
    return {"status": "healthy", "service": "math-operations-api"}

@app.get("/square/{number}", response_model=SquareResponse)
async def api_square(number: Union[int, float]) -> SquareResponse:
    """Calculate the square of a number."""
    try:
        result = square(number)
        return SquareResponse(operation="square", input=number, result=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.get("/factorial/{number}", response_model=FactorialResponse)
async def api_factorial(number: int) -> FactorialResponse:
    """Calculate the factorial of a non-negative integer."""
    try:
        result = factorial(number)
        return FactorialResponse(operation="factorial", input=number, result=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.get("/fibonacci/{count}", response_model=FibonacciResponse)
async def api_fibonacci(count: int) -> FibonacciResponse:
    """Generate the first N numbers in the Fibonacci sequence."""
    try:
        result = fibonacci(count)
        return FibonacciResponse(operation="fibonacci", count=count, sequence=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.get("/prime/{number}", response_model=PrimeResponse)
async def api_is_prime(number: int) -> PrimeResponse:
    """Check if a number is prime."""
    try:
        result = is_prime(number)
        return PrimeResponse(operation="is_prime", input=number, is_prime=result)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.post("/power", response_model=PowerResponse)
async def api_power(request: PowerRequest) -> PowerResponse:
    """Calculate base raised to the power of exponent."""
    try:
        result = power(request.base, request.exponent)
        return PowerResponse(
            operation="power",
            base=request.base,
            exponent=request.exponent,
            result=result,
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

@app.post("/stats", response_model=StatsResponse)
async def api_calculate_stats(request: StatsRequest) -> StatsResponse:
    """Calculate basic statistics for a list of numbers."""
    try:
        result = calculate_stats(request.numbers)
        return StatsResponse(
            operation="calculate_stats",
            input_numbers=request.numbers,
            statistics=StatisticsData(**result),
        )
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
```

### 4. cli.py
Create command-line interface with math operation commands (adapt for your domain):

```python
#!/usr/bin/env python3
"""
Command Line Interface for Mathematical Operations

This CLI demonstrates how the same business logic used by the API
can be accessed directly from the command line. This shows the
separation of concerns: the business logic is independent of the
interface (API vs CLI).

NOTE: Update command names and descriptions to match your domain
while keeping the same structure and argument parsing patterns.

Usage:
    python cli.py square 5
    python cli.py power 2 8
    python cli.py factorial 5
    python cli.py fibonacci 10
    python cli.py prime 17
    python cli.py stats 1 2 3 4 5
"""

import argparse
import sys

from src.math_operations import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)

def format_result(operation: str, result, **kwargs):
    """Format and print the result of an operation."""
    print(f"\n=== {operation.upper()} OPERATION ===")

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    if isinstance(result, list):
        print(f"Result: {result}")
        print(f"Length: {len(result)}")
    elif isinstance(result, dict):
        print("Result:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print(f"Result: {result}")

    print("=" * (len(operation) + 15))

def cmd_square(args):
    """Handle square command."""
    try:
        number = float(args.number) if "." in args.number else int(args.number)
        result = square(number)
        format_result("square", result, input=number)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def cmd_power(args):
    """Handle power command."""
    try:
        base = float(args.base) if "." in args.base else int(args.base)
        exponent = float(args.exponent) if "." in args.exponent else int(args.exponent)
        result = power(base, exponent)
        format_result("power", result, base=base, exponent=exponent)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def cmd_factorial(args):
    """Handle factorial command."""
    try:
        result = factorial(args.number)
        format_result("factorial", result, input=args.number)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def cmd_fibonacci(args):
    """Handle fibonacci command."""
    try:
        result = fibonacci(args.count)
        format_result("fibonacci", result, count=args.count)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def cmd_prime(args):
    """Handle prime check command."""
    try:
        result = is_prime(args.number)
        prime_status = "is prime" if result else "is not prime"
        format_result("prime check", f"{args.number} {prime_status}", input=args.number)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def cmd_stats(args):
    """Handle statistics command."""
    try:
        numbers = []
        for num_str in args.numbers:
            # Convert to appropriate numeric type
            if "." in num_str:
                numbers.append(float(num_str))
            else:
                numbers.append(int(num_str))

        result = calculate_stats(numbers)
        format_result("statistics", result, input_numbers=numbers)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Mathematical Operations CLI - Direct access to business logic",
        epilog="Examples:\n"
        "  python cli.py square 5\n"
        "  python cli.py power 2 8\n"
        "  python cli.py factorial 5\n"
        "  python cli.py fibonacci 10\n"
        "  python cli.py prime 17\n"
        "  python cli.py stats 1 2 3 4 5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available operations")
    subparsers.required = True

    # Square command
    square_parser = subparsers.add_parser("square", help="Calculate square of a number")
    square_parser.add_argument("number", type=str, help="Number to square")
    square_parser.set_defaults(func=cmd_square)

    # Power command
    power_parser = subparsers.add_parser("power", help="Calculate base^exponent")
    power_parser.add_argument("base", type=str, help="Base number")
    power_parser.add_argument("exponent", type=str, help="Exponent")
    power_parser.set_defaults(func=cmd_power)

    # Factorial command
    factorial_parser = subparsers.add_parser("factorial", help="Calculate factorial")
    factorial_parser.add_argument(
        "number", type=int, help="Number for factorial (must be non-negative integer)"
    )
    factorial_parser.set_defaults(func=cmd_factorial)

    # Fibonacci command
    fibonacci_parser = subparsers.add_parser(
        "fibonacci", help="Generate Fibonacci sequence"
    )
    fibonacci_parser.add_argument(
        "count", type=int, help="Number of Fibonacci numbers to generate"
    )
    fibonacci_parser.set_defaults(func=cmd_fibonacci)

    # Prime command
    prime_parser = subparsers.add_parser("prime", help="Check if number is prime")
    prime_parser.add_argument("number", type=int, help="Number to check for primality")
    prime_parser.set_defaults(func=cmd_prime)

    # Statistics command
    stats_parser = subparsers.add_parser(
        "stats", help="Calculate statistics for numbers"
    )
    stats_parser.add_argument(
        "numbers", nargs="+", type=str, help="List of numbers for statistics"
    )
    stats_parser.set_defaults(func=cmd_stats)

    return parser

def main():
    """Main CLI entry point."""
    print("Mathematical Operations CLI")
    print("Demonstrating direct access to business logic functions")
    print("(The same functions used by the REST API)")

    parser = create_parser()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    try:
        args = parser.parse_args()
        args.func(args)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### 5. Test Files
Generate test files with corresponding stubbed tests that follow the same patterns as the original project.

### 6. Scripts Directory
Copy all shell scripts exactly from the sample-api project (check-all.sh, format.sh, lint.sh, etc.)

### 7. Configuration Files
Copy .gitignore and .github/copilot-instructions.md, updating placeholders for the new domain.

## Customization Instructions

When using this template:

1. **Replace placeholders**: 
   - `{project-name}` → actual project name
   - `{Domain}` → domain name (capitalized)
   - `{domain}` → domain name (lowercase)

2. **Update business logic**:
   - Replace the logic inside each function in `src/math_operations.py` with domain-specific implementations
   - Keep the same function names and signatures initially (square, power, factorial, fibonacci, is_prime, calculate_stats)
   - Maintain proper error handling patterns and input validation
   - Update docstrings to describe your domain-specific functionality

3. **Update API endpoints**:
   - Modify endpoint paths to match domain terminology (e.g., `/square/` → `/validate/`, `/power/` → `/transform/`)
   - Update Pydantic model names and field descriptions for domain-specific data
   - Keep the same response structure patterns
   - Update API documentation strings

4. **Update CLI commands**:
   - Rename CLI commands to match domain functions (e.g., `square` → `validate`, `power` → `transform`)
   - Update help text and command descriptions
   - Maintain the same argument parsing patterns
   - Update the CLI description and examples

5. **Update tests**:
   - Replace test assertions with domain-specific expectations
   - Keep the same test structure and patterns
   - Maintain comprehensive coverage

## Key Principles to Maintain

1. **Separation of Concerns**: Keep business logic in `src/`, API in `app.py`, CLI in `cli.py`
2. **Pure Functions**: Business logic should have no side effects
3. **Comprehensive Testing**: Unit tests for business logic, integration tests for API/CLI
4. **Code Quality**: Use the same linting, formatting, and type checking setup
5. **Documentation**: Maintain extensive docstrings and README documentation
6. **Educational Focus**: Structure should teach API design principles

## Example Domain Adaptations

Here are examples of how to adapt the math functions for different domains:

### Data Processing API
- `square()` → `normalize_value()` - normalize a single data point
- `power()` → `transform_data()` - apply transformation with parameters
- `factorial()` → `calculate_permissions()` - calculate access levels
- `fibonacci()` → `generate_sequence()` - create data sequences
- `is_prime()` → `is_valid()` - validate data integrity
- `calculate_stats()` → `analyze_dataset()` - comprehensive data analysis

### String Processing API
- `square()` → `duplicate_string()` - duplicate text content
- `power()` → `repeat_pattern()` - repeat pattern N times
- `factorial()` → `generate_combinations()` - create text combinations
- `fibonacci()` → `build_sequence()` - create progressive text patterns
- `is_prime()` → `is_palindrome()` - check text properties
- `calculate_stats()` → `analyze_text()` - text analysis metrics

### File Processing API
- `square()` → `compress_file()` - single file compression
- `power()` → `encrypt_data()` - encryption with key strength
- `factorial()` → `calculate_hash()` - generate file hash
- `fibonacci()` → `create_backups()` - incremental backup sequence
- `is_prime()` → `is_corrupted()` - file integrity check
- `calculate_stats()` → `analyze_directory()` - directory statistics

### Validation Service API
- `square()` → `validate_format()` - format validation
- `power()` → `check_strength()` - password/security strength
- `factorial()` → `calculate_score()` - validation scoring
- `fibonacci()` → `generate_rules()` - progressive validation rules
- `is_prime()` → `meets_criteria()` - criteria checking
- `calculate_stats()` → `validation_report()` - comprehensive validation results

The key is to maintain the infrastructure and patterns while replacing the mathematical logic with domain-appropriate operations.
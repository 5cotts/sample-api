# Math Operations Implementation Switch

The API can use either the functional or object-oriented implementation of math operations, controlled via the `MATH_OPERATIONS_IMPL` environment variable.

## Usage

### Functional Implementation (Default)

```bash
# Default behavior - no environment variable needed
uv run uvicorn app:app --reload

# Or explicitly set it
MATH_OPERATIONS_IMPL=functional uv run uvicorn app:app --reload
```

### Object-Oriented Implementation

```bash
MATH_OPERATIONS_IMPL=oop uv run uvicorn app:app --reload
```

## Verification

Check which implementation is active by calling the health endpoint:

```bash
# Check health endpoint
curl http://localhost:8000/health
```

The response will show which implementation is being used:
- `"service": "math-operations-api (functional)"` - Functional implementation
- `"service": "math-operations-api (object-oriented)"` - OOP implementation

## File Structure

The implementations are located in:
- `src/math_operations/functional.py` - Functional implementation
- `src/math_operations/oop.py` - Object-oriented implementation

Both modules are part of the `math_operations` package and can be imported via:
- `from src.math_operations.functional import square, ...`
- `from src.math_operations.oop import MathOperations`
- `from src.math_operations import square, MathOperations` (package-level imports)

## Implementation Details

Both implementations provide identical functionality:
- `square(number)` - Calculate square
- `power(base, exponent)` - Calculate power
- `factorial(n)` - Calculate factorial
- `fibonacci(n)` - Generate Fibonacci sequence
- `is_prime(n)` - Check if prime
- `calculate_stats(numbers)` - Calculate statistics

The API layer remains unchanged regardless of which implementation is used, demonstrating the principle of separating business logic from the API interface.


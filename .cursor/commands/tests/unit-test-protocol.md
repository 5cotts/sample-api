# Unit Test Protocol: Testing Guidelines for AI Agents

## Overview

This document provides comprehensive guidelines for structuring and writing tests in this project. It demonstrates the testing patterns used throughout the codebase and serves as a reference for AI agents when creating or modifying tests.

## Testing Philosophy

### Core Principles

1. **Separation of Concerns**: Business logic tests are separate from API/CLI integration tests
2. **Test Independence**: Each test should be able to run independently without side effects
3. **Comprehensive Coverage**: Tests cover happy paths, edge cases, and error conditions
4. **Clear Documentation**: Test names and docstrings clearly describe what is being tested
5. **Fast Execution**: Unit tests should be fast and not require external dependencies

### Test Structure

```
backend/
├── tests/
│   ├── unit/                    # Unit tests for business logic
│   │   ├── math_operations/    # Tests matching source structure
│   │   │   ├── test_functional.py
│   │   │   └── test_oop.py
│   │   └── test_data_parsing.py
│   └── integration/            # Integration tests for interfaces
│       ├── test_api_integration.py
│       └── test_cli_integration.py
```

## Unit Test Patterns

### File Structure

Every unit test file should follow this structure:

```python
"""
Module-level docstring explaining:
- What is being tested
- Why these tests exist
- What scenarios are covered
"""

import unittest
from src.module import function_to_test


class TestFunctionName(unittest.TestCase):
    """Tests for the function_name function."""

    def test_happy_path_scenario(self):
        """Test description of the happy path."""
        # Arrange
        input_value = 5
        
        # Act
        result = function_to_test(input_value)
        
        # Assert
        self.assertEqual(result, expected_value)

    def test_edge_case(self):
        """Test description of edge case."""
        # Test implementation

    def test_error_condition(self):
        """Test description of error condition."""
        with self.assertRaises(ValueError):
            function_to_test(invalid_input)


if __name__ == "__main__":
    unittest.main()
```

### Test Class Organization

**Pattern**: One test class per function or method being tested.

**Example from `test_functional.py`:**
```python
class TestSquareFunction(unittest.TestCase):
    """Tests for the square function."""

    def test_square_positive_integer(self):
        """Test squaring positive integers."""
        self.assertEqual(square(5), 25)
        self.assertEqual(square(10), 100)
        self.assertEqual(square(1), 1)

    def test_square_negative_integer(self):
        """Test squaring negative integers."""
        self.assertEqual(square(-5), 25)
        self.assertEqual(square(-10), 100)

    def test_square_zero(self):
        """Test squaring zero."""
        self.assertEqual(square(0), 0)

    def test_square_float(self):
        """Test squaring floating-point numbers."""
        self.assertEqual(square(2.5), 6.25)
        self.assertAlmostEqual(square(0.1), 0.01, places=7)

    def test_square_invalid_input(self):
        """Test error handling for invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            square("5")
```

### Test Method Naming

**Pattern**: `test_<function>_<scenario>`

Examples:
- `test_square_positive_integer` - Tests square function with positive integers
- `test_factorial_negative_input` - Tests factorial with invalid negative input
- `test_stats_empty_list` - Tests statistics with empty list edge case
- `test_load_csv_file_not_found` - Tests error handling for missing file

### Test Documentation

**Required Elements:**

1. **Module docstring** at the top explaining:
   - What module/functionality is being tested
   - Why these tests exist
   - What scenarios are covered

2. **Class docstring** describing:
   - What function/class is being tested

3. **Method docstring** for each test method:
   - What specific scenario is being tested
   - Use imperative mood: "Test squaring positive integers" not "Tests squaring..."

**Example:**
```python
"""
Unit Tests for Mathematical Operations Business Logic (Functional Implementation)

These tests demonstrate how to test business logic functions independently
of any API or interface implementation. By separating business logic from
the API layer, we can write focused, fast unit tests that don't require
spinning up a web server or making HTTP requests.

Tests cover:
- Happy path scenarios
- Edge cases
- Error conditions
- Input validation
"""

class TestSquareFunction(unittest.TestCase):
    """Tests for the square function."""

    def test_square_positive_integer(self):
        """Test squaring positive integers."""
        # Test implementation
```

## Test Categories

### 1. Happy Path Tests

Test normal, expected usage with valid inputs.

**Pattern:**
- Use clear, descriptive assertions
- Test multiple valid inputs when appropriate
- Verify expected outputs match specifications

**Example:**
```python
def test_factorial_small_numbers(self):
    """Test factorial of small numbers."""
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(2), 2)
    self.assertEqual(factorial(3), 6)
    self.assertEqual(factorial(4), 24)
    self.assertEqual(factorial(5), 120)
```

### 2. Edge Case Tests

Test boundary conditions and special cases.

**Common Edge Cases:**
- Zero values
- Empty collections
- Single element collections
- Maximum/minimum values
- Boundary conditions

**Example:**
```python
def test_stats_single_number(self):
    """Test statistics with a single number."""
    numbers = [42]
    result = calculate_stats(numbers)

    self.assertEqual(result["count"], 1)
    self.assertEqual(result["mean"], 42)
    self.assertEqual(result["median"], 42)
    self.assertEqual(result["min"], 42)
    self.assertEqual(result["max"], 42)
    self.assertEqual(result["sum"], 42)
```

### 3. Error Condition Tests

Test that appropriate exceptions are raised for invalid inputs.

**Pattern:**
- Use `self.assertRaises()` or `self.assertRaisesRegex()` for exception testing
- Verify exception type matches expected type
- Optionally verify exception message matches expected pattern

**Example:**
```python
def test_factorial_negative_input(self):
    """Test factorial with negative input."""
    with self.assertRaisesRegex(
        ValueError, "Factorial is only defined for non-negative integers"
    ):
        factorial(-1)

    with self.assertRaisesRegex(
        ValueError, "Factorial is only defined for non-negative integers"
    ):
        factorial(-5)
```

### 4. Type Validation Tests

Test that functions properly validate input types.

**Pattern:**
- Test with various invalid types (strings, lists, None, etc.)
- Verify TypeError is raised with appropriate message
- Test each invalid type separately for clarity

**Example:**
```python
def test_square_invalid_input(self):
    """Test error handling for invalid input types."""
    with self.assertRaisesRegex(TypeError, "Input must be a number"):
        square("5")

    with self.assertRaisesRegex(TypeError, "Input must be a number"):
        square([5])

    with self.assertRaisesRegex(TypeError, "Input must be a number"):
        square(None)
```

### 5. Data Type Variation Tests

Test functions with different numeric types (int, float).

**Pattern:**
- Test with integers
- Test with floats
- Use `assertAlmostEqual()` for floating-point comparisons

**Example:**
```python
def test_power_with_floats(self):
    """Test power with floating-point numbers."""
    self.assertEqual(power(2.0, 3.0), 8.0)
    self.assertEqual(power(4, 0.5), 2.0)
    self.assertEqual(power(9, 0.5), 3.0)
```

## OOP-Specific Patterns

### Class Instantiation Tests

When testing object-oriented implementations, include tests for class instantiation.

**Pattern:**
```python
class TestMathOperationsClass(unittest.TestCase):
    """Tests for MathOperations class instantiation."""

    def test_class_instantiation(self):
        """Test that MathOperations can be instantiated."""
        calculator = MathOperations()
        self.assertIsInstance(calculator, MathOperations)

    def test_multiple_instances(self):
        """Test that multiple instances can be created independently."""
        calc1 = MathOperations()
        calc2 = MathOperations()
        self.assertIsNot(calc1, calc2)
```

### Using setUp() for Test Fixtures

**Pattern:** Use `setUp()` to create reusable test fixtures.

**Example:**
```python
class TestSquareMethod(unittest.TestCase):
    """Tests for the square method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_square_positive_integer(self):
        """Test squaring positive integers."""
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.square(10), 100)
```

### Testing Multiple Instances

**Pattern:** Verify that multiple instances work independently.

**Example:**
```python
class TestMultipleInstances(unittest.TestCase):
    """Tests demonstrating that multiple instances work independently."""

    def test_independent_instances(self):
        """Test that multiple instances produce the same results independently."""
        calc1 = MathOperations()
        calc2 = MathOperations()

        # Both instances should produce the same results
        self.assertEqual(calc1.square(5), calc2.square(5))
        self.assertEqual(calc1.factorial(5), calc2.factorial(5))
```

## File I/O and External Resources

### Testing File Operations

**Pattern:** Use temporary files and directories for file I/O tests.

**Example from `test_data_parsing.py`:**
```python
import tempfile
from pathlib import Path

class TestLoadCSV(unittest.TestCase):
    """Tests for the load_csv function."""

    def test_load_csv_from_data_directory(self):
        """Test loading CSV from data directory."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn("name", df.columns)

    def test_load_csv_invalid_file(self):
        """Test loading invalid CSV file that causes pandas error."""
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)
            with self.assertRaises(ValueError):
                load_csv(dir_path)
```

### Path Resolution

**Pattern:** Calculate paths relative to test file location.

**Example:**
```python
# Calculate path to backend/data directory
# Test file location: backend/tests/unit/test_data_parsing.py
# Going up: unit -> tests -> backend, then into data/
TEST_DIR = Path(__file__).parent  # backend/tests/unit/
TESTS_DIR = TEST_DIR.parent  # backend/tests/
BACKEND_DIR = TESTS_DIR.parent  # backend/
DATA_DIR = BACKEND_DIR / "data"  # backend/data/
```

## Integration Tests

**Note:** For comprehensive guidelines on writing integration tests (API and CLI), see [integration-test-protocol.md](integration-test-protocol.md).

Integration tests verify that different components work together correctly. They are located in `tests/integration/` and are separate from unit tests.

## Assertion Patterns

### Common Assertions

**Equality:**
```python
self.assertEqual(actual, expected)
self.assertNotEqual(actual, expected)
```

**Type Checking:**
```python
self.assertIsInstance(obj, ClassName)
```

**Boolean:**
```python
self.assertTrue(condition)
self.assertFalse(condition)
```

**Membership:**
```python
self.assertIn(item, container)
self.assertNotIn(item, container)
```

**Exceptions:**
```python
with self.assertRaises(ValueError):
    function_that_raises()

with self.assertRaisesRegex(TypeError, "expected message"):
    function_that_raises()
```

**Floating Point:**
```python
self.assertAlmostEqual(actual, expected, places=7)
```

**Comparisons:**
```python
self.assertGreater(value, threshold)
self.assertLess(value, threshold)
self.assertGreaterEqual(value, threshold)
```

## Test Organization Best Practices

### 1. One Test Class Per Function/Method

Each function or method should have its own test class.

**Good:**
```python
class TestSquareFunction(unittest.TestCase):
    """Tests for the square function."""
    # ... tests ...

class TestPowerFunction(unittest.TestCase):
    """Tests for the power function."""
    # ... tests ...
```

**Bad:**
```python
class TestAllFunctions(unittest.TestCase):
    """Tests for all functions."""
    # Mixing tests for different functions
```

### 2. Group Related Tests

Group related test methods within a class by scenario type.

**Pattern:**
1. Happy path tests first
2. Edge cases next
3. Error conditions last

### 3. Use Descriptive Test Names

Test names should clearly indicate what is being tested.

**Good:**
- `test_square_positive_integer`
- `test_factorial_negative_input`
- `test_stats_empty_list`

**Bad:**
- `test_square`
- `test_factorial`
- `test1`

### 4. Keep Tests Focused

Each test should verify one specific behavior.

**Good:**
```python
def test_square_positive_integer(self):
    """Test squaring positive integers."""
    self.assertEqual(square(5), 25)
    self.assertEqual(square(10), 100)

def test_square_negative_integer(self):
    """Test squaring negative integers."""
    self.assertEqual(square(-5), 25)
    self.assertEqual(square(-10), 100)
```

**Bad:**
```python
def test_square_everything(self):
    """Test everything about square."""
    # Testing positive, negative, zero, floats, errors all in one test
```

### 5. Test Independence

Each test should be able to run independently.

**Good:**
```python
def test_square_positive_integer(self):
    """Test squaring positive integers."""
    result = square(5)
    self.assertEqual(result, 25)
```

**Bad:**
```python
def test_square_positive_integer(self):
    """Test squaring positive integers."""
    # Relies on previous test setting up state
    result = square(self.previous_result)
```

## Running Tests

### Run All Tests
```bash
uv run python -m unittest discover -s tests -p "test_*.py" -v
```

### Run Specific Test File
```bash
uv run python -m unittest tests.unit.math_operations.test_functional -v
```

### Run Specific Test Class
```bash
uv run python -m unittest tests.unit.math_operations.test_functional.TestSquareFunction -v
```

### Run Specific Test Method
```bash
uv run python -m unittest tests.unit.math_operations.test_functional.TestSquareFunction.test_square_positive_integer -v
```

## Checklist for New Tests

When creating new tests, ensure:

- [ ] Module docstring explains what is being tested
- [ ] Test class has descriptive docstring
- [ ] Each test method has a docstring
- [ ] Test names follow `test_<function>_<scenario>` pattern
- [ ] Happy path scenarios are covered
- [ ] Edge cases are covered
- [ ] Error conditions are tested with appropriate exceptions
- [ ] Type validation is tested
- [ ] Tests are independent and can run in any order
- [ ] Assertions are clear and specific
- [ ] Temporary files/resources are cleaned up
- [ ] Paths are resolved relative to test file location

## Examples from Codebase

### Complete Unit Test Example

See `backend/tests/unit/math_operations/test_functional.py` for a complete example of unit tests covering:
- Multiple test classes (one per function)
- Happy path tests
- Edge case tests
- Error condition tests
- Type validation tests
- Floating-point comparisons

### Integration Test Examples

For complete integration test examples, see [integration-test-protocol.md](integration-test-protocol.md), which covers:
- API integration tests (`backend/tests/integration/test_api_integration.py`)
- CLI integration tests (`backend/tests/integration/test_cli_integration.py`)

### File I/O Test Example

See `backend/tests/unit/test_data_parsing.py` for examples of:
- Testing file loading operations
- Using temporary files
- Path resolution
- Error handling for file operations
- Integration tests combining multiple functions

## Notes for AI Agents

1. **Always follow existing patterns**: Look at similar tests in the codebase before writing new ones
2. **Match the structure**: Follow the file structure and naming conventions used in existing tests
3. **Be comprehensive**: Include happy paths, edge cases, and error conditions
4. **Document clearly**: Use docstrings to explain what each test verifies
5. **Keep tests focused**: One test should verify one specific behavior
6. **Use appropriate assertions**: Choose assertions that clearly express the expected behavior
7. **Test independently**: Ensure tests don't depend on each other
8. **Clean up resources**: Use context managers for temporary files and resources


# Integration Test Protocol: Testing Guidelines for AI Agents

## Overview

This document provides comprehensive guidelines for structuring and writing integration tests in this project. Integration tests verify that different components work together correctly, including API endpoints, CLI commands, and the interaction between business logic and interfaces.

**Note:** For unit test guidelines, see [unit-test-protocol.md](unit-test-protocol.md).

## Testing Philosophy

### Core Principles

1. **End-to-End Verification**: Integration tests verify the full request/response cycle
2. **Interface Testing**: Tests focus on API contracts, CLI behavior, and user-facing interfaces
3. **Realistic Scenarios**: Tests simulate actual usage patterns
4. **Separation from Unit Tests**: Integration tests are separate from unit tests that test business logic in isolation

### Test Structure

```
backend/
├── tests/
│   ├── unit/                    # Unit tests for business logic
│   │   └── ...
│   └── integration/            # Integration tests for interfaces
│       ├── test_api_integration.py
│       └── test_cli_integration.py
```

## API Integration Tests

### Overview

API integration tests verify that HTTP endpoints work correctly, including:
- HTTP routing and request handling
- Request/response serialization
- API contracts and response models
- Error handling and status codes
- Request validation

### File Structure

Every API integration test file should follow this structure:

```python
"""
Integration tests for the Sample API.

These tests demonstrate testing the actual HTTP API endpoints using FastAPI's test
client. Unlike unit tests that test business logic directly, integration tests
verify that:
- HTTP routing works correctly
- Request/response serialization works
- API contracts are maintained
- The full request/response cycle functions properly

This shows how to test the API layer separately from the business logic layer.
"""

import unittest
from fastapi.testclient import TestClient
from app import app

# Create test client
client = TestClient(app)


class TestAPIRootEndpoints(unittest.TestCase):
    """Test basic API information endpoints."""

    def test_root_endpoint(self):
        """Test the root API information endpoint."""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["message"], "Mathematical Operations API")
        self.assertEqual(data["version"], "1.0.0")


if __name__ == "__main__":
    unittest.main()
```

### Using FastAPI TestClient

**Pattern:** Create a TestClient instance at module level and use it in all tests.

**Example:**
```python
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
```

### Testing GET Endpoints

**Pattern:** Test GET endpoints with path parameters.

**Example from `test_api_integration.py`:**
```python
class TestGETEndpoints(unittest.TestCase):
    """Test GET endpoints for mathematical operations."""

    def test_square_positive_integer(self):
        """Test square endpoint with positive integer."""
        response = client.get("/square/5")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "square")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], 5)
        self.assertEqual(data["result"], 25)

    def test_square_negative_integer(self):
        """Test square endpoint with negative integer."""
        response = client.get("/square/-4")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "square")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], -4)
        self.assertEqual(data["result"], 16)

    def test_square_float(self):
        """Test square endpoint with float."""
        response = client.get("/square/2.5")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "square")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], 2.5)
        self.assertEqual(data["result"], 6.25)
```

**Key Elements:**
- Test HTTP status codes (200 for success)
- Verify response structure (JSON keys, types)
- Test with different input types (positive, negative, floats)
- Verify response data matches expected values

### Testing POST Endpoints

**Pattern:** Test POST endpoints with JSON payloads.

**Example:**
```python
class TestPOSTEndpoints(unittest.TestCase):
    """Test POST endpoints with JSON payloads."""

    def test_power_valid_input(self):
        """Test power endpoint with valid input."""
        payload = {"base": 2, "exponent": 8}
        response = client.post("/power", json=payload)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "power")
        self.assertTrue(data["success"])
        self.assertEqual(data["base"], 2)
        self.assertEqual(data["exponent"], 8)
        self.assertEqual(data["result"], 256)

    def test_stats_valid_input(self):
        """Test stats endpoint with valid input."""
        payload = {"numbers": [1, 2, 3, 4, 5]}
        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "calculate_stats")
        self.assertTrue(data["success"])
        self.assertEqual(data["input_numbers"], [1, 2, 3, 4, 5])

        stats = data["statistics"]
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["mean"], 3.0)
        self.assertEqual(stats["median"], 3)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 5)
        self.assertEqual(stats["sum"], 15)
```

**Key Elements:**
- Use `json=payload` parameter for POST requests
- Test nested response structures
- Verify all expected fields are present

### Testing Error Responses

**Pattern:** Test that invalid inputs return appropriate error status codes.

**Example:**
```python
class TestErrorHandling(unittest.TestCase):
    """Test error handling and edge cases."""

    def test_factorial_invalid_negative(self):
        """Test factorial endpoint with negative number (should fail)."""
        response = client.get("/factorial/-5")
        self.assertEqual(response.status_code, 400)

        data = response.json()
        self.assertIn("Invalid input", data["detail"])

    def test_stats_empty_list(self):
        """Test stats endpoint with empty list (should fail validation)."""
        payload = {"numbers": []}
        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 422)  # Validation error

        data = response.json()
        self.assertIn("detail", data)

    def test_nonexistent_endpoint(self):
        """Test calling a non-existent endpoint."""
        response = client.get("/nonexistent")
        self.assertEqual(response.status_code, 404)

    def test_invalid_http_method(self):
        """Test using wrong HTTP method."""
        response = client.post("/square/5")  # Should be GET
        self.assertEqual(response.status_code, 405)  # Method not allowed

    def test_invalid_path_parameter_type(self):
        """Test with invalid path parameter types where FastAPI expects int."""
        response = client.get("/factorial/invalid")
        self.assertEqual(response.status_code, 422)  # Validation error
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `404` - Not Found (endpoint doesn't exist)
- `405` - Method Not Allowed (wrong HTTP method)
- `422` - Unprocessable Entity (validation error)

### Testing Request Validation

**Pattern:** Test that missing or invalid fields are properly validated.

**Example:**
```python
def test_power_missing_field(self):
    """Test power endpoint with missing required field."""
    payload = {"base": 2}  # Missing exponent
    response = client.post("/power", json=payload)
    self.assertEqual(response.status_code, 422)  # Validation error

    data = response.json()
    self.assertIn("detail", data)
    # FastAPI returns validation errors in specific format
    self.assertTrue(any("exponent" in str(error) for error in data["detail"]))

def test_power_invalid_types(self):
    """Test power endpoint with invalid data types."""
    payload = {"base": "invalid", "exponent": 2}
    response = client.post("/power", json=payload)
    self.assertEqual(response.status_code, 422)  # Validation error
```

### Testing Response Models

**Pattern:** Verify that response structures match expected models.

**Example:**
```python
class TestResponseModels(unittest.TestCase):
    """Test that response models are properly validated."""

    def test_square_response_structure(self):
        """Verify square response has all expected fields."""
        response = client.get("/square/3")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        required_fields = {"operation", "success", "input", "result"}
        assert required_fields.issubset(data.keys())

    def test_fibonacci_response_structure(self):
        """Verify fibonacci response has all expected fields."""
        response = client.get("/fibonacci/5")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        required_fields = {"operation", "success", "count", "sequence"}
        assert required_fields.issubset(data.keys())
        assert isinstance(data["sequence"], list)

    def test_stats_response_nested_structure(self):
        """Verify stats response has proper nested structure."""
        payload = {"numbers": [1, 2, 3]}
        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("statistics", data)

        stats = data["statistics"]
        required_stats = {"count", "mean", "median", "min", "max", "sum"}
        assert required_stats.issubset(stats.keys())
```

### Performance Testing (Basic Examples)

**Pattern:** Test that endpoints handle multiple requests and larger datasets.

**Example:**
```python
class TestPerformance(unittest.TestCase):
    """Basic performance testing examples."""

    def test_multiple_requests_performance(self):
        """Test making multiple requests to ensure stability."""
        # Make 20 requests to square endpoint
        for i in range(1, 21):
            response = client.get(f"/square/{i}")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["result"], i * i)

    def test_large_fibonacci_sequence(self):
        """Test with larger Fibonacci sequence."""
        response = client.get("/fibonacci/20")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data["sequence"]), 20)
        self.assertEqual(data["sequence"][-1], 4181)  # 20th Fibonacci number

    def test_large_statistics_dataset(self):
        """Test statistics with larger dataset."""
        large_dataset = list(range(1, 101))  # 1 to 100
        payload = {"numbers": large_dataset}

        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        stats = data["statistics"]
        self.assertEqual(stats["count"], 100)
        self.assertEqual(stats["mean"], 50.5)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 100)
```

## CLI Integration Tests

### Overview

CLI integration tests verify that command-line commands work correctly, including:
- Command-line argument parsing
- Command execution and output formatting
- Error handling and exit codes
- Integration with business logic

### File Structure

Every CLI integration test file should follow this structure:

```python
"""
Integration Tests for CLI Commands

These tests demonstrate testing the command-line interface by running
the actual CLI commands as subprocesses. This verifies that:
- CLI argument parsing works correctly
- Commands execute successfully
- Output formatting is correct
- Error handling works properly
"""

import os
import subprocess
import sys
import unittest

# Get the path to the CLI script
CLI_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "cli.py")


class TestCLICommands(unittest.TestCase):
    """Test CLI commands by running them as subprocesses."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands and return result."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_cli_help(self):
        """Test CLI help command."""
        result = self.run_cli_command("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Mathematical Operations CLI", result.stdout)


if __name__ == "__main__":
    unittest.main()
```

### CLI Path Resolution

**Pattern:** Calculate the path to the CLI script relative to the test file.

**Example:**
```python
import os

# Get the path to the CLI script
CLI_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "cli.py")
```

### Helper Method Pattern

**Pattern:** Create a reusable helper method to run CLI commands.

**Example:**
```python
def run_cli_command(self, *args):
    """Helper method to run CLI commands and return result."""
    cmd = [sys.executable, CLI_PATH] + list(args)
    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
    )
    return result
```

**Key Parameters:**
- `capture_output=True` - Capture stdout and stderr
- `text=True` - Return strings instead of bytes
- `cwd=os.path.dirname(CLI_PATH)` - Set working directory to CLI script location

### Testing Successful Commands

**Pattern:** Test that commands execute successfully and produce expected output.

**Example:**
```python
class TestSquareCommand(unittest.TestCase):
    """Test the square CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_square_positive_integer(self):
        """Test square command with positive integer."""
        result = self.run_cli_command("square", "5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("SQUARE OPERATION", output)
        self.assertIn("Input: 5", output)
        self.assertIn("Result: 25", output)

    def test_square_negative_integer(self):
        """Test square command with negative integer."""
        result = self.run_cli_command("square", "-4")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input: -4", output)
        self.assertIn("Result: 16", output)

    def test_square_float(self):
        """Test square command with float."""
        result = self.run_cli_command("square", "2.5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input: 2.5", output)
        self.assertIn("Result: 6.25", output)
```

**Key Elements:**
- Check `returncode` (0 for success)
- Verify stdout contains expected output
- Test with different input types

### Testing Error Conditions

**Pattern:** Test that invalid inputs produce appropriate error messages and exit codes.

**Example:**
```python
def test_factorial_negative_input(self):
    """Test factorial with negative input (should fail)."""
    result = self.run_cli_command("factorial", "-5")
    self.assertEqual(result.returncode, 1)  # Should exit with error
    self.assertIn("Error:", result.stdout)

def test_fibonacci_invalid_zero(self):
    """Test fibonacci with zero (should fail)."""
    result = self.run_cli_command("fibonacci", "0")
    self.assertEqual(result.returncode, 1)
    self.assertIn("Error:", result.stdout)

def test_power_missing_argument(self):
    """Test power command with missing argument."""
    result = self.run_cli_command("power", "2")
    assert result.returncode != 0  # Should fail
    self.assertIn(
        "error", result.stderr.lower()
    ) or "required" in result.stderr.lower()
```

**Key Elements:**
- Check `returncode` (non-zero for errors)
- Verify error messages in stdout or stderr
- Test missing arguments, invalid inputs, etc.

### Testing Help and Usage

**Pattern:** Test that help commands work correctly.

**Example:**
```python
def test_cli_help(self):
    """Test CLI help command."""
    result = self.run_cli_command("--help")
    self.assertEqual(result.returncode, 0)
    self.assertIn("Mathematical Operations CLI", result.stdout)
    self.assertIn("square", result.stdout)
    self.assertIn("power", result.stdout)
    self.assertIn("factorial", result.stdout)

def test_square_help(self):
    """Test square command help output"""
    result = self.run_cli_command("square", "--help")
    self.assertEqual(result.returncode, 0)
    self.assertIn("Number to square", result.stdout)
```

### Testing Output Format Consistency

**Pattern:** Verify that all commands have consistent output formatting.

**Example:**
```python
def test_cli_output_format_consistency(self):
    """Test that all commands have consistent output format."""
    commands = [
        (["square", "4"], "SQUARE OPERATION"),
        (["factorial", "4"], "FACTORIAL OPERATION"),
        (["fibonacci", "5"], "FIBONACCI OPERATION"),
        (["prime", "7"], "PRIME CHECK OPERATION"),
        (["stats", "1", "2", "3"], "STATISTICS OPERATION"),
    ]

    for cmd_args, expected_header in commands:
        result = self.run_cli_command(*cmd_args)
        self.assertEqual(result.returncode, 0)
        assert expected_header in result.stdout
        self.assertIn("===", result.stdout)  # All should have separator lines
```

### Testing Integration with Business Logic

**Pattern:** Verify that CLI results match expected business logic behavior.

**Example:**
```python
class TestCLIIntegrationWithBusinessLogic(unittest.TestCase):
    """Test that CLI properly integrates with business logic functions."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_cli_matches_direct_function_calls(self):
        """Test that CLI results match direct function calls."""
        # We know from unit tests that square(7) = 49
        result = self.run_cli_command("square", "7")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Result: 49", result.stdout)

        # We know factorial(4) = 24
        result = self.run_cli_command("factorial", "4")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Result: 24", result.stdout)

    def test_cli_power_matches_expected_calculations(self):
        """Test that CLI power results are mathematically correct."""
        test_cases = [
            ("2", "3", "8"),  # 2^3 = 8
            ("5", "2", "25"),  # 5^2 = 25
            ("10", "0", "1"),  # 10^0 = 1
        ]

        for base, exp, expected in test_cases:
            result = self.run_cli_command("power", base, exp)
            self.assertEqual(result.returncode, 0)
            assert f"Result: {expected}" in result.stdout
```

## Test Organization Best Practices

### 1. Group Tests by Endpoint/Command

Organize tests into classes by endpoint or command.

**Good:**
```python
class TestGETEndpoints(unittest.TestCase):
    """Test GET endpoints for mathematical operations."""
    # ... tests ...

class TestPOSTEndpoints(unittest.TestCase):
    """Test POST endpoints with JSON payloads."""
    # ... tests ...

class TestErrorHandling(unittest.TestCase):
    """Test error handling and edge cases."""
    # ... tests ...
```

### 2. Use Descriptive Test Names

Test names should clearly indicate what endpoint/command and scenario is being tested.

**Good:**
- `test_square_positive_integer`
- `test_factorial_invalid_negative`
- `test_stats_empty_list`
- `test_cli_help`

**Bad:**
- `test_endpoint`
- `test_command`
- `test1`

### 3. Test Both Success and Failure Cases

Include tests for both successful operations and error conditions.

**Pattern:**
- Test valid inputs → expect success
- Test invalid inputs → expect appropriate errors
- Test missing fields → expect validation errors
- Test wrong HTTP methods → expect 405

### 4. Verify Response Structure

Always verify that responses contain expected fields and have correct types.

**Example:**
```python
def test_square_response_structure(self):
    """Verify square response has all expected fields."""
    response = client.get("/square/3")
    self.assertEqual(response.status_code, 200)

    data = response.json()
    required_fields = {"operation", "success", "input", "result"}
    assert required_fields.issubset(data.keys())
```

## Running Integration Tests

### Run All Integration Tests
```bash
uv run python -m unittest discover -s tests/integration -p "test_*.py" -v
```

### Run Specific Integration Test File
```bash
uv run python -m unittest tests.integration.test_api_integration -v
```

### Run Specific Test Class
```bash
uv run python -m unittest tests.integration.test_api_integration.TestGETEndpoints -v
```

## Checklist for New Integration Tests

When creating new integration tests, ensure:

- [ ] Module docstring explains what is being tested
- [ ] Test class has descriptive docstring
- [ ] Each test method has a docstring
- [ ] Test names follow `test_<endpoint/command>_<scenario>` pattern
- [ ] HTTP status codes are verified (for API tests)
- [ ] Return codes are verified (for CLI tests)
- [ ] Response/output structure is validated
- [ ] Error conditions are tested
- [ ] Request validation is tested (for API tests)
- [ ] Argument parsing is tested (for CLI tests)
- [ ] Tests are independent and can run in any order
- [ ] Helper methods are used for repeated patterns (CLI command execution)

## Examples from Codebase

### Complete API Integration Test Example

See `backend/tests/integration/test_api_integration.py` for a complete example of API integration tests covering:
- HTTP endpoint testing with GET and POST
- Request/response validation
- Error handling (400, 404, 405, 422)
- Response structure validation
- Performance testing examples

### Complete CLI Integration Test Example

See `backend/tests/integration/test_cli_integration.py` for a complete example of CLI integration tests covering:
- Command execution via subprocess
- Output format verification
- Error handling and exit codes
- Help command testing
- Integration with business logic verification

## Notes for AI Agents

1. **Always follow existing patterns**: Look at similar integration tests in the codebase before writing new ones
2. **Test the interface, not the implementation**: Focus on verifying API contracts and CLI behavior
3. **Be comprehensive**: Include tests for success cases, error cases, and edge cases
4. **Document clearly**: Use docstrings to explain what each test verifies
5. **Use helper methods**: Create reusable helper methods for common patterns (like CLI command execution)
6. **Verify structure**: Always verify response structures and output formats
7. **Test independently**: Ensure tests don't depend on each other
8. **Separate concerns**: Keep API tests separate from CLI tests, and both separate from unit tests


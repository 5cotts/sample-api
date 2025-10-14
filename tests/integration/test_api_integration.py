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
        self.assertEqual(data["docs_url"], "/docs")
        self.assertIn("endpoints", data)
        self.assertIsInstance(data["endpoints"], dict)

    def test_health_endpoint(self):
        """Test the health check endpoint."""
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["service"], "math-operations-api")


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

    def test_factorial_valid_input(self):
        """Test factorial endpoint with valid input."""
        response = client.get("/factorial/5")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "factorial")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], 5)
        self.assertEqual(data["result"], 120)

    def test_factorial_zero(self):
        """Test factorial endpoint with zero."""
        response = client.get("/factorial/0")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "factorial")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], 0)
        self.assertEqual(data["result"], 1)

    def test_factorial_invalid_negative(self):
        """Test factorial endpoint with negative number (should fail)."""
        response = client.get("/factorial/-5")
        self.assertEqual(response.status_code, 400)

        data = response.json()
        self.assertIn("Invalid input", data["detail"])

    def test_fibonacci_sequence(self):
        """Test fibonacci endpoint."""
        response = client.get("/fibonacci/8")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "fibonacci")
        self.assertTrue(data["success"])
        self.assertEqual(data["count"], 8)
        self.assertEqual(data["sequence"], [0, 1, 1, 2, 3, 5, 8, 13])

    def test_fibonacci_invalid_zero(self):
        """Test fibonacci endpoint with zero (should fail)."""
        response = client.get("/fibonacci/0")
        self.assertEqual(response.status_code, 400)

        data = response.json()
        self.assertIn("Invalid input", data["detail"])

    def test_prime_check_prime_number(self):
        """Test prime endpoint with a prime number."""
        response = client.get("/prime/17")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "is_prime")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], 17)
        self.assertTrue(data["is_prime"])

    def test_prime_check_composite_number(self):
        """Test prime endpoint with a composite number."""
        response = client.get("/prime/15")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "is_prime")
        self.assertTrue(data["success"])
        self.assertEqual(data["input"], 15)
        self.assertFalse(data["is_prime"])

    def test_prime_check_invalid_input(self):
        """Test prime endpoint with invalid input (< 2)."""
        response = client.get("/prime/1")
        self.assertEqual(response.status_code, 400)

        data = response.json()
        self.assertIn("Invalid input", data["detail"])


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

    def test_power_float_inputs(self):
        """Test power endpoint with float inputs."""
        payload = {"base": 4.0, "exponent": 0.5}
        response = client.post("/power", json=payload)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["operation"], "power")
        self.assertTrue(data["success"])
        self.assertEqual(data["base"], 4.0)
        self.assertEqual(data["exponent"], 0.5)
        self.assertEqual(data["result"], 2.0)

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

    def test_stats_float_numbers(self):
        """Test stats endpoint with float numbers."""
        payload = {"numbers": [1.5, 2.5, 3.5]}
        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        stats = data["statistics"]
        self.assertEqual(stats["count"], 3)
        self.assertEqual(stats["mean"], 2.5)
        self.assertEqual(stats["median"], 2.5)

    def test_stats_empty_list(self):
        """Test stats endpoint with empty list (should fail validation)."""
        payload = {"numbers": []}
        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 422)  # Validation error

        data = response.json()
        self.assertIn("detail", data)

    def test_stats_missing_numbers_field(self):
        """Test stats endpoint with missing numbers field."""
        payload = {}
        response = client.post("/stats", json=payload)
        self.assertEqual(response.status_code, 422)  # Validation error

    def test_stats_invalid_content_type(self):
        """Test POST endpoint without proper JSON content type."""
        response = client.post("/stats", data="invalid")
        self.assertEqual(response.status_code, 422)  # Should fail validation


class TestErrorHandling(unittest.TestCase):
    """Test error handling and edge cases."""

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


# Performance and load testing (basic examples)
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


if __name__ == "__main__":
    # Run integration tests when script is executed directly
    unittest.main()

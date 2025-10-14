"""
Unit Tests for Mathematical Operations Business Logic

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

import unittest

from src.math_operations import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)


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
        self.assertEqual(square(-1), 1)

    def test_square_zero(self):
        """Test squaring zero."""
        self.assertEqual(square(0), 0)

    def test_square_float(self):
        """Test squaring floating-point numbers."""
        self.assertEqual(square(2.5), 6.25)
        self.assertEqual(square(-2.5), 6.25)
        self.assertAlmostEqual(square(0.1), 0.01, places=7)

    def test_square_invalid_input(self):
        """Test error handling for invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            square("5")

        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            square([5])

        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            square(None)


class TestPowerFunction(unittest.TestCase):
    """Tests for the power function."""

    def test_power_positive_integers(self):
        """Test power with positive integers."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)

    def test_power_with_floats(self):
        """Test power with floating-point numbers."""
        self.assertEqual(power(2.0, 3.0), 8.0)
        self.assertEqual(power(4, 0.5), 2.0)
        self.assertEqual(power(9, 0.5), 3.0)

    def test_power_negative_base(self):
        """Test power with negative base."""
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        self.assertEqual(power(2, -2), 0.25)
        self.assertEqual(power(10, -1), 0.1)

    def test_power_zero_cases(self):
        """Test power with zero values."""
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(5, 0), 1)

    def test_power_invalid_input(self):
        """Test error handling for invalid input types."""
        with self.assertRaisesRegex(
            TypeError, "Both base and exponent must be numbers"
        ):
            power("2", 3)

        with self.assertRaisesRegex(
            TypeError, "Both base and exponent must be numbers"
        ):
            power(2, "3")


class TestFactorialFunction(unittest.TestCase):
    """Tests for the factorial function."""

    def test_factorial_small_numbers(self):
        """Test factorial of small numbers."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_factorial_larger_numbers(self):
        """Test factorial of larger numbers."""
        self.assertEqual(factorial(10), 3628800)

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

    def test_factorial_non_integer_input(self):
        """Test factorial with non-integer input."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            factorial(5.5)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            factorial("5")


class TestFibonacciFunction(unittest.TestCase):
    """Tests for the fibonacci function."""

    def test_fibonacci_small_sequences(self):
        """Test small Fibonacci sequences."""
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_larger_sequence(self):
        """Test larger Fibonacci sequence."""
        result = fibonacci(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)

    def test_fibonacci_invalid_input(self):
        """Test fibonacci with invalid input."""
        with self.assertRaisesRegex(ValueError, "Input must be a positive integer"):
            fibonacci(0)

        with self.assertRaisesRegex(ValueError, "Input must be a positive integer"):
            fibonacci(-1)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            fibonacci(5.5)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            fibonacci("5")


class TestIsPrimeFunction(unittest.TestCase):
    """Tests for the is_prime function."""

    def test_prime_numbers(self):
        """Test with known prime numbers."""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(97))

    def test_composite_numbers(self):
        """Test with composite (non-prime) numbers."""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(21))
        self.assertFalse(is_prime(100))

    def test_prime_edge_cases(self):
        """Test edge cases for prime checking."""
        with self.assertRaisesRegex(
            ValueError, "Prime numbers are defined for integers >= 2"
        ):
            is_prime(0)

        with self.assertRaisesRegex(
            ValueError, "Prime numbers are defined for integers >= 2"
        ):
            is_prime(1)

        with self.assertRaisesRegex(
            ValueError, "Prime numbers are defined for integers >= 2"
        ):
            is_prime(-5)

    def test_prime_invalid_input(self):
        """Test is_prime with invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            is_prime(5.5)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            is_prime("5")


class TestCalculateStatsFunction(unittest.TestCase):
    """Tests for the calculate_stats function."""

    def test_stats_basic(self):
        """Test basic statistics calculation."""
        numbers = [1, 2, 3, 4, 5]
        result = calculate_stats(numbers)

        self.assertEqual(result["count"], 5)
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["median"], 3)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 5)
        self.assertEqual(result["sum"], 15)

    def test_stats_even_count(self):
        """Test statistics with even number of elements (median calculation)."""
        numbers = [1, 2, 3, 4]
        result = calculate_stats(numbers)

        self.assertEqual(result["count"], 4)
        self.assertEqual(result["mean"], 2.5)
        self.assertEqual(result["median"], 2.5)  # Average of 2 and 3
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 4)
        self.assertEqual(result["sum"], 10)

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

    def test_stats_with_floats(self):
        """Test statistics with floating-point numbers."""
        numbers = [1.5, 2.5, 3.5]
        result = calculate_stats(numbers)

        self.assertEqual(result["count"], 3)
        self.assertAlmostEqual(result["mean"], 2.5, places=7)
        self.assertEqual(result["median"], 2.5)
        self.assertEqual(result["min"], 1.5)
        self.assertEqual(result["max"], 3.5)
        self.assertAlmostEqual(result["sum"], 7.5, places=7)

    def test_stats_negative_numbers(self):
        """Test statistics with negative numbers."""
        numbers = [-3, -1, 0, 1, 3]
        result = calculate_stats(numbers)

        self.assertEqual(result["count"], 5)
        self.assertEqual(result["mean"], 0)
        self.assertEqual(result["median"], 0)
        self.assertEqual(result["min"], -3)
        self.assertEqual(result["max"], 3)
        self.assertEqual(result["sum"], 0)

    def test_stats_empty_list(self):
        """Test statistics with empty list."""
        with self.assertRaisesRegex(ValueError, "List cannot be empty"):
            calculate_stats([])

    def test_stats_invalid_input_type(self):
        """Test statistics with invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be a list"):
            calculate_stats("not a list")

        with self.assertRaisesRegex(TypeError, "Input must be a list"):
            calculate_stats(123)

    def test_stats_non_numeric_elements(self):
        """Test statistics with non-numeric elements in list."""
        with self.assertRaisesRegex(TypeError, "All elements must be numbers"):
            calculate_stats([1, 2, "3", 4])

        with self.assertRaisesRegex(TypeError, "All elements must be numbers"):
            calculate_stats([1, 2, None, 4])

        with self.assertRaisesRegex(TypeError, "All elements must be numbers"):
            calculate_stats([1, 2, [3], 4])


# unittest configuration
if __name__ == "__main__":
    # Run tests if this file is executed directly
    unittest.main()

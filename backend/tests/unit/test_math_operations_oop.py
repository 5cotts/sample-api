"""
Unit Tests for Mathematical Operations Business Logic (OOP Implementation)

These tests demonstrate how to test business logic implemented using
object-oriented programming. The tests verify that the OOP implementation
provides the same functionality as the functional implementation, but
accessed through instance methods of the MathOperations class.

Tests cover:
- Happy path scenarios
- Edge cases
- Error conditions
- Input validation
- Class instantiation
"""

import unittest

from src.math_operations_oop import MathOperations


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


class TestSquareMethod(unittest.TestCase):
    """Tests for the square method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_square_positive_integer(self):
        """Test squaring positive integers."""
        self.assertEqual(self.calculator.square(5), 25)
        self.assertEqual(self.calculator.square(10), 100)
        self.assertEqual(self.calculator.square(1), 1)

    def test_square_negative_integer(self):
        """Test squaring negative integers."""
        self.assertEqual(self.calculator.square(-5), 25)
        self.assertEqual(self.calculator.square(-10), 100)
        self.assertEqual(self.calculator.square(-1), 1)

    def test_square_zero(self):
        """Test squaring zero."""
        self.assertEqual(self.calculator.square(0), 0)

    def test_square_float(self):
        """Test squaring floating-point numbers."""
        self.assertEqual(self.calculator.square(2.5), 6.25)
        self.assertEqual(self.calculator.square(-2.5), 6.25)
        self.assertAlmostEqual(self.calculator.square(0.1), 0.01, places=7)

    def test_square_invalid_input(self):
        """Test error handling for invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.calculator.square("5")

        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.calculator.square([5])

        with self.assertRaisesRegex(TypeError, "Input must be a number"):
            self.calculator.square(None)


class TestPowerMethod(unittest.TestCase):
    """Tests for the power method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_power_positive_integers(self):
        """Test power with positive integers."""
        self.assertEqual(self.calculator.power(2, 3), 8)
        self.assertEqual(self.calculator.power(5, 2), 25)
        self.assertEqual(self.calculator.power(10, 0), 1)

    def test_power_with_floats(self):
        """Test power with floating-point numbers."""
        self.assertEqual(self.calculator.power(2.0, 3.0), 8.0)
        self.assertEqual(self.calculator.power(4, 0.5), 2.0)
        self.assertEqual(self.calculator.power(9, 0.5), 3.0)

    def test_power_negative_base(self):
        """Test power with negative base."""
        self.assertEqual(self.calculator.power(-2, 3), -8)
        self.assertEqual(self.calculator.power(-2, 2), 4)

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        self.assertEqual(self.calculator.power(2, -2), 0.25)
        self.assertEqual(self.calculator.power(10, -1), 0.1)

    def test_power_zero_cases(self):
        """Test power with zero values."""
        self.assertEqual(self.calculator.power(0, 5), 0)
        self.assertEqual(self.calculator.power(5, 0), 1)

    def test_power_invalid_input(self):
        """Test error handling for invalid input types."""
        with self.assertRaisesRegex(
            TypeError, "Both base and exponent must be numbers"
        ):
            self.calculator.power("2", 3)

        with self.assertRaisesRegex(
            TypeError, "Both base and exponent must be numbers"
        ):
            self.calculator.power(2, "3")


class TestFactorialMethod(unittest.TestCase):
    """Tests for the factorial method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_factorial_small_numbers(self):
        """Test factorial of small numbers."""
        self.assertEqual(self.calculator.factorial(0), 1)
        self.assertEqual(self.calculator.factorial(1), 1)
        self.assertEqual(self.calculator.factorial(2), 2)
        self.assertEqual(self.calculator.factorial(3), 6)
        self.assertEqual(self.calculator.factorial(4), 24)
        self.assertEqual(self.calculator.factorial(5), 120)

    def test_factorial_larger_numbers(self):
        """Test factorial of larger numbers."""
        self.assertEqual(self.calculator.factorial(10), 3628800)

    def test_factorial_negative_input(self):
        """Test factorial with negative input."""
        with self.assertRaisesRegex(
            ValueError, "Factorial is only defined for non-negative integers"
        ):
            self.calculator.factorial(-1)

        with self.assertRaisesRegex(
            ValueError, "Factorial is only defined for non-negative integers"
        ):
            self.calculator.factorial(-5)

    def test_factorial_non_integer_input(self):
        """Test factorial with non-integer input."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            self.calculator.factorial(5.5)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            self.calculator.factorial("5")


class TestFibonacciMethod(unittest.TestCase):
    """Tests for the fibonacci method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_fibonacci_small_sequences(self):
        """Test small Fibonacci sequences."""
        self.assertEqual(self.calculator.fibonacci(1), [0])
        self.assertEqual(self.calculator.fibonacci(2), [0, 1])
        self.assertEqual(self.calculator.fibonacci(3), [0, 1, 1])
        self.assertEqual(self.calculator.fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_larger_sequence(self):
        """Test larger Fibonacci sequence."""
        result = self.calculator.fibonacci(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(result, expected)

    def test_fibonacci_invalid_input(self):
        """Test fibonacci with invalid input."""
        with self.assertRaisesRegex(ValueError, "Input must be a positive integer"):
            self.calculator.fibonacci(0)

        with self.assertRaisesRegex(ValueError, "Input must be a positive integer"):
            self.calculator.fibonacci(-1)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            self.calculator.fibonacci(5.5)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            self.calculator.fibonacci("5")


class TestIsPrimeMethod(unittest.TestCase):
    """Tests for the is_prime method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_prime_numbers(self):
        """Test with known prime numbers."""
        self.assertTrue(self.calculator.is_prime(2))
        self.assertTrue(self.calculator.is_prime(3))
        self.assertTrue(self.calculator.is_prime(5))
        self.assertTrue(self.calculator.is_prime(7))
        self.assertTrue(self.calculator.is_prime(11))
        self.assertTrue(self.calculator.is_prime(13))
        self.assertTrue(self.calculator.is_prime(17))
        self.assertTrue(self.calculator.is_prime(19))
        self.assertTrue(self.calculator.is_prime(97))

    def test_composite_numbers(self):
        """Test with composite (non-prime) numbers."""
        self.assertFalse(self.calculator.is_prime(4))
        self.assertFalse(self.calculator.is_prime(6))
        self.assertFalse(self.calculator.is_prime(8))
        self.assertFalse(self.calculator.is_prime(9))
        self.assertFalse(self.calculator.is_prime(10))
        self.assertFalse(self.calculator.is_prime(15))
        self.assertFalse(self.calculator.is_prime(21))
        self.assertFalse(self.calculator.is_prime(100))

    def test_prime_edge_cases(self):
        """Test edge cases for prime checking."""
        with self.assertRaisesRegex(
            ValueError, "Prime numbers are defined for integers >= 2"
        ):
            self.calculator.is_prime(0)

        with self.assertRaisesRegex(
            ValueError, "Prime numbers are defined for integers >= 2"
        ):
            self.calculator.is_prime(1)

        with self.assertRaisesRegex(
            ValueError, "Prime numbers are defined for integers >= 2"
        ):
            self.calculator.is_prime(-5)

    def test_prime_invalid_input(self):
        """Test is_prime with invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            self.calculator.is_prime(5.5)

        with self.assertRaisesRegex(TypeError, "Input must be an integer"):
            self.calculator.is_prime("5")


class TestCalculateStatsMethod(unittest.TestCase):
    """Tests for the calculate_stats method."""

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = MathOperations()

    def test_stats_basic(self):
        """Test basic statistics calculation."""
        numbers = [1, 2, 3, 4, 5]
        result = self.calculator.calculate_stats(numbers)

        self.assertEqual(result["count"], 5)
        self.assertEqual(result["mean"], 3.0)
        self.assertEqual(result["median"], 3)
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 5)
        self.assertEqual(result["sum"], 15)

    def test_stats_even_count(self):
        """Test statistics with even number of elements (median calculation)."""
        numbers = [1, 2, 3, 4]
        result = self.calculator.calculate_stats(numbers)

        self.assertEqual(result["count"], 4)
        self.assertEqual(result["mean"], 2.5)
        self.assertEqual(result["median"], 2.5)  # Average of 2 and 3
        self.assertEqual(result["min"], 1)
        self.assertEqual(result["max"], 4)
        self.assertEqual(result["sum"], 10)

    def test_stats_single_number(self):
        """Test statistics with a single number."""
        numbers = [42]
        result = self.calculator.calculate_stats(numbers)

        self.assertEqual(result["count"], 1)
        self.assertEqual(result["mean"], 42)
        self.assertEqual(result["median"], 42)
        self.assertEqual(result["min"], 42)
        self.assertEqual(result["max"], 42)
        self.assertEqual(result["sum"], 42)

    def test_stats_with_floats(self):
        """Test statistics with floating-point numbers."""
        numbers = [1.5, 2.5, 3.5]
        result = self.calculator.calculate_stats(numbers)

        self.assertEqual(result["count"], 3)
        self.assertAlmostEqual(result["mean"], 2.5, places=7)
        self.assertEqual(result["median"], 2.5)
        self.assertEqual(result["min"], 1.5)
        self.assertEqual(result["max"], 3.5)
        self.assertAlmostEqual(result["sum"], 7.5, places=7)

    def test_stats_negative_numbers(self):
        """Test statistics with negative numbers."""
        numbers = [-3, -1, 0, 1, 3]
        result = self.calculator.calculate_stats(numbers)

        self.assertEqual(result["count"], 5)
        self.assertEqual(result["mean"], 0)
        self.assertEqual(result["median"], 0)
        self.assertEqual(result["min"], -3)
        self.assertEqual(result["max"], 3)
        self.assertEqual(result["sum"], 0)

    def test_stats_empty_list(self):
        """Test statistics with empty list."""
        with self.assertRaisesRegex(ValueError, "List cannot be empty"):
            self.calculator.calculate_stats([])

    def test_stats_invalid_input_type(self):
        """Test statistics with invalid input types."""
        with self.assertRaisesRegex(TypeError, "Input must be a list"):
            self.calculator.calculate_stats("not a list")

        with self.assertRaisesRegex(TypeError, "Input must be a list"):
            self.calculator.calculate_stats(123)

    def test_stats_non_numeric_elements(self):
        """Test statistics with non-numeric elements in list."""
        with self.assertRaisesRegex(TypeError, "All elements must be numbers"):
            self.calculator.calculate_stats([1, 2, "3", 4])

        with self.assertRaisesRegex(TypeError, "All elements must be numbers"):
            self.calculator.calculate_stats([1, 2, None, 4])

        with self.assertRaisesRegex(TypeError, "All elements must be numbers"):
            self.calculator.calculate_stats([1, 2, [3], 4])


class TestMultipleInstances(unittest.TestCase):
    """Tests demonstrating that multiple instances work independently."""

    def test_independent_instances(self):
        """Test that multiple instances produce the same results independently."""
        calc1 = MathOperations()
        calc2 = MathOperations()

        # Both instances should produce the same results
        self.assertEqual(calc1.square(5), calc2.square(5))
        self.assertEqual(calc1.factorial(5), calc2.factorial(5))
        self.assertEqual(calc1.is_prime(17), calc2.is_prime(17))

    def test_instance_methods_work_together(self):
        """Test that all methods work together on the same instance."""
        calc = MathOperations()

        # Use multiple methods on the same instance
        result1 = calc.square(5)
        result2 = calc.power(2, 3)
        result3 = calc.factorial(5)
        result4 = calc.is_prime(17)
        result5 = calc.calculate_stats([1, 2, 3, 4, 5])

        self.assertEqual(result1, 25)
        self.assertEqual(result2, 8)
        self.assertEqual(result3, 120)
        self.assertTrue(result4)
        self.assertEqual(result5["mean"], 3.0)


# unittest configuration
if __name__ == "__main__":
    # Run tests if this file is executed directly
    unittest.main()

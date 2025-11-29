"""
Object-Oriented Programming (OOP) Implementation of Mathematical Operations

This module provides an OOP alternative to the functional programming approach
in math_operations_functional.py. It demonstrates how the same business logic can be
organized using object-oriented principles.

OOP Benefits Demonstrated:
- Encapsulation: All related mathematical operations are grouped within a single class
- Extensibility: Easy to add new operations or modify behavior through inheritance
- State Management: Class can maintain state (e.g., operation history, configuration)
- Interface Consistency: All operations accessed through a consistent interface
- Polymorphism: Can be subclassed to provide different implementations

Usage:
    # Create an instance
    calculator = MathOperations()

    # Use instance methods
    result = calculator.square(5)
    stats = calculator.calculate_stats([1, 2, 3, 4, 5])

    # Multiple instances can have different configurations if state is added
    calculator1 = MathOperations()
    calculator2 = MathOperations()
"""

from typing import List, Union


class MathOperations:
    """
    A class that encapsulates mathematical operations using object-oriented design.

    This class provides the same functionality as the functional implementation
    in math_operations_functional.py, but organized as instance methods. While the current
    implementation is stateless, the OOP design allows for future enhancements
    such as:
    - Operation history tracking
    - Configuration settings (precision, rounding modes)
    - Caching of results
    - Different calculation strategies

    All methods maintain the same behavior, error handling, and type signatures
    as their functional counterparts.
    """

    def __init__(self) -> None:
        """
        Initialize a MathOperations instance.

        Currently, the class is stateless, but this constructor can be extended
        to accept configuration parameters or initialize instance variables
        for features like operation history or caching.
        """
        pass

    def square(self, number: Union[int, float]) -> Union[int, float]:
        """
        Calculate the square of a number.

        This method provides the same functionality as the square() function
        in the functional implementation, but as an instance method. This
        allows it to be part of a cohesive interface and enables potential
        state management or logging at the class level.

        Args:
            number: The number to square

        Returns:
            The square of the input number

        Raises:
            TypeError: If input is not a number
        """
        if not isinstance(number, (int, float)):
            raise TypeError("Input must be a number (int or float)")

        return number**2

    def power(
        self, base: Union[int, float], exponent: Union[int, float]
    ) -> Union[int, float]:
        """
        Calculate base raised to the power of exponent.

        As an instance method, this operation can be extended to support
        features like operation logging or result caching without changing
        the public interface.

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

        return base**exponent

    def factorial(self, n: int) -> int:
        """
        Calculate the factorial of a non-negative integer.

        The OOP implementation allows this method to be part of a larger
        mathematical operations suite, making it easy to extend with
        features like memoization or different calculation algorithms
        through inheritance.

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

        if n == 0 or n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            result *= i

        return result

    def fibonacci(self, n: int) -> List[int]:
        """
        Generate the first n numbers in the Fibonacci sequence.

        As an instance method, this could be extended to cache sequences
        or maintain a history of generated sequences as instance state.

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

        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

        return fib_sequence

    def is_prime(self, n: int) -> bool:
        """
        Check if a number is prime.

        The OOP design allows this method to be part of a comprehensive
        number theory class that could include related operations like
        prime factorization, GCD, LCM, etc.

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

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        # Check odd divisors up to sqrt(n)
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False

        return True

    def calculate_stats(self, numbers: List[Union[int, float]]) -> dict:
        """
        Calculate basic statistics for a list of numbers.

        This method demonstrates how OOP can encapsulate complex operations
        that return structured data. The class design allows for easy extension
        with additional statistical methods (variance, standard deviation, etc.)
        or configuration options (precision, rounding).

        Args:
            numbers: List of numbers

        Returns:
            Dictionary containing count, mean, median, min, max, and sum

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

        sorted_numbers = sorted(numbers)
        count = len(numbers)

        # Calculate mean
        mean = sum(numbers) / count

        # Calculate median
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

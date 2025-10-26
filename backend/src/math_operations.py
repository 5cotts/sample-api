"""
Business Logic Module for Mathematical Operations

This module contains pure business logic functions that can be used
independently of any API implementation. This demonstrates the important
principle of separating business logic from API infrastructure.

These functions are designed to be:
- Pure functions with no side effects
- Easily testable
- Reusable across different interfaces (API, CLI, etc.)
"""

from typing import List, Union


def square(number: Union[int, float]) -> Union[int, float]:
    """
    Calculate the square of a number.

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


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Calculate base raised to the power of exponent.

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


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

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


def fibonacci(n: int) -> List[int]:
    """
    Generate the first n numbers in the Fibonacci sequence.

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


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

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


def calculate_stats(numbers: List[Union[int, float]]) -> dict:
    """
    Calculate basic statistics for a list of numbers.

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

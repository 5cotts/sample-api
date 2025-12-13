"""
Sample API Business Logic Package

This package contains the core business logic for mathematical operations.
The package provides two implementations:
- Functional: Pure functions with no side effects (default exports)
- Object-Oriented: Class-based implementation with MathOperations class

All functions are designed to be pure, testable, and reusable across
different interfaces (API, CLI, etc.).
"""

from .math_operations.functional import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)
from .math_operations.oop import MathOperations

__version__ = "1.0.0"
__all__ = [
    # Functional implementation (default)
    "square",
    "power",
    "factorial",
    "fibonacci",
    "is_prime",
    "calculate_stats",
    # Object-oriented implementation
    "MathOperations",
]

"""
Math Operations Package

This package contains mathematical operations implementations in both
functional and object-oriented programming paradigms.

Modules:
- functional: Pure function-based implementation
- oop: Class-based object-oriented implementation
"""

from .functional import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)
from .oop import MathOperations

__all__ = [
    # Functional implementation
    "square",
    "power",
    "factorial",
    "fibonacci",
    "is_prime",
    "calculate_stats",
    # Object-oriented implementation
    "MathOperations",
]

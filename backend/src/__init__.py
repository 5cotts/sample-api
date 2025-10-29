"""
Sample API Business Logic Package

This package contains the core business logic for mathematical operations.
All functions are designed to be pure, testable, and reusable across
different interfaces (API, CLI, etc.).
"""

from .math_operations import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)

__version__ = "1.0.0"
__all__ = ["square", "power", "factorial", "fibonacci", "is_prime", "calculate_stats"]

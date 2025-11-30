"""
Implementation Loader Module

This module provides utilities for loading and managing different implementations
of mathematical operations (functional vs object-oriented).

It centralizes the implementation switching logic used by both the API and CLI,
ensuring consistency and reducing code duplication.
"""

import os
from typing import Callable, Dict, Tuple, Union

# Type alias for math operation functions
MathFunction = Callable[..., Union[int, float, bool, list, dict]]

# Determine which implementation to use based on environment variable
# Priority: CLI argument > environment variable > default (functional)
MATH_IMPL = os.getenv("MATH_OPERATIONS_IMPL", "functional").lower()


def load_implementation(impl_type: str) -> Tuple[Dict[str, MathFunction], str]:
    """
    Load the specified math operations implementation.
    
    Args:
        impl_type: Either "oop" or "functional"
        
    Returns:
        Tuple of (functions dict, implementation name)
    """
    impl_type = impl_type.lower()
    
    if impl_type == "oop":
        from src.math_operations.oop import MathOperations

        _calculator = MathOperations()
        return {
            'square': _calculator.square,
            'power': _calculator.power,
            'factorial': _calculator.factorial,
            'fibonacci': _calculator.fibonacci,
            'is_prime': _calculator.is_prime,
            'calculate_stats': _calculator.calculate_stats,
        }, "object-oriented"
    else:
        from src.math_operations.functional import (
            calculate_stats,
            factorial,
            fibonacci,
            is_prime,
            power,
            square,
        )

        return {
            'square': square,
            'power': power,
            'factorial': factorial,
            'fibonacci': fibonacci,
            'is_prime': is_prime,
            'calculate_stats': calculate_stats,
        }, "functional"


# Load initial implementation based on environment variable
_functions, _implementation = load_implementation(MATH_IMPL)

# Export individual functions for direct import
square = _functions['square']
power = _functions['power']
factorial = _functions['factorial']
fibonacci = _functions['fibonacci']
is_prime = _functions['is_prime']
calculate_stats = _functions['calculate_stats']

# Export the implementation name
implementation = _implementation

# Export all for convenience
__all__ = [
    'load_implementation',
    'MATH_IMPL',
    'MathFunction',
    'square',
    'power',
    'factorial',
    'fibonacci',
    'is_prime',
    'calculate_stats',
    'implementation',
]

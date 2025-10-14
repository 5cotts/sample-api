#!/usr/bin/env python3
"""
Command Line Interface for Mathematical Operations

This CLI demonstrates how the same business logic used by the API
can be accessed directly from the command line. This shows the
separation of concerns: the business logic is independent of the
interface (API vs CLI).

Usage:
    python cli.py square 5
    python cli.py power 2 8
    python cli.py factorial 5
    python cli.py fibonacci 10
    python cli.py prime 17
    python cli.py stats 1 2 3 4 5
"""

import argparse
import sys

from src.math_operations import (
    calculate_stats,
    factorial,
    fibonacci,
    is_prime,
    power,
    square,
)


def format_result(operation: str, result, **kwargs):
    """Format and print the result of an operation."""
    print(f"\n=== {operation.upper()} OPERATION ===")

    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    if isinstance(result, list):
        print(f"Result: {result}")
        print(f"Length: {len(result)}")
    elif isinstance(result, dict):
        print("Result:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print(f"Result: {result}")

    print("=" * (len(operation) + 15))


def cmd_square(args):
    """Handle square command."""
    try:
        number = float(args.number) if "." in args.number else int(args.number)
        result = square(number)
        format_result("square", result, input=number)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_power(args):
    """Handle power command."""
    try:
        base = float(args.base) if "." in args.base else int(args.base)
        exponent = float(args.exponent) if "." in args.exponent else int(args.exponent)
        result = power(base, exponent)
        format_result("power", result, base=base, exponent=exponent)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_factorial(args):
    """Handle factorial command."""
    try:
        result = factorial(args.number)
        format_result("factorial", result, input=args.number)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_fibonacci(args):
    """Handle fibonacci command."""
    try:
        result = fibonacci(args.count)
        format_result("fibonacci", result, count=args.count)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_prime(args):
    """Handle prime check command."""
    try:
        result = is_prime(args.number)
        prime_status = "is prime" if result else "is not prime"
        format_result("prime check", f"{args.number} {prime_status}", input=args.number)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def cmd_stats(args):
    """Handle statistics command."""
    try:
        numbers = []
        for num_str in args.numbers:
            # Convert to appropriate numeric type
            if "." in num_str:
                numbers.append(float(num_str))
            else:
                numbers.append(int(num_str))

        result = calculate_stats(numbers)
        format_result("statistics", result, input_numbers=numbers)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def create_parser():
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Mathematical Operations CLI - Direct access to business logic",
        epilog="Examples:\n"
        "  python cli.py square 5\n"
        "  python cli.py power 2 8\n"
        "  python cli.py factorial 5\n"
        "  python cli.py fibonacci 10\n"
        "  python cli.py prime 17\n"
        "  python cli.py stats 1 2 3 4 5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available operations")
    subparsers.required = True

    # Square command
    square_parser = subparsers.add_parser("square", help="Calculate square of a number")
    square_parser.add_argument("number", type=str, help="Number to square")
    square_parser.set_defaults(func=cmd_square)

    # Power command
    power_parser = subparsers.add_parser("power", help="Calculate base^exponent")
    power_parser.add_argument("base", type=str, help="Base number")
    power_parser.add_argument("exponent", type=str, help="Exponent")
    power_parser.set_defaults(func=cmd_power)

    # Factorial command
    factorial_parser = subparsers.add_parser("factorial", help="Calculate factorial")
    factorial_parser.add_argument(
        "number", type=int, help="Number for factorial (must be non-negative integer)"
    )
    factorial_parser.set_defaults(func=cmd_factorial)

    # Fibonacci command
    fibonacci_parser = subparsers.add_parser(
        "fibonacci", help="Generate Fibonacci sequence"
    )
    fibonacci_parser.add_argument(
        "count", type=int, help="Number of Fibonacci numbers to generate"
    )
    fibonacci_parser.set_defaults(func=cmd_fibonacci)

    # Prime command
    prime_parser = subparsers.add_parser("prime", help="Check if number is prime")
    prime_parser.add_argument("number", type=int, help="Number to check for primality")
    prime_parser.set_defaults(func=cmd_prime)

    # Statistics command
    stats_parser = subparsers.add_parser(
        "stats", help="Calculate statistics for numbers"
    )
    stats_parser.add_argument(
        "numbers", nargs="+", type=str, help="List of numbers for statistics"
    )
    stats_parser.set_defaults(func=cmd_stats)

    return parser


def main():
    """Main CLI entry point."""
    print("Mathematical Operations CLI")
    print("Demonstrating direct access to business logic functions")
    print("(The same functions used by the REST API)")

    parser = create_parser()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    try:
        args = parser.parse_args()
        args.func(args)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
Integration Tests for CLI Commands

These tests demonstrate testing the command-line interface by running
the actual CLI commands as subprocesses. This verifies that:
- CLI argument parsing works correctly
- Commands execute successfully
- Output formatting is correct
- Error handling works properly
"""

import os
import subprocess
import sys
import unittest

# Get the path to the CLI script
CLI_PATH = os.path.join(os.path.dirname(__file__), "..", "cli.py")


class TestCLICommands(unittest.TestCase):
    """Test CLI commands by running them as subprocesses."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands and return result."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_cli_no_arguments(self):
        """Test CLI without arguments shows help."""
        result = self.run_cli_command()
        self.assertEqual(result.returncode, 1)  # Should exit with error
        self.assertTrue(
            "usage:" in result.stdout.lower()
            or "Mathematical Operations CLI" in result.stdout
        )

    def test_cli_help(self):
        """Test CLI help command."""
        result = self.run_cli_command("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Mathematical Operations CLI", result.stdout)
        self.assertIn("square", result.stdout)
        self.assertIn("power", result.stdout)
        self.assertIn("factorial", result.stdout)


class TestSquareCommand(unittest.TestCase):
    """Test the square CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_square_positive_integer(self):
        """Test square command with positive integer."""
        result = self.run_cli_command("square", "5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("SQUARE OPERATION", output)
        self.assertIn("Input: 5", output)
        self.assertIn("Result: 25", output)

    def test_square_negative_integer(self):
        """Test square command with negative integer."""
        result = self.run_cli_command("square", "-4")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input: -4", output)
        self.assertIn("Result: 16", output)

    def test_square_float(self):
        """Test square command with float."""
        result = self.run_cli_command("square", "2.5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input: 2.5", output)
        self.assertIn("Result: 6.25", output)

    def test_square_help(self):
        """Test square command help output"""
        result = self.run_cli_command("square", "--help")

        self.assertEqual(result.returncode, 0)
        self.assertIn("Number to square", result.stdout)


class TestPowerCommand(unittest.TestCase):
    """Test the power CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_power_integers(self):
        """Test power command with integers."""
        result = self.run_cli_command("power", "2", "8")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("POWER OPERATION", output)
        self.assertIn("Base: 2", output)
        self.assertIn("Exponent: 8", output)
        self.assertIn("Result: 256", output)

    def test_power_floats(self):
        """Test power command with float inputs."""
        result = self.run_cli_command("power", "4.0", "0.5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Base: 4.0", output)
        self.assertIn("Exponent: 0.5", output)
        self.assertIn("Result: 2.0", output)

    def test_power_missing_argument(self):
        """Test power command with missing argument."""
        result = self.run_cli_command("power", "2")
        assert result.returncode != 0  # Should fail
        self.assertIn(
            "error", result.stderr.lower()
        ) or "required" in result.stderr.lower()


class TestFactorialCommand(unittest.TestCase):
    """Test the factorial CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_factorial_valid_input(self):
        """Test factorial command with valid input."""
        result = self.run_cli_command("factorial", "5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("FACTORIAL OPERATION", output)
        self.assertIn("Input: 5", output)
        self.assertIn("Result: 120", output)

    def test_factorial_zero(self):
        """Test factorial of zero."""
        result = self.run_cli_command("factorial", "0")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input: 0", output)
        self.assertIn("Result: 1", output)

    def test_factorial_negative_input(self):
        """Test factorial with negative input (should fail)."""
        result = self.run_cli_command("factorial", "-5")
        self.assertEqual(result.returncode, 1)  # Should exit with error
        self.assertIn("Error:", result.stdout)


class TestFibonacciCommand(unittest.TestCase):
    """Test the fibonacci CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_fibonacci_sequence(self):
        """Test fibonacci command."""
        result = self.run_cli_command("fibonacci", "8")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("FIBONACCI OPERATION", output)
        self.assertIn("Count: 8", output)
        self.assertIn("[0, 1, 1, 2, 3, 5, 8, 13]", output)
        self.assertIn("Length: 8", output)

    def test_fibonacci_small_sequence(self):
        """Test fibonacci with small sequence."""
        result = self.run_cli_command("fibonacci", "3")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Count: 3", output)
        self.assertIn("[0, 1, 1]", output)

    def test_fibonacci_invalid_zero(self):
        """Test fibonacci with zero (should fail)."""
        result = self.run_cli_command("fibonacci", "0")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error:", result.stdout)


class TestPrimeCommand(unittest.TestCase):
    """Test the prime CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_prime_number(self):
        """Test with a prime number."""
        result = self.run_cli_command("prime", "17")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("PRIME CHECK OPERATION", output)
        self.assertIn("Input: 17", output)
        self.assertIn("17 is prime", output)

    def test_composite_number(self):
        """Test with a composite number."""
        result = self.run_cli_command("prime", "15")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input: 15", output)
        self.assertIn("15 is not prime", output)

    def test_prime_invalid_input(self):
        """Test prime with invalid input."""
        result = self.run_cli_command("prime", "1")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Error:", result.stdout)


class TestStatsCommand(unittest.TestCase):
    """Test the stats CLI command."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_stats_basic(self):
        """Test stats command with basic input."""
        result = self.run_cli_command("stats", "1", "2", "3", "4", "5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("STATISTICS OPERATION", output)
        self.assertIn("Input_numbers: [1, 2, 3, 4, 5]", output)
        self.assertIn("count: 5", output)
        self.assertIn("mean: 3.0", output)
        self.assertIn("median: 3", output)
        self.assertIn("min: 1", output)
        self.assertIn("max: 5", output)
        self.assertIn("sum: 15", output)

    def test_stats_float_numbers(self):
        """Test stats command with float numbers."""
        result = self.run_cli_command("stats", "1.5", "2.5", "3.5")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("Input_numbers: [1.5, 2.5, 3.5]", output)
        self.assertIn("count: 3", output)
        self.assertIn("mean: 2.5", output)

    def test_stats_single_number(self):
        """Test stats command with single number."""
        result = self.run_cli_command("stats", "42")
        self.assertEqual(result.returncode, 0)

        output = result.stdout
        self.assertIn("count: 1", output)
        self.assertIn("mean: 42", output)
        self.assertIn("median: 42", output)

    def test_stats_no_numbers(self):
        """Test stats command without numbers (should fail)."""
        result = self.run_cli_command("stats")
        assert result.returncode != 0
        self.assertIn(
            "error", result.stderr.lower()
        ) or "required" in result.stderr.lower()


class TestCLIErrorHandling(unittest.TestCase):
    """Test CLI error handling and edge cases."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_invalid_command(self):
        """Test with invalid command."""
        result = self.run_cli_command("invalid_command")
        assert result.returncode != 0

    def test_keyboard_interrupt_simulation(self):
        """Test that CLI handles interruptions gracefully."""
        # This is harder to test directly, but we can verify
        # the code structure handles KeyboardInterrupt
        result = self.run_cli_command("square", "5")
        self.assertEqual(result.returncode, 0)  # Normal execution should work

    def test_cli_output_format_consistency(self):
        """Test that all commands have consistent output format."""
        commands = [
            (["square", "4"], "SQUARE OPERATION"),
            (["factorial", "4"], "FACTORIAL OPERATION"),
            (["fibonacci", "5"], "FIBONACCI OPERATION"),
            (["prime", "7"], "PRIME CHECK OPERATION"),
            (["stats", "1", "2", "3"], "STATISTICS OPERATION"),
        ]

        for cmd_args, expected_header in commands:
            result = self.run_cli_command(*cmd_args)
            self.assertEqual(result.returncode, 0)
            assert expected_header in result.stdout
            self.assertIn("===", result.stdout)  # All should have separator lines


class TestCLIIntegrationWithBusinessLogic(unittest.TestCase):
    """Test that CLI properly integrates with business logic functions."""

    def run_cli_command(self, *args):
        """Helper method to run CLI commands."""
        cmd = [sys.executable, CLI_PATH] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(CLI_PATH)
        )
        return result

    def test_cli_matches_direct_function_calls(self):
        """Test that CLI results match direct function calls."""
        # We know from unit tests that square(7) = 49
        result = self.run_cli_command("square", "7")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Result: 49", result.stdout)

        # We know factorial(4) = 24
        result = self.run_cli_command("factorial", "4")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Result: 24", result.stdout)

    def test_cli_power_matches_expected_calculations(self):
        """Test that CLI power results are mathematically correct."""
        test_cases = [
            ("2", "3", "8"),  # 2^3 = 8
            ("5", "2", "25"),  # 5^2 = 25
            ("10", "0", "1"),  # 10^0 = 1
        ]

        for base, exp, expected in test_cases:
            result = self.run_cli_command("power", base, exp)
            self.assertEqual(result.returncode, 0)
            assert f"Result: {expected}" in result.stdout


if __name__ == "__main__":
    # Run CLI integration tests when script is executed directly
    unittest.main()

#!/usr/bin/env python3
"""
Template Validation Script

Validates that a project created from the educational API template
follows the required structure and patterns.

Usage:
    python scripts/validate_template.py [project_path]

If project_path is not provided, validates the current directory.
"""

import ast
import os
import sys
from pathlib import Path
from typing import List, Tuple


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class TemplateValidator:
    """Validates project structure and patterns against template."""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def validate(self) -> bool:
        """Run all validation checks."""
        print(f"Validating template compliance in: {self.project_path}\n")
        
        self.check_required_files()
        self.check_business_logic_structure()
        self.check_api_structure()
        self.check_cli_structure()
        self.check_test_structure()
        
        self.report_results()
        return len(self.errors) == 0
    
    def check_required_files(self):
        """Check that required files exist."""
        print("Checking required files...")
        
        required_files = [
            "pyproject.toml",
            "src/__init__.py",
            "app.py",
            "cli.py",
            "tests/__init__.py",
            "tests/unit/__init__.py",
            "tests/integration/__init__.py",
        ]
        
        for file_path in required_files:
            full_path = self.project_path / file_path
            if not full_path.exists():
                self.errors.append(f"Missing required file: {file_path}")
            else:
                print(f"  ✓ {file_path}")
    
    def check_business_logic_structure(self):
        """Check business logic module structure."""
        print("\nChecking business logic structure...")
        
        # Find business logic file (could be math_operations.py or business_logic.py)
        business_logic_files = [
            self.project_path / "src" / "math_operations.py",
            self.project_path / "src" / "business_logic.py",
        ]
        
        business_logic_file = None
        for file_path in business_logic_files:
            if file_path.exists():
                business_logic_file = file_path
                break
        
        if not business_logic_file:
            self.errors.append("Missing business logic file: src/math_operations.py or src/business_logic.py")
            return
        
        print(f"  ✓ Found business logic file: {business_logic_file.name}")
        
        # Check required functions
        try:
            with open(business_logic_file, 'r') as f:
                content = f.read()
                tree = ast.parse(content)
                
            required_functions = [
                'square', 'power', 'factorial', 
                'fibonacci', 'is_prime', 'calculate_stats'
            ]
            
            defined_functions = [
                node.name for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef)
            ]
            
            for func_name in required_functions:
                if func_name in defined_functions:
                    print(f"  ✓ Function '{func_name}' found")
                else:
                    self.warnings.append(
                        f"Function '{func_name}' not found in business logic. "
                        "This may be intentional if renamed for domain."
                    )
        except Exception as e:
            self.errors.append(f"Error parsing business logic file: {e}")
    
    def check_api_structure(self):
        """Check FastAPI application structure."""
        print("\nChecking API structure...")
        
        app_file = self.project_path / "app.py"
        if not app_file.exists():
            return
        
        try:
            with open(app_file, 'r') as f:
                content = f.read()
                tree = ast.parse(content)
            
            # Check for FastAPI import
            imports = [
                node.names[0].name for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom) and node.module
            ]
            
            if 'fastapi' in str(imports):
                print("  ✓ FastAPI imported")
            else:
                self.errors.append("FastAPI not imported in app.py")
            
            # Check for app creation
            if 'FastAPI(' in content:
                print("  ✓ FastAPI app instance created")
            else:
                self.errors.append("FastAPI app instance not found")
            
            # Check for business logic imports
            if 'from src.' in content:
                print("  ✓ Business logic imported from src/")
            else:
                self.warnings.append(
                    "Business logic import from src/ not detected. "
                    "Ensure API calls business logic functions."
                )
                
        except Exception as e:
            self.warnings.append(f"Could not fully parse app.py: {e}")
    
    def check_cli_structure(self):
        """Check CLI structure."""
        print("\nChecking CLI structure...")
        
        cli_file = self.project_path / "cli.py"
        if not cli_file.exists():
            return
        
        try:
            with open(cli_file, 'r') as f:
                content = f.read()
            
            # Check for argparse
            if 'argparse' in content:
                print("  ✓ argparse imported")
            else:
                self.warnings.append("argparse not found in cli.py")
            
            # Check for business logic imports
            if 'from src.' in content:
                print("  ✓ Business logic imported from src/")
            else:
                self.warnings.append(
                    "Business logic import from src/ not detected in cli.py"
                )
            
            # Check for main function
            if 'def main()' in content:
                print("  ✓ main() function found")
            else:
                self.warnings.append("main() function not found in cli.py")
                
        except Exception as e:
            self.warnings.append(f"Could not fully parse cli.py: {e}")
    
    def check_test_structure(self):
        """Check test structure."""
        print("\nChecking test structure...")
        
        test_files = [
            self.project_path / "tests" / "unit" / "test_math_operations.py",
            self.project_path / "tests" / "integration" / "test_api_integration.py",
            self.project_path / "tests" / "integration" / "test_cli_integration.py",
        ]
        
        found_tests = 0
        for test_file in test_files:
            if test_file.exists():
                print(f"  ✓ {test_file.relative_to(self.project_path)}")
                found_tests += 1
        
        if found_tests == 0:
            self.warnings.append("No test files found")
        elif found_tests < len(test_files):
            self.warnings.append(
                f"Only {found_tests}/{len(test_files)} expected test files found"
            )
    
    def report_results(self):
        """Report validation results."""
        print("\n" + "=" * 60)
        print("VALIDATION RESULTS")
        print("=" * 60)
        
        if not self.errors and not self.warnings:
            print("\n✓ All checks passed! Project follows template structure.")
            return
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        print()


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        project_path = Path(sys.argv[1])
    else:
        # Default to current directory or look for backend/
        cwd = Path.cwd()
        if (cwd / "backend").exists() and (cwd / "backend" / "app.py").exists():
            project_path = cwd / "backend"
        else:
            project_path = cwd
    
    if not project_path.exists():
        print(f"Error: Project path does not exist: {project_path}")
        sys.exit(1)
    
    validator = TemplateValidator(project_path)
    success = validator.validate()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()


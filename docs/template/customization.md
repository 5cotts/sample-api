# Customization Guide

## Overview

This guide explains how to adapt the template for different domains while maintaining the infrastructure and patterns.

## Step-by-Step Customization

### 1. Replace Placeholders

- `{project-name}` → actual project name
- `{Domain}` → domain name (capitalized)
- `{domain}` → domain name (lowercase)

### 2. Update Business Logic

- Replace the logic inside each function in `src/math_operations.py` (or rename to `business_logic.py`)
- Keep the same function names and signatures initially
- Maintain proper error handling patterns and input validation
- Update docstrings to describe your domain-specific functionality
- Remove TODO markers after implementing domain logic

### 3. Update API Endpoints

- Modify endpoint paths to match domain terminology (e.g., `/square/` → `/validate/`, `/power/` → `/transform/`)
- Update Pydantic model names and field descriptions for domain-specific data
- Keep the same response structure patterns
- Update API documentation strings

### 4. Update CLI Commands

- Rename CLI commands to match domain functions (e.g., `square` → `validate`, `power` → `transform`)
- Update help text and command descriptions
- Maintain the same argument parsing patterns
- Update the CLI description and examples

### 5. Update Tests

- Replace test assertions with domain-specific expectations
- Keep the same test structure and patterns
- Maintain comprehensive coverage
- Update test descriptions to match domain terminology

## Example Domain Adaptations

### Data Processing API
- `square()` → `normalize_value()` - normalize a single data point
- `power()` → `transform_data()` - apply transformation with parameters
- `factorial()` → `calculate_permissions()` - calculate access levels
- `fibonacci()` → `generate_sequence()` - create data sequences
- `is_prime()` → `is_valid()` - validate data integrity
- `calculate_stats()` → `analyze_dataset()` - comprehensive data analysis

### String Processing API
- `square()` → `duplicate_string()` - duplicate text content
- `power()` → `repeat_pattern()` - repeat pattern N times
- `factorial()` → `generate_combinations()` - create text combinations
- `fibonacci()` → `build_sequence()` - create progressive text patterns
- `is_prime()` → `is_palindrome()` - check text properties
- `calculate_stats()` → `analyze_text()` - text analysis metrics

### File Processing API
- `square()` → `compress_file()` - single file compression
- `power()` → `encrypt_data()` - encryption with key strength
- `factorial()` → `calculate_hash()` - generate file hash
- `fibonacci()` → `create_backups()` - incremental backup sequence
- `is_prime()` → `is_corrupted()` - file integrity check
- `calculate_stats()` → `analyze_directory()` - directory statistics

### Validation Service API
- `square()` → `validate_format()` - format validation
- `power()` → `check_strength()` - password/security strength
- `factorial()` → `calculate_score()` - validation scoring
- `fibonacci()` → `generate_rules()` - progressive validation rules
- `is_prime()` → `meets_criteria()` - criteria checking
- `calculate_stats()` → `validation_report()` - comprehensive validation results

## Key Reminders

The key is to maintain the infrastructure and patterns while replacing the mathematical logic with domain-appropriate operations. Always:

1. Keep business logic in `src/`
2. Keep API thin (calls business logic)
3. Keep CLI calling business logic
4. Maintain test patterns
5. Update documentation


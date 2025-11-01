"""
Data Parsing Utilities

This module provides utility functions for parsing and processing common data formats.
These functions demonstrate common data processing patterns that may be useful in
coding interviews and data analysis tasks.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Union

import pandas as pd


def load_csv(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path: Path to the CSV file

    Returns:
        pandas DataFrame containing the CSV data

    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file cannot be parsed as CSV
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        return pd.read_csv(path)
    except Exception as e:
        raise ValueError(f"Failed to parse CSV file {file_path}: {str(e)}") from e


def load_json(file_path: Union[str, Path]) -> Union[Dict, List]:
    """
    Load a JSON file and return its contents.

    Args:
        file_path: Path to the JSON file

    Returns:
        Parsed JSON data (dict or list)

    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file cannot be parsed as JSON
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file {file_path}: {str(e)}") from e
    except Exception as e:
        raise ValueError(f"Error reading file {file_path}: {str(e)}") from e


def json_to_dataframe(data: Union[Dict, List]) -> pd.DataFrame:
    """
    Convert JSON data (dict or list of dicts) to a pandas DataFrame.

    Args:
        data: JSON data to convert (dict or list of dicts)

    Returns:
        pandas DataFrame

    Raises:
        ValueError: If data format is not supported
    """
    if isinstance(data, list):
        if len(data) == 0:
            return pd.DataFrame()
        if isinstance(data[0], dict):
            return pd.DataFrame(data)
        raise ValueError("List must contain dictionaries")
    elif isinstance(data, dict):
        # Try to normalize nested structure
        return pd.json_normalize(data)
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")


def dataframe_summary(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate a summary of a DataFrame including statistics.

    Args:
        df: pandas DataFrame to summarize

    Returns:
        Dictionary containing summary statistics
    """
    if df.empty:
        return {
            "row_count": 0,
            "column_count": 0,
            "columns": [],
            "dtypes": {},
        }

    summary = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }

    # Add statistics for numeric columns
    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        summary["numeric_stats"] = df[numeric_cols].describe().to_dict()

    # Add null counts
    null_counts = df.isnull().sum()
    summary["null_counts"] = null_counts[null_counts > 0].to_dict()

    return summary


def filter_dataframe(
    df: pd.DataFrame, column: str, condition: str, value: Any
) -> pd.DataFrame:
    """
    Filter a DataFrame based on a simple condition.

    Args:
        df: pandas DataFrame to filter
        column: Column name to filter on
        condition: Condition operator ('>', '<', '==', '!=', '>=', '<=', 'in', 'contains')
        value: Value to compare against

    Returns:
        Filtered pandas DataFrame

    Raises:
        ValueError: If column doesn't exist or condition is invalid
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")

    if condition == "==":
        return df[df[column] == value]
    elif condition == "!=":
        return df[df[column] != value]
    elif condition == ">":
        return df[df[column] > value]
    elif condition == "<":
        return df[df[column] < value]
    elif condition == ">=":
        return df[df[column] >= value]
    elif condition == "<=":
        return df[df[column] <= value]
    elif condition == "in":
        return df[df[column].isin(value)]
    elif condition == "contains":
        if df[column].dtype == "object":
            return df[df[column].str.contains(str(value), na=False)]
        else:
            raise ValueError(f"Cannot use 'contains' on non-string column '{column}'")
    else:
        raise ValueError(f"Unsupported condition: {condition}")


def save_dataframe(df: pd.DataFrame, file_path: Union[str, Path], format: str = "csv") -> None:
    """
    Save a DataFrame to a file.

    Args:
        df: pandas DataFrame to save
        file_path: Path where to save the file
        format: File format ('csv' or 'json')

    Raises:
        ValueError: If format is not supported
    """
    path = Path(file_path)
    format_lower = format.lower()

    if format_lower == "csv":
        df.to_csv(path, index=False)
    elif format_lower == "json":
        df.to_json(path, orient="records", indent=2)
    else:
        raise ValueError(f"Unsupported format: {format}. Use 'csv' or 'json'")


def merge_dataframes(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    on: Union[str, List[str]],
    how: str = "inner",
) -> pd.DataFrame:
    """
    Merge two DataFrames on common columns.

    Args:
        df1: First DataFrame
        df2: Second DataFrame
        on: Column name(s) to merge on
        how: Type of merge ('inner', 'outer', 'left', 'right')

    Returns:
        Merged pandas DataFrame

    Raises:
        ValueError: If merge columns don't exist or how is invalid
    """
    if isinstance(on, str):
        on = [on]

    for col in on:
        if col not in df1.columns:
            raise ValueError(f"Column '{col}' not found in first DataFrame")
        if col not in df2.columns:
            raise ValueError(f"Column '{col}' not found in second DataFrame")

    valid_how = ["inner", "outer", "left", "right"]
    if how not in valid_how:
        raise ValueError(f"Invalid 'how' parameter: {how}. Must be one of {valid_how}")

    return pd.merge(df1, df2, on=on, how=how)


def aggregate_dataframe(
    df: pd.DataFrame, group_by: Union[str, List[str]], aggregations: Dict[str, List[str]]
) -> pd.DataFrame:
    """
    Aggregate DataFrame by grouping and applying functions.

    Args:
        df: pandas DataFrame to aggregate
        group_by: Column name(s) to group by
        aggregations: Dictionary mapping column names to list of aggregation functions
                     e.g., {'column': ['mean', 'sum', 'count']}

    Returns:
        Aggregated pandas DataFrame

    Raises:
        ValueError: If columns don't exist
    """
    if isinstance(group_by, str):
        group_by = [group_by]

    for col in group_by:
        if col not in df.columns:
            raise ValueError(f"Group column '{col}' not found in DataFrame")

    for col, funcs in aggregations.items():
        if col not in df.columns:
            raise ValueError(f"Aggregation column '{col}' not found in DataFrame")

    return df.groupby(group_by).agg(aggregations).reset_index()


"""
Unit Tests for Data Parsing Utilities

These tests demonstrate how to test data parsing functions independently
of any API or interface implementation. Tests cover CSV/JSON loading,
data filtering, aggregation, merging, and summary generation.

Tests cover:
- Happy path scenarios for CSV and JSON loading
- DataFrame operations (filtering, aggregation, merging)
- Edge cases and error conditions
- Input validation
"""

import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from src.data_parsing import (
    aggregate_dataframe,
    dataframe_summary,
    filter_dataframe,
    json_to_dataframe,
    load_csv,
    load_json,
    merge_dataframes,
    save_dataframe,
)

# Calculate path to backend/data directory
# Test file location: backend/tests/unit/test_data_parsing.py
# Going up: unit -> tests -> backend, then into data/
TEST_DIR = Path(__file__).parent  # backend/tests/unit/
TESTS_DIR = TEST_DIR.parent  # backend/tests/
BACKEND_DIR = TESTS_DIR.parent  # backend/
DATA_DIR = BACKEND_DIR / "data"  # backend/data/


class TestLoadCSV(unittest.TestCase):
    """Tests for the load_csv function."""

    def test_load_csv_from_data_directory(self):
        """Test loading CSV from data directory."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn("name", df.columns)
        self.assertIn("age", df.columns)
        self.assertIn("salary", df.columns)
        self.assertIn("department", df.columns)

    def test_load_csv_file_not_found(self):
        """Test loading non-existent CSV file."""
        csv_path = DATA_DIR / "nonexistent.csv"
        with self.assertRaises(FileNotFoundError):
            load_csv(csv_path)

    def test_load_csv_invalid_file(self):
        """Test loading invalid CSV file that causes pandas error."""
        # Create a directory path instead of a file - this will cause pandas to fail
        # pandas will raise an error when trying to read a directory
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = Path(temp_dir)
            # Try to load a directory as if it were a CSV file
            # This will cause pandas to raise an exception
            with self.assertRaises(ValueError):
                load_csv(dir_path)


class TestLoadJSON(unittest.TestCase):
    """Tests for the load_json function."""

    def test_load_json_from_data_directory(self):
        """Test loading JSON from data directory."""
        json_path = DATA_DIR / "sample_data.json"
        data = load_json(json_path)

        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)
        self.assertIn("id", data[0])
        self.assertIn("name", data[0])

    def test_load_json_file_not_found(self):
        """Test loading non-existent JSON file."""
        json_path = DATA_DIR / "nonexistent.json"
        with self.assertRaises(FileNotFoundError):
            load_json(json_path)

    def test_load_json_invalid_file(self):
        """Test loading invalid JSON file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{ invalid json }")
            temp_path = Path(f.name)

        try:
            with self.assertRaises(ValueError):
                load_json(temp_path)
        finally:
            temp_path.unlink()


class TestJSONToDataFrame(unittest.TestCase):
    """Tests for the json_to_dataframe function."""

    def test_json_to_dataframe_from_list(self):
        """Test converting JSON list to DataFrame."""
        json_path = DATA_DIR / "sample_data.json"
        json_data = load_json(json_path)
        df = json_to_dataframe(json_data)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn("id", df.columns)
        self.assertIn("name", df.columns)
        self.assertIn("price", df.columns)
        self.assertIn("category", df.columns)

    def test_json_to_dataframe_empty_list(self):
        """Test converting empty JSON list to DataFrame."""
        df = json_to_dataframe([])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 0)

    def test_json_to_dataframe_invalid_data(self):
        """Test converting invalid JSON structure."""
        with self.assertRaises(ValueError):
            json_to_dataframe([1, 2, 3])  # List of non-dicts

        with self.assertRaises(ValueError):
            json_to_dataframe("not a dict or list")


class TestDataFrameSummary(unittest.TestCase):
    """Tests for the dataframe_summary function."""

    def test_dataframe_summary_basic(self):
        """Test generating summary for sample data."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)
        summary = dataframe_summary(df)

        self.assertIn("row_count", summary)
        self.assertIn("column_count", summary)
        self.assertIn("columns", summary)
        self.assertIn("dtypes", summary)
        self.assertGreater(summary["row_count"], 0)
        self.assertGreater(summary["column_count"], 0)

    def test_dataframe_summary_numeric_stats(self):
        """Test summary includes numeric statistics."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)
        summary = dataframe_summary(df)

        # Should have numeric_stats since we have numeric columns
        self.assertIn("numeric_stats", summary)
        self.assertIn("salary", summary["numeric_stats"])
        self.assertIn("age", summary["numeric_stats"])

    def test_dataframe_summary_empty(self):
        """Test summary for empty DataFrame."""
        df = pd.DataFrame()
        summary = dataframe_summary(df)

        self.assertEqual(summary["row_count"], 0)
        self.assertEqual(summary["column_count"], 0)
        self.assertEqual(summary["columns"], [])


class TestFilterDataFrame(unittest.TestCase):
    """Tests for the filter_dataframe function."""

    def test_filter_equals(self):
        """Test filtering with equals condition."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        filtered = filter_dataframe(df, "department", "==", "Engineering")

        self.assertIsInstance(filtered, pd.DataFrame)
        self.assertGreater(len(filtered), 0)
        self.assertTrue(all(filtered["department"] == "Engineering"))

    def test_filter_greater_than(self):
        """Test filtering with greater than condition."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        filtered = filter_dataframe(df, "age", ">", 30)

        self.assertIsInstance(filtered, pd.DataFrame)
        self.assertTrue(all(filtered["age"] > 30))

    def test_filter_less_than(self):
        """Test filtering with less than condition."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        filtered = filter_dataframe(df, "salary", "<", 70000)

        self.assertIsInstance(filtered, pd.DataFrame)
        self.assertTrue(all(filtered["salary"] < 70000))

    def test_filter_invalid_column(self):
        """Test filtering with non-existent column."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        with self.assertRaises(ValueError):
            filter_dataframe(df, "nonexistent_column", "==", "value")

    def test_filter_invalid_condition(self):
        """Test filtering with invalid condition."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        with self.assertRaises(ValueError):
            filter_dataframe(df, "department", "invalid", "Engineering")


class TestMergeDataFrames(unittest.TestCase):
    """Tests for the merge_dataframes function."""

    def test_merge_dataframes_left_join(self):
        """Test merging DataFrames with left join."""
        employees_path = DATA_DIR / "employees.csv"
        departments_path = DATA_DIR / "departments.csv"
        employees_df = load_csv(employees_path)
        departments_df = load_csv(departments_path)

        merged = merge_dataframes(
            employees_df, departments_df, on="department_id", how="left"
        )

        self.assertIsInstance(merged, pd.DataFrame)
        self.assertGreater(len(merged), 0)
        self.assertIn("employee_id", merged.columns)
        self.assertIn("name", merged.columns)
        self.assertIn("department_name", merged.columns)

    def test_merge_dataframes_inner_join(self):
        """Test merging DataFrames with inner join."""
        employees_path = DATA_DIR / "employees.csv"
        departments_path = DATA_DIR / "departments.csv"
        employees_df = load_csv(employees_path)
        departments_df = load_csv(departments_path)

        merged = merge_dataframes(
            employees_df, departments_df, on="department_id", how="inner"
        )

        self.assertIsInstance(merged, pd.DataFrame)
        self.assertGreater(len(merged), 0)

    def test_merge_dataframes_invalid_column(self):
        """Test merging with non-existent column."""
        employees_path = DATA_DIR / "employees.csv"
        departments_path = DATA_DIR / "departments.csv"
        employees_df = load_csv(employees_path)
        departments_df = load_csv(departments_path)

        with self.assertRaises(ValueError):
            merge_dataframes(employees_df, departments_df, on="nonexistent", how="left")

    def test_merge_dataframes_invalid_how(self):
        """Test merging with invalid join type."""
        employees_path = DATA_DIR / "employees.csv"
        departments_path = DATA_DIR / "departments.csv"
        employees_df = load_csv(employees_path)
        departments_df = load_csv(departments_path)

        with self.assertRaises(ValueError):
            merge_dataframes(
                employees_df, departments_df, on="department_id", how="invalid"
            )


class TestAggregateDataFrame(unittest.TestCase):
    """Tests for the aggregate_dataframe function."""

    def test_aggregate_dataframe_by_department(self):
        """Test aggregating data by department."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        stats = aggregate_dataframe(
            df,
            group_by="department",
            aggregations={"salary": ["mean", "min", "max"], "age": ["mean"]},
        )

        self.assertIsInstance(stats, pd.DataFrame)
        self.assertGreater(len(stats), 0)
        self.assertIn("department", stats.columns)

    def test_aggregate_dataframe_invalid_group_column(self):
        """Test aggregating with non-existent group column."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        with self.assertRaises(ValueError):
            aggregate_dataframe(
                df, group_by="nonexistent", aggregations={"salary": ["mean"]}
            )

    def test_aggregate_dataframe_invalid_agg_column(self):
        """Test aggregating with non-existent aggregation column."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        with self.assertRaises(ValueError):
            aggregate_dataframe(
                df, group_by="department", aggregations={"nonexistent": ["mean"]}
            )


class TestSaveDataFrame(unittest.TestCase):
    """Tests for the save_dataframe function."""

    def test_save_dataframe_to_csv(self):
        """Test saving DataFrame to CSV."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            temp_path = Path(f.name)

        try:
            save_dataframe(df, temp_path, format="csv")
            self.assertTrue(temp_path.exists())

            # Verify we can load it back
            loaded_df = load_csv(temp_path)
            self.assertEqual(len(df), len(loaded_df))
        finally:
            if temp_path.exists():
                temp_path.unlink()

    def test_save_dataframe_to_json(self):
        """Test saving DataFrame to JSON."""
        json_path = DATA_DIR / "sample_data.json"
        json_data = load_json(json_path)
        df = json_to_dataframe(json_data)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_path = Path(f.name)

        try:
            save_dataframe(df, temp_path, format="json")
            self.assertTrue(temp_path.exists())

            # Verify it's valid JSON
            with open(temp_path, "r") as f:
                loaded_data = json.load(f)
            self.assertIsInstance(loaded_data, list)
        finally:
            if temp_path.exists():
                temp_path.unlink()

    def test_save_dataframe_invalid_format(self):
        """Test saving with invalid format."""
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            temp_path = Path(f.name)

        try:
            with self.assertRaises(ValueError):
                save_dataframe(df, temp_path, format="invalid")
        finally:
            if temp_path.exists():
                temp_path.unlink()


class TestDataParsingIntegration(unittest.TestCase):
    """Integration tests combining multiple data parsing functions."""

    def test_full_workflow_csv_analysis(self):
        """Test complete workflow: load, filter, aggregate, save."""
        # Load CSV
        csv_path = DATA_DIR / "sample_data.csv"
        df = load_csv(csv_path)
        self.assertGreater(len(df), 0)

        # Get summary
        summary = dataframe_summary(df)
        self.assertIn("row_count", summary)

        # Filter
        filtered = filter_dataframe(df, "department", "==", "Engineering")
        self.assertGreater(len(filtered), 0)

        # Aggregate
        stats = aggregate_dataframe(
            filtered,
            group_by="department",
            aggregations={"salary": ["mean", "count"], "age": ["mean"]},
        )
        self.assertGreater(len(stats), 0)

    def test_full_workflow_json_analysis(self):
        """Test complete workflow: load JSON, convert, filter."""
        # Load JSON
        json_path = DATA_DIR / "sample_data.json"
        json_data = load_json(json_path)
        self.assertIsInstance(json_data, list)

        # Convert to DataFrame
        df = json_to_dataframe(json_data)
        self.assertGreater(len(df), 0)

        # Filter
        filtered = filter_dataframe(df, "category", "==", "Electronics")
        self.assertGreater(len(filtered), 0)

    def test_full_workflow_merge_and_aggregate(self):
        """Test complete workflow: merge DataFrames and aggregate."""
        # Load both DataFrames
        employees_path = DATA_DIR / "employees.csv"
        departments_path = DATA_DIR / "departments.csv"
        employees_df = load_csv(employees_path)
        departments_df = load_csv(departments_path)

        # Merge
        merged = merge_dataframes(
            employees_df, departments_df, on="department_id", how="left"
        )
        self.assertGreater(len(merged), 0)

        # Get summary
        summary = dataframe_summary(merged)
        self.assertIn("row_count", summary)


# unittest configuration
if __name__ == "__main__":
    # Run tests if this file is executed directly
    unittest.main()

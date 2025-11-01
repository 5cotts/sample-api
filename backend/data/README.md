# Data Directory

This directory contains example data files and scripts demonstrating data parsing and analysis patterns.

## Data Files

The following sample data files are included:

- **`sample_data.csv`** - Employee data with names, ages, salaries, and departments
- **`sample_data.json`** - Product catalog with IDs, names, prices, and categories
- **`employees.csv`** - Employee IDs and department relationships
- **`departments.csv`** - Department IDs and names for merging examples

## Quick Start

After installing dependencies, run the unit tests:

```bash
cd backend
uv sync
uv run python -m unittest tests.unit.test_data_parsing -v
```

## Available Utilities

The `src/data_parsing.py` module provides:

- **`load_csv()`** - Load CSV files into pandas DataFrames
- **`load_json()`** - Load JSON files
- **`json_to_dataframe()`** - Convert JSON to pandas DataFrame
- **`dataframe_summary()`** - Generate summary statistics
- **`filter_dataframe()`** - Filter DataFrames with various conditions
- **`save_dataframe()`** - Save DataFrames to CSV or JSON
- **`merge_dataframes()`** - Join multiple DataFrames
- **`aggregate_dataframe()`** - Group and aggregate data

## Example Patterns

### Load and Analyze CSV

```python
from pathlib import Path
from src.data_parsing import load_csv, dataframe_summary

# Load from the data directory
data_dir = Path("backend/data")
df = load_csv(data_dir / "sample_data.csv")
summary = dataframe_summary(df)
print(summary)
```

### Filter Data

```python
from src.data_parsing import load_csv, filter_dataframe

df = load_csv("data/sample_data.csv")
filtered = filter_dataframe(df, "department", "==", "Engineering")
```

### Merge Data Sources

```python
from pathlib import Path
from src.data_parsing import load_csv, merge_dataframes

data_dir = Path("backend/data")
df1 = load_csv(data_dir / "employees.csv")
df2 = load_csv(data_dir / "departments.csv")
merged = merge_dataframes(df1, df2, on="department_id", how="left")
```

### Aggregate Data

```python
from src.data_parsing import load_csv, aggregate_dataframe

df = load_csv("data/sample_data.csv")
stats = aggregate_dataframe(
    df,
    group_by="department",
    aggregations={"salary": ["mean", "min", "max"]}
)
```

## Testing

Unit tests for all data parsing utilities are available in `tests/unit/test_data_parsing.py`. 
The tests demonstrate usage patterns and can serve as examples:

```bash
# Run all data parsing tests
uv run python -m unittest tests.unit.test_data_parsing -v

# Run all unit tests
uv run python -m unittest discover -s tests/unit -p "test_*.py" -v
```

## Interview Tips

When working with datasets in interviews:

1. **Start by exploring**: Use `dataframe_summary()` to understand the data structure
2. **Load efficiently**: Use `load_csv()` or `load_json()` based on your data format
3. **Filter early**: Reduce data size before heavy processing
4. **Merge carefully**: Understand join types (inner, outer, left, right)
5. **Aggregate meaningfully**: Group data to find patterns and insights

## Common File Formats

The utilities support:
- **CSV** files (`.csv`)
- **JSON** files (`.json`) - both single objects and arrays of objects

For other formats (Excel, Parquet, etc.), you can extend the utilities or use pandas directly.


"""CSV analysis utilities.

This module provides functions to extract structural information and
descriptive statistics from CSV data stored in pandas DataFrames.
"""

import pandas as pd


def analyze_csv(data: pd.DataFrame) -> dict:
    """
    Generate descriptive statistics for a CSV DataFrame.

    The analysis includes the number of rows and columns, column names,
    total number of missing values, and numerical columns.
    Descriptive statistics are calculated for numerical columns when
    available.

    Args:
        data: The DataFrame to analyze.

    Returns:
     A dictionary containing the following information:
            - row_count: Number of rows.
            - column_count: Number of columns.
            - columns: List of column names.
            - missing_values: Total number of missing values.
            - numeric_columns: List of numerical column names.
            - statistics: Descriptive statistics for numerical columns,
              or an empty dictionary if no numerical columns are present.
    """
    numeric_data = data.select_dtypes(include="number")

    analysis = {
        "row_count": len(data),
        "column_count": len(data.columns),
        "columns": list(data.columns),
        "missing_values": int(data.isnull().sum().sum()),
        "numeric_columns": list(numeric_data.columns),
    }

    if not numeric_data.empty:
        analysis["statistics"] = numeric_data.describe().round(2).to_dict()
    else:
        analysis["statistics"] = {}

    return analysis

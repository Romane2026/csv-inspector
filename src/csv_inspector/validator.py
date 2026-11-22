"""CSV validation utilities.

This module provides functions to validate CSV data and detect common
structural issues, such as missing column names, duplicate columns,
and missing values.
"""

import pandas as pd


def validate_csv(data: pd.DataFrame) -> list[str]:
    """
    Validate a CSV DataFrame and return a list of detected problems.

    The validation checks that the DataFrame contains columns and data,
    that column names are not empty or duplicated, and that no missing
    values are present.

    Args:
        data: The DataFrame to validate.

    Returns:
        A list of validation error messages.
        An empty list is returned if no problems are detected.
    """

    errors = []

    if len(data.columns) == 0:
        errors.append("The CSV file contains no columns.")
        return errors

    if data.empty:
        errors.append("The CSV file contains no data.")
        return errors

    # Check for missing column names
    if any(str(column).strip() == "" for column in data.columns):
        errors.append("The CSV file contains empty column names.")

    # Check for duplicate column names
    if data.columns.duplicated().any():
        errors.append("The CSV file contains duplicate column names.")

    # Check for missing values
    missing_values = data.isnull().sum()

    for column, count in missing_values.items():
        if count > 0:
            errors.append(f"Column '{column}' contains {count} missing value(s).")

    return errors

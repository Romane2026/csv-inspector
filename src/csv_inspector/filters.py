import pandas as pd


def filter_csv(
    data: pd.DataFrame,
    column: str,
    operator: str,
    value: str,
) -> pd.DataFrame:
    """
    Filter a DataFrame using a comparison condition.

    Supported operators: ==, !=, >, <, >=, <=

    Args:
        data: The DataFrame to filter.
        column: The column on which to apply the filter.
        operator: The comparison operator.
        value: The value to compare against.

    Returns:
        A filtered DataFrame.

    Raises:
        ValueError: If the column or operator is invalid.
    """
    if column not in data.columns:
        raise ValueError(f"Column '{column}' does not exist.")

    operators = {
        "==": lambda series, target: series == target,
        "!=": lambda series, target: series != target,
        ">": lambda series, target: series > target,
        "<": lambda series, target: series < target,
        ">=": lambda series, target: series >= target,
        "<=": lambda series, target: series <= target,
    }

    if operator not in operators:
        raise ValueError(f"Unsupported operator: {operator}")

    series = data[column]

    # Convert the comparison value when the column is numeric.
    if pd.api.types.is_numeric_dtype(series):
        try:
            value = float(value)
        except ValueError:
            raise ValueError(
                f"Value '{value}' must be numeric for column '{column}'."
            ) from None

    try:
        return data[operators[operator](series, value)]
    except TypeError:
        raise ValueError(
            f"Cannot apply operator '{operator}' to column '{column}'."
        ) from None

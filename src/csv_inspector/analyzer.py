
import pandas as pd


def analyze_csv(data: pd.DataFrame) -> dict:
    """
    Generate descriptive statistics for a CSV DataFrame.

    Args:
        data: The DataFrame to analyze.

    Returns:
        A dictionary containing the analysis results.
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

from pathlib import Path

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file and return its content as a DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the CSV data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or invalid.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        data = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.") from None
    except pd.errors.ParserError:
        raise ValueError("The CSV file is invalid.") from None

    if data.empty:
        raise ValueError("The CSV file contains no data.")

    return data

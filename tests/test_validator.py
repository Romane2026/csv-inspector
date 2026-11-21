import pandas as pd

from csv_inspector.validator import validate_csv


def test_validate_csv_valid_data():
    data = pd.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "age": [20, 22],
        }
    )

    assert validate_csv(data) == []


def test_validate_csv_empty_dataframe():
    data = pd.DataFrame(columns=["name", "age"])

    result = validate_csv(data)

    assert "The CSV file contains no data." in result


def test_validate_csv_no_columns():
    data = pd.DataFrame(index=[0, 1])

    result = validate_csv(data)

    assert "The CSV file contains no columns." in result


def test_validate_csv_empty_column_names():
    data = pd.DataFrame(
        [["Alice", 20]],
        columns=["name", " "],
    )

    result = validate_csv(data)

    assert "The CSV file contains empty column names." in result


def test_validate_csv_duplicate_column_names():
    data = pd.DataFrame(
        [[20, 21]],
        columns=["age", "age"],
    )

    result = validate_csv(data)

    assert "The CSV file contains duplicate column names." in result


def test_validate_csv_missing_values():
    data = pd.DataFrame(
        {
            "name": ["Alice", None],
            "age": [20, None],
        }
    )

    result = validate_csv(data)

    assert "Column 'name' contains 1 missing value(s)." in result
    assert "Column 'age' contains 1 missing value(s)." in result

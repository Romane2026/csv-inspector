import pandas as pd

from csv_inspector.analyzer import analyze_csv


def test_analyze_csv_basic_information():
    data = pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "age": [18, 20, 22],
            "grade": [12.5, 15.0, 17.5],
        }
    )

    result = analyze_csv(data)

    assert result["row_count"] == 3
    assert result["column_count"] == 3
    assert result["columns"] == ["name", "age", "grade"]
    assert result["missing_values"] == 0
    assert result["numeric_columns"] == ["age", "grade"]


def test_analyze_csv_statistics():
    data = pd.DataFrame({"age": [18, 20, 22]})

    result = analyze_csv(data)

    statistics = result["statistics"]["age"]

    assert statistics["count"] == 3.0
    assert statistics["mean"] == 20.0
    assert statistics["min"] == 18.0
    assert statistics["max"] == 22.0


def test_analyze_csv_missing_values():
    data = pd.DataFrame(
        {
            "name": ["Alice", "Bob", None],
            "age": [18, None, 22],
        }
    )

    result = analyze_csv(data)

    assert result["missing_values"] == 2


def test_analyze_csv_no_numeric_columns():
    data = pd.DataFrame(
        {
            "name": ["Alice", "Bob"],
            "city": ["Paris", "Lyon"],
        }
    )

    result = analyze_csv(data)

    assert result["numeric_columns"] == []
    assert result["statistics"] == {}

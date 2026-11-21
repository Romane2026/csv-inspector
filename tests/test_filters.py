import pandas as pd
import pytest

from csv_inspector.filters import filter_csv


@pytest.mark.parametrize(
    ("operator", "value", "expected_ages"),
    [
        ("==", "20", [20]),
        ("!=", "20", [18, 22]),
        (">", "20", [22]),
        ("<", "20", [18]),
        (">=", "20", [20, 22]),
        ("<=", "20", [18, 20]),
    ],
)
def test_filter_csv_numeric_operators(operator, value, expected_ages):
    data = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [18, 20, 22]})

    result = filter_csv(data, "age", operator, value)

    assert result["age"].tolist() == expected_ages


def test_filter_csv_column_not_found():
    data = pd.DataFrame({"age": [18, 20, 22]})

    with pytest.raises(ValueError, match="does not exist"):
        filter_csv(data, "height", ">", "18")


def test_filter_csv_unsupported_operator():
    data = pd.DataFrame({"age": [18, 20, 22]})

    with pytest.raises(ValueError, match="Unsupported operator"):
        filter_csv(data, "age", "=", "20")


def test_filter_csv_non_numeric_value():
    data = pd.DataFrame({"age": [18, 20, 22]})

    with pytest.raises(ValueError, match="must be numeric"):
        filter_csv(data, "age", ">", "abc")


def test_filter_csv_incompatible_types():
    data = pd.DataFrame({"value": ["Alice", 10, "Charlie"]})

    with pytest.raises(ValueError, match="Cannot apply operator"):
        filter_csv(data, "value", ">", "Bob")

import pandas as pd
import pytest

from csv_inspector.loader import load_csv


def test_load_csv_success(tmp_path):
    csv_file = tmp_path / "students.csv"
    csv_file.write_text("name,age\nAlice,20\nBob,22\n", encoding="utf-8")

    result = load_csv(str(csv_file))

    expected = pd.DataFrame({"name": ["Alice", "Bob"], "age": [20, 22]})

    pd.testing.assert_frame_equal(result, expected)


def test_load_csv_file_not_found(tmp_path):
    csv_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="File not found"):
        load_csv(str(csv_file))


def test_load_csv_empty_file(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="The CSV file is empty"):
        load_csv(str(csv_file))


def test_load_csv_no_data(tmp_path):
    csv_file = tmp_path / "no_data.csv"
    csv_file.write_text("name,age\n", encoding="utf-8")

    with pytest.raises(ValueError, match="The CSV file contains no data"):
        load_csv(str(csv_file))

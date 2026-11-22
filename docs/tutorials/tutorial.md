# CSV Inspector Tutorial

This tutorial explains how to install and use CSV Inspector to inspect, validate, and analyze CSV files from the command line.

## 1. Prerequisites

Before starting, make sure you have installed:

- Python 3.10 or newer
- Poetry

## 2. Install the project

Clone the repository:

```bash
git clone https://github.com/Romane2026/csv-inspector.git
cd csv-inspector
```

Install the project and its dependencies:

```bash
poetry install
```

## 3. Prepare your CSV file

CSV Inspector works with CSV files. For example, a file named `data/students.csv` could contain:

```csv
name,age,grade
Alice,20,15.5
Bob,21,12
Charlie,19,17
David,22,9.5
```

Make sure your CSV file exists and contains valid data.

## 4. Analyze a CSV file

Run CSV Inspector with the path to your file:

```bash
poetry run csv-inspector data/students.csv
```

The tool displays a report containing:

- The number of rows and columns
- The column names
- The number of missing values
- The numerical columns
- Descriptive statistics for numerical columns, such as mean, standard deviation, minimum and maximum values

The results are displayed as readable tables in the terminal.

## 5. Filter rows

You can filter rows using the `--filter` option, followed by a column name, an operator, and a value.

For example, to display students whose grade is greater than 12:

```bash
poetry run csv-inspector data/students.csv --filter grade ">" 12
```

Supported comparison operators are:

- `==` : equal to
- `!=` : not equal to
- `>` : greater than
- `<` : less than
- `>=` : greater than or equal to
- `<=` : less than or equal to

Another example, to select students aged 20 or older:

```bash
poetry run csv-inspector data/students.csv --filter age ">=" 20
```

## 6. Change the logging level

You can change the amount of logging information displayed using the `--log-level` option.

For example:

```bash
poetry run csv-inspector data/students.csv --log-level DEBUG
```

Available logging levels are:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

## 7. Development commands

If you want to contribute to or modify the project, you can run the tests:

```bash
poetry run pytest
```

Check code quality and formatting with Ruff:

```bash
poetry run ruff check .
poetry run ruff format --check .
```

Install the Git hooks to automatically run code quality checks before each commit:

```bash
poetry run pre-commit install
```

You can also run the pre-commit hooks manually:

```bash
poetry run pre-commit run --all-files
```

## 8. Troubleshooting

If the file does not exist, CSV Inspector reports an error.

If the CSV file is empty, malformed, or contains invalid data, the tool may report an error or validation warnings.

Make sure that:

- The file path is correct.
- The CSV file uses a valid format.
- The file contains data.
- The column name used for filtering exists.
- The filter operator is supported.

## Conclusion

CSV Inspector provides a simple way to inspect, validate, filter, and analyze CSV files directly from the command line.

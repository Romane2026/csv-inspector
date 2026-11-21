# CSV Inspector

## Description

CSV Inspector is a command-line tool developed in Python for inspecting, validating, and analyzing CSV files.

Key features include:
- Reading CSV files
- Displaying the number of rows and columns
- Detecting missing values
- Identifying numerical columns and calculating descriptive statistics
- Filtering rows based on a column, an operator, and a value
- Displaying results as readable tables in the terminal.

## Installation

Clone the repository:

```bash
git clone https://github.com/Romane2026/csv-inspector.git
cd csv-inspector
```

Install the project and its dependencies using Poetry:

```bash
poetry install
```

## Usage

Analyze a CSV file:

```bash
poetry run csv-inspector data/students.csv
```

Filter rows using a condition:

```bash
poetry run csv-inspector data/students.csv --filter grade ">" 12
```

Supported comparison operators are `==`, `!=`, `>`, `<`, `>=`, and `<=`.

To change the logging level:

```bash
poetry run csv-inspector data/students.csv --log-level DEBUG
```

Available logging levels are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

## Development

Install the project and its dependencies:

```bash
poetry install
```

### Pre-commit hooks

Install the Git hooks to automatically run code quality checks before each commit:

```bash
poetry run pre-commit install
```

To manually run all hooks on every tracked file:

```bash
poetry run pre-commit run --all-files
```

### Tests

Run the unit tests:

```bash
poetry run pytest
```

### Code quality

Check code quality and formatting with Ruff:

```bash
poetry run ruff check .
poetry run ruff format --check .
```

### Build

Build the project distributions:

```bash
poetry build
```

## Technologies

- Python 3.10+
- Poetry
- Pandas
- Rich
- pytest
- Ruff

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
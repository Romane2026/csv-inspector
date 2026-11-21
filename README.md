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

## Technologies Used

- Python 3.10+: Programming language
- Poetry 2.x: Dependency, environment, and project management
- Pandas: Reading and analyzing CSV data
- Rich: Formatted terminal output.

## Installation

Clone the repository:

git clone https://github.com/Romane2026/csv-inspector.git
cd csv-inspector


Install dependencies and the project:

poetry install

The 'poetry.lock' file ensures that the resolved versions of dependencies are used.

## Static Code Analysis

The project uses Ruff for static code analysis and code formatting.

### Installation

Ruff is included as a development dependency. Install the project dependencies using:

```bash
poetry install
```

### Run the analysis

To check the source code for errors and code quality issues:

```bash
poetry run ruff check .
```

To check whether the code follows Ruff's formatting rules:

```bash
poetry run ruff format --check .
```

To automatically fix supported linting issues:

```bash
poetry run ruff check --fix .
```

To automatically format the source code:

```bash
poetry run ruff format .
```

The Ruff configuration is defined in `pyproject.toml`.

## Pre-commit Hooks

The project uses pre-commit hooks to automatically run Ruff checks before each Git commit. This helps maintain code quality and consistent formatting.

### How to set it up

1. Install the project dependencies:

```bash
poetry install
```

2. Install the pre-commit Git hooks:

```bash
poetry run pre-commit install
```

### How to use it

Hooks run automatically before each commit. If a check fails, the commit is blocked until the issues are fixed.

To manually run all hooks on every tracked file:

```bash
poetry run pre-commit run --all-files
```

The hooks include:

- **Ruff lint:** checks for code quality issues.
- **Ruff format:** checks code formatting.


## Usage

Analyze a CSV file:

poetry run csv-inspector data/students.csv


Filter rows based on a condition:

poetry run csv-inspector data/students.csv --filter grade ">" 12

Available operators are '==', '!=', '>', '<', '>=', and '<='.


## Logging

The application uses Python's standard `logging` module to report information about its execution.

Five logging levels are available:

- **DEBUG**: detailed information about file loading, CSV dimensions, filtering and analysis.
- **INFO**: confirmation of successful operations.
- **WARNING**: non-blocking issues, such as missing values or empty filtering results.
- **ERROR**: errors that prevent an operation from completing, such as invalid input files or filters.
- **CRITICAL**: unexpected fatal errors.

### Usage

The default logging level is `INFO`.

To change the logging level, use the `--log-level` option:

```bash
poetry run csv-inspector data/students.csv --log-level DEBUG
```

Available levels are `DEBUG`, `INFO`, `WARNING`, `ERROR` and `CRITICAL`.

For example, to display only errors:

```bash
poetry run csv-inspector data/students.csv --log-level ERROR
```


## Building and Packaging

The project uses Poetry and its 'poetry-core' backend.

To build the distributions:

poetry build

This command generates two files in the 'dist/' directory:

- A '.whl' file (Wheel distribution).
- A '.tar.gz' file (source distribution).

As this project is an interpreted Python application, it does not require native compilation into machine code. The build process described here involves preparing and packaging the project for distribution.

## Versioning

The project version is defined in 'pyproject.toml' under the 'version' field.

Current version: 0.1.0.

Dependency versions are declared in 'pyproject.toml', and their resolved versions are recorded in 'poetry.lock'.

## Project Structure

csv-inspector/
├── data/
│   └── students.csv
├── src/
│   └── csv_inspector/
│       ├── __init__.py
│       ├── cli.py
│       ├── loader.py
│       ├── validator.py
│       ├── analyzer.py
│       ├── filters.py
│       └── report.py
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md


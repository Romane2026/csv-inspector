
import argparse
import sys

from csv_inspector.loader import load_csv
from csv_inspector.validator import validate_csv
from csv_inspector.analyzer import analyze_csv
from csv_inspector.filters import filter_csv
from csv_inspector.report import display_report


def main() -> None:
    """Run the CSV Inspector command-line application."""

    parser = argparse.ArgumentParser(
        description="Inspect, validate and analyze CSV files."
    )

    parser.add_argument(
        "file",
        help="Path to the CSV file to inspect."
    )

    parser.add_argument(
        "--filter",
        nargs=3,
        metavar=("COLUMN", "OPERATOR", "VALUE"),
        help="Filter rows, for example: --filter age '>' 25"
    )

    args = parser.parse_args()

    try:
        # Load the CSV file
        data = load_csv(args.file)

        # Validate the CSV data
        errors = validate_csv(data)

        if errors:
            print("\nCSV validation warnings:")
            for error in errors:
                print(f"- {error}")
            print()

        # Apply an optional filter
        if args.filter:
            column, operator, value = args.filter
            data = filter_csv(data, column, operator, value)
            print(f"Filter applied: {column} {operator} {value}")

        if data.empty:
            print("No rows match the selected filter.")
            return

        # Analyze the data
        analysis = analyze_csv(data)

        # Display the report
        display_report(analysis)

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

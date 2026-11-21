import argparse
import logging
import sys

from csv_inspector.analyzer import analyze_csv
from csv_inspector.filters import filter_csv
from csv_inspector.loader import load_csv
from csv_inspector.report import display_report
from csv_inspector.validator import validate_csv

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the CSV Inspector command-line application."""

    parser = argparse.ArgumentParser(
        description="Inspect, validate and analyze CSV files."
    )

    parser.add_argument("file", help="Path to the CSV file to inspect.")

    parser.add_argument(
        "--filter",
        nargs=3,
        metavar=("COLUMN", "OPERATOR", "VALUE"),
        help="Filter rows, for example: --filter age '>' 25",
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level (default: INFO).",
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    try:
        # Load the CSV file
        logger.debug("Loading CSV file: %s", args.file)
        data = load_csv(args.file)
        logger.info("CSV file successfully loaded: %s", args.file)
        logger.debug(
            "CSV dimensions: %d rows and %d columns",
            len(data),
            len(data.columns),
        )

        # Validate the CSV data
        errors = validate_csv(data)

        if errors:
            for error in errors:
                logger.warning("%s", error)

        # Apply an optional filter
        if args.filter:
            column, operator, value = args.filter
            logger.debug(
                "Applying filter: column=%s, operator=%s, value=%s",
                column,
                operator,
                value,
            )
            data = filter_csv(data, column, operator, value)
            logger.info("Filter successfully applied.")
            logger.debug("Number of rows after filtering: %d", len(data))

        if data.empty:
            logger.warning("No rows match the selected filter.")
            return

        # Analyze the data
        logger.debug("Starting CSV analysis.")
        analysis = analyze_csv(data)
        logger.info("CSV analysis completed successfully.")

        # Display the report
        display_report(analysis)
        logger.info("Report displayed successfully.")

    except (FileNotFoundError, ValueError) as error:
        logger.error("%s", error)
        sys.exit(1)

    except Exception:
        logger.critical("An unexpected fatal error occurred.", exc_info=True)
        sys.exit(2)


if __name__ == "__main__":
    main()

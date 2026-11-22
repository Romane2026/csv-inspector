"""CSV analysis report display utilities.

This module uses Rich to display CSV analysis results as formatted
tables in the terminal.
"""

from rich.console import Console
from rich.table import Table

console = Console()


def display_report(analysis: dict) -> None:
    """
    Display a formatted analysis report in the terminal.

    The report includes general information about the CSV file,
    such as the number of rows, columns, and missing values.
    If numerical columns are available, their descriptive statistics
    are displayed in a separate table.

    Args:
        analysis: Dictionary containing the CSV analysis results.
            Expected keys include ``row_count``, ``column_count``,
            ``missing_values``, ``statistics``, and ``numeric_columns``.
    """
    console.print("\n[bold cyan]CSV INSPECTION REPORT[/bold cyan]\n")

    # General information
    general_table = Table(title="General Information")
    general_table.add_column("Metric", style="cyan")
    general_table.add_column("Value", justify="right")

    general_table.add_row("Number of rows", str(analysis["row_count"]))
    general_table.add_row("Number of columns", str(analysis["column_count"]))
    general_table.add_row("Missing values", str(analysis["missing_values"]))

    console.print(general_table)

    # Numeric statistics
    statistics = analysis["statistics"]

    if statistics:
        stats_table = Table(title="Numeric Statistics")
        stats_table.add_column("Metric", style="cyan")

        for column in analysis["numeric_columns"]:
            stats_table.add_column(str(column), justify="right")

        metrics = ["mean", "std", "min", "25%", "50%", "75%", "max"]

        for metric in metrics:
            values = [metric.capitalize()]

            for column in analysis["numeric_columns"]:
                value = statistics.get(column, {}).get(metric)
                values.append(str(value) if value is not None else "-")

            stats_table.add_row(*values)

        console.print(stats_table)
    else:
        console.print("[yellow]No numeric columns found.[/yellow]")

    console.print()

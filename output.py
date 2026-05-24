import json
from rich.console import Console
from rich.table import Table

console = Console()

def render_screen_results(results, export_json=False):
    """Outputs security posture audit evaluations via interactive table or JSON."""
    if export_json:
        print(json.dumps(results, indent=2))
        return

    table = Table(title="🛡️ Live Azure Cloud Posture Assessment Summary", title_style="bold cyan")
    table.add_column("Status", justify="center")
    table.add_column("Check ID", style="bold")
    table.add_column("Resource Type", style="magenta")
    table.add_column("Resource Name")
    table.add_column("Description")

    fail_count = 0
    for r in results:
        if r["status"] == "FAIL":
            status_str = "[red]FAIL[/red]"
            fail_count += 1
        else:
            status_str = "[green]PASS[/green]"

        table.add_row(
            status_str,
            r["check_id"],
            r["resource_type"],
            r["resource_name"],
            r["description"]
        )

    console.print("\n")
    console.print(table)
    console.print(f"\n[bold yellow]Scan Complete:[/bold yellow] Found [bold red]{fail_count}[/bold red] posture gaps out of {len(results)} evaluated data points.\n")
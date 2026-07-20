from rich import print
from rich.console import Console
from rich.table import Table

table = Table(title="Student Grades")
table.add_column("Name", style="cyan")
table.add_column("Grade", justify="right", style="green")

table.add_row("Alice", "95")
table.add_row("Bob", "87")

console = Console()
console.print(table)

print("[bold red]Error:[/bold red] something went wrong")
print("[green]Success![/green] :thumbs_up:")
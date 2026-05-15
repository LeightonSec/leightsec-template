import sys

import typer
from rich.console import Console

from project_name import __version__

app = typer.Typer(add_completion=False, no_args_is_help=True)
console = Console()

_ETHICAL_WARNING = (
    "[yellow]⚠  For authorised use only.[/yellow]\n"
    "[dim]Only run against systems you own or have explicit written permission to test.\n"
    "Unauthorised use may violate the Computer Misuse Act and equivalent laws.[/dim]\n"
)


@app.callback()
def _startup() -> None:
    """TODO: one-line description of the tool."""
    console.print(_ETHICAL_WARNING)


@app.command()
def run() -> None:
    """TODO: primary action — implement me."""
    console.print("[bold]run[/bold] — replace this with real logic.")


@app.command()
def version() -> None:
    """Show version and exit."""
    console.print(f"v{__version__}")


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[dim]Interrupted.[/dim]")
        sys.exit(0)

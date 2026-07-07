from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(help="A CLI APP to review code using an AI agent")


@app.command()
def review(path: Annotated[Path, typer.Argument(exists=True)]):
    """
    Command to review your code.
    Prints the path for now
    """
    typer.echo(f"Would review '{path}'")


@app.callback()
def callback():
    """
    Review your code.
    """


def main() -> None:
    app()


if __name__ == "__main__":
    main()

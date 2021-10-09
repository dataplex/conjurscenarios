"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Conjur Scenarios."""


if __name__ == "__main__":
    main(prog_name="conjurscenarios")  # pragma: no cover

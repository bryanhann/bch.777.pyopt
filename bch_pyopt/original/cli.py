import click

import bch_pyopt
@click.group()
@click.version_option()
def cli():
    "Parse command line options via docstrings."


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")


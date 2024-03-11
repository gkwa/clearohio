import click


@click.group()
def main():
    """A simple Python click app."""


@main.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
@click.option("--age", type=int, prompt="Enter your age", help="The age of the user")
def greet(name, age):
    """Greets the user."""
    click.echo(f"Hello, {name}! You are {age} years old.")


@main.group()
def subcommand():
    """A subcommand group."""


@subcommand.command()
@click.option("--store", is_flag=True, help="Enable store mode")
def subsubcommand(store):
    """A subsubcommand."""
    if store:
        click.echo("Store mode enabled.")
    else:
        click.echo("Store mode disabled.")


if __name__ == "__main__":
    main()

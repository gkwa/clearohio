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


@main.command()
@click.option("--fake", is_flag=True, help="Enable fake mode")
def work(fake):
    """Performs work."""
    if fake:
        click.echo("Performing fake work...")
    else:
        click.echo("Performing real work...")


if __name__ == "__main__":
    main()

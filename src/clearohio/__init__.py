import click


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
@click.option("--age", type=int, prompt="Enter your age", help="The age of the user")
def main(name, age):
    """A simple Python click app that greets the user."""
    click.echo(f"Hello, {name}! You are {age} years old.")


if __name__ == "__main__":
    main()

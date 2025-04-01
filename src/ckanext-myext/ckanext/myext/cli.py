import click


@click.group(short_help="myext CLI.")
def myext():
    """myext CLI.
    """
    pass


@myext.command()
@click.argument("name", default="myext")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [myext]

import click


@click.group(short_help="extended_dataset_details CLI.")
def extended_dataset_details():
    """extended_dataset_details CLI.
    """
    pass


@extended_dataset_details.command()
@click.argument("name", default="extended_dataset_details")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [extended_dataset_details]

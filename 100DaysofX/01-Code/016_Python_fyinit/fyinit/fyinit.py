import click


@click.command()
@click.option(
    "-c",
    "--content",
    default="World",
    help="Content to be written to file after greeting.",
)
@click.option("--name", "-n", prompt=True)
@click.argument("out", type=click.File("w"), default="-", required=False)
def cli(content, name, out):
    """Just a tezt."""
    out.write(f"My name is {name}.\n")
    out.write("----+----\n")
    out.write("Content:\n")
    out.write(f"{content}\n")
    # click.echo(f"Hello, {name}.\n--+--\n Content:\n {content}.", file=out)

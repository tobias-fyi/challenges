import click

# import os


@click.command()
@click.argument("input", type=click.File("rb"), nargs=-1)
@click.argument("output", type=click.File("wb"))
def cli(input, output):
    """Initialize session from input."""
    for f in input:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            output.write(chunk)
            output.flush

    # with open(input, "r") as rf:
    #     with open(output, "w") as wf:
    #         for line in rf:
    #             wf.write(line)


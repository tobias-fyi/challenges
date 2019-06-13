import click
import re
import datetime


@click.command()
@click.argument("input", type=click.File(mode="rb"), default="template.md")
@click.argument("output", type=click.File(mode="wb"), default="journal.md")
def cli(input, output):
    """Initialize session from input."""

    def date_search(p):
        p.decode()
        return re.sub(r"{{date}}", str(datetime.date.today()), p)

    def j_search(p):
        today = datetime.date.today()
        start_date = datetime.date(2019, 3, 4)
        day_num = str((today - start_date).days + 1).zfill(3)

        return re.sub(r"{{j_num}}", day_num, p)

    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        date_search(chunk)
        j_search(chunk)
        output.write(chunk)
        output.flush

import click
import os
import sys
import time


def justify_center(content, width, symbol):
    """Centers string in symbol - width chars wide."""

    text = content
    lines = text.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].center(width, symbol)
    text = "\n".join(lines)
    return text


def table_printer(array, title, table_width):
    """Format an array - table of contents style."""

    print(f"{title}".center(table_width, icon_seperator))

    for k, v in enumerate(array):
        right_width = len(v)
        left_width = table_width - right_width
        print(
            str(k).ljust(left_width, icon_justified)
            + str(v).rjust(right_width)
        )


def exit_program():
    """Pretty self-explanatory?"""

    print("Exiting program...")
    time.sleep(1)
    sys.exit()


def dir_picker(path, prefix):
    """Allows user to choose from list of paths in cwd."""

    os.chdir(path)

    dir_list = os.listdir(os.getcwd())
    dir_list.sort()

    for d in dir_list:
        if d.startswith("."):
            dir_list.remove(d)  # removes .file + .folders from list

    print(sep)
    table_printer(dir_list, "Projects", v_width)
    print(sep)
    print(sep_ps)

    try:  # find selected directory + add path to dict for later
        d_index = int(input())
        d_root = dir_list[d_index]
        paths[f"{prefix}_root"] = os.path.join(path, d_root)
        os.chdir(paths[f"{prefix}_root"])
        print()
    except FileNotFoundError:
        print()
        print("Dir not found...")
        print(sep)
        exit_program()


def separator(line):
    pass


# aesthetic informatics
v_width = 33
icon_project = "º"
icon_seperator = "-"
icon_justified = "."
spacer = " "
ps_spacer = f"{icon_seperator*2}{icon_project}{icon_seperator*2}"

# visual separators
sep = justify_center(icon_project, v_width, icon_seperator)
sep_space = justify_center(icon_project, v_width, spacer)
sep_ps = justify_center(ps_spacer, v_width, spacer)


paths = {
    "all_projects": "/Users/Tobias/Documents/Projects/",
    "apps": "30_Applications",
}

starting_directory = ["project", "app"]


@click.command()
@click.argument("project")
@click.option(
    "-d", "--directory", type=click.Choice(starting_directory), prompt=True
)
def cli(project, directory):
    """Generates a project directory tree,
    starting at the root."""

    def init_root(project_name, directory):
        """Takes in project name to create a single directory."""

        # if statement that uses the click.Choice option
        if directory == "project":
            directory = paths["all_projects"]
            os.chdir(directory)

        if directory == "app":
            directory = os.path.join(paths["all_projects"], paths["apps"])
            os.chdir(directory)

        click.echo(sep)
        click.echo()
        click.echo("'ere's where you're at...")
        dir_picker(os.getcwd(), "dir_list")
        click.echo(sep)

        click.echo()
        click.echo(f"So, you wanna create a root for {project_name}?")
        click.echo(sep)
        # TODO: confirmation
        click.echo()
        click.echo("This is where it shall be created...")
        click.echo(os.getcwd())
        click.echo(sep)
        # os.makedirs(project_name)

    init_root(project, directory)

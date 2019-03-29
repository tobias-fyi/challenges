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


def table_printer(array, title, left_width, right_width):
    """Formats list - table of contents style."""

    print(f"{title}".center(left_width + right_width, "-"))

    for k, v in enumerate(array):
        print(str(k).ljust(left_width, ".") + str(v).rjust(right_width))


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
    table_printer(dir_list, "Choose-a-Dir", 8, 25)
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
p_icon = "º"
s_icon = "-"
spacer = " "
ps_spacer = f"{s_icon*2}{p_icon}{s_icon*2}"

# visual separators
sep = justify_center(p_icon, v_width, s_icon)
sep_space = justify_center(p_icon, v_width, spacer)
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
        click.echo(os.getcwd())
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

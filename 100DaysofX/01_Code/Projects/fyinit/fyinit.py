import click
import os
import sys
import datetime
import subprocess
import time


@click.command()
def cli():
    """Initializes new coding session."""

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
        """Waits 1 second then aborts the program."""
        print("Exiting program...")
        time.sleep(1)
        sys.exit()

    def prompter(prompt, scope):
        """Returns user input from prompt."""

        print(sep)
        print(f"What is this {scope}'s {prompt}:")
        print(sep)
        print(sep_ps)
        return input()

    def dir_picker(path, prefix):
        """Allows user to choose from list of paths in cwd."""

        os.chdir(path)

        dir_list = os.listdir(os.getcwd())
        dir_list.sort()

        for d in dir_list:
            if d.startswith("."):
                # removes files from list - .DS_STORE, README, etc.
                dir_list.remove(d)
                # TODO: also remove other .file directories like .git

        print(sep)
        table_printer(dir_list, "Choose-a-Dir", 8, 25)
        print(sep)
        print(sep_ps)

        try:  # find selected directory + add path to dict for later
            d_index = int(input())
            d_root = dir_list[d_index]
            p_paths[f"{prefix}_root"] = os.path.join(path, d_root)
            os.chdir(p_paths[f"{prefix}_root"])
            print()
        except FileNotFoundError:
            print()
            print("Dir not found...")
            print(sep)
            exit_program()

    # set up all the time + date variables
    c_time = time.strftime("%H:%M", time.localtime(time.time()))
    today = datetime.date.today()
    c_date = str(today)

    c_year = str(today.year)
    c_month = str(today.month).zfill(2)
    # c_day = str(today.day).zfill(2)

    start_date = datetime.date(2019, 3, 4)
    day_num = str((today - start_date).days + 1).zfill(3)

    # aesthetic informatics
    v_width = 33
    p_icon = "º"
    s_icon = "-"
    escape = "\\"  # linter doesn't like the escaped hash in template below
    spacer = " "
    ps_spacer = f"{s_icon*2}{p_icon}{s_icon*2}"

    # visual separators - horizontal lines - confirm
    sep = justify_center(p_icon, v_width, s_icon)
    sep_sm = justify_center(p_icon, 17, s_icon)
    sep_space = justify_center(p_icon, v_width, spacer)
    sep_ps = justify_center(ps_spacer, v_width, spacer)

    p_paths = {
        "p_all": "/Users/Tobias/workshop/Challenges/",
        "chal_root": "100DaysofX/01_Code",
    }  # dict to hold paths

    term_commands = {
        "code": ["code"],
        "ws_code": ["code", "challenges.code-workspace"],
    }  # dict to hold terminal commands

    os.chdir(p_paths["p_all"])
    p_paths["current_root"] = os.path.join(os.getcwd(), p_paths["chal_root"])
    os.chdir(p_paths["current_root"])

    # dir_picker(os.getcwd(), "chal")
    # dir_picker(os.getcwd(), "day")

    subject = prompter("language", "session")
    project = prompter("project", "session")
    project_icon = prompter("icon", "project")
    project_goal = prompter("goal", "project")
    session_goal = prompter("goal", "session")

    template = f"""# {c_date} | #{day_num}

{escape}#100DaysofCode

---

## SELECT * FROM Project

### Project.abstract

    GOAL__ : {project_goal}

### Project.loxocache({c_year}-{c_month})

    TASK__ : Collect tags from other documents

--------{project_icon}--------

## SELECT * FROM Session

### Session.abstract

    GOAL_{day_num} : {session_goal}  

#### Session.cache

- pass

---

## Session.journal({c_date})

### Loxocache

--------{project_icon}--------

### {c_time} -+- Session.init
"""

    day_dir = f"{day_num}-{subject}_{project}"
    p_paths["day_path"] = os.path.join(os.getcwd(), day_dir)

    if os.path.isdir(p_paths["day_path"]):
        print("Directory already exists.")
        time.sleep(1)
        exit_program()

    os.makedirs(day_dir)
    time.sleep(0.8)
    print(sep)
    print(sep_space)
    print(sep_sm)
    print("Directory created.")
    print(sep_sm)
    os.chdir(p_paths["day_path"])

    j_name = f"{day_num}-journal.md"
    p_paths["j_path"] = os.path.join(os.getcwd(), j_name)
    term_commands["code"].append(p_paths["j_path"])

    print(sep_space)
    print(sep_sm)
    print(f"Creating journal entry...")
    print(sep_sm)
    time.sleep(0.8)

    with open(f"{j_name}", "w") as j:
        j.write(template)

    time.sleep(0.6)
    print("...")
    time.sleep(0.6)
    print(sep_space)
    print(sep_sm)
    print("Opening workspace...")
    print(sep_sm)
    time.sleep(0.5)

    p_paths["ws_path"] = os.path.join(p_paths["p_all"], "00_Admin")
    os.chdir(p_paths["ws_path"])

    click.echo("And BOOM!")
    time.sleep(1)
    click.echo("No more Chinese laundry...")

    subprocess.run(term_commands["ws_code"])
    subprocess.run(term_commands["code"])

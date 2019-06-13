# 2019-03-27 | #024

\#100DaysofCode

- [2019-03-27 | #024](#2019-03-27--024)
  - [Today's Menu](#todays-menu)
    - [Main Course](#main-course)
    - [SELECT](#select)
      - [Session Sounds](#session-sounds)
  - [Session Log](#session-log)
    - [13:21 -+- Sessionit](#1321----sessionit)
    - [13:46 -+- Arguments](#1346----arguments)
    - [13:57 -+- EchoTest](#1357----echotest)
    - [14:10 -+- Choice Options](#1410----choice-options)
    - [14:25 -+- SessionDis](#1425----sessiondis)

---

## Today's Menu

### Main Course

    GOAL_ : Write Python Cli Tool With Click That Creates Full Project Directory Structure

--------∫--------

### SELECT

#### Session Sounds

[Wild Dark - Like a Whisper \[Nazca\]](https://www.youtube.com/watch?v=Ic4VRorUH9I) which I found while listening to [Mira on the Mayan Warrior in Tulumn](https://soundcloud.com/mayanwarriorofficial/mira-mayan-warrior-tulum-2019).

---

## Session Log

### 13:21 -+- Sessionit

Going to go through the process of creating a new Click app / Python package.

[Projects/directree](../Projects/directree/)

I'm going to start out hard-coding the tree structure into the script.  
However, if I have time today or once I pick it up again I'm going to write it so the directory structure is modular and can be defined for specific projects.

---

### 13:46 -+- Arguments

Instead of using prompts to gather the relevant information, I'm going to write it correctly this time to actually take advantage of the fact that Click makes a full CLI tool.

    i.e. Relevant information will be passed in via arguments and/or options

In a continued effort to start with small steps and work my way up to more complex functionality, I'm going to start by simply having it take in an argument for the title of the project and create a new directory somewhere (a specific somewhere).

Finishing up the setup of the Python package by installing it into the current virtual environment, which in this case is fyinit:

    $ conda activate fyinit
    $ pip install --editable .
    > Installing collected packages: directree
      Running setup.py develop for directree
      Successfully installed directree

Shweeeeet!  

    $ tree
    .
    ├── __pycache__
    │   └── directree.cpython-37.pyc
    ├── directree.egg-info
    │   ├── PKG-INFO
    │   ├── SOURCES.txt
    │   ├── dependency_links.txt
    │   ├── entry_points.txt
    │   ├── requires.txt
    │   └── top_level.txt
    ├── directree.py
    └── setup.py

---

### 13:57 -+- EchoTest

Now to test it out with a simple click.echo command. Here's the code:

    import click

    @click.command()
    @click.argument("project")
    def cli(project):
        """Generates a project directory tree,
        starting at the root."""

        def init_root(project_name):
            """Takes in Project Title."""
            click.echo(f"Create root for {project_name}?")
            # os.makedirs(project_name)

        init_root(project)

...and running it in terminal:

    $ directree some_new_project
    > Create root for some_new_project?

Sweet like shoogurr.

Also going to test out the os module before creating any directories:

    $ directree some_new_project
    > Create root for some_new_project?
      /Users/Tobias/Documents/Projects/Challenges/100DaysofX/01_Code/Projects/directree

Used os.chdir to navigate to projects directory and reused the dir_picker function I wrote in fyinit to print out a list of the directories.

That also means I had to bring along some other functions from that same script.  
That, kids (aka $ME) is why you stay DRY.

---

### 14:10 -+- Choice Options

To allow the choice of starting directory, I decided to use an option that can only be chosen from a list of available choices.

The same option (--directory) will also have a prompt so it doesn't ***have*** to be entered right away.

    starting_directory = ["project", "app"]

    @click.option(
        "-d", "--directory", type=click.Choice(starting_directory), prompt=True
    )

---

### 14:25 -+- SessionDis

...just realized that all those functions I brought over don't have to be inside the click command...duh.  
Wow that makes it a ton more readable.  
Now I'm going to have to do this same change to fyinit.

Maybe next time.

Time to give the tool a test as it is now before ending the sesh:

    $ directree some_new_project
    > Directory (project, app): app
      ----------------º----------------

      'ere's where you're at...
      /Users/Tobias/Documents/Projects/30_Applications
      ----------------º----------------

      So, you wanna create a root for some_new_project?
      ----------------º----------------

      This is where it shall be created...
      /Users/Tobias/Documents/Projects/30_Applications
      ----------------º----------------

Sweet! That'll have to do for now.

Hasta Gotta keep'm sep'rated, Amigo!
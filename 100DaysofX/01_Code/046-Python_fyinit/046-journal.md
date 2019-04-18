# 2019-04-18 | #046

\#100DaysofCode

- [2019-04-18 | #046](#2019-04-18--046)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.journal(2019-04-18)](#sessionjournal2019-04-18)
    - [Loxocache](#loxocache)
    - [12:11 -+- Session.init](#1211----sessioninit)
    - [10:17 -+- DAY 046 - PRE-CONFIG](#1017----day-046---pre-config)
    - [10:53 -+- fyinit](#1053----fyinit)
    - [12:26 -+- Surroundings Assessment](#1226----surroundings-assessment)

---

## SELECT * FROM Project

### Project.abstract

    GOAL__ : Convenient CLI tool for initiating a session

### Project.loxocache(2019-04)

    TASK_044 : Copy session from on_form build journal  
    TASK_ : write cli tool for initializing a new project  

--------ƒ--------

## SELECT * FROM Session

### Session.abstract

    GOAL√046 : My initial goal for this session is to get my fyinit click program up and running with the new environment setup  
    GOAL_046 : Create better UX for fyinit  

#### Session.cache

- pass

---

## Session.journal(2019-04-18)

### Loxocache

    TASK_046 : move important dirs (fineyedesign + tobiasfyi) into ~/workshop  

--------ƒ--------

### 12:11 -+- Session.init

It worked! Woop Woop!

I wrote the first section of the journal in Day 045 until I got fyinit up and running in the new environment.

---

### 10:17 -+- DAY 046 - PRE-CONFIG

    GOAL√046 : My initial goal for this session is to get my fyinit click program up and running with the new environment setup  

I copied over the Challenges repository / directory using one of my favorite bash tools `rsync`

    $ rsync -ah --info=progress2 --append-verify ~/Documents/Projects/Challenges ~/workshop

1. Installed pyenv-virtualenv
2. Installed pyenv-virtualenvwrapper

With virtualenvwrapper all your virtualenvs are kept on a same directory and your projects’ code on another. As I defined yesterday (and won't spend any more time on today, I promise...):

    # All virtualenvs will be in...
    mkdir ~/.vega
    # All projects will be in...
    mkdir ~/workshop

I created my .zshenv file and edited as follows:

    export WORKON_HOME=~/.vega
    export PROJECT_HOME=~/workshop
    if command -v pyenv 1>/dev/null 2>&1; then
        eval "$(pyenv init -)"
    fi

Restarted the shell. Now installing CPython 3.7.3. 

Here's a handy link to the [pyenv commands reference](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md).

    $ pyenv install 3.7.3
    ... zlib not available

I got the notorious zlib not available error because I'm running Mojave. Went through some [GitHub issue discussion](https://github.com/pyenv/pyenv/issues/1219) and tried this (which worked):

    $ CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install -v 3.7.3
    Installed Python-3.7.3 to /Users/Tobias/.pyenv/versions/3.7.3

    $ pyenv global 3.7.3

---

### 10:53 -+- fyinit

Setting environment variables specific to each virtual environment. Once inside the project root:

    $ touch .env
    SECRET_KEY="SuperSecretQue"

Gettings fyinit up and running.

    $ cd ~/workshop/Challenges/100DaysofX/01_Code/Projects/fyinit
    $ pipenv install
    $ pipenv install click
    Installing click…
    Adding click to Pipfile's [packages]…
    ✔ Installation Succeeded
    Pipfile.lock (182788) out of date, updating to (a65489)…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    ✔ Success!
    Updated Pipfile.lock (182788)!
    Installing dependencies from Pipfile.lock (182788)…
    🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:01
    To activate this project's virtualenv, run pipenv shell.
    Alternatively, run a command inside the virtualenv with pipenv run.

    $ pip install --editable .
    Obtaining file:///Users/Tobias/workshop/Challenges/100DaysofX/01_Code/Projects/fyinit
    Requirement already satisfied: Click in /Users/Tobias/.local/share/virtualenvs/fyinit-Ctn_MiSA/lib/python3.7/site-packages (from fyinit==0.1) (7.0)
    Installing collected packages: fyinit
    Running setup.py develop for fyinit
    Successfully installed fyinit

    $ pip install pylint

Decided I should probably use `git clone` instead of rsync to bring the repository over to the new workshop directory.

    $ rm -rf Challenges
    $ git status
    $ git add 045-...
    $ git commit -m "Updated day 045 with 046 until new entry created"

Got that working nicely. Now some final notes on pipenv before switching gears to work on the fyinit cli tool.

[Pipenv Configuration with Environment Variables](https://pipenv.readthedocs.io/en/latest/advanced/#configuration-with-environment-variables)

    PIPENV_CACHE_DIR
        Location for Pipenv to store it’s package cache.
        Default is to use appdir’s user cache directory.

    PIPENV_EMULATOR
        If set, the terminal emulator’s name for pipenv shell to use.
        Default is to detect emulators automatically. This should be set if your emulator, e.g. Cmder, cannot be detected correctly.

    PIPENV_SHELL
        An absolute path to the preferred shell for pipenv shell.
        Default is to detect automatically what shell is currently in use.

    PIPENV_SHELL_FANCY
        If set, always use fancy mode when invoking pipenv shell.
        Default is to use the compatibility shell if possible.

    PIPENV_IGNORE_VIRTUALENVS
        If set, Pipenv will always assign a virtual environment for this project.
        By default, Pipenv tries to detect whether it is run inside a virtual environment, and reuses it if possible. This is usually the desired behavior, and enables the user to use any user-built environments with Pipenv.

    PIPENV_VENV_IN_PROJECT
        If set, creates .venv in your project directory.
        Default is to create new virtual environments in a global location.

    ☤ Custom Virtual Environment Location
        Pipenv automatically honors the WORKON_HOME environment variable, if you have it set — so you can tell pipenv to store your virtual environments wherever you want, e.g.:

            export WORKON_HOME=~/.venvs

    ☤ Shell Completion
        To enable completion in fish, add this to your config:

        eval (pipenv --completion)
        Alternatively, with bash or zsh, add this to your config:

        eval "$(pipenv --completion)"
        Magic shell completions are now enabled!

---

### 12:26 -+- Surroundings Assessment

Although it's felt like an absolute slog the last couple of days, I think I'm finally coming to understand pipenv.

I still feel very uninformed about pyenv so I will have to do more work with that later on.

For now, I'm going to try getting a django project up and running. I don't want to fall into any of the mistakes I made on Tuesday, so I'm going to create the repository from scratch.

    $ cd ~/workshop
    $ git clone git@github.com:tobias-fyi/onform.git

----ø----

I keep doing the same few things over and over again whenever starting a new project. What does that tell me? That I can make that process much easier and quicker with a little automation.

    TASK_ : write cli tool for initializing a new project  

    TASK_046 : move important dirs (fineyedesign + tobiasfyi) into ~/workshop  

----ø----

    $ touch .gitignore
    $ mkdir 00-Admin
    $ mkdir 01-Docs
    $ mkdir xx-db_data

I found a good [RealPython article on pyenv](https://realpython.com/intro-to-pyenv/).


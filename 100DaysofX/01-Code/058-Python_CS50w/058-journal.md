# 2019-04-30 | #100DaysofCode

## Day 058 / 100

---

## SELECT * FROM Project

### Project.abstract

    GOAL_CS50w_Project1 : Build a book review application with Flask / SQL  

### Project.loxocache(2019-05)

    TASK__ : Collect tags from other documents

--------©--------

## SELECT * FROM Session

### Session.abstract

    GOAL_059 : Get started on the project  

#### Session.cache

- pass

---

## Session.journal(2019-04-30)

### Loxocache

--------©--------

### 15:42 ~ Session.init

I am quite a ways behind schedule on my goal of finishing CS50w by the time this challenge is complete. I'm only just now starting the second project / 3 weeks into the course. I want to spend a ton more time on this going forward, as the subjects discussed in the course are very aligned with what I want to be studying / practicing.

Time to groooooove!

---

### 15:38 ~ New Project (The Easy Way)

I wanted to try out the new method I have for starting up a project, which is much simpler than any of the methods I'd used before.

    $ mkproject sketchbox/CS50Flask
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/sketchbox/CS50Flask/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/sketchbox/CS50Flask/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/sketchbox/CS50Flask/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/sketchbox/CS50Flask/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/sketchbox/CS50Flask/bin/get_env_details
    Creating /Users/Tobias/workshop/sketchbox/CS50Flask
    Setting project for CS50Flask to /Users/Tobias/workshop/sketchbox/CS50Flask

### 16:34 ~ Settings Things Ups

Decided to get some practice setting up a new python dev environment in vscode. After installing pylint and black, here are the settings.

    {   "folders": [
            { "path": "/Users/Tobias/workshop/sketchbox/CS50Flask" }
        ],
        "settings": {
            "python.pythonPath": "/Users/Tobias/.vega/sketchbox/CS50Flask/bin/python",
            "python.venvPath": "/Users/Tobias/.vega",
            "python.linting.pylintEnabled": true,
            "python.linting.pylintPath": "/Users/Tobias/.vega/sketchbox/CS50Flask/bin/pylint",
            "python.linting.pylintArgs": [
                "--load-plugins",
                "pylint_django,pylint_flask",
            ],
            "editor.formatOnSave": true,
            "files.exclude": {
                "**/.git": true,
                "**/.svn": true,
                "**/.hg": true,
                "**/CVS": true,
                "**/.DS_Store": true,
            },
            "python.formatting.provider": "black",
            "python.formatting.blackPath": "/Users/Tobias/.vega/sketchbox/CS50Flask/bin/black",
            "python.formatting.blackArgs": [
                "--line-length=79",
            ]
        }
    }

This is making me want to recreate the fineyedesign project using the new method. Makes much more sense than what I was doing when I created this one.

Started up a new terminal and realized that I didn't know off the top of my head how to activate the venv that was created when I created the project. Remembered something about `workon`, but didn't remember the specifics. It's crazy easy...to work on the CS50Flask project:

    $ workon sketchbox/CS50Flask
    CS50Flask » tobiasfyi » ..shop/sketchbox/CS50Flask

It not only activates the virtual environment but `cd`s into that project's directory as well. 

Neat!

---

### Some Python Review

#### 16:47 ~ Classes

A way to create a new type of thing that doesn't have a standardized or defined type within Python. e.g. a type for x,y coordinates:

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

I want to get more into working with Classes. Not at the current moment, but will soon be going over them in more detail with the help of youtube and some books (namely Dan Bader's Python Tricks).

Actually, might as well go over them a little bit right now...coz why not?

\#flippittyyfloppitty

Because right now I want to focus on Flask...that's why not.

---

### Flask

#### 16:53 ~ Getting Started

    $ pip install flask
    Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.2 flask-1.0.2 itsdangerous-1.1.0

Kept receiving the prompt to update pip, so I did so (outside and inside the virtual environment).

    $ pip install --upgrade pip
    Successfully installed pip-19.1

#### 16:55 ~ Hello World

Tried to run the web server after writing in the hello world app. Received an error due to Flask not being able to find an application for which to run the server...

> CS50Flask/Flask

    $ flask run
    Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.

I changed the name of the file to `app.py` and tried again, this time with success...

    $ flask run
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

> CS50Flask/Flask/app.py

    from flask import Flask

    app = Flask(__name__)


    @app.route("/")
    def index():
        return "Hello, Worlds!"

#### 17:01 ~ More Routing

Added another route to say hello to myself...

> CS50Flask/Flask/app.py

    ...
    @app.route("/toby")
    def toby():
        return "Hello, Tobias!"

Now getting a little tricky with some dynamic greetings!

    @app.route("/<string:name>")
    def greetings(name):
        return f"Greetings, {name.title()}!"

Shows on the site as "Greetings, Vibes!"

#### 17:15 ~ The Knights Templartes

---

### 21:23 ~ Debug'n'Done

Set up my .zshrc so it sets the Flask debug mode to true.

    export FLASK_DEBUG=1

----ƒ----

Hasta Luegos, Amigos!
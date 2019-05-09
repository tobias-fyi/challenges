# 2019-05-08 | #100DaysofCode

## Day 066 / 100

---

## SELECT * FROM Project

### Project.abstract

    GOAL_AptDraft : Reading journal + book review application using Flask + Postgres  

### Project.loxocache(2019-05)

- pass

--------å--------

## SELECT * FROM Session

### Session.abstract

    GOAL_066 : Complete SQL lecture + actually start the build  

#### Session.cache

- Some good tracks in [this Mira set](https://trackidpls.com/mira-mayan-warrior-burning-man-2018-tracklist)

---

## Session.sojourn(2019-05-08)

### Loxocache

--------å--------

### 20:19 ~ å.init

Quite stoked on my progress last session. Mostly that I was able to establish a two-way connection with my library database and set up project-specific envirovars without much trouble at all.

Feels güdį

---

### 20:20 ~ MoreSQL

The lecture goes over prompting the user for a flight ID then displaying the passengers on that flight. i.e. multiple types of queries in one script.

---

### 20:21 ~ FlaSQL

Now it's time to get groovin' on using SQL with Flask...or Flask with SQL...

Cruising through the lecture because I really want to just start building AptDraft instead of spending time figuring out the little things in the lecture. I think I have a good enough idea of what I'm doing, now that I can connect to the DB, to be a little *dangerous*.

--------å--------

---

### 20:31 -+- å.init

#### PostgreSQL

The project1 specification document says to use a Postgres instance on Heroku rather than one locally.

I already have an account set up under fyi@tobyreaper.com, so I'll just use that.

1. Created a new app called `aptdraft`
2. Overview > Configure Add-Ons > `Heroku Postgres`
3. Click through to the database
4. Settings > View Credentials

    Please note that these credentials are not permanent.

    Heroku rotates credentials periodically and updates applications where this database is attached.

    Host            ec2-23-23-195-205.compute-1.amazonaws.com
    Database        d5np4jgp8jmq9r
    User            vlmzdmznxzkmfs
    Port            5432
    Password        590dd22418b2c03c816092c6011381d512e0ec0a8d7b2d49d74f9c0088fa08e1
    URI             postgres://vlmzdmznxzkmfs:590dd22418b2c03c816092c6011381d512e0ec0a8d7b2d49d74f9c0088fa08e1@ec2-23-23-195-205.compute-1.amazonaws.com:5432/d5np4jgp8jmq9r
    Heroku CLI      heroku pg:psql postgresql-corrugated-31413 --app aptdraft

I can access the database from Adminer `adminer.cs50.net`. The spec mentions that if Postgres is installed locally, I "should be able to run `psql URI` on the command line. Not sure what that does but I should be able to access the database from elsewhere if need be.

---

### 21:29 ~ Make Da Project

#### Requirements

The project1 distribution directory includes a requirements file. Once all requirements are installed in a venv, set the environment variables for Flask and db, then let 'er rip!

I love making new projects even more now than before because of how intuitive and easy it is.

    ╭─ tobiasfyi » ~/workshop                                  19.05.08 ∫ 21:30:30
    ╰─ mkproject aptdraft
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/aptdraft/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/aptdraft/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/aptdraft/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/aptdraft/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/aptdraft/bin/get_env_details
    Creating /Users/Tobias/workshop/aptdraft
    Setting project for aptdraft to /Users/Tobias/workshop/aptdraft

Downloaded the project1 distro into the new project dir...

> workshop/aptdraft

    .
    └── project1
        ├── README.md
        ├── application.py
        ├── books.csv
        └── requirements.txt

    1 directory, 4 files

> requirements.txt

    Flask
    Flask-Session
    psycopg2
    SQLAlchemy

With a little pip and a little install, viola!

...well maybe not quite. At least not with the requirements file. The reason is something I've run into before—psycopg2 needs to be built or installed as `psycopg2-binary`.

So I'm going to install the requirements by hand...

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:36:27
    ╰─ pip install flask

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:37:43
    ╰─ pip install flask-session

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:40:20
    ╰─ pip install psycopg2-binary

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:40:31
    ╰─ pip install sqlalchemy

Now installing my personal stuffs...

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:40:51
    ╰─ pip install black

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:41:22
    ╰─ pip install pylint

    ╭─ aptdraft » tobiasfyi » ..ptdraft/project1               19.05.08 ∫ 21:41:37
    ╰─ pip install ipython

#### EnviroVars

Oh boy this is also exciting now that I know just where to put them...

> ~/.vega/aptdraft/bin/postactivate

    export FLASK_APP=application.py
    export FLASK_ENV=development
    export DATABASE_URL="postgres://vlmzdmznxzkmfs:590dd22418b2c03c816092c6011381d512e0ec0a8d7b2d49d74f9c0088fa08e1@ec2-23-23-195-205.compute-1.amazonaws.com:5432/d5np4jgp8jmq9r"

> ~/.vega/aptdraft/bin/postdeactivate

    unset FLASK_APP
    unset FLASK_ENV
    unset DATABASE_URL

Reactivated the venv to set those variables, then test it...

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft               19.05.08 ∫ 21:48:49
    ╰─ deactivate

    ╭─ tobiasfyi » ..orkshop/aptdraft                          19.05.08 ∫ 21:50:42
    ╰─ workon aptdraft

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft               19.05.08 ∫ 21:50:46
    ╰─ echo $FLASK_APP
    application.py

Boooom goes the dynamite!

Now let's see if the flask app runs, and if it does, I gotta go catch it...

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft               19.05.08 ∫ 21:52:13
    ╰─ flask run
    * Serving Flask app "application.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 755-058-491
    127.0.0.1 - - [08/May/2019 21:52:20] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [08/May/2019 21:52:20] "GET /favicon.ico HTTP/1.1" 404 -

And we're live!

I also took the database for a spin with adminer, and that worked fine and dandy on the first go.

Groovy...

---

### 21:55 ~ GoodReads API

Signed up for an account. Applied for and received my API keys...

    Here is your developer key for using the Goodreads API. This key must be appended to every request using the form variable 'key'. (If you're using our write API, you'll need your secret too.)

    key: lPR3RTkiUqXn9ZmGezYPfg
    secret: 47MSaOVWmLSdQNDeR6gULLNSBpMazwSu6nWoJapzfw

Now I should be able to run the following code (`KEY` is my API key) and get something back...

    import requests
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
    print(res.json())

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft                        19.05.08 ∫ 22:04:28
    ╰─ python 01-Docs/20-Code/api_test.py
    Traceback (most recent call last):
    File "01-Docs/20-Code/api_test.py", line 1, in <module>
        import requests
    ModuleNotFoundError: No module named 'requests'

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft                        19.05.08 ∫ 22:04:34
    ╰─ pip install requests

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft                        19.05.08 ∫ 22:05:03
    ╰─ python 01-Docs/20-Code/api_test.py
    {'books': [{'id': 29207858, 'isbn': '1632168146', 'isbn13': '9781632168146', 'ratings_count': 0, 'reviews_count': 2, 'text_reviews_count': 0, 'work_ratings_count': 28, 'work_reviews_count': 123, 'work_text_reviews_count': 10, 'average_rating': '4.07'}]}

Succyess! But I wanted to see it nice and formatted, so piped it into a .json file. All I had to do was replace the single quotes with doubles and it formatted itself...

    ╭─ aptdraft » tobiasfyi » ..orkshop/aptdraft                        19.05.08 ∫ 22:05:06
    ╰─ python 01-Docs/20-Code/api_test.py > 01-Docs/20-Code/api_test.json

    {
        "books": [
            {
                "id": 29207858,
                "isbn": "1632168146",
                "isbn13": "9781632168146",
                "ratings_count": 0,
                "reviews_count": 2,
                "text_reviews_count": 0,
                "work_ratings_count": 28,
                "work_reviews_count": 123,
                "work_text_reviews_count": 10,
                "average_rating": "4.07"
            }
        ]
    }

---

### 22:44 ~ Planning

Going to hit the hay soon, but wanted to list out some key things about the site first...

Pages

1. Registration
2. Login / Logout
3. Search / Results List
4. Book Detail
5. Submit a Review

From reading the requirements again, it seems a basic understanding of APIs is required. Not sure if that means I should go onto the next lectures, but I'm assuming not. I think I can handle it.

Hasta Luego, Amigo!
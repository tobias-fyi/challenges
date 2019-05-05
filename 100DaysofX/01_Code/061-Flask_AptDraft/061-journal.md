# 2019-05-03 | #100DaysofCode

## Day 061 / 100



## SELECT * FROM Project

### Project.abstract

    GOAL__: Book review / reading journal application with Flask / Postgres  

### Project.loxocache(2019-05)

    TASK__: Collect any other tags from relevant entries  

--------∫--------

## SELECT * FROM Session

### Session.abstract

    GOAL_060 : Complete SQL lecture while working on AptDraft / Project 1  

#### Session.cache

- [CS50w Lecture 3 - SQL](https://youtu.be/Eda-NmcE5mQ)

---

## Session.journal(2019-05-03)

### Loxocache

----ƒ----

---

### 14:20 ~ sess.init

I know much of the subjects in this lecture already, but it doesn't hurt to get more practice

Created a new folder in the CS50Flask Project Directory. However, I think I might create yet another project and move all the files into that one from what I was working on yesterday and what I worked on for the previous project.

I don't want the project to only be the flask project. I'll be creating a new project called `AptDraft` for that anyways.

I'll do that later, though. Right now I just want to focus on learning.

---

### 14:20 ~ Creatation

Using separate .psql files (as I'm already a dedicated Postgres fanboy) to practice writing the queries along with the lecture.

----ƒ----

#### New Project

Decided to create a new project, simply titled CS50. I had a previous one but wanted to create a new one to have it be standardized with the rest of my current projects.

    $ mkproject CS50
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/CS50/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/CS50/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/CS50/bin/preactivate

    $ rsync -ah --info=progress2 --append-verify ../sketchbox/CS50Flask/ .
            38.53K 100%    1.31MB/s    0:00:00 (xfr#39, to-chk=0/69)

    $ pip install black
    Installing collected packages: toml, click, appdirs, attrs, black
    Successfully installed appdirs-1.4.3 attrs-19.1.0 black-19.3b0 click-7.0 toml-0.10.0

    $ pip install pylint
    Installing collected packages: mccabe, isort, wrapt, lazy-object-proxy, typed-ast, six, astroid, pylint
    Successfully installed astroid-2.2.5 isort-4.3.18 lazy-object-proxy-1.3.1 mccabe-0.6.1 pylint-2.3.1 six-1.12.0 typed-ast-1.3.5 wrapt-1.11.1

    $ pip install flask
    Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, flask
    Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.2 flask-1.0.2 itsdangerous-1.1.0

    $ pip install sqlalchemy
    Installing collected packages: sqlalchemy
        Running setup.py install for sqlalchemy ... done
    Successfully installed sqlalchemy-1.3.3

    $ rsync -ah --info=progress2 --append-verify ~/Documents/Projects/CS50/project0 .
            4.17K 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=0/2)

----ƒ----

#### Postgres Me Timbers

Created a new postgres server, database, user, and table.

    postgres=# CREATE DATABASE readinglist;
    CREATE DATABASE

    postgres=# \c readinglist
    You are now connected to database "readinglist" as user "Tobias".

    readinglist=# CREATE USER reader WITH SUPERUSER PASSWORD 'r34d3r';
    CREATE ROLE

    readinglist=# CREATE TABLE books (
    readinglist(#     id SERIAL PRIMARY KEY,
    readinglist(#     author VARCHAR NOT NULL,
    readinglist(#     genre VARCHAR NOT NULL,
    readinglist(#     pub INTEGER NOT NULL,
    readinglist(#     wordcount INTEGER NULL
    readinglist(# );
    CREATE TABLE

    readinglist=# \c readinglist reader
    You are now connected to database "readinglist" as user "reader".

    readinglist=# \d
                List of relations
    Schema |     Name     |   Type   | Owner
    -------+--------------+----------+-------
    public | books        | table    | Tobias
    public | books_id_seq | sequence | Tobias
    (2 rows)

I realized after creating the table that I forgot to include the title of the book in the CREATE TABLE command. Whoops.

Time for some quality alteration...

    readinglist=# ALTER TABLE books ADD COLUMN title VARCHAR NOT NULL;
    ALTER TABLE

I also decided to add a subgenre column...

    readinglist=# ALTER TABLE books ADD COLUMN subgenre VARCHAR NULL;
    ALTER TABLE

And instead of wordcount, I found that number of pages is a much easier number to find...

    readinglist=# ALTER TABLE books RENAME COLUMN wordcount TO pages;
    ALTER TABLE

---

### 15:18 ~ Insertion

Time to add some data to ye ol' database table.

    readinglist=# INSERT INTO books (
    readinglist(#     title,
    readinglist(#     author,
    readinglist(#     genre,
    readinglist(#     subgenre,
    readinglist(#     pub,
    readinglist(#     pages
    readinglist(# )
    readinglist-#
    readinglist-# VALUES (
    readinglist(#     'Turings Cathedral',
    readinglist(#     'George Dyson',
    readinglist(#     'Nonfiction',
    readinglist(#     'Biography',
    readinglist(#     2012,
    readinglist(#     505
    readinglist(# );
    INSERT 0 1

Added a bunch more but not inserting them into this document because that's a bit unneccesary.

---

### 15:34 ~ Dropped To Make Anew

In true flippitty floppitty fashion, I decided to drop the table and create it fresh with all of the columns that I added. Not a big deal but I want the columns to be in the correct order without changing the queries to do so. Not sure if there is a way to rearrange the columns after the fact, but I doubt it.

    readinglist=# DROP TABLE books;
    DROP TABLE

    readinglist=# CREATE TABLE books (
    readinglist(#     id SERIAL PRIMARY KEY,
    readinglist(#     title VARCHAR NOT NULL,
    readinglist(#     author VARCHAR NOT NULL,
    readinglist(#     genre VARCHAR NOT NULL,
    readinglist(#     subgenre VARCHAR NOT NULL,
    readinglist(#     pub_year INTEGER NOT NULL,
    readinglist(#     pages INTEGER NULL
    readinglist(# );
    CREATE TABLE

Then I inserted the same data again (that's why I wrote them in a separate file, duh). Here's just one of the inserts:

    readinglist=# INSERT INTO books (
    readinglist(#     title,
    readinglist(#     author,
    readinglist(#     genre,
    readinglist(#     subgenre,
    readinglist(#     pub_year,
    readinglist(#     pages
    readinglist(# )
    readinglist-#
    readinglist-# VALUES (
    readinglist(#     'Surface Detail',
    readinglist(#     'Iain M. Banks',
    readinglist(#     'Fiction',
    readinglist(#     'Sci-fi',
    readinglist(#     2010,
    readinglist(#     627
    readinglist(# );
    INSERT 0 1

---

### 15:40 ~ Selectation

    readinglist=# SELECT * FROM books;
    id |        title        |    author     |   genre    | subgenre  | pub_year | pages
    ---+---------------------+---------------+------------+-----------+----------+------
    1  | Turings Cathedral   | George Dyson  | Nonfiction | Biography |     2012 |   505
    2  | Walkaway            | Cory Doctorow | Fiction    | Sci-fi    |     2017 |   384
    3  | Consider Phlebas    | Iain M. Banks | Fiction    | Sci-fi    |     1988 |   471
    4  | The Player of Games | Iain M. Banks | Fiction    | Sci-fi    |     1988 |   293
    5  | Use of Weapons      | Iain M. Banks | Fiction    | Sci-fi    |     1990 |   411
    6  | Surface Detail      | Iain M. Banks | Fiction    | Sci-fi    |     2010 |   627
    (6 rows)

That's better =)

----ƒ----

Now to get into some different SELECT queries...

    readinglist=# SELECT title, author FROM books;
            title       |    author
    --------------------+--------------
    Turings Cathedral   | George Dyson
    Walkaway            | Cory Doctorow
    Consider Phlebas    | Iain M. Banks
    The Player of Games | Iain M. Banks
    Use of Weapons      | Iain M. Banks
    Surface Detail      | Iain M. Banks
    (6 rows)

    readinglist=# SELECT title, author FROM books WHERE id < 3;
        title         |    author
    ------------------+--------------
    Turings Cathedral | George Dyson
    Walkaway          | Cory Doctorow
    (2 rows)

    readinglist=# SELECT title, pages FROM books WHERE author = 'Iain M. Banks' AND id > 4;
        title      | pages
    ---------------+------
    Use of Weapons |   411
    Surface Detail |   627
    (2 rows)

----ƒ----

Using functions (such as average) to define specific selections...

    readinglist=# SELECT AVG(pages) FROM books;
            avg
    --------------------
    448.5000000000000000
    (1 row)

---

### 15:54 ~ Finitamos

Calling it now because I'm going out to dinner with some famalamabambam.

Hasta Luego, Amigo!
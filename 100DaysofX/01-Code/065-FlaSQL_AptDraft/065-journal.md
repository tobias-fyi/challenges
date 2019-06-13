# 2019-05-07 | #100DaysofCode

## Day 065 / 100

- [2019-05-07 | #100DaysofCode](#2019-05-07--100daysofcode)
  - [Day 065 / 100](#day-065--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-05)](#projectloxocache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-07)](#sessionsojourn2019-05-07)
    - [Loxocache](#loxocache)
    - [15:35 ~ Session.INDEX](#1535--sessionindex)
    - [15:36 ~ this.INDEX](#1536--thisindex)
    - [15:41 ~ Nested Queries](#1541--nested-queries)
    - [15:45 ~ SQL Injection](#1545--sql-injection)
    - [16:04 ~ Race Conditions / SQL Transactions](#1604--race-conditions--sql-transactions)
    - [16:09 ~ SQLAlchemy](#1609--sqlalchemy)
      - [TASK√065 : Connect to Postgres using SQLAlchemy](#task065--connect-to-postgres-using-sqlalchemy)
      - [TASK√065 : Read data from Postgres db using SQLAlchemy](#task065--read-data-from-postgres-db-using-sqlalchemy)
    - [16:44 ~ Importing Into DB](#1644--importing-into-db)
      - [TASK√065 : Write data to Postgres db using SQLAlchemy](#task065--write-data-to-postgres-db-using-sqlalchemy)
    - [17:11 ~ MorenviroVars](#1711--morenvirovars)
      - [TASK√065 : Export EnviroVars on a per-project basis](#task065--export-envirovars-on-a-per-project-basis)
    - [17:34 ~ œ.this.NEXT](#1734--œthisnext)

---

## SELECT * FROM Project

### Project.abstract

    GOAL_AptDraft : Reading journal / Book review application with Flask / Postgres  

### Project.loxocache(2019-05)

- Project Symbol
  - æ | å | ā
  - Æ | Å | Ā
  - œ | … | Æ
  - √ | ∫ | Â
  - ¿

--------@--------

## SELECT * FROM Session

### Session.abstract

    GOAL_066 : Workon AptDraft  

#### Session.cache

- Virtualenvwrapper Docs [Tips / Tricks](https://virtualenvwrapper.readthedocs.io/en/latest/tips.html#clean-up-environments-on-exit)

---

## Session.sojourn(2019-05-07)

### Loxocache

    TASK√065 : Connect to Postgres using SQLAlchemy  
    TASK√065 : Read data from Postgres db using SQLAlchemy  
    TASK√065 : Write data to Postgres db using SQLAlchemy  
    TASK√065 : Export EnviroVars on a per-project basis  

--------@--------

### 15:35 ~ Session.INDEX

Getting it going with some hot + heavy SQL INDEX action.

---

### 15:36 ~ this.INDEX

`CREATE INDEX` on a table.column speeds up the SELECT based on that column, but has the tradeoff of being more difficult / slower to INSERT or UPDATE.

---

### 15:41 ~ Nested Queries

Querying multiple tables where one query depends on the result of another.

    library=# SELECT * FROM authors WHERE id IN (
    library(#     SELECT author_id FROM books GROUP BY author_id HAVING COUNT(*) > 1
    library(# );
    id |  first_name  | last_name
    ---+--------------+-----------
    3  | Iain M.      | Banks
    4  | Arthur C.    | Clarke
    5  | George R. R. | Martin
    6  | James S. A.  | Corey
    7  | Robert A.    | Heinlein
    9  | J. R. R.     | Tolkein
    11 | Sam          | Harris
    (7 rows)

---

### 15:45 ~ SQL Injection

When the query to login isn't escaped properly, hackers can get access to the row in the database containing a user's login information.

    Username: hacker
    Password: 1' OR '1' = '1

    SELECT * FROM users
        WHERE (username = 'hacker')
        AND (password = '1' OR '1' = '1');

---

### 16:04 ~ Race Conditions / SQL Transactions

Example in the lecture is two simultaneous transactions against one bank account where one transaction does not complete before the next one starts, leading to an incorrect balance.

    BEGIN
    ...
    COMMIT

To prevent this, the queries are put into a SQL Transaction, using the syntax above.

---

### 16:09 ~ SQLAlchemy

#### TASK√065 : Connect to Postgres using SQLAlchemy  

    ╭─ Fineyedesign » tobiasfyi » ..hop/Fineyedesign »  master ● ?          19.05.08 ∫ 16:20:08
    ╰─ python
    Python 3.7.3 (default, Apr 18 2019, 18:36:52)
    ...
    >>> import sqlalchemy
    >>>

Installed iPython into the CS50 venv to be able to use the python shell...*in style*.

    ─ CS50 » tobiasfyi » ~/workshop/CS50                        19.05.08 ∫ 16:21:22
    ╰─ pip install ipython
    Collecting ipython
    ...
    Successfully installed appnope-0.1.0 backcall-0.1.0 decorator-4.4.0 ipython-7.5.0 ipython-genutils-0.2.0 jedi-0.13.3 parso-0.4.0 pexpect-4.7.0 pickleshare-0.7.5 prompt-toolkit-2.0.9 ptyprocess-0.6.0 pygments-2.4.0 traitlets-4.3.2 wcwidth-0.1.7

And now running the python shell is much nicer...

    ╭─ CS50 » tobiasfyi » ~/workshop/CS50                       19.05.08 ∫ 16:24:24
    ╰─ ipython
    Python 3.7.3 (default, Apr 18 2019, 18:36:52)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: import sqlalchemy

    In [2]:

Sweet...now time to figure out how to connect to my postgres db using sqlalchemy...

According to the docs, the following is the connect string format when using psycopg2:

    postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]

Using psycopg2 means I need to pip install it into ye ol' venv:

    ╭─ CS50 » tobiasfyi » ~/workshop/CS50                       19.05.08 ∫ 16:30:13
    ╰─ pip install psycopg2-binary
    Collecting psycopg2-binary
    ...
    Successfully installed psycopg2-binary-2.8.2

Here's the connection string for my library db:

    postgresql+psycopg2://librarian:l1br4r14n@localhost:5432/library

Let's see if it works...

#### TASK√065 : Read data from Postgres db using SQLAlchemy  

After some jiggling I got it to work! I didn't have to include the +psycopg2 portion of the connection string. Once I removed that it worked just fine...

    ╭─ CS50 » tobiasfyi » ..QL/07-sqlalchemy                        19.05.08 ∫ 16:41:03
    ╰─ python list.py
    Lying (Philosophy) by Sam Harris, published in 2013
    Nemesis Games (Science fiction) by James S. A. Corey, published in 2015
    A Game of Thrones (Fantasy) by George R. R. Martin, published in 1996
    2001: A Space Odyssey (Science fiction) by Arthur C. Clarke, published in 1968
    Consider Phlebas (Science fiction) by Iain M. Banks, published in 1988
    ...

Which is returned by running the following code (incomplete)...

    engine = create_engine(os.getenv("DATABASE_URL"))
    db = scoped_session(sessionmaker(bind=engine))

    def main():
        books = db.execute(
            "SELECT title, subgenre, pub_year, first_name, last_name FROM books JOIN authors ON authors.id = books.author_id JOIN subgenres ON subgenres.id = books.subgenre_id"
        ).fetchall()
        for book in books:
            print(
                f"{book.title} ({book.subgenre}) by {book.first_name} {book.last_name}, published in {book.pub_year}"
            )

    if __name__ == "__main__":
        main()

---

### 16:44 ~ Importing Into DB

#### TASK√065 : Write data to Postgres db using SQLAlchemy  

Created a .csv file to use for import practice...

> books.csv

After a little more jagmaddling, I got it to import!

    ╭─ CS50 » tobiasfyi » ..QL/07-sqlalchemy                        19.05.08 ∫ 17:09:04
    ╰─ python import.py
    Added The Color of Magic to the library.
    Added The Light Fantastic to the library.
    Added Django For Beginners to the library.

---

### 17:11 ~ MorenviroVars

I wanted to try using a .env file to export the DATABASE_URL...so let's do it!

#### TASK√065 : Export EnviroVars on a per-project basis  

I guess it worked?

    ╭─ CS50 » tobiasfyi » ..QL/07-sqlalchemy                        19.05.08 ∫ 17:14:04
    ╰─ source ~/workshop/CS50/.env

    ╭─ CS50 » tobiasfyi » ..QL/07-sqlalchemy                        19.05.08 ∫ 17:14:13
    ╰─ echo $DATABASE_URL
    postgresql://librarian:l1br4r14n@localhost:5432/library

The only thing left is to figure out how to have that .env file sourced in terminal every time I work on that project. Unless...maybe my current workflow makes that easy?

It didn't happen automatically, so I'll have to look up how to have terminal auto-source from the .env file whenever the project is activated via the `workon` command.

[Maybe if I put the EnviroVar](https://virtualenvwrapper.readthedocs.io/en/latest/tips.html) in the $WORKON_HOME/postactivate file?

This looks promising!

> ~/.vega/CS50/bin/postactivate

    #!/bin/zsh
    # This hook is sourced after this virtualenv is activated.

    # ---- Flask ----#
    export FLASK_DEBUG=1
    export DATABASE_URL="postgresql://librarian:l1br4r14n@localhost:5432/library"

Now time to test it out...and it worked!

    ╭─ tobiasfyi » ~/.vega/CS50/bin                                                19.05.08 ∫ 17:22:33
    ╰─ workon CS50

    ╭─ CS50 » tobiasfyi » ~/workshop/CS50                                          19.05.08 ∫ 17:22:43
    ╰─ echo $DATABASE_URL
    postgresql://librarian:l1br4r14n@localhost:5432/library

Fuck ya I've been trying to figure that out since I started down the path of redefining my workflow. That's real nice...

Last thing—I should probably unset the envirovar in the postdeactivate script as well. I'll try accessing the envirovar after deactivating to see if it's necessary.

    ╭─ CS50 » tobiasfyi » ~/workshop/CS50                         19.05.08 ∫ 17:25:00
    ╰─ deactivate

    ╭─ tobiasfyi » ~/workshop/CS50                                19.05.08 ∫ 17:25:04
    ╰─ echo $DATABASE_URL
    postgresql://librarian:l1br4r14n@localhost:5432/library

YUUUPP! That's what I thought. Starting to understand this stuff now!

> ~/.vega/CS50/bin/postdeactivate

    #!/bin/zsh
    # This hook is sourced after this virtualenv is deactivated.

    # ---- Flask ---- #
    unset FLASK_DEBUG
    unset DATABASE_URL

Now, let's try it again to make sure it worked...stay tuned for the results!

    ╭─ tobiasfyi » ~/workshop/CS50                                19.05.08 ∫ 17:30:34
    ╰─ workon CS50

    ╭─ CS50 » tobiasfyi » ~/workshop/CS50                         19.05.08 ∫ 17:30:40
    ╰─ echo $DATABASE_URL
    postgresql://librarian:l1br4r14n@localhost:5432/library

    ╭─ CS50 » tobiasfyi » ~/workshop/CS50                         19.05.08 ∫ 17:30:48
    ╰─ deactivate

    ╭─ tobiasfyi » ~/workshop/CS50                                19.05.08 ∫ 17:30:51
    ╰─ echo $DATABASE_URL


    ╭─ tobiasfyi » ~/workshop/CS50                                19.05.08 ∫ 17:30:52
    ╰─ echo $SUCC_YESS
    No...
    More...
    Chinese...
    LAUNDRY!

And BOOM! ${SUCC_YESS}...

That is really exciting...I've been wanting to have that all figured out for weeks.

Aaaaand I'm almost done with the SQL lecture.

---

### 17:34 ~ œ.this.NEXT

It'll hafta wait until next session. Though it *will* happen next session...

Finish the lecture, I mean.

Hasta la próxima vez, amiga!
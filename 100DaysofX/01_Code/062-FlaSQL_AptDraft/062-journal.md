# 2019-05-04 | #100DaysofCode

## Day 062 / 100

- [2019-05-04 | #100DaysofCode](#2019-05-04--100daysofcode)
  - [Day 062 / 100](#day-062--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-05)](#projectloxocache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-04)](#sessionsojourn2019-05-04)
    - [Loxocache](#loxocache)
    - [20:24 ~ BookSQL](#2024--booksql)
    - [21:02 ~ Fresh Churns](#2102--fresh-churns)
    - [21:56 ~ Book.dinit](#2156--bookdinit)

---

## SELECT * FROM Project

### Project.abstract

    GOAL__: Book review + reading journal application using Flask / Postgres  

### Project.loxocache(2019-05)

- pass

--------ƒ--------

## SELECT * FROM Session

### Session.abstract

    GOAL_062 : Complete the SQL lecture + workon AptDraft  

#### Session.cache

- [Tron Legacy Soundtrack](https://www.youtube.com/watch?v=m4cgLL8JaVI)
  - And the [Reconfigured version](https://youtu.be/K2B4CYT7FNg)

---

## Session.sojourn(2019-05-04)

### Loxocache

--------ƒ--------

### 20:24 ~ BookSQL

I still need to finish up the SQL lecture...so here we go!

    readinglist=# SELECT author, COUNT(*) FROM books GROUP BY author;
        author     | count
    ---------------+-------
    Cory Doctorow |     1
    Iain M. Banks |     4
    George Dyson  |     1
    (3 rows)

As I had mentioned a few sessions back when starting SQL, it makes sense to separate out the authors into their own table...

    readinglist=# CREATE TABLE authors (
    readinglist(#     id SERIAL PRIMARY KEY,
    readinglist(#     first_name VARCHAR NOT NULL,
    readinglist(#     last_name VARCHAR NOT NULL,
    readinglist(#     books_id INTEGER REFERENCES books
    readinglist(# );
    CREATE TABLE

I just realized that this isn't really a good way to go about this. As far as I can tell right now, this is a many to one relationship between the authors and books, respectively. That's the opposite of what I want.

I need each book to only have one author while allowing each author to have references to many books. This means I should really have the foreignkey in the books table referencing the authors table.

---

### 21:02 ~ Fresh Churns

Instead of modifying the current setup to accomodate the change, I'm going to start fresh with a new database to practice the routine once more.

First, created the new database and superuser (just coz)...

    postgres=# CREATE DATABASE library;
    CREATE DATABASE
    postgres=# CREATE USER librarian WITH SUPERUSER PASSWORD 'l1br4r14n';
    CREATE ROLE
    postgres=# \c library librarian
    You are now connected to database "library" as user "librarian".

Then create separate tables for authors, books, genres, and subgenres (why subgenres in their own table?...just coz)...

    library=# CREATE TABLE authors (
    library(#     id SERIAL   PRIMARY KEY,
    library(#     first_name  VARCHAR NOT NULL,
    library(#     last_name   VARCHAR NOT NULL
    library(# );
    CREATE TABLE
    library=# CREATE TABLE genres (
    library(#     id SERIAL   PRIMARY KEY,
    library(#     genre       VARCHAR NOT NULL
    library(# );
    CREATE TABLE
    library=# CREATE TABLE subgenres (
    library(#     id SERIAL   PRIMARY KEY,
    library(#     subgenre    VARCHAR NOT NULL,
    library(#     genre_id    INTEGER REFERENCES genres
    library(# );
    CREATE TABLE
    library=# CREATE TABLE books (
    library(#     id SERIAL   PRIMARY KEY,
    library(#     title       VARCHAR NOT NULL,
    library(#     author_id   INTEGER REFERENCES authors,
    library(#     genre_id    INTEGER REFERENCES genres,
    library(#     subgenre_id INTEGER REFERENCES subgenres,
    library(#     pub_year    INTEGER NOT NULL,
    library(#     pages       INTEGER NULL
    library(# );
    CREATE TABLE

Third, INSERTion of some data to manipulate...

    # INSERT authors
    library=# SELECT * FROM authors;
    id |  first_name  | last_name
    ---+--------------+----------
    1  | George       | Dyson
    2  | Cory         | Doctorow
    3  | Iain M.      | Banks
    4  | Arthur C.    | Clarke
    5  | George R. R. | Martin
    6  | James S. A.  | Corey
    7  | Robert A.    | Heinlein
    8  | Scott        | Adams
    9  | J. R. R.     | Tolkein
    10 | Philip K.    | Dick
    11 | Sam          | Harris
    (11 rows)

    # INSERT genres
    library=# SELECT * FROM genres;
    id |   genre
    ---+-----------
    1  | Fiction
    2  | Nonfiction
    3  | Technical
    (3 rows)

Yes, I know having genres and subgenres in separate tables is overkill. Maybe it isn't though?...  
And yes, technically technical books are nonfiction. I just wanted another genre to INSERT.

I just realized that a good reason to have the subgenres table separate would be to have the ability to assign multiple subgenres to each book. Time for some ALTERation...

    library=# ALTER TABLE books ADD COLUMN subgenre2_id INTEGER REFERENCES subgenres;
    ALTER TABLE

I added another author that I forgot about earlier but I've been reading on and off for a year or two:

    ...
    library-# VALUES (
    library(#     'Terry',
    library(#     'Pratchett'
    library(# );
    INSERT 0 1

And another one, just so I have at least one technical book...

    ...
    library-# VALUES (
    library(#     'William',
    library(#     'Vincent'
    library(# );

I also just realized that I've got some reading up to do about many-to-many relationships as there are other relationships that I think should be as such. For example, the subgenre `humor` could be fiction or nonfiction.

    library=# SELECT * FROM subgenres;
    id |    subgenre     | genre_id
    ---+-----------------+---------
    1  | Science fiction |        1
    2  | Fantasy         |        1
    3  | Swashbuckler    |        1
    4  | Humor           |        1
    5  | Mystery         |        1
    6  | Biography       |        2
    7  | Self-help       |        2
    8  | Psychology      |        2
    9  | Philosophy      |        2
    10 | History         |        2
    11 | Tutorial        |        3
    (11 rows)

---

### 21:56 ~ Book.dinit

I'll have to leave the INSERT books until next time, as I have other responsibilities to attend to.

Hasta biblioteca, amigas!

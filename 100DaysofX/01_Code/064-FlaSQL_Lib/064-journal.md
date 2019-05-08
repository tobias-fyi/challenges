# 2019-05-06 | #100DaysofCode

## Day 064 / 100

- [2019-05-06 | #100DaysofCode](#2019-05-06--100daysofcode)
  - [Day 064 / 100](#day-064--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-05)](#projectloxocache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-06)](#sessionsojourn2019-05-06)
    - [Loxocache](#loxocache)
    - [14:50 ~ findinit](#1450--findinit)
    - [14:55 ~ FlaSQL.init](#1455--flasqlinit)
    - [14:58 ~ JOIN Me BB](#1458--join-me-bb)
    - [15:29 ~ More JOINs](#1529--more-joins)
    - [15:31 ~ INDEX.de-init](#1531--indexde-init)

---

## SELECT * FROM Project

### Project.abstract

    GOAL_AptDraft : Reading journal / Book review application with Flask / Postgres  

### Project.loxocache(2019-05)

- pass

--------@--------

## SELECT * FROM Session

### Session.abstract

    GOAL_066 : Workon AptDraft  

#### Session.cache

- [Corey Schafer's tutorial](https://youtu.be/KCVaNb_zOuw) on `find`

---

## Session.sojourn(2019-05-06)

### Loxocache

--------@--------

### 14:50 ~ findinit

Find is a pretty sweet little command.

    ╭─ Fineyedesign » tobiasfyi » ../2019-05 »  master ● ?     19.05.08 ∫ 12:00:31
    ╰─ find . -type f
    ./19-05-08-twos_dae.md
    ./19-05-02-edexxx_thurs.md
    ./19-05-04-caturdae.md
    ./19-05-03-PYR_freeday.md
    ./19-05-05-cinco_sundae.md
    ./assets/smyppets.gif
    ./assets/coolFont.png
    ./19-05-06-signmondae.md
    ./project0.md

I removed four of the ellipses in the path segment of the prompt. That says to me I need to modify it a bit more. I changed the shorten strategy back to what it was before last session, but reduced the characters to shorten to 16 (rather than 24)...

> ~/.zshrc

    POWERLEVEL9K_SHORTEN_DIR_LENGTH=16
    POWERLEVEL9K_SHORTEN_DELIMITER=".."
    POWERLEVEL9K_SHORTEN_STRATEGY="truncate_absolute_chars"

---

### 14:55 ~ FlaSQL.init

Alriiiiight finally got a bunch of books into the library database...

    library=# SELECT * FROM books;
    id |             title                | author_id | genre_id | sub_id | pub_yr | pages | sub2_id
    ---+----------------------------------+-----------+----------+--------+--------+-------+--------
    1  | Lying                            |        11 |        2 |      9 |   2013 |   108 |     8
    2  | Free Will                        |        11 |        2 |      9 |   2012 |    97 |     8
    3  | Waking Up                        |        11 |        2 |      9 |   2014 |   256 |     8
    4  | The Return of the King           |         9 |        1 |      2 |   1955 |   490 |    10
    5  | The Two Towers                   |         9 |        1 |      2 |   1954 |   322 |    10
    6  | The Fellowship of the Ring       |         9 |        1 |      2 |   1954 |   398 |    10
    7  | The Hobbit                       |         9 |        1 |      2 |   1937 |   366 |    10
    8  | How to Fail at Almost ...        |         8 |        2 |      6 |   2013 |   248 |     7
    9  | Citizen of the Galaxy            |         7 |        1 |      1 |   1957 |   272 |     4
    10 | The Moon is a Harsh Mistress     |         7 |        1 |      1 |   1966 |   288 |     4
    11 | Starship Troopers                |         7 |        1 |      1 |   1959 |   335 |     4
    12 | Starship Troopers                |         7 |        1 |      1 |   1959 |   335 |     4
    13 | Stranger in a Strange Land       |         7 |        1 |      1 |   1961 |   528 |     4
    14 | Nemesis Games                    |         6 |        1 |      1 |   2015 |   536 |     5
    15 | Cibola Burn                      |         6 |        1 |      1 |   2014 |   581 |     5
    16 | Abaddons Gate                    |         6 |        1 |      1 |   2013 |   539 |     5
    17 | Calibans War                     |         6 |        1 |      1 |   2012 |   595 |     5
    18 | Leviathan Wakes                  |         6 |        1 |      1 |   2011 |   561 |     5
    19 | A Feast for Crows                |         5 |        1 |      2 |   2005 |  1061 |    10
    20 | A Storm of Swords                |         5 |        1 |      2 |   2000 |  1177 |    10
    21 | A Clash of Kings                 |         5 |        1 |      2 |   1998 |   969 |    10
    22 | A Game of Thrones                |         5 |        1 |      2 |   1996 |   848 |    10
    23 | Rama II                          |         4 |        1 |      1 |   1989 |   480 |     1
    24 | Rendesvous With Rama             |         4 |        1 |      1 |   1973 |   243 |     1
    25 | 2001: A Space Odyssey            |         4 |        1 |      1 |   1968 |   297 |     1
    26 | Consider Phlebas                 |         3 |        1 |      1 |   1988 |   471 |     1
    27 | The Player of Games              |         3 |        1 |      1 |   1988 |   293 |     1
    28 | Use of Weapons                   |         3 |        1 |      1 |   1990 |   411 |     1
    29 | Surface Detail                   |         3 |        1 |      1 |   2010 |   627 |     1
    30 | Walkaway                         |         2 |        1 |      1 |   2017 |   384 |     9
    31 | Turings Cathedral                |         1 |        2 |      6 |   2012 |   505 |    10
    (31 rows)

Probably could've saved a ton of time on that by doing it some other way that didn't require mostly typing in by hand. Oh well...

---

### 14:58 ~ JOIN Me BB

    library=# SELECT title, first_name, last_name FROM books JOIN authors ON authors.id = books.author_id;
                        title                        |  first_name  | last_name
    ----------------------------------------------------+--------------+-----------
    Lying                                              | Sam          | Harris
    Free Will                                          | Sam          | Harris
    Waking Up                                          | Sam          | Harris
    The Return of the King                             | J. R. R.     | Tolkein
    The Two Towers                                     | J. R. R.     | Tolkein
    The Fellowship of the Ring                         | J. R. R.     | Tolkein
    The Hobbit                                         | J. R. R.     | Tolkein
    How to Fail at Almost Everything and Still Win Big | Scott        | Adams

That Scott Adams title is making this too complicated with formatting for my notes. I'm going to shorten the title a little bit.

    library=# UPDATE books SET title = 'How to Fail at...' WHERE id = 8;
    UPDATE 1

Ok now for that sweet, sweet JOIN...

    library=# SELECT title, first_name, last_name FROM books JOIN authors ON authors.id = books.author_id LIMIT 10;
                title            | first_name | last_name
    -----------------------------+------------+-----------
    Lying                        | Sam        | Harris
    Free Will                    | Sam        | Harris
    Waking Up                    | Sam        | Harris
    The Return of the King       | J. R. R.   | Tolkein
    The Two Towers               | J. R. R.   | Tolkein
    The Fellowship of the Ring   | J. R. R.   | Tolkein
    The Hobbit                   | J. R. R.   | Tolkein
    Citizen of the Galaxy        | Robert A.  | Heinlein
    The Moon is a Harsh Mistress | Robert A.  | Heinlein
    Starship Troopers            | Robert A.  | Heinlein
    (10 rows)

---

### 15:29 ~ More JOINs

Attempted to join more than one table to the main table and it worked!

    library=# SELECT title, first_name, last_name, genre FROM books JOIN authors ON authors.id = books.author_id JOIN genres ON genres.id = books.genre_id LIMIT 5;
            title          | first_name | last_name |   genre
    -----------------------+------------+-----------+------------
    Lying                  | Sam        | Harris    | Nonfiction
    Free Will              | Sam        | Harris    | Nonfiction
    Waking Up              | Sam        | Harris    | Nonfiction
    The Return of the King | J. R. R.   | Tolkein   | Fiction
    The Two Towers         | J. R. R.   | Tolkein   | Fiction
    (5 rows)

Other types of JOIN - namely LEFT JOIN and RIGHT JOIN...

    library=# SELECT title, first_name, last_name, genre FROM books RIGHT JOIN authors ON authors.id = books.author_id RIGHT JOIN genres ON genres.id = books.genre_id LIMIT 5;
            title        | first_name | last_name |  genre
    ---------------------+------------+-----------+---------
    Walkaway            | Cory       | Doctorow  | Fiction
    Surface Detail      | Iain M.    | Banks     | Fiction
    Use of Weapons      | Iain M.    | Banks     | Fiction
    The Player of Games | Iain M.    | Banks     | Fiction
    Consider Phlebas    | Iain M.    | Banks     | Fiction
    (5 rows)

---

### 15:31 ~ INDEX.de-init

Spent a long time writing the SQL, so didn't get that much farther on the lecture. That's ok, there's always next time!

Hasta Nextime, Amiga!

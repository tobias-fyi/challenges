# 2019-05-05 | #100DaysofCode

## Day 063 / 100

---

## SELECT * FROM Project

### Project.abstract

    GOAL_AptDraft : Book review / reading journal application with Flask and Postgres  

### Project.loxocache(2019-05)

    TASK__ : Collect tags from other documents

--------∫--------

## SELECT * FROM Session

### Session.abstract

    GOAL_063 : Workon  

#### Session.cache

- pass

---

## Session.sojourn(2019-05-05)

### Loxocache

--------∫--------

### 21:48 ~ FlaSQL.init

    readinglist=# SELECT SUM(pages) FROM books;
    sum
    ----
    2691
    (1 row)

    readinglist=# SELECT AVG(pages) FROM books WHERE author = 'Iain M. Banks';
            avg
    ----------------------
    450.5000000000000000
    (1 row)

    readinglist=# SELECT COUNT(*) FROM books WHERE author = 'Iain M. Banks';
    count
    -------
        4
    (1 row)

---

### 21:54 ~ IN, UPDATE, and Others

    readinglist=# SELECT * FROM books WHERE title LIKE '%t%';
    id |       title       |    author     |   genre    | subgenre  | pub_year | pages
    ---+-------------------+---------------+------------+-----------+----------+------
    1  | Turings Cathedral | George Dyson  | Nonfiction | Biography |     2012 |   505
    6  | Surface Detail    | Iain M. Banks | Fiction    | Sci-fi    |     2010 |   627
    (2 rows)

    readinglist=# SELECT * FROM books WHERE author = 'Iain M. Banks' ORDER BY pages ASC;
    id |        title        |    author     |  genre  | subgenre | pub_year | pages
    ---+---------------------+---------------+---------+----------+----------+------
    4  | The Player of Games | Iain M. Banks | Fiction | Sci-fi   |     1988 |   293
    5  | Use of Weapons      | Iain M. Banks | Fiction | Sci-fi   |     1990 |   411
    3  | Consider Phlebas    | Iain M. Banks | Fiction | Sci-fi   |     1988 |   471
    6  | Surface Detail      | Iain M. Banks | Fiction | Sci-fi   |     2010 |   627
    (4 rows)

    readinglist=# SELECT * FROM books WHERE author = 'Iain M. Banks' ORDER BY pages ASC LIMIT 2;
    id |        title        |    author     |  genre  | subgenre | pub_year | pages
    ---+---------------------+---------------+---------+----------+----------+------
    4  | The Player of Games | Iain M. Banks | Fiction | Sci-fi   |     1988 |   293
    5  | Use of Weapons      | Iain M. Banks | Fiction | Sci-fi   |     1990 |   411
    (2 rows)


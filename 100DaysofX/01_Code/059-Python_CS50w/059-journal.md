# 2019-05-01 | #100DaysofCode

## Day 59/100

- [2019-05-01 | #100DaysofCode](#2019-05-01--100daysofcode)
  - [Day 59/100](#day-59100)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.cache(2019-05)](#projectcache2019-05)
  - [---- SELECT * FROM Session(2019-05-01) ----](#-----select--from-session2019-05-01-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn](#sessionsojourn)
    - [20:35 -+- Session.init](#2035----sessioninit)
    - [21:11 ~ AptDraft.com](#2111--aptdraftcom)
    - [21:36 ~ FlaskDraft Inheritance](#2136--flaskdraft-inheritance)
    - [21:47 ~ Onupwards](#2147--onupwards)

## ---- SELECT * FROM Project ----

### Project.abstract

    GOAL_CS50w : Create a book review application with Flask / Postgres  

### Project.cache(2019-05)

--------∫--------

## ---- SELECT * FROM Session(2019-05-01) ----

### Session.abstract

    GOAL_2019-05-04 : Finish the Flask lecture and get some practice by building  

### Session.cache

---

## Session.sojourn

--------∫--------

### 20:35 -+- Session.init

More practice and learning with Flask.

Went over the basics of jinja and templates.

---

### 21:11 ~ AptDraft.com

I decided to utilize these lessons to the fullest by building little bits and pieces of project 1 as I follow along with the lectures.

The app will not only be a book review app...it will also be a place to keep a reading journal. That way users can keep notes on the books as they're reading them, which can be easily converted / summarized into book reviews that can be published to the site for others to read.

I purchased yet another domain, as it is one that I think is way too nice of a name: `AptDraft.com`

This will allow me to get the most out of this time spent learning Flask, as I will be building an application that I will actually put into production. That motivates me a lot to make it good, and to spend time on it in general.

---

### 21:36 ~ FlaskDraft Inheritance

One thing that's been a little difficult for me to figure out is how to write jinja code such that the navbar nav-items automatically make themselves active according to what page is active.

With previous projects I did a more brute force method where I used a block, but I know there is a better way than that.

I found [this page that has a section on it](http://jinja.pocoo.org/docs/2.10/tricks/), though the documentation doesn't go into much depth on anything really.

Yesss! Thanks to a [nice and simple response on StackOverflow](https://stackoverflow.com/questions/18600031/changing-the-active-class-of-a-link-with-the-twitter-bootstrap-css-in-python-fla#answer-43071349), I got it to work. I really like this method more than what is in the jinja docs.

    <li class="nav-item {{ 'active' if active_page == 'review' else '' }}">
        <a class="nav-link" href="{{ url_for('review') }}">Review</a>
    </li>

So simple and clean. Sometimes things don't make sense until looked at from a certain perspective. This perspective worked for me when the other did not.

---

### 21:47 ~ Onupwards

That about does it for this session.

Hasta in the next session, amiga!
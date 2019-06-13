# 2019-05-26 | #100DaysofCode

    GOAL-05-26 ~ Start building Iterum / Learn web scraping with Python  

## Day 084/100 | 146/365

- [2019-05-26 | #100DaysofCode](#2019-05-26--100daysofcode)
  - [Day 084/100 | 146/365](#day-084100--146365)

---- Notes ----

    CUE-146 : AskPhilip - Try..except..else..finally indentations  

    IDEA-146 : Python package combining my venv workflow + Pipenv  

---- Resources ----

- [Python 3 Docs - Error Handling](https://docs.python.org/3/tutorial/errors.html)
- [RealPython article on exceptions](https://realpython.com/python-exceptions/)

---- Sojourn ----

### 08:52 -+- Session.init

I knew I was forgetting something...my computer charger.

I guess I'll just have to be conservative with what I do on this machine and when I let it sleep. I could go home during lunch to get it, but my motivation to do that will depend on how low my battery gets by then and what the weather is like outside. If it's nice, I'll probably prefer to take a walk during my lunch hour instead of drive to my house and back.

---

### 09:16 ~ Initeresante

I'm going to start writing the script to scrape the words off the Phrontistery.

Just to warm up my brain.

I believe I have a couple of ebooks about web scraping. If I can do it in Python that would be pretty sweet. Otherwise I'll probably just poke around in the JavaScript dev console.

---

## Web Scraping with Python

----ƒ----

### 09:22 ~ My First Web Scraper

Well...that was rather easy.

```python
from urllib.request import urlopen
html = urlopen("http://phrontistery.info/latin.html")
print(html.read())
```

The three (very) simple lines of code above resulted in printing out the entire html contents of the page.

    ╭─ Fineyedesign » tobiasfyi » ..hon/Web_Scraping »  master ● ?     19.05.26 ∫ 09:38:04
    ╰─ python scrape1.py
    b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<title>Word List: Latin Adverbs and Prepositions in English</title>\r\n<meta name=description content="Definitions of Latin adverbs and prepositions borrowed into English">
    ...
    Links to this page may be made without permission.  </p>\r\n\r\n<div>\r\n<a href="#top">Top of page</a><br>\r\n<a href="index.html">Return to the Phrontistery</a>
    ...

Nice! This is going to be fun. Not to mention valuable to be able to do efficiently and effectively.

That command literally just reads the entirety of the contents of the html file that the URL points to. I could figure out how to pull the words and definitions somewhat easily just from that raw data. However, I bet there are tons of better methods of picking out specific data. This is literally the very first example in the book.

---

### 09:45 ~ Interlude for "Real" Work

Tom is having me do some graphic work. So I'll have to take a break from this for a bit. This is good motivation to get the graphics stuff done as quickly as possible.

---

### 10:48 ~ Not Quite Ubique

Ubique: everywhere.

Not quite done with the pyramid work but I'm waiting on some things so I'll do this while I wait.

#### Beauterum Soup

Named after a Lewis Carroll poem of the same name which appears in Alice in Wonderland.

I'm going to create a new project in ~/workshop to put this stuff, as now that beautiful soup is going to be used, I'd like to have a separate venv to install the libraries into. Plus it will help keep things a little organized from the get-go.

Iterum: again; afresh; anew.

    ╭─ tobiasfyi » ~/workshop                               19.05.26 ∫ 11:02:18
    ╰─ mkproject iterum
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/iterum/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/iterum/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/iterum/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/iterum/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/iterum/bin/get_env_details
    Creating /Users/Tobias/workshop/iterum
    Setting project for iterum to /Users/Tobias/workshop/iterum

    ╭─ iterum » tobiasfyi » ~/workshop/iterum                               19.05.26 ∫ 11:05:26
    ╰─ pip install beautifulsoup4
    Collecting beautifulsoup4
    ...
    Successfully installed beautifulsoup4-4.7.1 soupsieve-1.9.1

---

### 11:26 ~ Dev Dependencies

    ╭─ iterum » tobiasfyi » ~/workshop/iterum                                       19.05.26 ∫ 11:31:45
    ╰─ pip install black
    ...
    Successfully installed appdirs-1.4.3 attrs-19.1.0 black-19.3b0 click-7.0 toml-0.10.0

    ╭─ iterum » tobiasfyi » ~/workshop/iterum                                       19.05.26 ∫ 11:31:52
    ╰─ pip install pylint
    ...
    Successfully installed astroid-2.2.5 isort-4.3.20 lazy-object-proxy-1.4.1 mccabe-0.6.1 pylint-2.3.1 six-1.12.0 typed-ast-1.3.5 wrapt-1.11.1

I just had something of an idea...what if I created a Python package that combines the best of my setup and Pipenv? I want to be able to create deterministic builds and have the Pipfile + Pipfile.lock, but I want to be able to keep my current workflow—or at least something as efficient as my current workflow.

#### IDEA-146 : Python package combining my venv workflow + Pipenv  

I also finished setting up the new vscode workspace with the black / pylint paths. I'll install any additional dependencies as I go along.

---

### 11:40 ~ Running BS4

Took me a few tries, as the code in the book isn't quite right for my version / setup. First time I ran it, I received a warning about it...

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                                      19.05.26 ∫ 11:41:29
    ╰─ python scrapebs1.py
    scrapebs1.py:6: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

    The code that caused this warning is on line 6 of the file scrapebs1.py. To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

    bs_object = BeautifulSoup(html.read())
    None

Fixed up the script...

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://phrontistery.info/latin.html")

bs_object = BeautifulSoup(html.read(), features="html.parser")
print(bs_object.head)
```

...and it worked great.

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                                      19.05.26 ∫ 11:45:57
    ╰─ python scrapebs1.py
    <head>
    <title>Word List: Latin Adverbs and Prepositions in English</title>
    <meta content="Definitions of Latin adverbs and prepositions borrowed into English" name="description"/>
    <meta content="words, word, word list, meaning, meanings, definition, definitions, dictionary, dictionaries, online dictionary, dictionary online, latin, adverb, adverbs, english to latin, latin to english, preposition, prepositions" name="keywords"/>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <link href="phron.css" rel="stylesheet" type="text/css"/>
    </head>

That's so dope! This is already fun but I can imagine how much more fun it will get.

---

### 11:58 ~ Accounting for Unreliable Connections

Added some try/except statements that will hopefully take care of the issues that may arise with the script not finding the webpage or server.

I purposefully passed in an incorrect URL to be sure that the error I'm excepting is correct. Looks like it is.

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                                      19.05.26 ∫ 11:59:49
    ╰─ python scrapebs2.py
    Traceback (most recent call last):
    ...
    File "/Users/Tobias/.pyenv/versions/3.7.3/lib/python3.7/urllib/request.py", line 649, in http_error_default
        raise HTTPError(req.full_url, code, msg, hdrs, fp)
    urllib.error.HTTPError: HTTP Error 404: Not Found

The only thing about try/except/else statements is that I don't want to have to indent every subsequent line. I'm going to see if that is the case.

#### CUE-146 : AskPhilip - Try..except..else..finally indentations  

I found the info I was looking for in the [Python 3 Docs - Error Handling](https://docs.python.org/3/tutorial/errors.html):

    The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception.

Ok good to know that it is optional. I guess the use-case is when I have code that is included in the try/except block that should run if the try clause is passed. Here's some more from that section:

    The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

I also found a [RealPython article on the subject](https://realpython.com/python-exceptions/), which didn't give me any new insight, but is good to have on hand. That reminds me that I still want to read through the [RealPython article on super()](https://realpython.com/python-super/).

Here's the web scrape code so far, not including imports:

```python
try:
    html = urlopen("http://phrontistery.info/latin.html")
except HTTPError as e:
    print(e)
else:
    if html is None:
        print("URL cannot be found")
    else:
        bs_object = BeautifulSoup(html.read(), features="html.parser")
        print(bs_object.head)
        print(bs_object.body.ul)
```

Buenos webNachos, amigos!

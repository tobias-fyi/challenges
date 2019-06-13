# 2019-05-25 | #100DaysofCode

    GOAL-05-25 ~ Productivity  

## Day 083/100 | 145/365

- [2019-05-25 | #100DaysofCode](#2019-05-25--100daysofcode)
  - [Day 083/100 | 145/365](#day-083100--145365)
    - [13:37 -+- Session.init](#1337----sessioninit)
      - [IDEA-145 : Write code that will create playlists based off of some arbitrary input](#idea-145--write-code-that-will-create-playlists-based-off-of-some-arbitrary-input)
    - [13:51 ~ Mainstay Mental Methodology](#1351--mainstay-mental-methodology)
      - [1 ≈ the Simplest Case Possible](#1--the-simplest-case-possible)
      - [CUE--083 : First make the change easy then make the easy change](#cue--083--first-make-the-change-easy-then-make-the-easy-change)
      - [2 ≈ Test-Driven Design + Productivity](#2--test-driven-design--productivity)
      - [3+ ≈ TBD](#3--tbd)
    - [14:30 ~ Resource Me Repoussé](#1430--resource-me-repoussé)
      - [CUE-Motif : Look for books + courses + tutorials on ecommerce + TDD](#cue-motif--look-for-books--courses--tutorials-on-ecommerce--tdd)
      - [IDEA-146 : Record internal tutorials](#idea-146--record-internal-tutorials)
    - [14:45 ~ Neophiliac](#1445--neophiliac)
    - [15:15 ~ Python Click Strings](#1515--python-click-strings)
    - [16:04 ~ Python Class Variables](#1604--python-class-variables)

---- Tasks ----



---- Notes ----

    IDEA-145 : Write code that will create playlists based off of some arbitrary input  
    CUE--083 : First make the change easy then make the easy change  
    CUE--083 : Look for books + courses + tutorials on ecommerce + TDD  

---- Resources ----

- Django CMS / Ecommerce Solutions
  - [Saleor](https://getsaleor.com/) (Ecommerce)
    - [Saleor Documentation](https://saleor.readthedocs.io/en/latest/)
  - [Oscar](http://oscarcommerce.com/) (Ecommerce)
  - [Mezzanine](http://mezzanine.jupo.org/) (CMS)
    - Similar layout to WordPress
  - [Wagtail](https://wagtail.io/) (CMS)

---- Selects ----

- [The Trail We Blaze](https://youtu.be/kVFHKUMHJ3Y)

---- Sojourn ----

### 13:37 -+- Session.init

Another idea regarding using random inputs to create interesting patterns:

#### IDEA-145 : Write code that will create playlists based off of some arbitrary input  

---

### 13:51 ~ Mainstay Mental Methodology

Mainstay: stay that extends from the main-top to the foot of the foremast.
Macroscian: one with a long shadow; one who inhabits polar regions.

I want to define my methodology for projects so I can be consistent and spend as little time as possible spinning my wheels.

#### 1 ≈ the Simplest Case Possible

#### CUE--083 : First make the change easy then make the easy change  

Like Corey Schafer's tutorials, I will start each bit of new code with the simplest case possible. Whenever I run up against a concept for which I get confused easily, I will start with the most basic instance of that concept, even if that simple instance seems too simple to worry about.

I will not continue to bash my code against the wall trying to make it work. I will try my best to first understand what it is that the code is *supposed* to do, and break it down until I get to a level that I understand.

This also goes for more high-level aspects of the build. i.e. I will not choose a more complex way of doing something unless there is a distinct, important reason to do so. The goal is to first build a working prototype; a proof-of-concept on which the complex functionality can be built.

#### 2 ≈ Test-Driven Design + Productivity

'task-driven workflow productivity': 'as with unit testing, come up with the test or task first then work toward finishing that task - then commit to the journal after it's done and all the tests pass'

In order to maximize my time/productivity ratio, I will define what it is I want to get done *before* I start working on getting it done.

#### 3+ ≈ TBD

...

---

### 14:30 ~ Resource Me Repoussé

Repoussé: raise din relief by hammering from behind or within

#### CUE-Motif : Look for books + courses + tutorials on ecommerce + TDD  

- Some Preliminary Resources
  - [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#.XMmUvDHChTA.reddit).
  - [Django REST Framework with React Tutorial](https://wsvincent.com/django-rest-framework-react-tutorial/)
  - [Django Search Tutorial](https://wsvincent.com/django-search/)
  - [Comprehensive Django CBV Guide](https://spapas.github.io/2018/03/19/comprehensive-django-cbv-guide/#a-gentle-introduction-to-cbvs)

#### IDEA-146 : Record internal tutorials  

---

### 14:45 ~ Neophiliac

Time to create the new project directory! How exciting for me, as a rather dedicated neophiliac.

    ╭─ tobiasfyi » ~                                                19.05.25 ∫ 14:44:56
    ╰─ mkproject motif
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/motif/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/motif/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/motif/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/motif/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/motif/bin/get_env_details
    Creating /Users/Tobias/workshop/motif
    Setting project for motif to /Users/Tobias/workshop/motif

---

    ╭─ motif » tobiasfyi » ~/workshop/motif                                 19.05.25 ∫ 15:05:15
    ╰─ tree -a
    .
    ├── .db-data
    ├── .gitignore
    ├── .vscode
    │   └── motif.code-workspace
    ├── 01-Docs
    │   ├── 01-Journals
    │   ├── 02-ResourceHub
    │   └── 03-Cache
    ├── 05-Assets
    │   ├── 01-Brand
    │   ├── 10-Data
    │   └── 20-Content
    ├── LICENSE
    └── README.md

    10 directories, 4 files

---

### 15:15 ~ Python Click Strings

Before I start on that, I'm finishing up the Click tool for adding strings to the beginning and end of lines in the clipboard.

I didn't have to add much to it. Just prompt for the string to add before / after each line.

    ╭─ Fineyedesign » tobiasfyi » ..rojects/stradder »  master ● ?       19.05.25 ∫ 11:34:48
    ╰─ pip install -e .
    Obtaining file:///Users/Tobias/workshop/Fineyedesign/08-Projects/stradder
    Requirement already satisfied: Click in /Users/Tobias/.vega/Fineyedesign/lib/python3.7/site-packages (from stradder==0.1) (7.0)
    Requirement already satisfied: pyperclip in /Users/Tobias/.vega/Fineyedesign/lib/python3.7/site-packages (from stradder==0.1) (1.7.0)
    Installing collected packages: stradder
    Running setup.py develop for stradder
    Successfully installed stradder

I just realized that something I might want to add to it is a strip call before adding the strings to each line. I'll try it out first.

    ╭─ Fineyedesign » tobiasfyi » ..rojects/stradder »  master ● ?       19.05.25 ∫ 11:38:04
    ╰─ stradder
    String to add before each line:
    "

    String to add after each line:
    ",

    New text has been copied back to clipboard.
    Paste at your leisure.

And the contents of my clipboard after running it...

    "Installing collected packages: stradder",
    "Running setup.py develop for stradder",
    "Successfully installed stradder",

Sweet!

I added the strip whitespace functionality. Now if I copy text with tabs I have the option of keeping or removing the tabs. For example...

    ╭─ Fineyedesign » tobiasfyi » ..rojects/stradder »  master ● ?       19.05.25 ∫ 11:53:23
    ╰─ stradder
    Strip whitespace from each line?
    [Y/n]
    n

    String to add before each line:
    "

    String to add after each line:
    ",

    New text has been copied back to clipboard.
    Paste at your leisure.

    "    Installing collected packages: stradder",
    "    Running setup.py develop for stradder",
    "    Successfully installed stradder",

and using the strip...which didn't work at first. It took me too long to realize that I had to set each line equal to its stripped self. i.e. The `.strip()` does not work in place...

```python
if strip_confirm != "n":
    lines[i] = lines[i].strip()
```

Now copying the text with tabs results in the following...

    ╭─ Fineyedesign » tobiasfyi » ..rojects/stradder »  master ● ?       19.05.25 ∫ 12:03:25
    ╰─ stradder
    Strip whitespace from each line?
    [Y/n]


    String to add before each line:
    "

    String to add after each line:
    ",
    The following text has been copied back to the clipboard.

    "Installing collected packages: stradder",
    "Running setup.py develop for stradder",
    "Successfully installed stradder",

    Paste at your leisure.

Cool. Now it works as I want it to work.

---

### 16:04 ~ Python Class Variables

Now time to get into some [Python OOP with Corey Schafer](https://youtu.be/BJ-VvGyQxho).

In true floppitty flipdurpdop fashion. I decided to just jump back into the CS50w lecture on ORMs and APIs

Hasta Flippy-Floppy, Amigos!

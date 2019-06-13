# 2019-04-06 | #034

\#100DaysofCode

---

## Today's Menu

### Main Course

    GOAL_ : Begin work on a prototype of my online resume / portfolio / store

----------∫--------

### SELECT * FROM session

#### Soundtrack

- [Avatar OST](https://youtu.be/-KefW_yjTuw) by James Horner
- Mat Zo
  - [Tracing Steps](https://soundcloud.com/matzo/sets/tracing-steps)
  - [THIS IS A MAD ZOO HOUSE EP](https://soundcloud.com/matzo/sets/this-is-a-mad-zoo-house-ep)
  - [NestHQ Minimix](https://soundcloud.com/nesthq/nest-hq-minimix-mat-zo)

#### Extras

- Django-based Content Management Systems
  - [Wagtail](https://wagtail.io/) + [StreamField](http://docs.wagtail.io/en/v2.4/topics/streamfield.html)
  - [Django CMS](https://www.django-cms.org/en/)

----∫----

- Apple Pages is my new favorite word processor / document creator (for now)
- Using different methods of finding the color scheme for a project
  - Creating hex codes from names

---

## Session Log

----------∫--------

### 16:00 -+- Sessionit

    TASK√01 : Write brief description of the project  

---

### 16:00 -+- Project tobias.fyi

I've been gathering ideas over the past couple of months for how to best represent my professional self / work on the internet, and came up with the idea for tobias.fyi.

I was stoked when that [url](https://tobias.fyi) was available, so snapped it up to use it as my central online presence. Eventually I'd like to get it to the point of being a beautiful custom-built (by me, of course) web app that showcases all of my skills in an intelligent and creative way.

I'm not going to give too much away right now, but it will have at least the following features:

- Online supplement to my resume
  - One version is presented to anyone that visits my site
  - Detailed version(s) with a dashboard-stype UI
    - Designed specifically for each prospective client / employer / partner
    - I input a job / company / industry and it will automatically create a page on the site and a hard-copy resume specifically for that company
    - Each one will be (mostly) unique, focusing on what's most important to that company or industry
    - The physical / PDf resume that I initially send out contains unique login to their tailored section of the site
    - When they log in, they are presented with an interactive version of the resume
    - They can view certain aspects of my life and work in even greater detail than what was provided on the hard-copy
- Portfolio / Online Storefront
  - Showcase my work to the general public
  - Provide a method for visitors to download / purchase my work / get in touch to hire me
- Articles / Essays / Books / Blog / Newsletter
  - The single source of truth for my written content

Other details:

- Hosted on Linode, DigitalOcean, or Heroku / AWS
- Libraries / Frameworks / Other Tech
  - Back
    - Django
    - Some sort of Django CMS
  - Front
    - HTML + CSS + SCSS
      - Bootstrap Dashboard and/or Pixelarity

As of now, I want to host the site on Linode. I've been wanting to learn how to deploy to the platform for a while and thought this would be a great opportunity for that.

I already have the [Bootstrap Dashboard](https://themes.getbootstrap.com/product/dashboard/) theme—got it for free for taking a course on Udemy. However, I'm really digging what I'm seeing on [Pixelarity](https://pixelarity.com/). It's only $19 for the entire bundle. I might buy that just to have for future projects / clients. I guess which one I use for tobias.fyi depends on if I can configure the Bootstrap theme to my needs and if there is a Pixelarity template that would be cool as a dashboard-style site. Or I use one that isn't and design the dashboard part myself.

*So many options!*

That is a brief intro to the important aspects of tobias.fyi. I'll leave it at that for now so I can get to actually building it!

---

### 16:16 -+- tobias.init

    TASK_02 : Start a new Django project/apps  
    TASK√02.01 : Create new virtual environment + install dependencies  
    TASK√02.02 : Initialize new git repo + set up remote  
    TASK√02.03 : Configure project directories + .gitignore + Visual Studio Code  
    TASK√02.04 : Make / push initial commit  
    TASK√02.05 : Create new django project  
    TASK_02.06 : Create / configure Postgres server + DB  
    TASK_02.04 : Create new django app  

More practice getting everything set up for a Django project!

    TASK√02.01 : Create new virtual environment + install dependencies  

    $ conda create -n tobiasfyi python=3.7 django pylint pep8 autopep8

    $ conda activate tobiasfyi

    $ conda install -c anaconda psycopg2
    $ conda install -c conda-forge ipython
    $ conda install -c conda-forge django-crispy-forms

Decided to install [crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) this time.  
I added the conda-forge channel so I don't have to write out the specific channel each time.  
I also updated conda.

    $ conda config --add channels conda-forge
    >  
    $ conda update -n base -c defaults conda

----∫----

    TASK√02.02 : Initialize new git repo + set up remote  

    $ git clone git@github.com:tobias-fyi/....

I'm making this one a private repo for now because it will have some personal information on it + other such reasons. I don't trust my knowledge of all of the systems enough yet to be sure I excluded all of the important bits.

---

### 17:16 -+- Project tobias.fyi Structure

    TASK√02.03 : Configure project directories + .gitignore + Visual Studio Code  

Set up some directories that I didn't have to for other things, plus got a little more complex with my .gitignore (only one level—I know, I'm literally a crazy person).

I wanted a directory to hold all of the visual and other assets that won't be actually on the site. e.g. creative files like .ai / .psd. I don't want those to be uploaded to GitHub as they tend to be quite large files.

I set up a whole directory for these types of things and added that to the .gitignore. Another way I considered doing it was to just include those file extensions. I decided on the former because the exported files can also be large before I process / optimize them further

    "settings": {
            "python.pythonPath": "/anaconda3/envs/tobiasfyi/bin/python",
            "python.linting.pep8Enabled": true,
            "python.linting.pylintArgs": [
                "--load-plugins",
                "pylint_django",
            ],
            "python.linting.pylintEnabled": true,
            "editor.formatOnSave": true,
            "files.exclude": {
                "**/.git": true,
                "**/.svn": true,
                "**/.hg": true,
                "**/CVS": true,
                "**/.DS_Store": true,
            },
            "editor.wordWrap": "on",
        }

    TASK√02.04 : Make / push initial commit  

----∫----

    TASK√02.05 : Create new django project  

    $ django-admin startproject tobiasfyi_project .

Woops! I accidentally started the project while in the assets directory.  
Deleted the files and started again. Glad I noticed now rather than later. Even so, more practice for me!

    .
    ├── 00_Admin
    │   └── tobiasfyi.code-workspace
    ├── 10_Assets
    │   └── 99_Untracked_Assets
    ├── LICENSE
    ├── README.md
    ├── db_data
    ├── manage.py
    └── tobiasfyi_project
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

    5 directories, 8 files

I've been reminded frequently in recent weeks that if I want to really learn something I need to do it over and over again until I don't have to follow any kind of guide. The more I experiment and break things, the more I learn how to fix things.

    TASK_02.06 : Create / configure Postgres server + DB  

Gotta be sure to add the database info at the beginning this time.

----∫----

    TASK_03 : Create Django app  

    TASK_03.01 : Create new branch of repo to work on the app (a different one for each)  

---

### 18:02 -+- DeSessioned (Early...)

Unfortunately, I have to end this session right there, before even the database is created and configured. I don't wanna leave!

But alas, dinner calls.

Hasta BBQ, Amigo!

---

### Cont'd in Smartass Knowledge Base
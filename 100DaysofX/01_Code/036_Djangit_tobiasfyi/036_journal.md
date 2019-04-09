# 2019-04-08 | #036

\#100DaysofCode

---

## Today's Menu

### Main Course

    GOAL_ : First prototype of new project

--------∫--------

### SELECT * FROM session

#### Soundtrack

- pass

#### Extras

- pass

---

## Session Log

--------∫--------

### 22:30 -+- Sessionit

The main résumé app in the tobias.fyi project will be called showcase.

Here are the main pieces of functionality again and their working titles:

- Showcase
  - An app that will generate and display my current résumé

Picking up where I left off with Git branching yesterday.

---

### 22:30 -+- Git Branching

Switching branches in Git will cause files the repository to change. Good thing to keep in mind.

    $ git branch showcase_app
    $ git checkout showcase_app
    Switched to branch 'showcase_app'

    $ git log --oneline --decorate
    d78631b (HEAD -> showcase_app, tag: v0.0.1, origin/master, origin/HEAD, master) Successful Postgres connection and migration
    ...
    f8e32a8 Initial commit

----∫----

### 22:32 -+- Smartass Branch

Decided that the first app I'm going to create for this thing is going to be...

    smartass_journal

Yup, *that* smartass_journal...I'm going to be working on it as part of this project for now. I might go back and turn it into it's own thing later on. We'll see

The full title is smartass_journal. However, I wanted to come up with a shortened version of the name—sajourn or maybe sajo.

I really like the word sojourn. I think it *kind of* fits with the theme of the app, but there isn't much connection between that and smartass_journal. For now, it will be sajourn. How about journass...? journalist? journart? journassart?

I also like just sajo, but is a bit vague. Not sure how I will use the name most—in what form, I mean. So I'll refine it as I go along.

I'm no stranger to starting fresh. It's good to be good at that.

---∫---

I need to delete the branch I made of the repo so I can start fresh with smartass_journal as the name of it.

    $ git branch -d showcase_app
    Deleted branch showcase_app (was d78631b).

> *I gave it that -d....*

Ok enough of that.

    $ git branch sajourn
    $ git checkout sajourn
    Switched to branch 'sajourn'

So far, sajourn has been very easy to type compared to smartass_journal. Even just by that measure that means it's a winner so far. Though sajo is even easier.

Sajourn kind of rolls off the fingertips. I like it. And it sounds pretty cool.

---

### 22:57 -+- First Smartass App Config

Just flippy-flopped my way back to naming it sajourn. I just like that name and don't want to type out the long one every time. I know, sooooo hard to do. But when it has to be done *a lot* it does get tiresome.

This way also means no underline. That also makes it a little easier in general.

    $ python manage.py startapp sajourn
    One sassy sajo sojourn

That was exciting!

Time for more egg-citing-ness.

The documentation / some tutorials I've seen them use just the name of the app in the installed apps section, but Corey Schafer uses the same notation that the default installed apps use. That's what I use as well.

> sajourn/apps.py

    from django.apps import AppConfig

    class SajournConfig(AppConfig):
        name = 'sajourn'

> tobiasfyi_project/settings.py

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sajourn.apps.SajournConfig',
]

---

### 23:18 -+- More SajournConfig

Created the templates and static directories:

    $ mkdir -p templates/sajourn
    $ mkdir -p static/sajourn

> sajourn/templates/sajourn/index.html
> sajourn/static/sajourn/main.scss | main.css | main.js

Added the bootstrap starter template just to get something up there.

----∫----

I'm also a little underwhelmed with autopep8 now that I've been using black.

I might have to switch back to black. I guess once you go...nevermind.

    $ conda install -c conda-forge black
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done

> Edited the VSCode workspace settings:

    "python.formatting.provider": "black",
    "python.formatting.blackPath": "/anaconda3/envs/pdform/bin/black",
    "python.formatting.blackArgs": [
        "--line-length=79"
    ],

Also disabled the wordwrap for now:

    // "editor.wordWrap": "on",

> tobiasfyi_project/urls.py:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("", include("sajournal.urls"), name="sajourn"),
        path("admin/", admin.site.urls),
    ]

> sajourn/urls.py:

    from django.urls import path
    from . import views

    urlpatterns = [path("", views.sajournal, name="sajournal")]

And BOOM! We have some smartass and *no more Chinese laundry*.

![SassyJo](Images/sassy.png)

---

### 00:18 -+- Text Widget

    CUE_01 : Create a sidebar nav  

    CUE_02 : Create base.html and extend it out to specific pages  

Here is the link to that section in the [realpython tutorial](https://realpython.com/get-started-with-django-1/#add-bootstrap-to-your-app).

Last item of the evening:

    TASK_01 : Create a simple text field that writes to the database  

First, putting in a simple navbar. Gotta give it at least a little *style*.

    TASK√02 : Add navbar to template  

Losing steam fast here, so must get this done quick-like.

Onto the first model!

I'd like to have the time_out field default to a certain time ahead of the time_in. Something to figure out later.

    CUE_03 : Default for time_out = (30mins) ahead of time_in  

This talk of time reminds me that I should set the timezone to "America/Denver"

    TASK√03 : Set timezone to Denver / Mountain time  

I found some potential solutions to calculating times and whatnot. I'm going to make the commit with these commented out so that I can come back to the working version if need be.

> sajourn/models.py:

    from django.db import models
    from django.utils import timezone

    class SajournalEntry(models.Model):
        time_in = models.DateTimeField(default=timezone.now)
        activity = models.CharField(max_length=79)
        project = models.CharField(max_length=79, blank=True)
        entry_notes = models.TextField(blank=True)
        time_out = models.DateTimeField(blank=True)
        duration = models.DurationField(default=960, blank=True)
        timestamp = models.DateTimeField(default=timezone.now, editable=False)

        # def calc_time_out(self):
        #     # default activity length in seconds
        #     default_duration = 1800
        #     return self.time_in + default_duration

        # def calc_duration(self):
        #     # calculates the duration
        #     return self.time_out - self.time_in

        # def time_save(self, *args, **kwargs):
        #     # save the modified time_out
        #     self.time_out = self.calc_time_out()
        #     pass

        def __str__(self):
            return self.project

Time to see if it migrates successfully.

    $ python manage.py makemigrations
    Migrations for 'sajourn':
    sajourn/migrations/0001_initial.py
        - Create model SajournalEntry

    $ python manage.py sqlmigrate sajourn 0001
    BEGIN;
    --
    -- Create model SajournalEntry
    --
    CREATE TABLE "sajourn_sajournalentry" ("id" serial NOT NULL PRIMARY KEY, "time_in" timestamp with time zone NOT NULL, "activity" varchar(79) NOT NULL, "project" varchar(79) NOT NULL, "entry_notes" text NOT NULL, "time_out" timestamp with time zone NOT NULL, "duration" interval NOT NULL, "timestamp" timestamp with time zone NOT NULL);
    COMMIT;

Let's get it!

    $ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sajourn, sessions
    Running migrations:
        Applying sajourn.0001_initial... OK

---

### 01:31 -+- DeSessiond

I would love to keep going and write to the database with a form on the page, but I took too long to get this far. It'll hafta wait until tomorrow.

Buenos nachos, amigas!
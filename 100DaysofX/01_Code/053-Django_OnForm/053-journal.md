# 2019-04-25 | #100DaysofCode

## Day 053/100

- [2019-04-25 | #100DaysofCode](#2019-04-25--100daysofcode)
  - [Day 053/100](#day-053100)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
    - [Global.loxicache(2019-04)](#globalloxicache2019-04)
  - [---- SELECT * FROM Session(2019-04-25) ----](#-----select--from-session2019-04-25-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-04-25)](#sessionsojourn2019-04-25)
    - [13:59 ~ Servironment](#1359--servironment)
      - [Virtual Environment](#virtual-environment)
      - [Testing the Django](#testing-the-django)
      - [Your Server Is Running So Go Catch It](#your-server-is-running-so-go-catch-it)
      - [PostgresQueuel](#postgresqueuel)
      - [Now Go Catch It For Real](#now-go-catch-it-for-real)
      - [LVL1_051 : Implement environment variables for secrets](#lvl1_051--implement-environment-variables-for-secrets)
      - [LVL2_051 : Footer should be stuck to bottom of page (login page)](#lvl2_051--footer-should-be-stuck-to-bottom-of-page-login-page)
    - [16:00 ~ Take Yo Owda Pweez](#1600--take-yo-owda-pweez)
      - [Conversations With Tom](#conversations-with-tom)
      - [LVL2_051 : Add our phone number to footer](#lvl2_051--add-our-phone-number-to-footer)
    - [16:36 ~ Serve the (Environ)MENTAL Interwubbz](#1636--serve-the-environmental-interwubbz)
      - [LVL1_051 : Install + Configure Web Server](#lvl1_051--install--configure-web-server)
      - [Environment Variables](#environment-variables)
    - [23:14 ~ Thought Gathering](#2314--thought-gathering)
      - [LVL1_051 : Install git on the onform server](#lvl1_051--install-git-on-the-onform-server)
      - [LVL1_051 : Export environment variables from venv activate script](#lvl1_051--export-environment-variables-from-venv-activate-script)
    - [23:47 ~ Git To It](#2347--git-to-it)
      - [CUE_051 : Create GitHub (repo) for the OnForm data](#cue_051--create-github-repo-for-the-onform-data)

## ---- SELECT * FROM Project ----

### Project.abstract

    GOAL_OnForm : A simple form-based application for PDF generation  

    LVL0_051 : Copy sojourn into Challanges + redact sensitive info  

### Project.loxocache(2019-04)

    GOAL_051 : Deploy to production server  

    LVL1_051 : Install git on the onform server  
    LVL1_051 : Export environment variables from venv activate script  
    LVL1_051 : Install + Configure nginx Web Server  
    LVL1_050 : Implement email feature with SendGrid  
    LVL1_050 : Create user account for jeffco  

    LVL2_051 : Add our phone number to footer  
    LVL2_051 : Footer should be stuck to bottom of page (login page)  
    LVL2_050 : Serialize model data + display PDF  
    LVL2_050 : Fix labels on OrderFormView  

    LVL3_050 : Add success message to orderdetail?  
    LVL3_044 : Ask if billing address is the same, if so, fill in automatically  
    LVL3_050 : Randomish numbering scheme for orders  
    LVL3_050 : Fix formatting of OrderDetail info @top - unless displaying PDF  

    IDEA_050 : render_pdf.js - loop through field_data for drawText  

### Global.loxicache(2019-04)

    CUE_043 : Set up script to automatically post parts of this coding journal to blog app  
    CUE_043 : Save the output PDF into a django/postgres table  
    CUE_047 : Start learning Django REST Framework  
    CUE_047 : Read up on REST = Representational State Transfer  

    IDEA_01 : Write CLI tool that sets up the basic Django template with a couple of commands  

--------∆--------

## ---- SELECT * FROM Session(2019-04-25) ----

### Session.abstract

    GOAL_052 : Deploy v1.0 to Production  

### Session.cache

    TASK_04-25 : Claim the Pyramid Print YelloPages listing  

---

## Session.sojourn(2019-04-25)

--------∆--------

### 13:59 ~ Servironment

#### Virtual Environment

    # On the server

    # Install pip3
    onformator@onformer:~/onform$ sudo apt-get install python3-pip
    ...
    After this operation, 266 MB of additional disk space will be used.
    Do you want to continue? [Y/n] y
    ...
    Setting up python3-dev (3.7.3-1) ...
    Processing triggers for man-db (2.8.5-2) ...
    Processing triggers for libc-bin (2.29-0ubuntu2) ...

    # Install venv
    onformator@onformer:~/onform$ sudo apt-get install python3-venv
    ...
    After this operation, 44.0 kB of additional disk space will be used.
    Do you want to continue? [Y/n] y
    ...
    Setting up python3.7-venv (3.7.3-2) ...
    Setting up python3-venv (3.7.3-1) ...
    Processing triggers for man-db (2.8.5-2) ...

    # Create virtual environment
    onformator@onformer:~$ python3 -m venv onform/venv
    onformator@onformer:~$ ls onform/
    00-Admin  01-Docs  LICENSE  onform_pdf  README.md  requirements.txt  venv

    # Activate venv
    onformator@onformer:~/onform$ source venv/bin/activate
    (venv) onformator@onformer:~/onform$

    # Install dependencies from requirements.txt
    (venv) onformator@onformer:~/onform$ pip install -r requirements.txt
    Failed building wheel for backcall
    Failed building wheel for lazy-object-proxy
    Failed building wheel for virtualenvwrapper
    Failed building wheel for wrapt

I got some errors while installing the dependencies, which seem to be related to the whole virtualenv(wrapper) situation. Maybe I shouldn't have installed those, but oh well, I'll try it out as is then fix it later if need be.

Of course Linode has a [guide on using Pipenv](https://www.linode.com/docs/development/python/manage-python-environments-pipenv/).

It's tempting to use that. However, I'm just going to go with what Corey does...for now, unless something breaks.

----ø----

#### Testing the Django

    # On the server
    # sudo nano onform_pdf/onform_pdf/settings.py
    ...
    ALLOWED_HOSTS = ["**.****.***.**.*"]
    ...
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    # Collect static
    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py collectstatic

    You have requested to collect static files at the destination
    location as specified in your settings:

        /home/onformator/onform/onform_pdf/static

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: no
    CommandError: Collecting static files cancelled.

Tried something I [found on stackoverflow](https://stackoverflow.com/questions/42970053/how-do-i-get-to-collect-static-files-i-cant-run-this-project-it-raises-the-err)...

Trying again with this setup:

    STATIC_ROOT = os.path.join(BASE_DIR, "static/")
    STATIC_URL = "/static/"

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "/home/onformator/onform/onform_pdf/", "static"), "/var/www/static/"]

Still got the error...trying again with this setup:

    STATIC_ROOT = os.path.join(BASE_DIR, "static_assets/")
    STATIC_URL = "/static/"

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), "/var/www/static/"]

Now a different error...

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py collectstatic
    Traceback (most recent call last):
    File "manage.py", line 21, in <module>
        main()
    ...
    FileNotFoundError: [Errno 2] No such file or directory: '/var/www/static'

Still got the error...trying again with this setup:

    STATIC_ROOT = os.path.join(BASE_DIR, "static_assets/")
    STATIC_URL = "/static/"

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

I'm hoping it asked me about overwriting because the last time Iran it, the dir was created...

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py collectstatic

    You have requested to collect static files at the destination
    location as specified in your settings:

        /home/onformator/onform/onform_pdf/static_assets

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes

    119 static files copied to '/home/onformator/onform/onform_pdf/static_assets', 17 unmodified.

----ø----

#### Your Server Is Running So Go Catch It

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py runserver 0.0.0.0:8000
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    Exception in thread Thread-1:
    Traceback (most recent call last):
        File "/home/onformator/onform/venv/lib/python3.7/site-packages/django/db/backends/base/base.py", line 217, in ensure_connection
    ...
    Is the server running on host "localhost" (127.0.0.1) and accepting
    TCP/IP connections on port 5432?

----ø----

#### PostgresQueuel

Oh ya, I forgot that there is no Postgres installed on the machine. I found this [article on how to do it](https://www.osradar.com/how-to-install-postgresql-on-ubuntu-19-04/). Time for some experimentation!

    (venv) onformator@onformer:~/onform/onform_pdf$ sudo apt install postgresql-11
    ...
    # for some reason this part of the scrollback is gone
    ...
    The database cluster will be initialized with locale "en_US.UTF-8".
    The default database encoding has accordingly been set to "UTF8".
    The default text search configuration will be set to "english".

    Data page checksums are disabled.

    fixing permissions on existing directory /var/lib/postgresql/11/main ... ok
    creating subdirectories ... ok
    selecting default max_connections ... 100
    selecting default shared_buffers ... 128MB
    selecting dynamic shared memory implementation ... posix
    creating configuration files ... ok
    running bootstrap script ... ok
    performing post-bootstrap initialization ... ok
    syncing data to disk ... ok

    Success. You can now start the database server using:

        /usr/lib/postgresql/11/bin/pg_ctl -D /var/lib/postgresql/11/main -l logfile start

    Ver Cluster Port Status Owner    Data directory              Log file
    11  main    5432 down   postgres /var/lib/postgresql/11/main /var/log/postgresql/postgresql-11-main.log
    update-alternatives: using /usr/share/postgresql/11/man/man1/postmaster.1.gz to provide /usr/share/man/man1/postmaster.1.gz (postmaster.1.gz) in auto mode
    Processing triggers for systemd (240-6ubuntu5) ...
    Processing triggers for man-db (2.8.5-2) ...
    Processing triggers for libc-bin (2.29-0ubuntu2) ...

Tried the URL suggested in the output:

    (venv) onformator@onformer:~/onform/onform_pdf$ /usr/lib/postgresql/11/bin/pg_ctl -D /var/lib/postgresql/11/main -l logfile start
    pg_ctl: could not open PID file "/var/lib/postgresql/11/main/postmaster.pid": Permission denied

So I tried what the article suggested:

    (venv) onformator@onformer:~/onform/onform_pdf$ sudo systemctl status postgresql
    ● postgresql.service - PostgreSQL RDBMS
        Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
        Active: active (exited) since Tue 2019-04-25 21:06:39 UTC; 4min 13s ago
    Main PID: 11135 (code=exited, status=0/SUCCESS)
        Tasks: 0 (limit: 1096)
        Memory: 0B
        CGroup: /system.slice/postgresql.service

    Apr 25 21:06:39 onformer systemd[1]: Starting PostgreSQL RDBMS...
    Apr 25 21:06:39 onformer systemd[1]: Started PostgreSQL RDBMS.

It looks good!

    (venv) onformator@onformer:~/onform/onform_pdf$ sudo -i -u postgres
    postgres@onformer:~$ psql
    psql (11.2 (Ubuntu 11.2-1))
    Type "help" for help.

    postgres=# \l
                                    List of databases
    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
    -----------+----------+----------+-------------+-------------+-----------------------
    postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
    template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
            |          |          |             |             | postgres=CTc/postgres
    template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
            |          |          |             |             | postgres=CTc/postgres
    (3 rows)

Still lookin good! Time to create the database and superuser as I do locally...

    postgres=# CREATE DATABASE onform;
    CREATE DATABASE
    postgres=# \c onform
    You are now connected to database "onform" as user "postgres".
    onform=# CREATE USER ****** WITH SUPERUSER PASSWORD '****';
    CREATE ROLE
    onform=# \q
    postgres=# \q
    postgres@onformer:~$ exit
    logout

Nice! That was actually quite painless.

--ø--

Found a [Linode article on installing Postgres](https://www.linode.com/docs/databases/postgresql/how-to-install-postgresql-on-ubuntu-16-04/) (but on Ubuntu 16.04).

It says to change the postgres user's Linux password:

    (venv) onformator@onformer:~/onform/onform_pdf$ sudo passwd postgres
    New password:
    Retype new password:
    passwd: password updated successfully

Note that this user is distinct from the postgres Linux user. The Linux user is used to access the database, and the PostgreSQL user is used to perform administrative tasks on the databases.

The password set in this step will be used to connect to the database via the network. Peer authentication will be used by default for local connections. See the [Secure Local PostgreSQL Access section](https://www.linode.com/docs/databases/postgresql/how-to-install-postgresql-on-ubuntu-16-04/#secure-local-postgresql-access) for information about changing this setting.

    (venv) onformator@onformer:~/onform/onform_pdf$ su - postgres
    Password:
    su: Authentication failure
    (venv) onformator@onformer:~/onform/onform_pdf$ psql -d template1 -c "ALTER USER postgres WITH PASSWORD '******';"
    psql: FATAL:  role "onformator" does not exist

Oh I didn't realize the first command was asking for an existing password.

    (venv) onformator@onformer:~/onform/onform_pdf$ su - postgres
    Password:
    postgres@onformer:~$ psql
    psql (11.2 (Ubuntu 11.2-1))
    Type "help" for help.

    postgres=# \c template1
    You are now connected to database "template1" as user "postgres".
    template1=# ALTER USER postgres WITH PASSWORD '****';
    ALTER ROLE
    template1=# \q
    postgres@onformer:~$ exit
    logout

----ø----

#### Now Go Catch It For Real

One thing I'm remembering now is the fact that my secret key and database URI are still visible in the code. I'll have to move them to an environment variable at some point soon.

#### LVL1_051 : Implement environment variables for secrets  

However, I'm going to try to catch the server (assuming that it will run when asked), before proceeding any further.

    (venv) onformator@onformer:~/onform/onform_pdf$ nano onform_pdf/settings.py
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "****",
            "USER": "****",
            "PASSWORD": "****",
            "HOST": "***********",
            "PORT": "*********",
        }
    }

Oh baby this is so exciting!

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py runserver 0.0.0.0:8000
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 24 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, onform, sessions.
    Run 'python manage.py migrate' to apply them.

    April 23, 2019 - 15:49:01
    Django version 2.2, using settings 'onform_pdf.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

So in Corey's example, he obviously brought over the whole database (sqlite3 document). Thus, he didn't have any migrations to apply. I did not, so I'll have to apply those now.

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, onform, sessions
    Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        ...
        Applying sessions.0001_initial... OK

Let's hope that works! I guess since all of the migrations are still there it can see those and apply them all. Let's give it a whirl!

HolyshitHolyshitHolyshitHolyshitHolyshitHolyshitHolyshitHolyshit!

Went to `**.**.**.***:8000` and the site is up there! LIT!

I do have to fix the footer though...

#### LVL2_051 : Footer should be stuck to bottom of page (login page)  

---

### 16:00 ~ Take Yo Owda Pweez

We have ourselves a fresh live production server serving up some fresh pages! I tried logging in with the credentials I set up on my local machine but then I remembered that I destroyed / recreated the database, so that user went with it. That means I'll have to create it.

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py createsuperuser
    Username (leave blank to use 'onformator'): adminonform
    Email address: tobyreaper@gmail.com
    Password:
    Password (again):
    Superuser created successfully.

EVERYTHING WORKS!

I'm quite surprised how little struggle there was getting the app up on the server.

I was a little worried because when I first tried to download the PDF, it came out corrupted. However, I clicked on the big button at the bottom to do it, which probably is what caused the error.

When I downloaded it via the button in the navbar, it came out perfectly!

----ø----

#### Conversations With Tom

- Pulled up the web app on the office iMac
  - Logged in
  - Filled out and submitted the form
  - Downloaded the PDF via download button at the bottom - corrupted
  - Downloaded the PDF via download button in the navbar - WE GUCCI BABY
- TODO
  - Add our phone number to the footer
- He had the idea to use this app to lay out standard business cards
  - Or any other standard product, really
- Confirmed that we are only giving JeffCo one user account/order

#### LVL2_051 : Add our phone number to footer  

----ø----

---

### 16:36 ~ Serve the (Environ)MENTAL Interwubbz

Corey uses Apache as the web server for his app. Not sure what I'll use yet, but I've heard gunicorn is a good one.

#### LVL1_051 : Install + Configure Web Server  

----ø----

#### Environment Variables

Started looking through the github repo for Corey's series for some clues as to how to use environment variables. I will watch his video on it (for the...third...fourth...fifth time?) but I would like to see how he implemented it in the django app. Here's what I found thus far:

    SECRET_KEY = os.environ.get('SECRET_KEY')

Just from the knowledge I've gained from this build alone I have a good idea of what I can do to set up environment variables, but I want to make sure it works / what the best practices are on the live server.

From spending so much time in my ~/.zshrc file over the past week, I'm almost positive I can export environment variables from something similar like ~/.bash_profile.

What I'm not sure about is if that is the best place to put them, as I also remember Corey, in his video on this topic, going through setting these up for the specific virtual environment.

[From Corey's video](https://youtu.be/cY2NXB_Tqq0?t=377):

Find out where the environment is located, and add a bash script that is run whenever the environment is activated. This would be in the activate script.

    #!/bin/sh
    export SECRET_KEY="How seCRET is THIS secreT KEy? Secret Enuff 4Ü?"
    export DATABASE_URI="postgresql://[user[:password]@][host][:port][/dbname]"

Then another when the venv is deactivated.

    #!/bin/sh
    UNSET DATABASE_URI

---

### 23:14 ~ Thought Gathering

#### LVL1_051 : Install git on the onform server  

#### LVL1_051 : Export environment variables from venv activate script  

Although [it is two years old, this article](https://medium.com/@gitudaniel/the-environment-variables-pattern-be73e6e0e5b7) has a clear and simple explanation of how to set environment variables on Ubuntu / Python venv.

[Django-environ](https://github.com/joke2k/django-environ) is package that automates envar management and makes the process [12factor](https://12factor.net/). Utilizes a .env file that holds all of the secrets.

Yet another option is [python-decouple](https://github.com/henriquebastos/python-decouple), another envar / configuration management package. Also uses a .env file.
[Here's an article about it.](https://medium.com/@nithinkvijayan/https-medium-com-nithinkvijayan-separating-django-application-config-and-secrets-from-code-python-decouple-e0787d2bcc2a). However, the last real commit on the github was two years ago.

It seems the latter two would be the best for me. The .env file would look something like this:

    DEBUG=TRUE
    EMAIL_PORT=465
    EMAIL_HOST=smtp.thiswebsite.com
    DATABASE_URI="postgresql://[user[:password]@][host][:port][/dbname]"
    ALLOWED_HOSTS=***.**.****.**

Here's a paragraph right after the above, which makes me think I might not be able to use this in production?

    Tip: You can use .env file for a local development to define env variables. While on production deployment use environment variables of the instance. Also remember to add .env to your gitignore file

---

### 23:47 ~ Git To It

#### CUE_051 : Create GitHub (repo) for the OnForm data  

The best thing to do first would be to get git going on the server so I can clone the repo to my local environment and make the other changes.

I might want to rebuild the app on the server before implementing the git workflow. Both to get more practice with the process and to do certain things better:

- Don't include unnecessary requirements / packages / dependencies
- Use virtualenv instead of venv
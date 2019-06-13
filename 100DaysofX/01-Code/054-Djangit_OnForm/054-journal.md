# 2019-04-26 | Onform

## Day 054 / 100

- [2019-04-26 | Onform](#2019-04-26--onform)
  - [Day 054 / 100](#day-054--100)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
    - [Global.loxicache(2019-04)](#globalloxicache2019-04)
  - [---- SELECT * FROM Session(2019-04-26) ----](#-----select--from-session2019-04-26-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn](#sessionsojourn)
    - [15:35 -+- Session.init](#1535----sessioninit)
    - [15:35 ~ Server Git Some](#1535--server-git-some)
      - [TASK√051 : Install git on the onform server](#task051--install-git-on-the-onform-server)
      - [Git Some Configuration](#git-some-configuration)
      - [TASK√050 : Connect server to GitHub remote repo](#task050--connect-server-to-github-remote-repo)
    - [16:33 ~ Envarrrrrs](#1633--envarrrrrs)
      - [TASK_051 : Set up env vars on server](#task_051--set-up-env-vars-on-server)
    - [21:31 ~ Committed to Change](#2131--committed-to-change)
      - [TASK√051 : No more SECRETs shall PASS](#task051--no-more-secrets-shall-pass)
      - [TASK√051 : Commit the newly private django + push to github](#task051--commit-the-newly-private-django--push-to-github)
    - [22:11 ~ Go Fetch, My Dawg](#2211--go-fetch-my-dawg)
      - [TASK√051 : Fetch the newly private django repo](#task051--fetch-the-newly-private-django-repo)
      - [TASK√051 : Set up env vars on local machine + verify everything works](#task051--set-up-env-vars-on-local-machine--verify-everything-works)
      - [LVL1_054 : Set production Postgres to only accept connections from application](#lvl1_054--set-production-postgres-to-only-accept-connections-from-application)
    - [22:46 ~ Email](#2246--email)
      - [LVL1_050 : Implement email feature with SendGrid](#lvl1_050--implement-email-feature-with-sendgrid)
      - [LVL1_054 : Set email environment variables in production](#lvl1_054--set-email-environment-variables-in-production)

## ---- SELECT * FROM Project ----

### Project.abstract

    GOAL_Onform : A simple form-based application for PDF generation  

### Project.loxocache(2019-04)

    LVL0_051 : Copy sojourn into Challanges + redact sensitive info  

    GOAL_051 : Deploy to production server  

    TASK√051 : Install git on the onform server  
    TASK√050 : Connect server to GitHub remote repo  
    LVL1_051 : Go through the Django Deployment Checklist  
        TASK√051 : Set up env vars on server  
        TASK√051 : No more SECRETs shall PASS  
        TASK√051 : Commit the newly private django + push to github  
        TASK√051 : Fetch the newly private django repo  
        TASK√051 : Set up env vars on local machine  
        LVL1_054 : Set production Postgres to only accept connections from application  
    LVL1_051 : Install + Configure Web Server  
    LVL1_051 : Configure subdomain  
    LVL1_050 : Add success message to orderdetail  
    TASK√054 : Format billing_phone/fax like normal phone  
    LVL1_050 : Create user account for jeffco  

    LVL2_050 : Implement email feature with SendGrid  
        LVL2_054 : Set email environment variables in production  

    TASK√051 : Footer should be stuck to bottom of page (login page)  
    TASK√051 : Add our phone number to footer  
    LVL2_050 : Serialize model data + display PDF  
    LVL2_050 : Fix labels on OrderFormView  

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

--------ø--------

## ---- SELECT * FROM Session(2019-04-26) ----

### Session.abstract

    GOAL_054 : Set up the OnForm application on a subdomain  
    GOAL_054 : Set up email functionality  

### Session.cache

---

## Session.sojourn

--------ø--------

### 15:35 -+- Session.init

I did a little research and it looks like I will be able to connect up a subdomain of our main website to point to the OnForm server.

That would be mighty chill.

---

### 15:35 ~ Server Git Some

#### TASK√051 : Install git on the onform server  

I guess the first thing I should do is see if the server came with git installed.

    # On the server
    onformator@onformer:~$ git --version
    git version 2.20.1

Cool! That was an easy task to complete.

Decided that I'm not going the deploy key route for git on the server. Instead I'm going to create a new user for the server to use—[a "machine" user](https://developer.github.com/v3/guides/managing-deploy-keys/#machine-users).

| Service  | Username             |
| -------- | -------------------- |
| Gmail    | onformator@gmail.com |
| GitHub   | onformator           |
| SendGrid | gmail                |
|          |                      |

The Containers extension for Firefox is SO MUCH BETTER than Sessionbox on Chrome. This one actually works...

#### Git Some Configuration

Configured git on the server...

    # On the server
    onformator@onformer:~$ git config --global user.name "OnForm Server"
    onformator@onformer:~$ git config --global user.email onformator@gmail.com
    onformator@onformer:~$ git config --global core.editor nano

Thought about starting to learn vim, but decided that would be a bit right now.

I added Onformator as a collaborator on the repo. Still have to set up ssh from the server to GitHub. Created an ssh key on the server.

    onformator@onformer:~/.ssh$ ssh-keygen -b 4096
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/onformator/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/onformator/.ssh/id_rsa.
    Your public key has been saved in /home/onformator/.ssh/id_rsa.pub.
    The key fingerprint is:
    ...
    The key's randomart image is:
    ...

Added the ssh key to the onformator github account and verified that it is working.

#### TASK√050 : Connect server to GitHub remote repo  

It looks like I have fetch / push access to the remote already! That was easy.

    onformator@onformer:~/onform$ git remote -v
    origin  git@github.com:tobias-fyi/onform.git (fetch)
    origin  git@github.com:tobias-fyi/onform.git (push)

---

### 16:33 ~ Envarrrrrs

I could commit with all of the information still in the database, but I need to set up the environment variables (or similar) functionality anyways. I might as well do it.

I believe that the only thing I need to change right now is SECRET_KEY, because the Postgres info is different on the server and has not been committed to the database yet.

Ok so the .gitignore file in the repo already lists the venv directory, so I should be good to add the environment variables to the activate script.

#### TASK_051 : Set up env vars on server  

> venv/bin/activate

    deactivate() {
        ...
        unset SECRET_KEY

        unset DEBUG

        unset DB_ENGINE
        unset DB_NAME
        unset DB_USER
        unset DB_PASS
        unset DB_HOST
        unset DB_PORT
    }

    ...

    export SECRET_KEY=""

    # Leaving it in debug mode until go-live
    export DEBUG="True"

    export DB_ENGINE=""
    export DB_NAME=""
    export DB_USER=""
    export DB_PASS=""
    export DB_HOST=""
    export DB_PORT=""

---

### 21:31 ~ Committed to Change

#### TASK√051 : No more SECRETs shall PASS  

Time to remove those pesky secrets from the codebase.

    SECRET_KEY = os.environ.get("SECRET_KEY")

    DEBUG = (os.environ.get("DEBUG_MODE") == "True")

    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE"),
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASS"),
            "HOST": os.environ.get("DB_HOST"),
            "PORT": os.environ.get("DB_PORT"),
        }
    }

Not sure if that's overkill or not but oh well, at least it's safe...I think.

#### TASK√051 : Commit the newly private django + push to github  

    (venv) onformator@onformer:~/onform$ git push origin master
    Enter passphrase for key '/home/onformator/.ssh/id_rsa':
    Enumerating objects: 143, done.
    Counting objects: 100% (143/143), done.
    Compressing objects: 100% (138/138), done.
    Writing objects: 100% (139/139), 555.66 KiB | 7.61 MiB/s, done.
    Total 139 (delta 47), reused 0 (delta 0)
    remote: Resolving deltas: 100% (47/47), completed with 4 local objects.
    To github.com:tobias-fyi/onform.git
    48f5d9b..910d203  master -> master
    (venv) onformator@onformer:~/onform$

---

### 22:11 ~ Go Fetch, My Dawg

#### TASK√051 : Fetch the newly private django repo  

Went through the `$ git pull` + `$ git push` flow and everything went through smoothly. Now all three repos (local, server, remote / github) are synced up...well I guess not quite yet. I still have to sync up the server with what was pushed to github from my local machine.

    Fast-forward
    onform_pdf/static/css/main.css        | 4 ++--
    onform_pdf/static/css/main.scss       | 4 ++--
    onform_pdf/templates/base.html        | 8 +++-----
    onform_pdf/templates/orderdetail.html | 4 ++--
    4 files changed, 9 insertions(+), 11 deletions(-)

Ok now we're good to go.

#### TASK√051 : Set up env vars on local machine + verify everything works  

Took me a little digging until I remembered where the activate script is for the local virtual environment, as it was installed using pyenv.

> /Users/Tobias/.pyenv/versions/onform/bin

Set the environment variables. Now another momento truthificotalis!

Nope. Doesn't seem like that did the trick. Oh well I'll figure it out later. For now I want to get this darn thing off the ground and onto a nice cozy subdomain of our main site.

#### LVL1_054 : Set production Postgres to only accept connections from application  

---

### 22:46 ~ Email

Decided to go ahead and set up the email.

#### LVL1_050 : Implement email feature with SendGrid  

> onform_pdf/settings.py

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_HOST_USER = "apikey"
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

#### LVL1_054 : Set email environment variables in production  

I will finish the email setup later.

However, [the docs mention using the EmailMessage class](https://docs.djangoproject.com/en/2.2/topics/email/#the-emailmessage-class) when attaching a file.
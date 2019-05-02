# 2019-04-27 | Onform

## Day 055 / 100

- [2019-04-27 | Onform](#2019-04-27--onform)
  - [Day 055 / 100](#day-055--100)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
    - [Global.loxicache(2019-04)](#globalloxicache2019-04)
  - [---- SELECT * FROM Session(2019-04-27) ----](#-----select--from-session2019-04-27-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn](#sessionsojourn)
    - [23:48 ~ Stairway to Cozy Subdomains](#2348--stairway-to-cozy-subdomains)
      - [TASK√051 : Footer should be stuck to bottom of page (login page)](#task051--footer-should-be-stuck-to-bottom-of-page-login-page)
      - [TASK√051 : Add our phone number to footer](#task051--add-our-phone-number-to-footer)
    - [00:53 ~ Apache](#0053--apache)
    - [LVL1_051 : Install + Configure Web Server](#lvl1_051--install--configure-web-server)
      - [Install Apache2 and mod-wsgi](#install-apache2-and-mod-wsgi)
      - [Configure Apache2](#configure-apache2)
      - [Enable Apache Site](#enable-apache-site)
      - [File / Database permissions](#file--database-permissions)
      - [Postgresql Database Location](#postgresql-database-location)
      - [PostgreSQL Client Auth Config File](#postgresql-client-auth-config-file)
      - [LVL1_054 : Set production Postgres to only accept connections from application](#lvl1_054--set-production-postgres-to-only-accept-connections-from-application)
      - [Apache Has Postgres Permission](#apache-has-postgres-permission)
    - [02:02 ~ Config File Instead of Env Vars](#0202--config-file-instead-of-env-vars)

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

## ---- SELECT * FROM Session(2019-04-27) ----

### Session.abstract

    GOAL_055 : Set up the OnForm application on a subdomain  
    GOAL_055 : Set up email functionality  

### Session.cache

---

## Session.sojourn

--------ø--------

### 23:48 ~ Stairway to Cozy Subdomains

[Here's a CSS-Tricks article on subdomain redirects and such](https://css-tricks.com/put-a-subdomain-on-a-different-server/).

Decided I don't want a passphrase on the ssh. I didn't realize that meant I would have to enter it every time I used ssh with that key.

    $ ssh-keygen -p

Your identification has been saved with the new passphrase.

So I ended up just asetting the environment variables globally in my ~/.zshrc file. It'll have to do, and it does! Got the local server up and running smoothly.

----ø----

Decided to fix up the footer. I did the positioning earlier, added the phone number just now.

#### TASK√051 : Footer should be stuck to bottom of page (login page)  

#### TASK√051 : Add our phone number to footer  

----ø----

I was going to use nginx / gunicorn to deploy the app / site, but I think that will take a bit longer than I want to spend right now. Corey's tutorial uses apache and I want to just get it working and he seems to know what he's doing.

However, once I have the time I would like to run nginx. Maybe that will be a different project though.

[Here's the uWSGI documentation tutorial on setting it up.](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

---

### 00:53 ~ Apache

Before I get going on this, I need to push the local changes to github and pull onto the server. I made some changes to the footer.

    # On the server
    (venv) onformator@onformer:~/onform$ git pull
    ...
    From github.com:tobias-fyi/onform
    3b4b6ce..24f457b  master     -> origin/master
    Updating 3b4b6ce..24f457b
    Fast-forward
    onform_pdf/onform_pdf/settings.py  | 15 +++++++++++++--
    onform_pdf/static/css/main.css     | 12 ++++++++++--
    onform_pdf/static/css/main.css.map |  2 +-
    onform_pdf/static/css/main.scss    | 20 +++++++++++++++++---
    onform_pdf/templates/base.html     | 11 ++++++++++-
    5 files changed, 51 insertions(+), 9 deletions(-)

Ok now we're good to go.

---

### LVL1_051 : Install + Configure Web Server  

#### Install Apache2 and mod-wsgi

    # On the server
    # Install Apache2
    (venv) onformator@onformer:~$ sudo apt-get install apache2
    After this operation, 8,613 kB of additional disk space will be used.
    Do you want to continue? [Y/n] y
    ...
    Setting up apache2 (2.4.38-2ubuntu2) ...

    # Install mod-wsgi
    sudo apt-get install libapache2-mod-wsgi-py3
    Setting up libapache2-mod-wsgi-py3 (4.6.5-1) ...
    apache2_invoke: Enable module wsgi

#### Configure Apache2

    # Apache configuration
    (venv) onformator@onformer:~/onform$ cd /etc/apache2/sites-available
    (venv) onformator@onformer:/etc/apache2/sites-available$ l
    000-default.conf  default-ssl.conf

    # Copy default configuration to start
    (venv) onformator@onformer:/etc/apache2/sites-available$ sudo cp 000-default.conf onform_pdf.conf

    # Custom config
    (venv) onformator@onformer:/etc/apache2/sites-available$ sudo nano onform_pdf.conf

    Alias /static /home/onformator/onform/onform_pdf/static_assets
    <Directory /home/onformator/onform/onform_pdf/static_assets>
        Require all granted
    </Directory>
        /home/onformator/onform/onform_pdf/static_assets
    <Directory>

    <Directory /home/onformator/onform/onform_pdf/onform_pdf>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIScriptAlias / /home/onformator/onform/onform_pdf/onform_pdf/wsgi.py
    WSGIDaemonProcess django_onform python-path=/home/onformator/onform python-home=/home/onformator/onform/venv
    WSGIProcessGroup django_onform

#### Enable Apache Site

    # Enable site via apache
    (venv) onformator@onformer:~$ sudo a2ensite onform_pdf
    Enabling site onform_pdf.
    To activate the new configuration, you need to run:
        systemctl reload apache2

    # Disable the default conf / site
    (venv) onformator@onformer:~$ sudo a2dissite 000-default.conf
    Site 000-default disabled.
    To activate the new configuration, you need to run:
        systemctl reload apache2

#### File / Database permissions

I had to find the postgresql data directory in order to give apache the right permissions to use it. Corey used sqlite3 for the video so I had to do a little digging. I found the configuration files which have a ton of great information...

#### Postgresql Database Location

> /etc/postgresql/11/main/postgresql.conf

    data_directory = '/var/lib/postgresql/11/main'

Looking through the configuration file I'm wondering if this is where I can set the DB to only accept connections from the app. Here are some settings I found that piqued my fancy:

    # - Connection Settings -
    #listen_addresses = 'localhost'     # what IP address(es) to listen on;
                                        # comma-separated list of addresses;
                                        # defaults to 'localhost'; use '*' for all
    ...
    # - SSL -
    ssl = on
    #ssl_ca_file = ''
    ...

Tons more and this is only one of the config files.

#### PostgreSQL Client Auth Config File

> pg_hba.conf

    # PostgreSQL Client Authentication Configuration File
    # ===================================================
    #
    # Refer to the "Client Authentication" section in the PostgreSQL
    # documentation for a complete description of this file.  A short
    # synopsis follows.
    #
    # This file controls: which hosts are allowed to connect, how clients
    # are authenticated, which PostgreSQL user names they can use, which
    # databases they can access.  Records take one of these forms:
    #
    # local      DATABASE  USER  METHOD  [OPTIONS]
    # host       DATABASE  USER  ADDRESS  METHOD  [OPTIONS]
    # hostssl    DATABASE  USER  ADDRESS  METHOD  [OPTIONS]
    # hostnossl  DATABASE  USER  ADDRESS  METHOD  [OPTIONS]

aaaaand...jackpot! Now I know where to go to do the following:

#### LVL1_054 : Set production Postgres to only accept connections from application  

Now back to the show.

#### Apache Has Postgres Permission

    # Make apache the owner of the group
    (venv) onformator@onformer:~$ sudo chown :www-data /etc/postgresql/11/main
    # Give the group the right permissions
    (venv) onformator@onformer:~$ sudo chmod 664 /etc/postgresql/11/main
    # Give apache ownership of the django project directory
    (venv) onformator@onformer:~$ sudo chown :www-data onform/

    (venv) onformator@onformer:~$ ls -la
    drwxr-xr-x 7 onformator www-data   4096 Apr 23 20:08 onform

---

### 02:02 ~ Config File Instead of Env Vars

Apparently Apache doesn't work well with environment variables. Best to create a config file with the sensitive into that can be read into the app.

    (venv) onformator@onformer:~$ sudo touch /etc/config_onform.json
    (venv) onformator@onformer:~$ sudo nano /etc/config_onform.json

> /etc/config_onform.json

    {
        "SECRET_KEY": "****",
        "DEBUG_MODE": "False",
        "DB_ENGINE": "django.db.backends.postgresql",
        "DB_NAME": "****",
        "DB_USER": "******",
        "DB_PASS": "****",
        "DB_HOST": "******",
        "DB_PORT": "8888888"
    }

> onform_pdf/settings.py

import json

with open("/etc/config_onform.json") as config_onfile:
    onfile = json.load(config_onfile)

SECRET_KEY = onfile.get("SECRET_KEY")

DEBUG = onfile.get("DEBUG_MODE")

DATABASES = {
    "default": {
        "ENGINE": onfile.get("DB_ENGINE"),
        "NAME": onfile.get("DB_NAME"),
        "USER": onfile.get("DB_USER"),
        "PASSWORD": onfile.get("DB_PASS"),
        "HOST": onfile.get("DB_HOST"),
        "PORT": onfile.get("DB_PORT"),
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = onfile.get("EMAIL_PASS")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

Saweeee! I just started using the replace function in nano `(^ + \)` and it made that a lot quicker.
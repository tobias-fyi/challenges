# 2019-04-29 | Onform

## Day 057 / 100

- [2019-04-29 | Onform](#2019-04-29--onform)
  - [Day 057 / 100](#day-057--100)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
    - [Global.loxicache(2019-04)](#globalloxicache2019-04)
  - [---- SELECT * FROM Session(2019-04-29) ----](#-----select--from-session2019-04-29-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn](#sessionsojourn)
    - [03:58 ~ Home Stretch](#0358--home-stretch)
      - [Collectstatic](#collectstatic)
      - [TASK√051 : Install + Configure Web Server](#task051--install--configure-web-server)
      - [TASK√054 : Format billing_phone/fax like normal phone](#task054--format-billing_phonefax-like-normal-phone)
      - [TASK√050 : Create user account for jeffco](#task050--create-user-account-for-jeffco)
      - [LVL1_050 : Add success message to orderdetail](#lvl1_050--add-success-message-to-orderdetail)
      - [LVL1_051 : Configure subdomain](#lvl1_051--configure-subdomain)
      - [Jeffco's user](#jeffcos-user)
    - [05:04 ~ Subdomain](#0504--subdomain)
    - [05:40 ~ de.Session'd](#0540--desessiond)

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

## ---- SELECT * FROM Session(2019-04-29) ----

### Session.abstract

    GOAL_057 : Set up the OnForm application on a subdomain  
    GOAL_057 : Set up email functionality  

### Session.cache

---

## Session.sojourn

--------ø--------

### 03:58 ~ Home Stretch

#### Collectstatic

    (venv) onformator@onformer:~$ python onform/onform_pdf/manage.py collectstatic

    You have requested to collect static files at the destination
    location as specified in your settings:

        /home/onformator/onform/onform_pdf/static_assets

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes

    3 static files copied to '/home/onformator/onform/onform_pdf/static_assets', 133 unmodified.
    (venv) onformator@onformer:~$ sudo service apache2 restart

And it's just about there. Something is still a little off because the footer isn't at the bottom, but that could be something else.

Yeah it's something else, as the code for the footer is the same as what I have locally.

#### TASK√051 : Install + Configure Web Server  

#### TASK√054 : Format billing_phone/fax like normal phone  

#### TASK√050 : Create user account for jeffco  

#### LVL1_050 : Add success message to orderdetail  

#### LVL1_051 : Configure subdomain  

#### Jeffco's user

Created new group that has permission to create orders.  
Created a new user for jeffco.  
Created new user for Tom.  

---

### 05:04 ~ Subdomain

Set up the subdomain to point at the ip address of the server.

It works! But is still not secure. Unfortunately Let's Encrypt apparently doesn't have a package for Ubuntu 19 yet but i'm going to try with the 18 package.

    # Ran this one
    $ sudo apt-get update

    # Did not run this one yet
    $ sudo apt-get install software-properties-common
    $ sudo add-apt-repository universe
    $ sudo add-apt-repository ppa:certbot/certbot
    $ sudo apt-get update
    $ sudo apt-get install certbot python-certbot-apache

Here's what the site says when i put in "Ubuntu (Other)"

    $ wget https://dl.eff.org/certbot-auto
    2019-04-29 11:27:50 (42.3 MB/s) - ‘certbot-auto’ saved [63564/63564]

    # Ran this one
    $ sudo mv certbot-auto /usr/local/bin/certbot-auto

    # Did not run this one yet
    $ sudo chown root /usr/local/bin/certbot-auto
    $ sudo chmod 0755 /usr/local/bin/certbot-auto

Here's the link to [certbot](https://certbot.eff.org/).

And to [Let's Encrypt.](https://letsencrypt.org/getting-started/)

It looks like I'll still be able to do it, just not have it automated for me.

----ø----

I'm going to worry about this later.

Whew it is UP!

I'm going to commit everything to the Git Repo / Push to GitHub before I do ANYTHING else.

---

### 05:40 ~ de.Session'd

    (venv) onformator@onformer:~/onform$ git push origin master
    Enumerating objects: 17, done.
    Counting objects: 100% (17/17), done.
    Compressing objects: 100% (9/9), done.
    Writing objects: 100% (9/9), 1.38 KiB | 1.38 MiB/s, done.
    Total 9 (delta 8), reused 0 (delta 0)
    remote: Resolving deltas: 100% (8/8), completed with 8 local objects.
    To github.com:tobias-fyi/onform.git
        24f457b..eaa8085  master -> master

And that's a solid night right there.

=)
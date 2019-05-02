# 2019-04-24 | #100DaysofCode

## Day 052/100

- [2019-04-23 | #100DaysofCode](#2019-04-23--100daysofcode)
  - [Day 051/100 | 113/365](#day-051100--113365)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
    - [Global.loxicache(2019-04)](#globalloxicache2019-04)
  - [---- SELECT * FROM Session(2019-04-23) ----](#-----select--from-session2019-04-23-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-04-23)](#sessionsojourn2019-04-23)
    - [10:11 -+- pre.session.init](#1011----presessioninit)
    - [10:18 ~ Session.init](#1018--sessioninit)
    - [10:18 ~ Linode Setup](#1018--linode-setup)
      - [Install software updoots](#install-software-updoots)
      - [Set hostname of the server](#set-hostname-of-the-server)
      - [Set hostname in hostfile](#set-hostname-in-hostfile)
      - [Set up a new limited user](#set-up-a-new-limited-user)
      - [Sshetting up SSH](#sshetting-up-ssh)
      - [Best Practices: SSH Config](#best-practices-ssh-config)
      - [Firewall](#firewall)
    - [12:17 ~ Linode Deployment](#1217--linode-deployment)
      - [Generate requirements.txt](#generate-requirementstxt)
      - [Side-note: rsync](#side-note-rsync)
      - [Copy Application to Server](#copy-application-to-server)
      - [Backstreet rsync Boys](#backstreet-rsync-boys)
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
      - [Topics Discussed (via text) with Philip](#topics-discussed-via-text-with-philip)
      - [Topics to Discuss with Philip](#topics-to-discuss-with-philip)
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

## ---- SELECT * FROM Session(2019-04-24) ----

### Session.abstract

    GOAL_052 : Deploy v1.0 to Production  

### Session.cache

    TASK_04-23 : Claim the Pyramid Print YelloPages listing  

---

## Session.sojourn(2019-04-24)

--------∆--------

### 12:17 ~ Linode Deployment

#### Generate requirements.txt

    $ cd ~/workshop/onform
    $ pip freeze > requirements.txt
    appdirs==1.4.3
    appnope==0.1.0
    astroid==2.2.5
    attrs==19.1.0
    backcall==0.1.0
    black==19.3b0
    Click==7.0
    decorator==4.4.0
    Django==2.2
    django-crispy-forms==1.7.2
    django-extensions==2.1.6
    ipython==7.4.0
    ipython-genutils==0.2.0
    isort==4.3.17
    jedi==0.13.3
    lazy-object-proxy==1.3.1
    mccabe==0.6.1
    parso==0.4.0
    pbr==5.1.3
    pexpect==4.7.0
    pickleshare==0.7.5
    prompt-toolkit==2.0.9
    psycopg2-binary==2.8.2
    ptyprocess==0.6.0
    Pygments==2.3.1
    pylint==2.3.1
    pytz==2019.1
    six==1.12.0
    sqlparse==0.3.0
    stevedore==1.30.1
    toml==0.10.0
    traitlets==4.3.2
    typed-ast==1.3.4
    virtualenv==16.4.3
    virtualenv-clone==0.5.3
    virtualenvwrapper==4.8.4
    wcwidth==0.1.7
    wrapt==1.11.1

----ø----

#### Side-note: rsync

I'm not going to use `rsync` right now, because I want to prevent any possible errors with the deployment. I don't think it would cause anything, but since it [does things a little differently](https://www.computerhope.com/unix/rsync.htm) than `scp`, it might bring along some permissions or something that might mess with things. I'm sticking with Corey's commands now until I have the application up and running.

    # Checking if rsync is installed / what version
    onformator@onformer:~$ rsync --version
    rsync  version 3.1.3  protocol version 31
    Copyright (C) 1996-2018 by Andrew Tridgell, Wayne Davison, and others.

Looked up the [difference between the two commands](https://unix.stackexchange.com/questions/39718/is-there-ever-a-reason-to-use-scp-instead-of-rsync), and found this:

    rsync: Transfers deltas(using its Delta Transfer Algorithm) between:

        local and remote hosts

    scp: Transfers whole files between:

        local and remote hosts
        remote and remote hosts

    Summary: scp can transfer files between two remote hosts while rsync doesn't support it.

----ø----

#### Copy Application to Server

    # On my local machine
    # Copy project directory to home folder on server
    $ scp -r onform onformator@**.*.*.**:~/
    ...
    requirements.txt            100%  640    17.1KB/s   00:00
    0000                        100% 8192   198.2KB/s   00:00
    0000                        100% 8192   198.7KB/s   00:00
    000000010000000000000003    100%   16MB 263.5KB/s   01:02
    000000010000000000000002     54% 8928KB 245.6KB/s   00:30 ETA^
    ^C

I accidentally started copying those damn Mac files. I was going to let it go but saw how big that third on is...16mb? Super weird. Apparently that is an "extended attribute"?

Oh...that's right. It's almost definitely the postgres db_data directory. Meaning those files have something to do with postgres. I'm going to try to simply exclude that directory from the `scp` command.

----ø----

#### Backstreet rsync Boys

...which it cannot do. Looks like I'll be using rsync after all.

    # On the server
    # Removed project and copied again
    onformator@onformer:~$ ls
    onform
    onformator@onformer:~$ rm -r onform/

    # On my local machine
    # -n means dry run
    $ rsync -avr -n --exclude='xx-db_data' onform onformator@**.**.*.*****:~/
    sending incremental file list
    onform/
    onform/.gitignore
    onform/.python-version
    onform/LICENSE
    onform/README.md
    onform/requirements.txt
    onform/.git/
    ...
    onform/onform_pdf/templates/registration/
    onform/onform_pdf/templates/registration/login.html

    sent 18,591 bytes  received 1,563 bytes  13,436.00 bytes/sec
    total size is 5,606,966  speedup is 278.21 (DRY RUN)

That dry run option is clutch. Decided to leave in some misc files like the pdf output, the git branch login, and some others, as I couldn't find something right off the bat to exclude multiple patterns.

Time to try again, this time as a wet run...

    # On my local machine
    $ rsync -avr --exclude='xx-db_data' onform onformator@**.**.*.*****:~/
    ...
    onform/onform_pdf/templates/registration/login.html

    sent 5,638,353 bytes  received 6,307 bytes  594,174.74 bytes/sec
    total size is 5,606,966  speedup is 0.99

And boom! Hopefully that doesn't mess anything up.

    # On the server
    onformator@onformer:~$ cd onform/
    onformator@onformer:~/onform$ ls
    00-Admin  01-Docs  LICENSE  onform_pdf  README.md  requirements.txt

Thought about copying the Postgres Data Directory `xx-db_data`, but I figure I can just spin up a fresh database on the server. It shouldn't be that much of an ordeal...ideally.

Taking a break for lunch, so closing the ssh connection...

    # On the server
    onformator@onformer:~/onform$ exit
    logout
    Connection to **.*.*.** closed.

    # Back to the server
    $ ssh onformator@*****.**.*.*****
    Welcome to Ubuntu 19.04 (GNU/Linux 5.0.0-13-generic x86_64)

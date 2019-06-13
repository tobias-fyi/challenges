# 2019-05-11 | #100DaysofCode

## Day 069 / 100

- [2019-05-11 | #100DaysofCode](#2019-05-11--100daysofcode)
  - [Day 069 / 100](#day-069--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-05)](#projectloxocache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-11)](#sessionsojourn2019-05-11)
    - [Loxocache](#loxocache)
    - [14:38 -+- Session.init](#1438----sessioninit)
    - [14:56 ~ Fantasticate Fresh Facia](#1456--fantasticate-fresh-facia)
    - [15:01 ~ Virtual Vardo](#1501--virtual-vardo)
    - [15:30 ~ Delirifacient Development](#1530--delirifacient-development)
    - [15:44 ~ Raad Runserver](#1544--raad-runserver)
    - [16:35 ~ Nesiote Node Neurism](#1635--nesiote-node-neurism)
      - [TASK-fyinit : Option to create directory](#task-fyinit--option-to-create-directory)
    - [16:55 ~ Benedict Blueballs](#1655--benedict-blueballs)

---

## SELECT * FROM Project

### Project.abstract

    GOAL-OnForm : Online Form + Automatic PDF Generation  

### Project.loxocache(2019-05)

- pass

--------Ø--------

## SELECT * FROM Session

### Session.abstract

    GOAL-069 : Save PDF to filesystem via Node  
    GOAL-069 : Email PDF via Python  

#### Session.cache

- Yarn Dependency Manager
  - [Main Site](https://yarnpkg.com/lang/en/)
  - [Documentation](https://yarnpkg.com/en/docs)
- [nvm](https://github.com/nvm-sh/nvm)

---

## Session.sojourn(2019-05-11)

### Loxocache

--------Ø--------

### 14:38 -+- Session.init

Just created a file with the new fyinit CLI!

Working at a basic level. Improvements still to be made, but at least it's working well.

I added the weekday to the filename because that's what I've been doing lately. Here's some ipython content that shows how I confirmed that I was doing it right.

    In [1]: import datetime

    In [2]: today = datetime.date.today()

    In [3]: today.isoweekday()
    Out[3]: 6

    In [4]: weekdays = {
    ...:     "1": "monday",
    ...:     "2": "tuesday",
    ...:     "3": "wednesday"
    ...:     "4": "thursday",
    ...:     "5": "friday",
    ...:     "6": "saturday",
    ...:     "7": "sunday",
    ...: }

    In [5]: wkday_int = today.isoweekday()
    ...: day_name = weekdays[f"{wkday_int}"]

    In [6]: print(day_name)
    saturday

Here's some output from running the CLI:

    ╭─ Fineyedesign » tobiasfyi » ..hop/Fineyedesign »  master ●       19.05.11 ∫ 14:38:27
    ╰─ fyinit
    ----------------º----------------
    ---------------------------------
    -----------Choose-a-Dir----------
    0.......                      cwd
    1.......                  01-Docs
    2.......                05-Visual
    3.......              08-Projects
    4.......               10-Clients
    5.......                 20-Alias
    ----------------º----------------
                  --º--
    1

    ----------------º----------------
    -------------01-Docs-------------
    -----------Choose-a-Dir----------
    0.......                       ..
    1.......                      cwd
    2.......              01-Journals
    3.......            02-Repertoire
    4.......                05-Guides
    ----------------º----------------
                  --º--
    2

    ...(redacted for brevity)...

    ----------------º----------------
    -------------2019-05-------------
    -----------Choose-a-Dir----------
    0.......                       ..
    1.......                      cwd
    2.......                   assets
    ----------------º----------------
                --º--
    1
                    º
    ----------------º----------------
    Creating 19-05-11-saturday.md
    At /Users/Tobias/workshop/Fineyedesign/01-Docs/01-Journals/10-Sessions/2019-05
    ----------------º----------------
    ...
    ...
    ...
    ...
    And BOOM!
    No more Chinese laundry...

### 14:56 ~ [Fantasticate](http://phrontistery.info/f.html) Fresh [Facia](http://phrontistery.info/f.html)

There are a few things I want to get up to this afternoon.

1. Create new virtual environment for local OnForm application
2. Begin using Node in application, namely for saving PDFs to filesystem
3. Write Python code to email PDFs from filesystem

Regarding #1: unfortunately I created this project before I was completely done setting up my new virtual environment / project management workflow. So the virtual environment is set up differently than my other projects.

However, I'm not going to create an entirely new project, as now I know that I can simply create a new venv with my new workflow without creating an entirely new project.

Let's get to it!

---

### 15:01 ~ Virtual [Vardo](http://phrontistery.info/v.html)

Cleaned things up a bit by removing the old pyenv-virtualenv...

    ╭─ tobiasfyi » ~                                                    19.05.11 ∫ 15:11:20
    ╰─ pyenv virtualenvs
    3.7.3/envs/onform (created from /Users/Tobias/.pyenv/versions/3.7.3)
    onform (created from /Users/Tobias/.pyenv/versions/3.7.3)

    ╭─ tobiasfyi » ~                                                    19.05.11 ∫ 15:12:29
    ╰─ pyenv virtualenv-delete onform
    pyenv-virtualenv: remove /Users/Tobias/.pyenv/versions/3.7.3/envs/onform? y

Now time to create a new virtualenv / [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) for the project...

    ╭─ tobiasfyi » ~/workshop                                           19.05.11 ∫ 15:14:17
    ╰─ mkvirtualenv -a ~/workshop/onform onform
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/onform/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/onform/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/onform/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/onform/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/onform/bin/get_env_details
    Setting project for onform to /Users/Tobias/workshop/onform

    ╭─ tobiasfyi » ~/workshop/onform »  master                         19.05.11 ∫ 15:18:32
    ╰─ workon onform
    pyenv-virtualenvwrapper: python is not available.

    ╭─ tobiasfyi » ~/workshop/onform »  master                         19.05.11 ∫ 15:18:56
    ╰─ lsvirtualenv
    pyenv-virtualenvwrapper: python is not available.

I got a little worried when I received this error. I really don't want to spend the time fixing my workflow right now in order to get to the development part.

Went in search of potential causes.

    ╭─ tobiasfyi » ~/workshop/onform »  master                         19.05.11 ∫ 15:20:21
    ╰─ pyenv versions
    pyenv: version `onform' is not installed (set by /Users/Tobias/workshop/onform/.python-version)
    system
    3.7.3
    3.8-dev

Saw that the `.python-version` file was doing something. That file is from the previous venv. Removed it...

    ╭─ tobiasfyi » ~/workshop/onform »  master                         19.05.11 ∫ 15:21:34
    ╰─ lsvirtualenv
    CS50
    ====

    Challenges
    ==========

    Fineyedesign
    ============
    ...

    onform
    ======

    tobiasfyi
    =========

    ╭─ tobiasfyi » ~/workshop/onform »  master                         19.05.11 ∫ 15:21:45
    ╰─ workon onform

    ╭─ onform » tobiasfyi » ~/workshop/onform »  master                19.05.11 ∫ 15:30:05
    ╰─ echo $FRESHIES
    Groovy!

Groovy! We in bidness.

---

### 15:30 ~ [Delirifacient](http://phrontistery.info/d.html) Development

    First things first, *install all the packages*!

    ╭─ onform » tobiasfyi » ~/workshop/onform »  master                19.05.11 ∫ 15:30:10
    ╰─ pip install -r requirements.txt

    Successfully installed ...
        Click-7.0
        Django-2.2
        Pygments-2.3.1
        appdirs-1.4.3 appnope-0.1.0 astroid-2.2.5 attrs-19.1.0
        backcall-0.1.0 black-19.3b0
        decorator-4.4.0 django-crispy-forms-1.7.2 django-extensions-2.1.6
        ipython-7.4.0 ipython-genutils-0.2.0 isort-4.3.17
        jedi-0.13.3
        lazy-object-proxy-1.3.1
        mccabe-0.6.1
        parso-0.4.0 pbr-5.1.3 pexpect-4.7.0 pickleshare-0.7.5 prompt-toolkit-2.0.9 psycopg2-binary-2.8.2 ptyprocess-0.6.0 pylint-2.3.1 pytz-2019.1
        six-1.12.0 sqlparse-0.3.0 stevedore-1.30.1
        toml-0.10.0 traitlets-4.3.2 typed-ast-1.3.4
        virtualenv-16.4.3 virtualenv-clone-0.5.3 virtualenvwrapper-4.8.4
        wcwidth-0.1.7 wrapt-1.11.1
    You are using pip version 19.0.3, however version 19.1.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.

I really want to fix the couple of messages that pop up every time I start a new venv. The pip version message as shown directly above, and the 'pywnv script is deprecated' message that runs when I start up a new venv.

I'm going to try [updating pyenv](https://github.com/pyenv/pyenv-installer).

I am wondering now if they are related. I don't think that updating pyenv did anything significant.

Oh well...

---

### 15:44 ~ [Raad](http://phrontistery.info/r.html) Runserver

Tried to get the onform application up and running. Looks like I'll have to grab the info from the config.json file on the linode server...

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master ●             19.05.11 ∫ 15:43:06
    ╰─ python manage.py runserver
    Traceback (most recent call last):
    File "manage.py", line 21, in <module>
        main()
    ...
    File "/Users/Tobias/workshop/onform/onform_pdf/onform_pdf/settings.py", line 16, in <module>
        with open("/etc/config_onform.json") as config_onfile:
    FileNotFoundError: [Errno 2] No such file or directory: '/etc/config_onform.json'

Or...

I think that information is still in my ~/.zshrc. That's how I was running my local environment. However, it would be nice to have the exact same—or as close to as possible—environment on my local machine.

    # on the server
    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master ●             19.05.11 ∫ 15:43:10
    ╰─ ssh onformator@****.**.*.**.*.**.*.****.*******.**.***
    Welcome to Ubuntu 19.04 (GNU/Linux 5.0.0-13-generic x86_64)

    onformator@onformer:~$ sudo nano /etc/config_onform.json
    [sudo] password for onformator:

Created the same file and copied over the data from the server. I think that the path is the same, though the permissions might be weird when accessing that file from within django. I'll give it a go anyways...

    # On my local machine
    ╭─ Fineyedesign » tobiasfyi  ⚙ /etc                                 19.05.11 ∫ 15:57:48
    ╰─ touch config_onform.json
    touch: config_onform.json: Permission denied

    ╭─ Fineyedesign » tobiasfyi  ⚙ /etc                                 19.05.11 ∫ 15:58:00
    ╰─ sudo touch config_onform.json
    Password:

    ╭─ Fineyedesign » tobiasfyi  ⚙ /etc                                 19.05.11 ∫ 15:58:07
    ╰─ sudo code config_onform.json

    # on the server
    onformator@onformer:~$ exit
    logout
    Connection to ****.**.*.**.*.**.*.****.*******.**.*** closed.

Trying the dev server once again...

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master ●             19.05.11 ∫ 16:01:48
    ╰─ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    May 11, 2019 - 16:01:57
    Django version 2.2, using settings 'onform_pdf.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

So far; soooo good...let's see if it really worked.

Nope! Received a `Bad Request (400)` error when trying to access the URL.

I wonder if I should've fetched the repo from github...maybe there are changes that I don't have on my local machine?  
It also will be trying to run via apache probably.

Went back into the server's `settings.py` file to check, and my local version is the same.

Going to turn on debug mode to do some debugging...wow look at me!

After setting `DEBUG_MODE = "True"` and `ALLOWED_HOSTS = []`...it works!

Dope...

---

### 16:35 ~ [Nesiote](http://phrontistery.info/n.html) Node [Neurism](http://phrontistery.info/n.html)

Now I finally get to do some JavaScript in a Node environment. I really have not spent much time with Node, so this is actually quite exciting, particularly now that I am much more knowledgeable of backend languages / frameworks in general. Referring to the last time I picked up Node.

I'm going to practice a bit in a different directory before starting up a node app within OnForm.

----ƒ----

Really quick—I want to add some code to `fyinit.py` so I can use it to generate a new sandbox for node learning.

    name_choice = prompter("name (hit enter to use today's date)", "entry")

    if name_choice:
        j_name = name_choice
    else:
        j_name = f"{c_year[2:]}-{c_month}-{c_day}-{day_name}.md"

This should allow me to choose a different name if I want...

    ...
    ----------------º----------------
    What is this entry's name (hit enter to use today's date):
    ----------------º----------------
                --º--
    19-05-11-basicnodes.md
                    º
    ----------------º----------------
    Creating 19-05-11-basicnodes.md
    At /Users/Tobias/workshop/Fineyedesign/01-Docs/01-Journals/30-KB/JavaScript/Node
    ----------------º----------------
    ...

Yup it works!

Another thing I want to add is the ability to create a directory if needed.

#### TASK-fyinit : Option to create directory  

---

### 16:55 ~ [Benedict](http://phrontistery.info/b.html) Blueballs

Surprise! Not getting to do any node this time...

Check back in tomorrow for some hawt, heavy, heroarchic node action!

Buenos nachos, amigos!  
🌮

Also, happy day 69! One month left until this challenge is complete and I start the next one!
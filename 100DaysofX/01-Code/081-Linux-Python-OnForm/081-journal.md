# 2019-05-23 | #100DaysofCode

    GOAL-05-23 ~ Deploy new changes to the OnForm Linode Server  

## Day 081/100 | 143/365

- [2019-05-23 | #100DaysofCode](#2019-05-23--100daysofcode)
  - [Day 081/100 | 143/365](#day-081100--143365)
    - [11:50 ~ Server Sferics](#1150--server-sferics)
      - [LVL2-OnForm : Remove extra javascript from OnForm](#lvl2-onform--remove-extra-javascript-from-onform)
    - [12:15 ~ Apache Autolatry](#1215--apache-autolatry)
    - [12:53 ~ Install Indagate](#1253--install-indagate)
    - [13:37 ~ Homeward Bound Blandiloquence](#1337--homeward-bound-blandiloquence)

---- Tasks ----

    LVL2-OnForm : Remove extra javascript from OnForm  

---- Resources ----

- I found [this stackoverflow answer on permissions](https://askubuntu.com/questions/767504/permissions-problems-with-var-www-html-and-my-own-home-directory-for-a-website)
- [The steps for allowing apps to access gmail](https://www.google.com/accounts/DisplayUnlockCaptcha)

---- Sojourn ----

### 11:50 ~ Server Sferics

Sferics: Study of storms using electronic detectors.

Time to go for it on the server!

Decided to remove the login branch because it's not being used.

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master                    19.05.23 ∫ 11:55:47
    ╰─ git branch -d login
    Deleted branch login (was cad0467).

However, that only deletes it locally. I need to delete the remote branches as well.

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master                    19.05.23 ∫ 11:55:54
    ╰─ git branch -a

    * master
    remotes/origin/HEAD -> origin/master
    remotes/origin/login
    remotes/origin/master
    remotes/origin/renderer
    (END)

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master                    19.05.23 ∫ 11:57:27
    ╰─ git push origin --delete renderer
    To github.com:tobias-fyi/onform.git
    - [deleted]         renderer

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master                    19.05.23 ∫ 11:59:09
    ╰─ git push origin --delete login
    To github.com:tobias-fyi/onform.git
    - [deleted]         login

Confirm that it all worked out.

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master                   19.05.23 ∫ 12:01:12
    ╰─ git branch -a

    * master
    remotes/origin/HEAD -> origin/master
    remotes/origin/master
    (END)

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master                   19.05.23 ∫ 12:01:27
    ╰─ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean

Now I'm on the server...

    (venv) onformator@onformer:~/onform$ git remote show origin
    * remote origin
    Fetch URL: git@github.com:tobias-fyi/onform.git
    Push  URL: git@github.com:tobias-fyi/onform.git
    HEAD branch: master
    Remote branches:
        master                    tracked
        refs/remotes/origin/login stale (use 'git remote prune' to remove)
    Local branch configured for 'git pull':
        master merges with remote master
    Local ref configured for 'git push':
        master pushes to master (local out of date)

For some reason whenever I try to prune the login branch it says that it does not exist. Oh well...I don't think it's completely necessary right now.

I'm going to get that `git pull` going...

    (venv) onformator@onformer:~/onform$ git log --oneline --decorate
    eaa8085 (HEAD -> master, origin/master, origin/HEAD) App is working - jeffco.pyramidprint.graphics
    24f457b Fixed footer and started setting up email
    ...
    8773756 Initial commit

The Pro Git book says to use the `git fetch` + `git merge` workflow. But I'm going to just use the `git pull` command. Simple is good.

    (venv) onformator@onformer:~/onform$ git pull origin
    ...
    eaa8085..7b27694  master     -> origin/master
    ...
    .../20-Assets/19-05-14-onform-blank.pdf                      | Bin 154775 -> 152493 bytes
    onform_pdf/onform/serializers.py                             |   8 -
    onform_pdf/onform/urls.py                                    |   4 +-
    onform_pdf/onform/views.py                                   | 161 ++++++++++-
    onform_pdf/onform_pdf/settings.py                            |  15 +-
    onform_pdf/static/assets/onform-logo-512.png                 | Bin 0 -> 27482 bytes
    onform_pdf/static/js/render_pdf.js                           | 338 +++++-----------------
    onform_pdf/static/js/smtp.js                                 |   2 +
    onform_pdf/static/pdf/onform-blank.pdf                       | Bin 0 -> 152493 bytes
    onform_pdf/static_assets/js/smtp.js                          |   2 +
    onform_pdf/templates/base.html                               |   2 +
    onform_pdf/templates/orderdetail.html                        |  23 +-
    17 files changed, 243 insertions(+), 1171 deletions(-)
    ...
    create mode 100644 onform_pdf/static_assets/js/smtp.js

And there we have it...

#### LVL2-OnForm : Remove extra javascript from OnForm  

One thing I just thought of is the fact that I included `pdfilled` in the .gitignore file. So I'll have to create the directory.

    (venv) onformator@onformer:~/onform/onform_pdf/static/pdf$ mkdir pdfilled

---

### 12:15 ~ Apache Autolatry

I'm going to try a simple reload of apache and see what happens.

    (venv) onformator@onformer:~/onform$ systemctl reload apache2
    Failed to reload apache2.service: The name org.freedesktop.PolicyKit1 was not provided by any .service files
    See system logs and 'systemctl status apache2.service' for details.

Doesn't seem like anything really happened. Going to confirm that the changes actually were applied when I did the `git pull`.

I guess I can try running collectstatic again.

    (venv) onformator@onformer:~/onform/onform_pdf$ python manage.py collectstatic
    You have requested to collect static files at the destination
    ...
    3 static files copied to '/home/onformator/onform/onform_pdf/static_assets', 135 unmodified.

I just wanted to be sure that the static_assets included the pdfilled directory. I don't think it really matters, but whatever...

...whoooooopsies...

...I forgot to install reportlab and PyPDF2...

...I knew there was something I was forgetting. Lol.

---

### 12:53 ~ Install Indagate

    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip install pillow
    ...
    Successfully installed pillow-6.0.0

    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip install reportlab
    ...
    Successfully installed reportlab-3.5.21

    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip install pypdf2
    ...
    Running setup.py bdist_wheel for pypdf2 ... error
    ...
    error: invalid command 'bdist_wheel'
    ...
    Failed building wheel for pypdf2
    Running setup.py clean for pypdf2
    Failed to build pypdf2
    Installing collected packages: pypdf2
    Running setup.py install for pypdf2 ... done
    Successfully installed pypdf2-1.26.0

That last part doesn't look too good...It says that it installed but failed to build. Found a stackoverflow page that uninstalled wheel and fixed it. I'll try that, and reinstalling it if there is an issue...then go from there.

Well...this might be the culprit...wheel wasn't installed at all.

    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip uninstall wheel
    Skipping wheel as it is not installed.
    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip install wheel
    ...
    Successfully installed wheel-0.33.4

    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip install pypdf2
    ...
    Successfully built pypdf2
    Installing collected packages: pypdf2
    Successfully installed pypdf2-1.26.0

Ok cool. Whewwww. Everything looks to be in order.

    (venv) onformator@onformer:~/onform/onform_pdf/onform$ pip list
    Package             Version
    ------------------- -------
    appdirs             1.4.3
    appnope             0.1.0
    ...
    wheel               0.33.4
    wrapt               1.11.1

Remembered to change debug mode to True while working. I got an error when submitting the form to the live site. This gives me a little bit of information. I think I might have to renew the permissions that Apache has...

    PermissionError at /
    [Errno 13] Permission denied: '/home/onformator/onform/onform_pdf/static/pdf/pdfilled/onform-4.pdf'

Oooooh or I never had to give Apache permission to write to the filesystem before. I guess that will have to happen.

----Ø----

I found [this stackoverflow answer](https://askubuntu.com/questions/767504/permissions-problems-with-var-www-html-and-my-own-home-directory-for-a-website) that might be what I'm looking for...

    There may be some cases where you have to give the web server write permission to a file, or to a directory - this can be achieved by doing `sudo chmod g+w /var/www/html/PATH` (where PATH is the path to the file or folder in the directory structure where you need to apply the write permissions for the web server).

so hopefully I can run the following to fix it...

    sudo chmod g+w /home/onformator/onform/onform_pdf/static/pdf/pdfilled

I'm a little scared of doing that since it's not using the group I created, which Apache owns...Instead I'm going to give the group ownership of the directory.

    (venv) onformator@onformer:~/onform/onform_pdf/static/pdf$ sudo chown :www-data /home/onformator/onform/onform_pdf/static/pdf/pdfilled

Ok well I got somewhere! This time it errored out the same `SMTPAuthenticationError` that happened earlier. Not sure how to fix it as I can't log into gmail via the server. I'll confirm that all of the information is correct. Also I should confirm that the pdf was generated...

Yep! At least there's that.

Now it's just the emailing that needs fixing now and we'll be groovin.

Ok I went [through the steps](https://www.google.com/accounts/DisplayUnlockCaptcha) and confirmed that new apps can access the account...

---

### 13:37 ~ Homeward Bound Blandiloquence

Yuuuuuuup! We are gold, Pony Boy! That took a little longer than I'd hoped, but it works!

I'd like to see if I can make the connection secure with Let's Encrypt. That would mean this thing could chug on for a while without being fixed if need be. I mean it'll chug along just fine right now, but it will need to be secured at some point or it just looks bad. I need to go for a walk. I'll look into that when I get back.

And I really need to implement some tests...basically everywhere.

Hasta proxima, amiga!

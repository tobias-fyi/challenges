# 2019-05-21 | #100DaysofCode

    GOAL-05-21 ~ Auto-email the auto-generated PDF  

## Day 079/100 | 141/365

- [2019-05-21 | #100DaysofCode](#2019-05-21--100daysofcode)
  - [Day 079/100 | 141/365](#day-079100--141365)

---- Tasks ----

    LVL1-OnForm : Add success message to confirm that PDF was generated and sent  
    LVL2-OnForm : Fix the Form Labels  
    LVL2-OnForm : Button / field to email another copy of PDF  
    LVL3-OnForm : Create email signature  
    LVL3-OnForm : Calculate time spent on developing OnForm  

    TASK√OnForm : Generate PDF from within Django  
    TASK√OnForm : Email generated PDF from within Django  

---- Notes ----

    CUE-OnForm : Calculate time spent on developing OnForm  

---- Resources ----

- [Supercharge Your Classes With super()](https://realpython.com/python-super/)
- [More Classy Views](http://ccbv.co.uk/projects/Django/2.1/django.views.generic.edit/CreateView/)

---- Selects ----

- Processing.py [tutorial on Getting Started](https://py.processing.org/tutorials/gettingstarted/)
- Emoji
  - Printing emojis in Python | [emoji.py](https://pypi.org/project/emoji/)
  - [List of all emoji as unicode](https://unicode.org/emoji/charts/full-emoji-list.html)

---- Sojourn ----

Let's review...

> 078-Django-OnForm/078-journal.md

    Now...I'm sure you (whoever may read this at some point in the distant far-out future) know what time it is...

---

### 22:42 ~ Time to SEND IT

Time to send it! Home stretch now baby!

For the email code, I wrote a new method `send_it()`, and called it at the very end of `render_pdf()`, passing in the filepath of the rendered pdf.

```python
def send_it(file):
    import smtplib
    import imghdr
    from email.message import EmailMessage

    EMAIL_ADDRESS = os.environ.get("EMAIL_AD")
    EMAIL_PASS = os.environ.get("EMAIL_PW")

    msg = EmailMessage()
    msg["Subject"] = "Env Order For Mr. Tom"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "tobyreaper@gmail.com"
    msg.set_content("JeffCo Env Order Attached")

    with open(f"onform-{order_id}.pdf", "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name,
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)
```

#### Rhizogenic - Producing or growing roots

[Rhinotillexomania](http://phrontistery.info/r.html)

I got a little sidetracked and created a little logo for OnForm. I wanted the site to have a favicon.

![Branding OnForm](onform-logo-512.png)

---

### 23:14 ~ More Email Send_It

Fixed the os import and added `self` as an argument to the method...

```python
def send_it(self, file):
    import smtplib
    import imghdr
    import os
    from email.message import EmailMessage

    EMAIL_ADDRESS = os.environ.get("EMAIL_AD")
    EMAIL_PASS = os.environ.get("EMAIL_PW")

    msg = EmailMessage()
    msg["Subject"] = "Env Order For Mr. Tom"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "tobyreaper@gmail.com"
    msg.set_content("JeffCo Env Order Attached")

    with open(file, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="application", subtype="octet-stream", filename=file_name
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)
```

----Ø----

OMGOMGOMGOMGOMGOMGOMG...

It didn't error out and took a while to get to OrderDetail. That makes me think that it was sending one nice email with a real nice PDF attached to it.

I guess we'll find out...I'm going to check my email when I'm out in the sunroom.

---

### 00:00 ~ Fundus Feelz

Two months of work—hard work...Of course I wasn't working on this full-time the entire time. But I did put a ton of time into it. I should calculate how much time I ended up putting in to get to a working prototype of the PDF generation and email functionality.

#### TASK-OnForm : Calculate time spent on developing OnForm  

    In [4]: msg = "\U0001F643 Hard Work Pays Off"
    In [5]: print(msg)
    🙃 Hard Work Pays Off

    In [6]: yumface = "\U0001F60B"
    In [7]: print(yumface)
    😋

#### GOAL√05-23 : Generate PDF from within Django  

#### GOAL√05-23 : Email generated PDF from within Django  

    In [8]: celeface = "\U0001F973"
    In [9]: print(celeface)
    🥳

    In [10]: nerdme = "\U0001F913"
    In [11]: print(nerdme)
    🤓

Just having a bit o' funz...I guess the party face doesn't work in vscode.

In [16]: print(msg)
I designed the PDF 🤓 AND wrote the code that generates it—thanks to the hard work of those who wrote the libraries. 😎

#### LVL3-OnForm : Create email signature  

---

### 00:38 ~ Git Girandole

Final action of the night: committing the code to the `renderer` branch, merging it into master, and pushing to le Hub.

    ╭─ onform » tobiasfyi » ..nform_pdf/onform »  renderer             19.05.22 ∫ 00:37:17
    ╰─ git checkout master
    Switched to branch 'master'
    Your branch is up to date with 'origin/master'.

    ╭─ onform » tobiasfyi » ..nform_pdf/onform »  master ?             19.05.22 ∫ 00:37:22
    ╰─ git merge renderer
    Updating 88682f6..5b674ed
    Fast-forward
    ...
    onform_pdf/onform/views.py                                   | 154 +++++++++++++++--
    onform_pdf/onform_pdf/settings.py                            |  15 +-
    onform_pdf/static/assets/onform-logo-512.png                 | Bin 0 -> 24906 bytes
    ...
    17 files changed, 239 insertions(+), 1168 deletions(-)
    ...

    ╭─ onform » tobiasfyi » ..nform_pdf/onform »  master ↑2            19.05.22 ∫ 00:37:30
    ╰─ git push origin master
    88682f6..5b674ed  master -> master

And boom!

No more of that Chinese laundry.

Hasta mañana, amigo!

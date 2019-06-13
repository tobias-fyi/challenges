# 2019-05-22 | #100DaysofCode

    GOAL-05-22 ~ Deploy new changes to the OnForm Linode Server  

## Day 080/100 | 142/365

- [2019-05-22 | #100DaysofCode](#2019-05-22--100daysofcode)
  - [Day 080/100 | 142/365](#day-080100--142365)
    - [09:13 ~ OnForm Fixity](#0913--onform-fixity)
      - [TASK√OnForm : Insert Email info onto the server's config_onform.json](#taskonform--insert-email-info-onto-the-servers-config_onformjson)
      - [TASK√OnForm : OnForm Server - pip install reportlab + pillow + PyPDF2](#taskonform--onform-server---pip-install-reportlab--pillow--pypdf2)
    - [09:44 ~ Decision Devoir](#0944--decision-devoir)
    - [10:05 ~ Committed Comitatus](#1005--committed-comitatus)
    - [10:46 ~ Something Septiferous Serotinous](#1046--something-septiferous-serotinous)

---- Tasks ----

    LVL1-OnForm : Set up Django Logging  
    LVL1-OnForm : Display PDF on the OrderDetail page  
    LVL2-OnForm : Fix the Form Labels  
    LVL2-OnForm : Create EnviroVar for destination filepath  
    LVL2-OnForm : Remove extra javascript from OnForm  
    LVL3-OnForm : Create email signature  
    LVL3-OnForm : Look into LastPass automated pw checking  

---- Notes ----

    IDEA-OnForm : Calculate time spent developing OnForm  
    IDEA-043 : Set up script to automatically post parts of this coding journal to blog app  

---- Resources ----

- I found [an article on Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) detailing how to get set up with Django + Postgres + nginx + Gunicorn
- [Django Logging](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#logging)
- [Supercharge Your Classes With super()](https://realpython.com/python-super/)
- [A Comprehensive Django CBV Guide](https://spapas.github.io/2018/03/19/comprehensive-django-cbv-guide/#a-gentle-introduction-to-cbvs)
- [More Classy Views](http://ccbv.co.uk/projects/Django/2.1/django.views.generic.edit/CreateView/)

---- Selects ----

- Processing.py [tutorial on Getting Started](https://py.processing.org/tutorials/gettingstarted/)
- Khan Academy [course on algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)

---- Sojourn ----

---

### 09:13 ~ OnForm Fixity

#### TASK√OnForm : Insert Email info onto the server's config_onform.json  

{
    "SECRET_KEY": "********",
    "DEBUG_MODE": "********",
    "DB_ENGINE": "********",
    "DB_NAME": "********",
    "DB_USER": "********",
    "DB_PASS": "********",
    "DB_HOST": "********",
    "DB_PORT": "********",
    "EMAIL_AD": "********",
    "EMAIL_PW": "********"
}

#### TASK√OnForm : OnForm Server - pip install reportlab + pillow + PyPDF2  

---

### 09:44 ~ Decision Devoir

Devoir: What is due; duty.

I am trying to decide what to do about this implementation. However, I think I just came to a decision as I wrote that last sentence. I was debating whether to set up a completely new Linode or try to finagle the existing one to work with the new functionality.

I am going to spend a couple of hours getting the functionality working on the current server, as I don't think it will take too long...hopefully. Then I will try to *also* get up and running with the application on a new server, if I still feel the need.

I would like to start from scratch again at some point to get used to the process and steps, as well as learn how to use nginx / gunicorn. I found [an article on Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) detailing how to get set up with Django + Postgres + nginx + Gunicorn.

But there are many other things that I could be focusing on as well. We'll see.

First order of bidnizz is to get the current apache server up and running with the new functionality.

I need to pull up the journal entries from when I first got the server up and running. I don't want to pull the new code from github until I know what it will do to the server.

---

### 10:05 ~ Committed Comitatus

Time to get to it! Don't want to waste any more time worrying about the details.

I believe if I simply pip install the new packages, pull the github repo, and restart the apache server, everything *should* work. All of the appropriate files should be in the correct location and all that.

Tested it out once more on my local machine and received an error regarding the `order_id`. It was scoped locally to the other function. I brought the same code over and ran it again...

    File "/Users/Tobias/workshop/onform/onform_pdf/onform/views.py", line 155, in send_it
        msg["Subject"] = f"New JeffCo Envelope Order (#{order_id}) Submitted"
    NameError: name 'order_id' is not defined

Brought it like it's not...

```python
order_id = str(self.object.id)
```

Now testies again...It worked, except for raising an `SMTPAuthenticationError` - I wonder if Tom changed the gmail account password.

    File "/Users/Tobias/.vega/onform/lib/python3.7/site-packages/django/views/generic/edit.py", line 142, in post
        return self.form_valid(form)
    ...
    Please log in via your web browser and then try again.
        Learn more at https://support.google.com/mail/answer/78754 - gsmtp')

Looks like I'll have to log in via a web browser. That's one other thing—I don't know how dependable the gmail smtp server is (obviously it's google so that's good). What I mean by that is whether things like this will happen a lot.

One positive thing is that it did not stop the server from running. It would be nice to have some sort of notification system for when things like this happen.

It might be worth it to implement the SendGrid feature instead, if only for consistency's sake.

----Ø----

Ok I logged in on the Pyramid iMac. Trying it again.

Still got the same error. Going to that URL listed in the error to learn more.

I confirmed that the environment variables are present...

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master ●                 19.05.22 ∫ 10:31:53
    ╰─ echo $EMAIL_AD
    *****@gmail.com

Aha! Gmail blocked access because it looked "suspicious". Logged into gmail on Firefox—man this containerized browsing is great on here.

Tried again...

...yay it worked!

The file was received successfully and correctly. The one thing that was not quite right was the filename. The name that was used was literally the entire filepath.

Changed some things up to try and correct that...

```python
def send_it(self, file):
    ...
    ppath = "/Users/Tobias/workshop/onform/onform_pdf/static/pdf/pdfilled"
    ...
    # cd into pdf directory
    os.chdir(ppath)

    with open(file, "rb") as f:
        file_data = f.read()
        file_name = f.name
```

Tried it again and it didn't error out. Checking the email now...cool it worked correctly this time.

NICE! It looks amazing.

---

### 10:46 ~ Something Septiferous Serotinous

This reminded me that I'll need to change all of the filepaths once this runs on the server. I would like to know how to use relative filepaths (if that even requires anything else), so I wouldn't have to change it.

Once I can access the BASE_DIR like it's set in the settings file, this should be a lot easier.

```python
from onform_pdf.settings import BASE_DIR
print(BASE_DIR)
...
print("Hi There from below the project root.")
```

    [22/May/2019 11:00:48] "GET /static/assets/onform-logo-512.png HTTP/1.1" 200 27482
    /Users/Tobias/workshop/onform/onform_pdf
    Hi There from below the project root.
    [22/May/2019 11:00:54] "POST / HTTP/1.1" 302 0

Sweet. Now filepaths will be much easier to manipulate and utilize. Now for the static directory.

```python
from onform_pdf.settings import BASE_DIR, STATICFILES_DIRS
print(STATICFILES_DIRS[0])
```

    [22/May/2019 11:25:40] "GET /static/assets/onform-logo-512.png HTTP/1.1" 200 27482
    /Users/Tobias/workshop/onform/onform_pdf/static
    [22/May/2019 11:25:43] "POST / HTTP/1.1" 302 0

Ok I tested it out with the new relative filepaths and it seems to have worked.

    [22/May/2019 11:33:13] "GET /static/assets/onform-logo-512.png HTTP/1.1" 200 27482
    /Users/Tobias/workshop/onform/onform_pdf/static/pdf/onform-blank.pdf
    /Users/Tobias/workshop/onform/onform_pdf/static/pdf/pdfilled/onform-33.pdf
    PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected. [pdf.py:1736]
    [22/May/2019 11:33:25] "POST / HTTP/1.1" 302 0

Yuuuuup! It is all groovy.

1. Deactivate the local dev server
2. Uncomment the line in settings - ALLOWED_HOSTS
3. Commit the changes to git + push to github
4. SSH into OnForm Linode
5. Disable the Apache server
6. Pull the new changes from github
7. Restart Apache

I just remembered that I never added the $EMAIL_AD and $EMAIL_PW to the json config file. I was still using the environment variable assignment...Hmmm, I thought that I did change it on the server already...Yup. But I want to use that method locally as well so the code is exactly the same.

----Ø----

Cleaned up the code in the `render_pdf()` and `send_it()` methods a little bit by declaring global variables globally instead of multiple times locally. Tested it out again and...

Hasta W3RK IT, amigos!

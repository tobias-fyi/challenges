# 2019-05-15 | #100DaysofCode

    GOAL-05-15 ~ Get the basic skeleton of AptDraft up and running  

## Day 073/100 | 134/365

Table of Contents

---- Tasks ----

    LVL1-136 : Design a simple branding package for AptDraft  
    LVL1-136 : Create basic templates for all pages  
    LVL1-136 : Connect to the Postgres database  
    LVL1-136 : Create user table + login functionality  
    LVL1-136 : User registration  

    LVL2-136 : Connect to the GoodReads API  
    LVL2-136 : Create reading journal table + journal page functionality  

---- Notes ----


---- Resources ----

- [Adobe Color](https://color.adobe.com/create)

---- Selects ----


---- Sojourn ----

### 06:39 -+- Session.init

On the plane atm. Decided I'm not going to be sleeping so will get some work done.

---

### 07:26 ~ Optional Optimization

Decided to set an alias and an environment variable for Fineyedesign (and probably other projects as I go) to make navigation a little quicker.

To start out I simply made it a three-letter command to navigate to the project home and a one-letter one to get the project name...

    # ================ Navigation ================ #
    export P="Fineyedesign"
    alias cdp="cd ~/workshop/Fineyedesign"

Decided to test out fyinit with my addition / re-addition of the code to open the correct workspace, and found another bug—when navigating up directories, the old paths are still in the dictionary and so any choice of path will result in the one previously chosen.

I need a way to remove the entry from the dictionary if navigating up. Or I could find another way to store the paths entirely.

---

### 07:59 ~ Cali Coding

Landed 30 mins ago or so. Philip isn't answering so I'm just hanging out writing some code.

Added one line of code to `fyinit` and fixed the bug...

    elif root == "..":
        prefix -= 1
        os.chdir(nav_target[prefix])
        nav_target.pop(prefix + 1) # new

There's likely a better way of doing this, but that works for now.

---

### 10:04 ~ Collaborative [Cacographic Caconym](http://phrontistery.info/c.html)

Made it into Phil's office around 09:30. Interesting little place nestled in amongst some "edgy" lofts. Definitely not what I was expecting, though it made me go down the mental pathway / practice of not setting any prior expectations.

There is not really anything good that can come out of them.

----ƒ----

There are a few things that I can be doing right now. Top of the list is AptDraft.

Go for launch.

---

### 10:19 ~ Absentaneous AptDraft

Time to get down and dirty with some flask.

---

### 10:35 -+- [Imponent](http://phrontistery.info/i.html).init

*Imponent: That which imposes an obligation.*

Pulling up the previous journal entry during which I started AptDraft. Using "started" here in a very loose way.

So far I've done the following:

- Set up Heroku Postgres instance
- Downloaded project distro
- Set up project
- Installed dependencies
- Set up environment variables for Flask
- Signed up for GoodReads account and received my API key

---

### 11:00 ~ [Fastuous](http://phrontistery.info/f.html) First Contact

Got the flask server up and running.

Thomas - "Pipenv install is not really working..." - It can be frustrating, that's for sure. I know the feelz.

----å----

Began building out templates for the site, starting with `base.html`.

#### LVL1-136 : Create basic templates for all pages  

---

### 11:41 ~ [Betimes](http://phrontistery.info/b.html) Brand

Picking some brand colors to start integrating them into the site right off the bat. Also going to create a simple brand package.

#### LVL1-136 : Design a simple branding package for AptDraft  

The branding should be reminscent of books, with [colors](https://color.adobe.com/create) and textures like those found in a nice leather-bound volume.

- Brown = leather
- Tan = pages
- Black = ink

Found a nice pallette on the Adobe Color Explore Page

| Hex     | Tag 1 | Tag 2     | Function |
| ------- | ----- | --------- | -------- |
| #252526 | Dark  | Off-black | BG / FG  |
| #92A69C | Light | Pale teal | Accent   |
| #F2E5D5 | Light | Tan       |          |
| #A68072 | Dark  | Tan       | Main     |
| #412D26 | Dark  | Brown     |          |
| #8C5743 | Light | Brown     |          |

Primary Pages

1. Home
2. Explore `the SELECTs`
3. Registration
4. Login / Logout
5. Search / Results List
6. Book Detail
7. Submit a Review

---

### 15:35 ~ [Carminative](http://phrontistery.info/c.html) Conversation

Just had a short conversation with Philip about the OnForm PDF strategy. He said that the best way for me to go about it, from a computer science standpoint, is to render the PDF on the server and send the rendered file to the client for display. I'm going to try to get the PDF logic to work with Python—fingers crossed.

I'm going to try again with ReportLab / Pillow. If that doesn't work I'll try again with WeasyPrint (assuming it's able to modify PDFs).

---

### 15:44 ~ More [Techytelic](http://phrontistery.info/t.html) Templates

Got a loop to work in the Flask app...

    <div class="container mt-4">
        <h1>Reading Journal</h1>
        <div>
            <h3>{{ user.username }}'s Entries:</h3>
        </div>
        <div>
            {% for entry in entries %}
            <p class="m-4">{{ entry.notes }}</p>
            {% endfor %}
        </div>
    </div>

#### Template Inheritance

For some reason the template is not being inherited...

> templates/base.html

        {% block content %}
        {% endblock content %}

> templates/home.html

    {% extends 'base.html' %}
    {% block content %}
    <div class="container mt-4">
        <h1>Reading Journal</h1>
        ...
        </div>
    </div>
    {% endblock content %}

And I believe the reason is that I did not change the name of the template being rendered in the app.

    return render_template(
        "home.html", title="Home", user=user, entries=entries
    )

Yup that did it. Always something small like that, ain't it?

---

### 16:08 ~ Left Off [Laccolith](http://phrontistery.info/l.html)

Finished the Templates chapter of the Flask Mega-Tutorial Book. Was going to start on the Web Forms chapter but decided against it.

I told Jared I'd maybe be there earlier and don't want to leave him hanging. So I'll leave it off here, and pick it back up next time with some good ol' [gnostic](http://phrontistery.info/g.html) web forms.

Hasta bananas, amigas!

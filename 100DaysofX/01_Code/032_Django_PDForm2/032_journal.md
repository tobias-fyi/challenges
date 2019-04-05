# 2019-04-04 | #032

\#100DaysofCode

- [2019-04-04 | #032](#2019-04-04--032)
  - [Today's Menu](#todays-menu)
    - [Main Course](#main-course)
    - [SELECT * FROM session](#select--from-session)
      - [Soundtrack](#soundtrack)
      - [Extras](#extras)
  - [Session Log](#session-log)
    - [12:00 -+- Sessionit](#1200----sessionit)
    - [00:20 -+- Another Method(s)](#0020----another-methods)
    - [01:05 -+- DrawThings](#0105----drawthings)
    - [01:34 -+- DeSession](#0134----desession)

---

## Today's Menu

### Main Course

    GOAL≈01 : Iteration of PDForm app that outputs real PDF

    GOAL≈02 : Add user login functionality  
    GOAL≈03 : Deploy to the web  

--------∫--------

### SELECT * FROM session

    CUE_01 : Complete Wes Bos' JavaScript20 course before this challenge is over.  
    CUE_02 : Build an app with a GUI using the Python kivy framework  

    IDEA_01 : Build an app called Remindception  

#### Soundtrack

- Actually I didn't listen to *anything* this time...crazy.

#### Extras

- [The Python Kivy Framework](https://github.com/kivy/kivy)
  - Hoping to build an iOS version of Smartass at some point, probably with Kivy

---

## Session Log

--------∫--------

### 12:00 -+- Sessionit

Decided to work a bit more on the Django PDForm app because I don't want to have to save a 20MB+ PDF every time.

I'm going to try to build the PDF only using jsPDF with it's positioning attributes.

Copied the template orderdetail.html:

> orderform/orderdetail_2.html

---

### 00:20 -+- Another Method(s)

Another method I could try first is to save only the envelope divs as images and embed those in the PDF. That might reduce the size of it, though the text inside the divs wouldn't be selectable.

Not an ideal solution.

I'm going to see if I can get it done just using jsPDF, though will probably use the html2canvas library to convert the logo images to dataURLs in order to render them using jsPDF.

---

### 01:05 -+- DrawThings

Miscalculated the sizes of the sections on the PDF (header, both envelopes, footer).  
However, this is a much more lightweight way of going about it and I don't think it will take much to make it look much better even than what I had before.

I can actually use JavaScript to automatically calculate the sizes of each section.

Gotta remember to use those semi-colons. As a writer of stories and other text alongside code, I love a good semi-colon. It is a cool-looking character. But now that I'm using it so much its specialness—though *not* losing its importance for obvious reasons.

Hmm I just realized I had left off some semi-colons but it still ran. Interesting.

---

### 01:34 -+- DeSession

Almost finished setting up all of the measurements for the main sections. This is actually rather fun! I can see a bit of why people like JavaScript so much for certain things.

That reminds me:

    CUE_01 : Complete Wes Bos' JavaScript20 course before this challenge is over.  

Now that I'm getting into js again I'm excited to do [that!](https://javascript30.com/) I signed up near the beginning of the challenge but have not started yet. Much more excited than I was before. It's so easy to get caught up in Python and only want to write Python code.

Wes also has a couple of other free courses that I signed up for and am excited to start: 

- Mastering Markdown
- Command Line Power User

Another reminder that I remembered while writing the above reminder—remindception, anyone?

    CUE_02 : Build an app with a GUI using the Python kivy framework  

And because I'll obviously just write a todo list app:

    IDEA_01 : Build an app called Remindception  

--∫--

*Alas*, 'tis late and I must attend the office en la mañana. Going to keep working on this when I get there.

Till then...

*Buenos nachos, amigos!*
# 2019-04-13 | #041

\#100DaysofCode

- [2019-04-13 | #041](#2019-04-13--041)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.cache(2019-04)](#projectcache2019-04)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.log](#sessionlog)
    - [Loxocache](#loxocache)
    - [19:08 -+- Session.init](#1908----sessioninit)
    - [19:12 -+- Positioning](#1912----positioning)
    - [19:23 -+- Worry Some](#1923----worry-some)
    - [19:47 -+- Testings](#1947----testings)
    - [19:56 -+- Position More](#1956----position-more)
    - [20:15 -+- de.Session](#2015----desession)

---

## SELECT * FROM Project

### Project.abstract

    GOAL__ : Web app for filling out PDF online  

### Project.cache(2019-04)

    TASK__ : Collect tags from other documents  

--------∏--------

## SELECT * FROM Session

### Session.abstract

    GOAL_041 : Integrate pdf-lib and Django to add data from Postgres onto PDF template  

#### Session.cache

- Atish & Slee at [Robot Heart / Burning Man 2016](https://youtu.be/HdYHJr7OcUA)

---

## Session.log

### Loxocache

    KB+01 : Input PDF must be exported as interactive PDF  

    TASK√01 : Export flat PDF version of the form  
    TASK_02 : Document the positions of each field  
    TASK_03 : Learn to place objects precisely / systematically using pdf-lib  

--------∏--------

### 19:08 -+- Session.init

Now that data from the database can be directly appended on top of the PDF, I don't really need original PDF to be interactive anymore. That would actually just make the UX worse.

Now that I have a better understanding of promises and can import / export PDF data, the game just got elevated to a new level. The options / functionality that this opens up are huge.

Getting a little excited over here...

---

### 19:12 -+- Positioning

    TASK√01 : Export flat PDF version of the form  

Exported a version of the order form without the interactive fields.

> /static/orderform/envelope_orderform.pdf

Changed the name of the folder where I'd been putting PDFs / old code.

> pdf_portal/xx_legacy_assets

    TASK_02 : Document the positions of each field  

I can't seem to find anywhere what units pdf-lib uses to position the objects on the PDF. I'll have to do some trial and error to find out.

From some initial tests it's obvious that the unit is very small—probably pixels. Going to go with that. Another useful piece of intel is that pdf-lib uses the bottom left as the origin.

---

### 19:23 -+- Worry Some

I edited the code some more and downloaded more PDFs but was confused that the added text was not moving around as it should when editing the x, y coordinates. Tried clearing the browser's cache to see if that helps.

Now I'm getting a blank output page with only the added text at the bottom. I don't like that. Not at all...Not one bit. I wonder if the interactivity of the PDf allowed it to be edited or something?

Or...I did change a few things in the code to make it more concise via arrow functions. I'll try changing them. I probably messed it up.

Nope, that wasn't it.

Hmm...I might be onto something with that interactive thing. As soon as I switched it back to the old file it worked again.

That's so weird. I'm going to try exporting one as an interactive PDF but without the fields on it and see what happens.

Yussss! I was right. I guess that's a *very*, **very** valuable piece of information, in case something happens in the future. 

    KB+01 : Input PDF must be exported as interactive PDF  

Now that I think about it a little more, I'm realizing just how lucky I was to have tried this with an interactive PDF. I don't want to think about how long I might've spent trying to figure out why it wasn't working...

I wonder if it also has something to do with how the PDF is passed in as well. Suppose I didn't create the request with a header?

----∫----

First, I'm going to commit this code to the repo so I can come back to it if need be.

---

### 19:47 -+- Testings

Ok now back to it. Trying it without passing a header into the request.

It still worked the same with the interactive one. Now how about the flat one?

Nope. Still a no-go. Interesting.

Still so happy that I got lucky with the interactive bit...And now the coordinates seem to be responding nicely.

---

### 19:56 -+- Position More

I can make some sort of conversion chart to make it easier. I'd prefer it if I didn't have to export a PDF every single time to recalibrate / test the positioning. If it is points I can get that information from the document itself.

I used an [online converter](https://uproer.com/articles/image-size-calculator-px-in/) to see if I could get some sort of starting point. I used this converter last time and found the dimensions for a letter-sized page in order to place things.

    8.5 in  = 612 px
    11      = 792

According to my precise calculations and in-depth scientifical testing, these dimensions hold true in this instance as well, as you can see in the figure below:

![O Marks The Spot](widthpx.png)

That is using the coordinates x: 600, y: 212. Seems to check out.

x, y - coordinates (in points?) from the origin / bottom left of page.

| Field                | x   | y   | Size |
| -------------------- | --- | --- | ---- |
| **Information**      |     |     |      |
| order_dept-school    |     |     |      |
| order_street_address |     |     |      |
| order_city           |     |     |      |
| order_state_code     |     |     |      |
| order_zip_code       |     |     |      |
| order_phone          |     |     |      |
| -------------------- | --- | --- | ---- |
| **Options**          |     |     |      |
| box_qty_1            |     |     |      |
| box_qty_2            |     |     |      |
| box_qty_3            |     |     |      |
| box_qty_4            |     |     |      |
| -------------------- | --- | --- | ---- |
| **Billing**          |     |     |      |
| billing_name         |     |     |      |
| billing_dept-school  |     |     |      |
| billing_address      |     |     |      |
| billing_city         |     |     |      |
| billing_state_code   |     |     |      |
| billing_zip_code     |     |     |      |
| billing_phone        |     |     |      |
| billing_fax          |     |     |      |
| billing_email        |     |     |      |
|                      |     |     |      |

---

### 20:15 -+- de.Session

I will spend some time tomorrow getting the field's positions and whatnot in order, then test it out using "real" fake data.

C'mon down and get your real fake data here!

![realfakedatas](realfakedatas.gif)

Hasta fakedatas, amigas!
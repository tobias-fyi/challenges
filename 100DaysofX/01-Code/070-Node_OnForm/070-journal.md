# 2019-05-12 | #100DaysofCode

## Day 070 / 100

- [2019-05-12 | #100DaysofCode](#2019-05-12--100daysofcode)
  - [Day 070 / 100](#day-070--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-05)](#projectloxocache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-12)](#sessionsojourn2019-05-12)
    - [17:11 ~ Session.init](#1711--sessioninit)
    - [17:27 ~ npm.init](#1727--npminit)
    - [23:05 ~ Palladian Postscript](#2305--palladian-postscript)
    - [23:46 ~ Module Mandarism](#2346--module-mandarism)
    - [00:32 ~ Forceful Fusiform Finagling](#0032--forceful-fusiform-finagling)
    - [00:56 ~ Hasta Habanera](#0056--hasta-habanera)

---

## SELECT * FROM Project

### Project.abstract

    GOAL-OnForm : Intuitive online order form / PDF generator  

### Project.loxocache(2019-05)

    LVL1-OnForm : Save PDF + auto-email  

--------Ø--------

## SELECT * FROM Session

### Session.abstract

    GOAL√070 : Save PDF to filesystem with Node + pdf-lib  

#### Session.cache

- Traversy Media [Node Crash Course](https://youtu.be/fBNz5xF-Kx4)

## Session.sojourn(2019-05-12)

--------Ø--------

### 17:11 ~ Session.init

I believe I am all groovy to get going on some Node action...

Not going to use the OnForm project directory just yet, because I want to practice just a bit while learning without risking messing something up—or just making a mess of things.

Created a new area to mess around with things while learning.

> ~/workshop/Fineyedesign/08-Projects/10-SketchBox/32-Node

---

### 17:27 ~ npm.init

    ╭─ Fineyedesign » tobiasfyi » ..ketchBox/32-Node »  master ● ?   19.05.12 ∫ 17:25:14
    ╰─ npm init
    This utility will walk you through creating a package.json file.
    ...
    About to write to /Users/Tobias/workshop/Fineyedesign/08-Projects/10-SketchBox/32-Node/package.json:

    {
        "name": "01-node_sketch",
        "version": "1.0.0",
        "description": "Getting messy in the Node Sketchbox",
        "main": "index.js",
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "author": "tobias-fyi",
        "license": "MIT"
    }

    Is this OK? (yes)
    # oh ya, it's more than ok ;P

Time to [incede](http://phrontistery.info/i.html) that init ish...

    ╭─ Fineyedesign » tobiasfyi » ..ketchBox/32-Node »  master ● ?   19.05.12 ∫ 17:30:44
    ╰─ npm install --save pdf-lib
    npm notice created a lockfile as package-lock.json. You should commit this file.
    npm WARN 01-node_sketch@1.0.0 No repository field.

    + pdf-lib@0.6.2
    added 8 packages from 15 contributors and audited 11 packages in 14.969s
    found 0 vulnerabilities

Dependencies can be installed only for development. Nodemon makes it so the server doesn't have to be restarted for every change...

    ╭─ Fineyedesign » tobiasfyi » ..ketchBox/32-Node »  master ● ?   19.05.12 ∫ 23:00:11
    ╰─ npm install -D nodemon
    ...
    + nodemon@1.19.0
    added 291 packages from 145 contributors and audited 2247 packages in 11.412s
    found 0 vulnerabilities

Created index.js and added some javascript to print to the console when called via node...

    ╭─ Fineyedesign » tobiasfyi » ..ketchBox/32-Node »  master ● ?   19.05.12 ∫ 23:03:27
    ╰─ node index
    Hey There from Node

---

### 23:05 ~ [Palladian](http://phrontistery.info/p.html) Postscript

Just got back to the studio after cooking pizza for the house and watching Game of Thrones.

Back at it with ye' ol' Node.

Created a new file with an object that is accessible from within index.js...

I looked at the page source for orderdetail to get the ids and content from a test order. Added those to data.js.

Can't get the object to import into index.js for some reason. My mind's a little slow right now.

Too much GoT...

----ƒ----

I did just have an idea for how to workaround this PDF thing.

I could have the Django OnForm app send an email whenever an order is submitted, then one of our people can go to that orderdetail page and download the PDF.

Obviously it will be best to get the automatic email working with an exported PDF, but if I can't get that to work in a timely fashion I might have to think about workarounds like that.

---

### 23:46 ~ Module [Mandarism](http://phrontistery.info/m.html)

Created a new directory to hold the render_pdf node app. I figure if I'm going to use pdf-lib to learn, might as well do it so I can easily transfer my gained knowledge into the OnForm environment.

    ╭─ Fineyedesign » tobiasfyi » ..-Node/render_pdf »  master ● ?         19.05.12 ∫ 23:53:17
    ╰─ npm init
    ...
    About to write to /Users/Tobias/workshop/Fineyedesign/08-Projects/10-SketchBox/32-Node/render_pdf/package.json:

    {
    "name": "render_pdf",
    "version": "1.0.0",
    "description": "Modify a PDF document",
    "main": "render_pdf.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "author": "tobias-fyi",
    "license": "ISC"
    }

    Is this OK? (yes)

---

### 00:32 ~ Forceful Fusiform Finagling

After some #ForcefulFinagling I got the render_pdf script to generate a PDF exactly how it would come out of OnForm! That didn't take too long, and I'm glad I went ahead and tried it out instead of trying to read / watch through something to try and learn that way.

I need to always remember *I learn best by doing*.

    ╭─ Fineyedesign » tobiasfyi » ..-Node/render_pdf »  master ● ?            19.05.13 ∫ 00:32:02
    ╰─ node render_pdf.js 
    PDF file written to: /Users/Tobias/workshop/Fineyedesign/08-Projects/10-SketchBox/32-Node/render_pdf/
    Mon May 13 2019 00:32:05 GMT-0600 (Mountain Daylight Time)-onform.pdf

Obviously that filename is terrible, as I didn't format the date at all...but besides that it all worked fantastically!

Ok there we go...

    ╭─ Fineyedesign » tobiasfyi » ..-Node/render_pdf »  master ● ?   19.05.13 ∫ 00:41:17
    ╰─ node render_pdf.js
    PDF file written to: /Users/Tobias/workshop/Fineyedesign/08-Projects/10-SketchBox/32-N
    ode/render_pdf/assets/2019-4-13-onform.pdf

For future reference, here's the javascript to get the date / make the name:

    var date = new Date();
    const filePath = `${__dirname}/assets/${date.getFullYear()}-${date.getMonth()}-${date.getDate()}-onform.pdf`;

I just realized that the month is technically incorrect this way. It counts up from 0, so 4 is May. Here's the corrected code, with a little extra formatting:

    // Create date for filename
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();

    // Add padding to month and day
    month = month.toString().padStart(2, "0");
    day = day.toString().padStart(2, "0");

And the result...

    ╭─ Fineyedesign » tobiasfyi » ..-Node/render_pdf »  master ● ?   19.05.13 ∫ 00:51:14
    ╰─ node render_pdf.js
    PDF file written to: ~/.../render_pdf/assets/2019-05-13-onform.pdf

Solid.

---

### 00:56 ~ Hasta Habanera

Stoked to have at least learn how to get to almost the functionality as the OnForm app has, in terms of javascript. Back when I first built this functionality into OnForm, I spent a whole day figuring out how to convert the pdf to a Uint8Array and make the proper request. Using Node saved a ton of time this time around, as I could simply use the fs.readFileSync function to do it automatically.

That's it for me today...

Hasta Jalapeño, Amigo!
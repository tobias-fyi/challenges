# 2019-04-12 | #040

\#100DaysofCode

- [2019-04-12 | #040](#2019-04-12--040)
  - [SELECT * FROM Project](#select--from-project)
    - [Abstract](#abstract)
    - [Loxocache](#loxocache)
  - [SELECT * FROM Session](#select--from-session)
    - [Attenoir](#attenoir)
  - [Session.log](#sessionlog)
    - [14:24 -+- Session.init](#1424----sessioninit)
    - [npm install](#npm-install)
    - [14:39 -+- VSCode Terminal](#1439----vscode-terminal)
      - [Fonts](#fonts)
    - [14:50 -+- Envirables](#1450----envirables)
    - [14:58 -+- Back to Promises](#1458----back-to-promises)
    - [15:14 -+- pdf-lib-ing It](#1514----pdf-lib-ing-it)
    - [15:36 -+- To The Rescue](#1536----to-the-rescue)
    - [00:10 -+- de.Session](#0010----desession)

---

## SELECT * FROM Project

### Abstract

    GOAL__ : Build web app for online fillable forms  
    GOAL_v0.2 : Insert data from database onto pre-made PDF template  

### Loxocache

    TASK√v0.2 : Convert PDF to Uint8Array  

--------◊--------

## SELECT * FROM Session

### Attenoir

    GOAL√040 : Read in the existing PDF and render additional text on top  

---

## Session.log

--------◊--------

### 14:24 -+- Session.init

Node.js

Started watching a tutorial on JS Promises and bn

If the npm package should be installed into a project directory, don't use the -g option.

    $ npm install package
    >>

[The Coding Train Video](https://www.youtube.com/watch?v=FjWbUK2HdCo)

### npm install

Rather than do npm installs on the global scope with sudo, better to create a directory for them. This seems similar to the reasoning behind virtual environments in Python.

    $ mkdir ~/.npm-global
    >>

Then tell npm to install in that directory.

    $ npm config set prefix '~/.npm-global'
    >>

Add the following line to ~/.zshrc:

    export PATH=~/.npm-global/bin:$PATH

Run the source to activate edited settings / profile.

    $ source ~/.zshrc
    >>

Now run the install again.

    $ npm install http-server -g
    httpserver.js
    + httpserver@0.3.0
    added 212 packages from 493 contributors in 6.55s

Install http-server.

    $ npm install -g http-server
    >>

Now I can spin up a local server using node as well.

---

### 14:39 -+- VSCode Terminal

#### Fonts

I want to use the integrated terminal but a font is not showing up correctly so the prompt looks terrible.  
[Time to fix it.](https://medium.com/@hippojs.guo/vs-code-fix-fonts-in-terminal-761cc821ef41)

1. Found font that iTerm is using
   1. 14pt Inconsolata for Powerline
2. Added it to vscode user settings
   1. "terminal.integrated.fontFamily": "Inconsolata for Powerline",
3. And BOOM! Chinese laundry

---

### 14:50 -+- Envirables


I thought it would be cool to have the conda virtual environment automatically activate when I cd into the project (root) directory. I remember hearing Corey Schafer mention this in his virtual environments video.

[Corey Schafer - Environment Variables](https://youtu.be/cY2NXB_Tqq0)

Created yaml file.

    $ conda env export > environment.yaml
    >> can create identical environment with this file

    $ conda create my_env
    $ conda activate my_env
    $ conda env create -f environment.yaml

I decided to remove some of the old environments that I don't really use anymore.

    $ conda remove -n pyr_portal --all
    $ conda remove -n pyr_print --all
    $ conda remove -n ...
    ...

Creating the (de)activate directories:

    $ mkdir -p etc/conda/activate.d
    $ mkdir -p etc/conda/deactivate.d
    >>
    $ touch etc/conda/activate.d/env_vars.sh
    $ touch etc/conda/deactivate.d/env_vars.sh

Decided to call it on this thread of thought / action. I don't want to spend this entire session fiddling with this. I'll finish setting it up later.

[Here's a link](https://github.com/chdoig/conda-auto-env/blob/master/conda_auto_env.sh) that might be useful.

---

### 14:58 -+- Back to Promises

Time to get after figuring out this promise thing.

It was very informative breaking down the code that I had thrown together yesterday. Shoutout to [TheCodingTrain](https://www.youtube.com/watch?v=QO4NXhWo_NM) for helping / motivating me to do it that way.

I had some idea of why it was constructed the way that it was, but not enough to really understand what was going on at a deeper level.

Started up a node server with some new js files to mess around with while going through the process from the beginning, this time breaking things down into their constituents.

> 01-promises.js

    // Location of the pdf to be fetched
    let pdfillable = "pdform_blank.pdf"

    // Long and basic version
    let promise = fetch(pdfillable);
    promise.then(gotData);
    promise.catch(gotErr);

    function gotData(data) {
        console.log(data);
    }

    function gotErr(err) {
        console.log(err);
    }

By using the .then notation to chain functions together, it can be condensed a bit.

    // Condensed a little
    fetch(pdfillable).then(gotData).catch(gotErr);

    function gotData(data) {
        console.log(data);
    }

    function gotErr(err) {
        console.log(err);
    }

The functions used to catch the errors and/or data coming from the promise can be used in place of their instance being called in fetch().then() to make it even more concise. They can then be converted to anonymous functions to cut down the length even more.

    // Condensed more using anonymous functions
    fetch(pdfillable)
        .then(function (data) {
            console.log(data);
        })
        .catch(function gotErr(err) {
            console.log(err);
        });

It keeps going! Using arrow functions, those .then() calls can take up only a single line each.

    // Condensed even more using arrow functions
    fetch(pdfillable)
        .then(data => console.log(data))
        .catch(err => console.log(err));

Doing this condensation step by step really helped me understand what was going on when I call fetch().

---

### 15:14 -+- pdf-lib-ing It

Now comes the fun part! This is around where I started getting caught up yesterday. Again, I was able to get the pdf file into an arrayBuffer, though this time it was much easier as I understood much better what's going on. I also got the point of the Uint8Array very quickly and painlessly.

    // define variables
    let PDFDocumentFactory = PDFLib.PDFDocumentFactory;
    let PDFDocumentWriter = PDFLib.PDFDocumentWriter;
    let drawText = PDFLib.drawText;

    // Create the request
    let pdform = "pdform_blank.pdf"
    let pdfInit = {
        headers: { "Content-Type": "application/pdf" },
    }
    let pdfRequest = new Request(pdform, pdfInit)

    // Use fetch() to load the pdf into buffer then to Uint8Array.
    fetch(pdfRequest)
        .then(response => response.arrayBuffer())
        .then(arrayBuffer => new Uint8Array(arrayBuffer))
        .then(Uint8Array => console.log(Uint8Array))
        .catch(err => console.log(err));

I'm writing this after the fact because I was so absorbed in this that I forgot to document the process.

Basically, I continued to run into the issue of not being able to extract the Uint8Array from the depths of the promise chain such that I could use it in the rest of the code. The pdf-lib functons required that type of data, and I had it! It was so close yet so far away.

I tried a number of different methods:

- Instantiating an array outside of the scope of the promise chain, then appending / adding the generated one to it
- Converting the TypedArray (Uint8Array is a TypedArray) to a conventional array, then doing a similar thing as above
- Copy / paste the entire rest of the code into the promise chain—this would've worked but I must have messed it up somehow because it still threw a similar error to what I'd been seeing

---

### 15:36 -+- To The Rescue

I texted my friend/mentor Philip to see if he'd happen to have any time to spare tonight to help me out. Lo and behold, while I was cooking dinner, he gave me a ring and we discussed it.

I took a break from cooking to get on a video chat / screenshare with him.

My understanding of the issue was starting to solidify—I'd realized not long before breaking for dinner that the main reason I was receiving the error was due to the fact that I was calling for the data before the promise had actually returned it.

Before this I really didn't have much experience with asynchronous programming, and I think that's why it took so long for the issue to seep into my understanding.

Luckily, Philip was able to give me the extra momentum to get me over the hump. He basically told me to pass the Uint8Array inside of the promise chain into a function, which would run whenever the promise was resolved. So I created a new function outside of the fetch / promise that included all of the rest of the functionality of the pdf-lib flow. Once I did that, I didn't receive any of the same errors. I managed to not get any after some tweaking.

After dinner, I returned to finish things up with the downloading part. Given that I'd not received any errors, I figured everything was working except the data had nowhere to go. Once I added the functionality to actually download the file, I was rewarded by a nice PDF that looked identical to the one what was passed in (even to the point of keeping the interactive fields intact) with an additional line of text that was added by the code.

Damn that felt good. It took me days and days of struggling and rewriting and relearning and struggling and relearning and reading and writing and rewriting...you get the idea. We've all been there to some degree or another. The resulting code is below.

> 00-promises.js

    function processArray(typedArray) {
        // Load the PDF file (Uint8Array) into a PDFDocument object
        const pdfDoc = PDFDocumentFactory.load(typedArray);

        // Set font
        const [helveticaRef, helveticaFont] = pdfDoc.embedStandardFont(
            PDFStandardFonts.Helvetica,
        );

        const pages = pdfDoc.getPages();
        const page = pages[0];

        page.addFontDictionary('Helvetica', helveticaRef);

        const contentStream = pdfDoc.createContentStream(
            drawText(helveticaFont.encodeText('This text was added to the PDF with JavaScript!'), {
                x: 25,
                y: 25,
                size: 24,
                font: 'Helvetica',
                colorRgb: [0.95, 0.26, 0.21],
            }),
        );

        page.addContentStreams(pdfDoc.register(contentStream));

        const pdfBytes = PDFDocumentWriter.saveToBytes(pdfDoc);

        const pdfFileData = new Blob([pdfBytes], { type: "application/pdf" })

        const pdfURL = window.URL.createObjectURL(pdfFileData);

        document.getElementById("download_link").href = pdfURL;
    }

    // Use fetch() to load the pdf into buffer then to Uint8Array.
    fetch(pdfRequest)
        .then(response => response.arrayBuffer())
        .then(arrayBuffer => new Uint8Array(arrayBuffer))
        .then(Uint8Array => processArray(Uint8Array))
        .catch(err => console.log(err));

---

### 00:10 -+- de.Session

I said it before, and I'll say it again...

Although what I was dealing with, all things considered, isn't all *that* complex, it really feels spectacular to get over that hump after struggling with it for so long.

I can't wait to continue working on this and integrating this new knowledge / code into the actual pdform app.

Till then...

Hasta fuego, amigo!
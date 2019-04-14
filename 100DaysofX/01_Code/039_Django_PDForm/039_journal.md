# 2019-04-11 | #039

#100DaysofCode

---

## SELECT * FROM Project

### Abstract

    GOAL__ : Build web app for online fillable forms  
    GOAL_v0.2 : Insert data from database onto pre-made PDF template  

### Loxocache

    TASK__ : Collect tags from other documents  

--------◊--------

## SELECT * FROM Session

### Attenoir

    GOAL_039 : v0.2 - utilize pdf-lib and/or weasyprint  

#### Extras

- pass

---

## Session.log

--------◊--------

### 21:10 -+- Python - Weasyprint

Found what [looks like a good article](https://dev.to/djangotricks/how-to-create-pdf-documents-with-django-in-2019-5gb9) on using Weasyprint to generate the PDF. Going to see if I can make it work.

    $ brew install python3 cairo pango gdk-pixbuf libffi
    ==> Caveats
    ==> icu4c
    icu4c is keg-only, which means it was not symlinked into /usr/local,
    because macOS provides libicucore.dylib (but nothing else).

    If you need to have icu4c first in your PATH run:
    echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
    echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc

    For compilers to find icu4c you may need to set:
    export LDFLAGS="-L/usr/local/opt/icu4c/lib"
    export CPPFLAGS="-I/usr/local/opt/icu4c/include"

No errors this time, so that's good. However, I think the errors came up when I tried using the library in the app. I had tried using the library before so everything was already satisfied af. However, I think the brew install went much better this time. I thought that it errored out there last time. Here are some notes from that article:

--∫----

Simple PDF View
This snippet generates a donation receipt and shows it directly in the browser. Should the PDF be downloadable immediately, change content disposition from inline to attachment.

    # -*- coding: UTF-8 -*-
    from __future__ import unicode_literals

    from django.http import HttpResponse
    from django.template.loader import render_to_string
    from django.utils.text import slugify
    from django.contrib.auth.decorators import login_required

    from weasyprint import HTML
    from weasyprint.fonts import FontConfiguration

    from .models import Donation

    @login_required
    def donation_receipt(request, donation_id):
        donation = get_object_or_404(Donation, pk=donation_id, user=request.user)
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = "inline; filename={date}-{name}-donation-receipt.pdf".format(
            date=donation.created.strftime('%Y-%m-%d'),
            name=slugify(donation.donor_name),
        )
        html = render_to_string("donations/receipt_pdf.html", {
            'donation': donation,
        })

        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response

----∫--

    TASK√02.01 : Export versions of logo without address  

Exported + copied + renamed :
> orderform/static/jeffco_icon_only_*Color.png

    TASK√02.02 : Create and implement main.sass stylesheet
    TASK√02.03 : Add new stylesheet + link to Order Detail page  

    $ sass --watch orderdetail.scss orderdetail.css
    Compiled orderdetail.scss to orderdetail.css.

    TASK√02.04 : Successfully download a pdf using weasyprint  

Finally, at 12:53, I successfully downloaded a pdf using weasyprint. Shoutout to that tutorial for getting me there. I'm actually digging weasyprint a lot now. Crazy how coming back to something later can make your view / mindset regarding a thing change so drastically. The styling didn't work very well, but that might be because I didn't hook up the correct stylesheet. Will work on that now.

    TASK_02.05 : Make the page the correct size + display some styling  

I've been spinning my wheels for the past couple of hours because I couldn't get the styles to show up in the pdf. I just found while looking through the Weasyprint docs that there is a plugin specifically for use with static images inside of Django.

    $ pip install django-weasyprint
    lil' weeezy

Hmm it seems that it was already installed. I guess I just hadn't utilized it yet.

---

### 21:50 JavaScript - pdf-lib

    TASK√01.01 : Download the pdf-lib library + load it onto page  
    TASK_01.02 : Convert PDF to bytes / JavaScript Uint8Array  

Found this library called pdf-lib that looks promising for taking in a PDF template and inserting variable data onto it.

    TASK√01.01 : Download the pdf-lib library + load it onto page  

Downloaded both pdf-lib.js and pdf-lib.min.js and loaded into static folder of orderform app.

    CUE_01.01 : Display a PDF on the page  

I need to display the PDF that I created last time on a web page, though I may be able to get around this for now.

    TASK_01.02 : Convert PDF to bytes / JavaScript Uint8Array  

From the pdf-lib documentation:

    // This should be a Uint8Array.
    // This data can be obtained in a number of different ways.
    // In the browser, you could make a fetch() call and use res.arrayBuffer().
    const existingPdfDocBytes = ...

Time to convert some BYTES YOOOOOO! No time waste—only converted. I did learn a lot and now know what I want to learn next in Django (after the recursive relationships thing).

Some notes from *Eloquent JavaScript*:

    The first argument to fetch is the URL that should be requested. When that URL doesn’t start with a protocol name (such as http:), it is treated as relative, which means it is interpreted relative to the current document.

    When it starts with a slash (/), it replaces the current path, which is the part after the server name. When it does not, the part of the current path up to and including its last slash character is put in front of the relative URL.

### 22:10 -+- Django Static Files

Went down a short and sweet rabbit hole trying to find out where the static files were being served. I had missed one part of the url. This worked as the url to the pdf object:

    /static/orderform/pyramid_pdform_blank.pdf

So now I'm only getting the error that says that the object I'm using is not an Uint8Array.

    Uncaught Error: "PDFDocumentFactory.load()" must be called with an argument of type Uint8Array.

### 22:15 JavaScript Promises

A promise is an asynchronous action that may complete at some point and produce a value. It is able to notify anyone who is interested when its value is available.

    let fifteen = Promise.resolve(15);
    fifteen.then(value => console.log(`Got ${value}`));
    // Got 15

To get the result of a promise, the `then` method can be used. This registers a callback function to be called when the promise resolves and produces a value.

---

### 22:16 -+- de.Session

I got caught up for way too long on JavaScript promises. I can do everything successfully except return the value from the promise. I know I'm close but for some reason just can't quite wrap my head around it.

Hopefully a fresh mind will do the trick tomorrow.

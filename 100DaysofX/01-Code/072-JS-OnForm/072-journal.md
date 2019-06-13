# 2019-05-14 | #100DaysofCode

## Day 072 / 100

- [2019-05-14 | #100DaysofCode](#2019-05-14--100daysofcode)
  - [Day 072 / 100](#day-072--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.cache(2019-05)](#projectcache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-14)](#sessionsojourn2019-05-14)
    - [09:13 ~ Tisicky Thoughts](#0913--tisicky-thoughts)
    - [09:33 ~ SMTPjs](#0933--smtpjs)
      - [CDN](#cdn)
      - [Send an Email](#send-an-email)
      - [Attachments](#attachments)
    - [09:36 ~ Eellogofusciouhipoppokunurious Email](#0936--eellogofusciouhipoppokunurious-email)
    - [10:26 ~ Tergal Testing](#1026--tergal-testing)
    - [10:28 ~ Other Sciophilous Strategies](#1028--other-sciophilous-strategies)
    - [10:37 ~ Enantiomorphic Environment](#1037--enantiomorphic-environment)
    - [11:22 ~ Whiffler Weirdness](#1122--whiffler-weirdness)
    - [11:29 ~ Troubleshootin' Tautophony](#1129--troubleshootin-tautophony)
    - [12:17 ~ Still No Naissant](#1217--still-no-naissant)
    - [13:06 ~ New Neolatry](#1306--new-neolatry)
    - [15:32 ~ Git Branch Barathrum](#1532--git-branch-barathrum)
    - [16:13 ~ Rhizogenic Research](#1613--rhizogenic-research)
    - [00:06 ~ Neomorphic NoGo](#0006--neomorphic-nogo)

---

## SELECT * FROM Project

### Project.abstract

    GOAL-OnForm : Intuitive online PDF order form  

### Project.cache(2019-05)

    LVL1-054 : Set production Postgres to only accept connections from application  
    LVL1-051 : Install + Configure Nginx Web Server  
    LVL1-051 : Configure SSL on subdomain  

    LVL2-050 : Add success message to orderdetail  
    LVL2-050 : Implement email feature  
    LVL2-050 : Serialize model data  
    LVL2-050 : Display PDF on OrderDetail  
    LVL2-050 : Fix labels on OrderFormView  

    LVL3-044 : Ask if billing address is the same, if so, fill in automatically  
    LVL3-050 : Randomish numbering scheme for orders  
    LVL3-050 : Fix formatting of OrderDetail info @top - unless displaying PDF  

--------Ø--------

## SELECT * FROM Session

### Session.abstract

    GOAL-072 : Render PDF + save to filesystem  

    TASK-134 : Pass the Uint8Array from pdf-lib to Django / Python instead of using Node  
    TASK√134 : Edit PDF Template - take out top header line  

#### Session.cache

- [SMTPjs](https://www.smtpjs.com/)

---

## Session.sojourn(2019-05-14)

--------Ø--------

### 09:13 ~ [Tisicky](http://phrontistery.info/t.html) Thoughts

The largest obstacle to overcome in order to get this feature to work is getting the PDF to save to the server's filesystem.

Unless there is a way, and I can think or find out how to do it, to email directly from the client-side JavaScript code.

Right now I'm thinking that [converting the JavaScript Uint8Array to PythonIO](https://github.com/pypyjs/pypyjs/issues/171) might be too complicated for the application. Plus I'm not sure what I would do with it once I had the PythonIO. I might be able to run it through one of the Python PDF libraries, but obviously there's no guarantee that it would work well. Or at all.

Another way I'm thinking this could be done is by acting like a browser from the server in order to download the PDF. Using Python, I could have the server connect to the site and download the PDF automatically. I'm not sure how much is involved with that, though I don't imagine it's too hard to do.

That just doesn't seem like a very trustworthy method, prone to breaking or bugs.

I'm going to do some research on sending email with JavaScript.

---

### 09:33 ~ SMTPjs

[smtpjs](https://www.smtpjs.com/) seems like a decently simple library for sending email. It's free to use, but doesn't look to have that much documentation. Basically, the site gives this code to get started...

#### CDN

    <script src="https://smtpjs.com/v3/smtp.js">
    </script>

#### Send an Email

    Email.send({
        Host : "smtp.yourisp.com",
        Username : "username",
        Password : "password",
        To : 'them@website.com',
        From : "you@isp.com",
        Subject : "This is the subject",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );

Seems relatively straightforward. However, I don't see any way to attach a PDF attachment...actually nevermind, it has a little section on that...

#### Attachments

Want to send with attachments?, use the Attachments property:

    Email.send({
        SecureToken : "C973D7AD-F097-4B95-91F4-40ABC5567812",
        To : 'them@website.com',
        From : "you@isp.com",
        Subject : "This is the subject",
        Body : "And this is the body",
        Attachments : [
        {
            name : "smtpjs.png",
            path : "https://networkprogramming.files.wordpress.com/2017/11/smtpjs.png"
        }]
    }).then(
    message => alert(message)
    );

Dev Tip: If you want to send an attachment in base64 format, instead of passing "path" as a property, send a "data" property in dataUri format. in dataUri format. (Example coming soon!)

Sending multiple emails: The "To" property can be an array of email addresses, instead of just one.

I believe I will be sending using a dataUri format, so that line there will be important. Maybe I can even help them out with the example...if I can get it to work.

I downloaded the script just in case, but I will try it out using the CDN link first.

---

### 09:36 ~ [Eellogofusciouhipoppokunurious](http://phrontistery.info/e.html) Email

It does seem a little sketch to have smtpjs get the email and password with every request. I'm going to create a new throwaway email to test it out. I'm also going to run the local version of the script instead of using the CDN.

...mmm I might just try to use the gmail API to send emails. Doing some more research before deciding.

Created the following email:

    pyramidemailsender@gmail.com
    ********

Used the smtpjs encrypt tool to generate a security token:

****-****-****-****

---

### 10:26 ~ [Tergal](http://phrontistery.info/t.html) Testing

    Email.send({
        SecureToken : "****-****-****-****",
        To : 'tpyramidprint@cs.com',
        From : "pyramidemailsender@gmail.com",
        Subject : "Test Email Subject",
        Body : "Test email body."
    }).then(
    message => alert(message)
    );

Test Email = Sciophilous Subject

Sciophilous = thriving in or loving shady conditions.

---

### 10:28 ~ Other Sciophilous Strategies

I thought of another strategy that may bear some fruits with regards to using Python to send the email. This would involve rendering the PDF to the page, then somehow pulling that data down using Python.

With this idea I am making the assumption that the PDf will be rendered as some sort of static object on the html page. If that is the case, then I can write some Python to pull that data down and save it to a file.

This is similar, in essence, to the idea I mentioned above—the one involving using the Python to imitate a browser in order to download the PDF to the server.

I will pursue one of these next, if smtpjs doesn't work.

---

### 10:37 ~ [Enantiomorphic](http://phrontistery.info/e.html) Environment

Excited to test this new render-pdf.js out on top of the email functionality.

Copied over and refactored the js code to fit with the new layout I wrote yesterday. I'll probably have to do some forceful finagling to get it to work, as it is running in the browser this time.

Didn't work a couple of times at first (corrupt file) before I found a mistake I had made. Forgot to re-delete the contentStream line after fixing something. Let's try it now...

Still can't get it to work.

But I don't feel too bad about it, because I reverted the file back to its original form and it still didn't work.

Going to try a few other things to see if I can't get this thing to render.

---

### 11:22 ~ [Whiffler](http://phrontistery.info/w.html) Weirdness

Weird...

It works on the server; no errors come up in the console when the script is run locally.

I'm wondering if something changed when it went on the server.

Useful to know how to compare across commits—just add `/compare/commit1..commit2`:

    https://github.com/tobias-fyi/onform/compare/f7fdd82..48f5d9b

But I want to only look at one file - render_pdf.js...As far as I can tell, everything is the same...but still not working correctly.

----ƒ----

One thing I've wondered is if it's possible to utilize jinja inside of javascript...

Nope—at least not without any extra things—because it runs in the browser, while jinja is server-side. There are some libraries that imitate the jinja syntax and behavior for javascript. But that defeats the purpose for me.

---

### 11:29 ~ Troubleshootin' [Tautophony](http://phrontistery.info/t.html)

I'm honestly stumped at the moment. I'm going to go for my daily lunch walk soon. Maybe being outside for a bit will help—a clear head is a good thing.

Decided to try collecting the static files again...

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  master ● ?        19.05.14 ∫ 11:53:10
    ╰─ python manage.py collectstatic

    You have requested to collect static files at the destination
    location as specified in your settings:

        /Users/Tobias/workshop/onform/onform_pdf/static_assets

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes

    124 static files copied to '/Users/Tobias/workshop/onform/onform_pdf/static_assets',
    13 unmodified.

Still don't w4rk...

----ƒ----

Useful to be reminded that I can check if the file that is being requested is actually there by heading to that url. In this example, I went to the following URL and downloaded the pdf_template. It wasn't corrupted or anything like that...

    http://127.0.0.1:8000/static/pdf/pdf_template.pdf

This gives me the idea to save the dataURL (once I get this damn thing working) as a URL, which can then be easily accessed by Python to send the email. That would be pretty nice.

---

### 12:17 ~ Still No [Naissant](http://phrontistery.info/n.html)

Still haven't figured it out. At least I did something—I updated the blank pdf template, removing the double header lines as I said I would. At least there's that.

I tried running the dev server in the *real* iTerm, instead of the integrated one. I've had issues with it before. Now that I think about it, they were *specifically* issues with Django.

Now I'm getting this error when loading the orderdetail page.

    Error: "WinAnsi cannot encode "
    ""
        encodeUnicodeCodePoint http://127.0.0.1:8000/static/js/pdf-lib.js:7842
        encodeTextAsGlyphs http://127.0.0.1:8000/static/js/pdf-lib.js:45613
        encodeText http://127.0.0.1:8000/static/js/pdf-lib.js:45568
        processArray http://127.0.0.1:8000/static/js/render_pdf.js:314
        <anonymous> http://127.0.0.1:8000/static/js/render_pdf.js:353

Looking at line 314 of render_pdf...

    drawText(helveticaFont.encodeText(field_data.billing_info.phone.data), {
        x: field_data.billing_info.phone.pos[0],
        y: field_data.billing_info.phone.pos[1],
        size: font_size,
        font: 'Helvetica',
        colorRgb: custom_colors.jeffco,
    }),

So it looks like something to do with the billing phone again. I'm going to try removing the changes I made...

...holy shit...that [natiform](http://phrontistery.info/n.html) integrated terminal. I can't believe I fell for that again.

Although the error wasn't directly a result of the integrated terminal, I'm fairly certain that it was the reason why debug wasn't working correctly. I wasn't getting that error when the server was being run from within vscode. I remember that the last time I ran into this was also something to do with debugging. I was using the integrated vscode debugger to run the development server and it wasn't working correctly.

Wheew! Glad I wasn't stuck on that *all* day...only half of the damn day.

Time to go for a walk then come back and bang the shit out of this thing.

---

### 13:06 ~ New [Neolatry](http://phrontistery.info/n.html)

Now that it's working I get to try out the new layout with loops n functions and whatnot. So DRY!

Woooooow just got a shit ton of errors on reloading the application. Not sure why though maybe it has something to do with the allowed hosts?

    Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css. (Reason: CORS request did not succeed).

I got one of those for each script I tried to load. I'm going to try reloading the server; if that doesn't work I'll try setting the ALLOWED_HOSTS = [*].

Oh...oops. I wasn't connected to the internet...connected and *we're back, baby!*

----ƒ----

I added a console.log statement for the dataURL...

    blob:http://127.0.0.1:8000/4357cb67-5eca-694a-a792-9dab8f47a30f

And when I navigate to it, I'm prompted to download the file. It's the same file as when accessed via the Download PDF button. Nice!

I think that means I can write the Python code to access it that way. I really hope so. That would make my life much easier right now.

If I can use a button that runs the python code (a function-based view, perhaps?) while leaving the current page open to `orderdetail`, I think that would do it.

The reason I mention leaving the page open is because I remember reading that thedataURL only lasts as long as the function that created it is done working.

Or I can see if running the python code on the OrderDetail view (if I even can in a ClassBasedView) will run correctly. Another way of saying this is: I could try to write the Python code such that it only looks for the dataURL after the javascript is run, meaning the dataURL exists. That's like what I said earlier—a button that triggers another view without losing the dataURL.

- Here's a RealPython article on the [Requests module](https://realpython.com/python-requests/)
- Here's the [Requests module documentation](https://2.python-requests.org/en/stable/)

---

### 15:32 ~ Git Branch [Barathrum](http://phrontistery.info/b.html)

Starting a new git branch on which to save these changes.

    ╭─ onform » tobiasfyi » ~/workshop/onform »  master ● ?          19.05.14 ∫ 15:33:39
    ╰─ git branch renderer

    ╭─ onform » tobiasfyi » ~/workshop/onform »  master ● ?          19.05.14 ∫ 15:33:56
    ╰─ git checkout renderer
    M  00-Admin/onform.code-workspace
    M  onform_pdf/onform/urls.py
    M  onform_pdf/onform/views.py
    M  onform_pdf/onform_pdf/settings.py
    M  onform_pdf/static/js/render_pdf.js
    M  onform_pdf/templates/orderdetail.html
    Switched to branch 'renderer'

Pushed it to github...

    ╭─ onform » tobiasfyi » ~/workshop/onform »  renderer            19.05.14 ∫ 15:36:48
    ╰─ git push origin renderer
    Enumerating objects: 40, done.
    ...
    remote: Resolving deltas: 100% (13/13), completed with 12 local objects.
    remote: Create a pull request for 'renderer' on GitHub by visiting:
    remote:      https://github.com/tobias-fyi/onform/pull/new/renderer
    To github.com:tobias-fyi/onform.git
    * [new branch]      renderer -> renderer

Now time to get to it!

I already created a new view and urlpattern.

---

### 16:13 ~ [Rhizogenic](http://phrontistery.info/r.html) Research

Also, [Rhinotillexomania](http://phrontistery.info/r.html)...quite the word!

I'm digging Rhizogenic though - Producting or growing roots.

----ƒ----

I was thinking of using a function-based view, but I think I'm able to add functions to CBVs.  

Either way I'm first going to try out the RedirectView to see if that could potentially be what I'm looking for.

I just found some interesting info in Two Scoops of Django...

    What we find really useful, even on projects which use a lot of generic class-based views, is using the django.views.generic.View class with a GET method for displaying JSON, PDF or other non-HTML content.

    All the tricks that we’ve used for rendering CSV, Excel, and PDF files in function-based views apply when using the GET method. For example:

    from django.contrib.auth.mixins import LoginRequiredMixin from django.http import HttpResponse
    from django.shortcuts import get_object_or_404
    from django.views.generic import View

    from .models import Flavor
    from .reports import make_flavor_pdf

    class FlavorPDFView(LoginRequiredMixin, View):
        def get(self, request, *args, **kwargs):
            # Get the flavor
            flavor = get_object_or_404(Flavor, slug=kwargs['slug'])

            # create the response
            response = HttpResponse(content_type='application/pdf')

            # generate the PDF stream and attach to the response
            response = make_flavor_pdf(response, flavor) return response

    This is a pretty straight-forward example, but if we have to leverage more mixins and deal with more custom logic, the simplicity of django.views.generic.View makes it much easier than the more heavyweight views. In essence, we get all the advantages of function-based views combined with the object-oriented power that CBVs give us.

Interesting...

I'm going to see what "tricks" they've used for rendering CSV, Excel, and PDF files in FBVs. But even just the above is very valuable.

I hadn't really thought of looking for libraries to help out with this...here's some more from that section:

- django-extra-views
  - Another great CBV library, django-extra-views covers the cases that django-braces does not.
- django-vanilla-views
- A very interesting library that provides all the power of classic Django GCBVs in a vastly simplified, easier-to-use package. Works great in combination with django-braces.

----ƒ----

I also haven't visited the ReportLab section of the Django documentation in forever. The example provided creates a buffer, so I might be able to just pass in the bytes from javascript and save the file that way.

I had the thought a few weeks back—not sure if I've written it down yet or not, though I'm pretty sure I did mention it briefly—that I could use ReportLab with [Pillow](https://pillow.readthedocs.io/en/stable/). Pillow is basically the new version of PIL; it's a "friendly PIL fork". The graphics in ReportLab depends on PIL, and the fact that PIL hasn't been maintained in probably 5 years caused me to abandon ReportLab in the first place.

I'll give it a go when I get home.

---

### 00:06 ~ [Neomorphic](http://phrontistery.info/n.html) NoGo

I didn't end up having time to get back to it this evening. Here are some resources that I had opened and want to explore further when I get back to this project:

- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Requests](https://2.python-requests.org/en/stable/)
- DjangoTricks tutorial on [using WeasyPrint](https://djangotricks.blogspot.com/2019/01/how-to-create-pdf--documents-with-django-in-2019.html)
- [ReportLab tutorials](https://www.reportlab.com/documentation/tutorial/)
- [Mozilla Django tutorial: Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
- [Vue.js](https://vuejs.org/)

It is time for this guy to hit the ol' haystack.

Buenos nachos, amigos!

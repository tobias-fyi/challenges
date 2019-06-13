# 2019-05-18 | #100DaysofCode

    GOAL-05-18 ~ Write PDF from within OnForm Django application  

## Day 076/100 | 138/365

- [2019-05-18 | #100DaysofCode](#2019-05-18--100daysofcode)
  - [Day 076/100 | 138/365](#day-076100--138365)
    - [17:13 ~ OnForm.init](#1713--onforminit)
      - [LVL1-141 : Figure out how to pull data from database for PDF](#lvl1-141--figure-out-how-to-pull-data-from-database-for-pdf)
    - [16:29 ~ Making Scortative Sense](#1629--making-scortative-sense)
      - [LVL2-141 : Fix the Form Labels](#lvl2-141--fix-the-form-labels)
      - [LVL-141 : Add success message to confirm that PDF was generated and sent](#lvl-141--add-success-message-to-confirm-that-pdf-was-generated-and-sent)
      - [LVL-141 : Create EnviroVar for destination filepath](#lvl-141--create-envirovar-for-destination-filepath)
    - [00:20 ~ Ridotto Random](#0020--ridotto-random)
    - [00:41 ~ Email Engastrimyth](#0041--email-engastrimyth)
    - [00:47 ~ Gnight](#0047--gnight)

---- Tasks ----

    LVL1-141 : Figure out how to pull data from database for PDF  

    LVL2-141 : Fix the Form Labels  
    LVL2-141 : Add success message to confirm that PDF was generated and sent  
    LVL2-141 : Create EnviroVar for destination filepath  

---- Resources ----

- [ClassBasedViews in Django Docs](https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/)
- I was checking out the Schedule module to schedule an email to be sent tomorrow morning, when I came across [a bit of info](https://schedule.readthedocs.io/en/stable/faq.html#i-m-getting-an-attributeerror-module-object-has-no-attribute-every-when-i-try-to-use-schedule-how-can-i-fix-this) that might be very useful for me in troubleshooting the error I ran into earlier
- Some relevant / useful info from Dan Bader's Python [Schedule Module Documentation](https://schedule.readthedocs.io/en/stable/)

---- Sojourn ----

### 17:13 ~ OnForm.init

#### LVL1-141 : Figure out how to pull data from database for PDF  

I can think of two options for how to integrate this into a Django view. The first, easier way would be to simply copy that code into the view directly. That would get a little lengthy, which is not how it *should* be done. The second way would be to put that Python code into a new module that I then import into the view.

----ƒ----

Here is some very useful information on ClassBasedViews from the [Django Docs](https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/)...

    Specifying model = Publisher is really just shorthand for saying queryset = Publisher.objects.all().

    However, by using queryset to define a filtered list of objects you can be more specific about the objects that will be visible in the view.

---

### 16:29 ~ Making Scortative Sense

Ok I believe I know how to access the data now. I was a little confused at first, but explanations like the one above helped. I think the "model" object is the actual Order that gets fetched, which sounds glaringly obvious now that I write it down...

```python
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orderdetail.html"

    login_url = "login"
```

What I'm thinking is that I can access the individual fields of the Order object by calling them...

```python
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orderdetail.html"

    login_url = "login"

    form_data = [
        [model.school, 184, 680],
        [model.address, 142, 655],
        [model.city, 72, 631],
        [model.state_code, 360, 631],
        [model.zip_code, 485, 631],
        [model.phone, 92, 608],
        [model.school, 35, 483],
        [model.address, 35, 469],
        [f"{model.city}, {model.state_code} {model.zip_code}", 35, 455],
        [model.school, 35, 336],
        [model.address, 35, 322],
        [f"{model.city}, {model.state_code} {model.zip_code}", 35, 308],
        [model.box_qty1, 532, 490],
        [model.box_qty2, 532, 461],
        [model.box_qty3, 532, 343],
        [model.box_qty4, 532, 314],
        [model.billing_name, 84, 209],
        [model.billing_school, 130, 184],
        [model.billing_address, 142, 158],
        [model.billing_city, 72, 132],
        [model.billing_state, 360, 132],
        [model.billing_zip, 485, 132],
        [model.billing_phone, 84, 106],
        [model.billing_fax, 360, 106],
        [model.billing_email, 84, 82],
    ]

    def text_drawer(canv, array):
        """Write content of array to the canvas"""
        for item in array:
            text, x, y = item

            canv.drawString(x, y, text)

    # Create the buffer
    packet = io.BytesIO()

    # Create PDF with the text data using ReportLab
    c = canvas.Canvas(packet, pagesize=letter)
    text_drawer(c, form_data)
    c.showPage()
    c.save()

    # Seek to the beginning of the buffer
    packet.seek(0)
    pdf = PdfFileReader(packet)

    # Read in existing PDF
    form_blank = PdfFileReader(open("onform-blank.pdf", "rb"))
    output = PdfFileWriter()

    # Merge the two PDFs
    form = form_blank.getPage(0)
    text = pdf.getPage(0)
    form.mergePage(text)
    output.addPage(form)

    # Write the output to file
    work_path = os.getcwd()
    dest_path = "/Users/Tobias/workshop/onform/onform_pdf/static/pdf/pdfilled"
    os.chdir(dest_path)
    output_stream = open("onform-filled.pdf", "wb")
    output.write(output_stream)
    output_stream.close()
    os.chdir(work_path)
```

VSCode comes up with the suggestions when I start typing those in so I'm assuming that my thinking is correct.

Some things I just remembered while cleaning up the views file:

#### LVL2-141 : Fix the Form Labels  

#### LVL-141 : Add success message to confirm that PDF was generated and sent  

#### LVL-141 : Create EnviroVar for destination filepath  

----ƒ----

I'm running into an error when attempting to runsesrver with the DetailView as coded above.

    File "/Users/Tobias/workshop/onform/onform_pdf/onform/views.py", line 43, in <module>
        class OrderDetailView(LoginRequiredMixin, DetailView):
    File "/Users/Tobias/workshop/onform/onform_pdf/onform/views.py", line 89, in OrderDetailView
        text_drawer(c, form_data)
    File "/Users/Tobias/workshop/onform/onform_pdf/onform/views.py", line 82, in text_drawer
        canv.drawString(x, y, text)
    File "/Users/Tobias/.vega/onform/lib/python3.7/site-packages/reportlab/pdfgen/canvas.py", line 1564, in drawString
        text = text.decode('utf-8')
    AttributeError: 'DeferredAttribute' object has no attribute 'decode'

Tried searching it on google, and it seems to be something about that the string is already decoded. The only difference I can think of that might cause this is the fact that I'm passing in the `model.field` instances in directly. I could try assigning them to variables first, as it is being done in the script that worked previously.

...ah I also just remembered that I didn't change the file-name or, more importantly, the path in which to look for the new template pdf...

It would be good to create a system for saving and organizing the files. I started writing one...

```python
# Input file info
form_filename = "onform-blank.pdf"
form_path = "/Users/Tobias/workshop/onform/onform_pdf/static/pdf"
form_filepath = os.path.join(form_path, form_filename)

# Output file info
out_filename = "onform-filled.pdf"
out_path = "/Users/Tobias/workshop/onform/onform_pdf/static/pdf/pdfilled"
out_filepath = os.path.join(out_path, out_filename)
...
pdf_in = PdfFileReader(open(form_filepath, "rb"))
...
output_stream = open(out_filepath, "wb")
```

Time to see if that fixed it. If not I'll try to assign the variables as I mentioned above...

Nope. Still received the same error. That means it really does have to do with the text.

----ƒ----

I also just realized that I had not spun up the Postgres database...yet.

Started it up, trying again...nope.

I opened `reportlab/canvas.py` to line 1561 - drawString function:

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  renderer ● ?          19.05.18 ∫ 17:18:48
    ╰─ code /Users/Tobias/.vega/onform/lib/python3.7/site-packages/reportlab/pdfgen/canvas.py

```python
def drawString(self, x, y, text, mode=None, charSpace=0, direction=None):
    """Draws a string in the current text styles."""
    if sys.version_info[0] == 3 and not isinstance(text, str):
        text = text.decode('utf-8')
    #we could inline this for speed if needed
    t = self.beginText(x, y, direction=direction)
    if mode is not None: t.setTextRenderMode(mode)
    if charSpace: t.setCharSpace(charSpace)
    t.textLine(text)
    if charSpace: t.setCharSpace(0)
    if mode is not None: t.setTextRenderMode(0)
    self.drawText(t)
```

---

### 00:20 ~ Ridotto Random

Ridotto: Social gathering with music and dancing.

I was checking out the Schedule module to schedule an email to be sent tomorrow morning, when I came across [a bit of info](https://schedule.readthedocs.io/en/stable/faq.html#i-m-getting-an-attributeerror-module-object-has-no-attribute-every-when-i-try-to-use-schedule-how-can-i-fix-this) that might be very useful for me in troubleshooting the error I ran into earlier.

I happened to be checking out a question in the FAQ to learn how to schedule a Python script to run only once and saw this:

    I’m getting an AttributeError: 'module' object has no attribute 'every' when I try to use schedule. How can I fix this? ¶

    This happens if your code imports the wrong schedule module. Make sure you don’t have a schedule.py file in your project that overrides the schedule module provided by this library.

What I'm wondering is if the variable name `text` that I used is conflicting with something in the library or in the script. I changed it to `content`.

```python
def text_drawer(canv, array):
    """Write content of array to the canvas"""
    for string in array:
        content, x, y, font_size = string

        canv.drawString(x, y, content)
```

I also tried swapping out the model for the Order, like so...

```python
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    ...
    order_school = Order.school
    order_address = Order.address
    ...
```

This wasn't the reason I logged into my computer tonight, but I can't resist trying it out.

Nope still getting the error...

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  renderer ● ?       19.05.19 ∫ 00:31:44
    ╰─ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    Traceback (most recent call last):
    ...
    File "manage.py", line 18, in <module>
    File "/Users/Tobias/.vega/onform/lib/python3.7/site-packages/reportlab/pdfgen/canvas.py", line 1564, in drawString
        text = text.decode('utf-8')
    AttributeError: 'DeferredAttribute' object has no attribute 'decode'

Oh well. I know I'll figure it out. I guess it wouldn't really make sense that the import would be conflicting because the issue is being traced back to the imported module.

---

### 00:41 ~ Email Engastrimyth

Some relevant / useful info from Dan Bader's Python [Schedule Module Documentation](https://schedule.readthedocs.io/en/stable/).

----ƒ----

How can I run a job only once?

```python
def job_that_executes_once():
    # Do some work ...
    return schedule.CancelJob

schedule.every().day.at('22:30').do(job_that_executes_once)
```

----ƒ----

What about timezones?

Check out [this pull request](https://github.com/dbader/schedule/pull/16) where someone added the functionality. However, I don't think I would really need it as I am only sending from / to Mountain Time.

---

### 00:47 ~ Gnight

Hasta Buenos Noches, Amigos!

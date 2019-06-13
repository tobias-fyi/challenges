# 2019-05-20 | #100DaysofCode

    GOAL-05-20 ~ PDF creation + automatic email  

## Day 078/100 | 140/365

- [2019-05-20 | #100DaysofCode](#2019-05-20--100daysofcode)
  - [Day 078/100 | 140/365](#day-078100--140365)
    - [20:21 -+- Session.init](#2021----sessioninit)
    - [21:12 ~ Phoning Philonoist Philip](#2112--phoning-philonoist-philip)
    - [22:15 ~ Semelparous SuccYESSSSS](#2215--semelparous-succyesssss)

---- Tasks ----

    LVL1-OnForm : Add success message to confirm that PDF was generated and sent  
    LVL2-OnForm : Fix the Form Labels  
    LVL2-OnForm : Button / field to email another copy of PDF  
    LVL3-OnForm : Create email signature  
    LVL3-OnForm : Calculate time spent on developing OnForm  

    TASK√OnForm : Generate PDF from within Django  

---- Notes ----

    CUE-141 : Industrial Fasteners Online Order Form  

---- Resources ----

- [Supercharge Your Classes With super()](https://realpython.com/python-super/)
- [More Classy Views](http://ccbv.co.uk/projects/Django/2.1/django.views.generic.edit/CreateView/)

---- Selects ----

- Processing.py [tutorial on Getting Started](https://py.processing.org/tutorials/gettingstarted/)
- Emoji
  - Printing emojis in Python | [emoji.py](https://pypi.org/project/emoji/)
  - [List of all emoji as unicode](https://unicode.org/emoji/charts/full-emoji-list.html)

---- Sojourn ----

### 20:21 -+- Session.init

I just figured out I can easily access the data in more specific ways than I had last night. However, I still have to be able to get the Order object by its primary key so it will use the Order object specific to that Order. Right now the index is hardcoded into the print statement.

---

### 21:12 ~ Phoning Philonoist Philip

Philip said that I should be generating the PDF within the CreateView (Form) instead of the DetailView, as the latter is meant mostly to simply GET the data from the database.

We looked for the method that I could override (inherit?) from the [generic CreateView](http://ccbv.co.uk/projects/Django/2.1/django.views.generic.edit/CreateView/). Philip directed me to the form_valid method.

```python
def form_valid(self, form):
    """If the form is valid, save the associated model."""
    self.object = form.save()
    return super().form_valid(form)
```

I copied over the above into the CreateView / OrderFormView and took out the middle, replacing it with a print statement that printed out the form object.

    def form_valid(self, form):
        print(self.object)
        return super().form_valid(form)

    {'instance': <Order: This Guy>, '_validate_unique': True, 'is_bound': True, 'data': <QueryDict:
    ...
    'school': ['Lo School'], 'address': ['222 Middle Dr'], 'city': ['Top Town'], 'state_code': ['CO'], 'zip_code': ['89879'], 'phone': ['8979879879'], 'box_qty1': ['6'], 'box_qty2': ['3'], 'box_qty3': ['10'], 'box_qty4': ['20'], 'billing_name': ['This Guy'], 'billing_school': ['Junior High School'] ...
    ...
    <django.forms.renderers.DjangoTemplates object at 0x10c14ba20>, 'cleaned_data': {'school': 'Lo School', 'address': '222 Middle Dr', 'city': 'Top Town', 'state_code': 'CO', 
    ...
    'billing_email': 'highguy@low.edu'}}

I recognize that `cleaned_data` from Corey Schafer's tutorials. I believe I can access the data by calling a method that returns that dictionary...

For posterity, I'll put these here...one way I accessed the form data.

```python
order_school = form.cleaned_data["school"]
...
order_billing_email = form.cleaned_data["billing_email"]
```

---

### 22:15 ~ Semelparous SuccYESSSSS

IT FUCKING WORKED!

Philip was a huge help as I knew he would be. It was honestly really really nice just having him on the line hanging out. After he had helped me and I was off finagling the code to make it work, he was playing some video games. What a homie.

I was worried because we got another one of those decode errors from reportlab...the one that took up most of my day earlier this week.

        text = text.decode('utf-8')
    AttributeError: 'int' object has no attribute 'decode'

After a little bit I decided to do the obvious thing and wrap all of the object data in the `str()` function to make sure they were all strings. Lo and behold, that fixed it. I still received the warning about the PDFRead not being 0 indexed. After some research, I determined that it is not a fatal error and will not usually cause problems with the PDFs.

    [20/May/2019 22:32:09] "GET /favicon.ico HTTP/1.1" 404 2439
    PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected. [pdf.py:1736]
    [20/May/2019 22:34:44] "POST / HTTP/1.1" 302 0

Just for posterity's sake, once again, here is the code that made it W3RK...I ellipsed the middle parts of the data field definitions to save some space...

```python
def form_valid(self, form):
    response = super().form_valid(form)
    self.render_pdf(form)
    return response

def render_pdf(self, form):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from PyPDF2 import PdfFileReader, PdfFileWriter
    import io
    import os

    order_id = str(self.object.id)
    order_school = str(self.object.school)
    ...
    order_billing_email = str(self.object.billing_email)

    # [0] text | [1] x | [2] y | [3] font size
    text_data = [
        [order_school, 184, 680, 14],
        ...
        [order_billing_email, 84, 82, 14],
    ]

    def text_drawer(canv, array):
        """Write content of array to the canvas"""
        for string in array:
            content, x, y, font_size = string
            canv.drawString(x, y, content)

    packet = io.BytesIO()  # Create the buffer

    # Input file info
    form_file = "onform-blank.pdf"
    fp = "/Users/Tobias/workshop/onform/onform_pdf/static/pdf"
    form_path = os.path.join(fp, form_file)

    # Output file info
    out_file = f"onform-{order_id}.pdf"
    op = "/Users/Tobias/workshop/onform/onform_pdf/static/pdf/pdfilled"
    out_path = os.path.join(op, out_file)

    # Create PDF with the text data using ReportLab
    c = canvas.Canvas(packet, pagesize=letter)
    text_drawer(c, text_data)
    c.showPage()
    c.save()

    # Seek to the beginning of the buffer
    packet.seek(0)
    pdf = PdfFileReader(packet)

    # Read in existing PDF
    pdf_in = PdfFileReader(open(form_path, "rb"))
    pdf_out = PdfFileWriter()

    # Merge the two PDFs
    form = pdf_in.getPage(0)
    text = pdf.getPage(0)
    form.mergePage(text)
    pdf_out.addPage(form)

    # Write the output to file
    output_stream = open(out_path, "wb")
    pdf_out.write(output_stream)
    output_stream.close()
```

Now...I'm sure you (whoever may read this at some point in the distant far-out future) know what time it is...

Buenos Nachos Time, Amigas!

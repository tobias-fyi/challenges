# 2019-04-19 | #100DaysofCode

## Day 047 / 100

----∫----

- [2019-04-19 | #100DaysofCode](#2019-04-19--100daysofcode)
  - [Day 047 / 100](#day-047--100)
  - [---- SELECT * FROM Project ----](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.cache(2019-04)](#projectcache2019-04)
  - [---- SELECT * FROM Session(2019-04-19) ----](#select--from-session2019-04-19)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn](#sessionsojourn)
    - [21:48 -+- Session.init](#2148----sessioninit)
    - [22:56 -+- OnForm_PDF](#2256----onformpdf)
      - [Congifuring Postgres](#congifuring-postgres)
    - [23:33 -+- OnForm the Application](#2333----onform-the-application)
    - [01:04 -+- Django request/response cycle](#0104----django-requestresponse-cycle)
    - [01:22 -+- Static and Templates](#0122----static-and-templates)
    - [10:28 -+- Cont'd From Onform Docs](#1028----contd-from-onform-docs)
    - [10:29 -+- Templating](#1029----templating)
  - [A Model PDF](#a-model-pdf)
  - [Getting It Werkin](#getting-it-werkin)
  - [Mo(re)del](#moredel)
    - [Class-Based Views](#class-based-views)
  - [Render PDF](#render-pdf)
  - [Tests](#tests)
  - [(Crispy) Forms](#crispy-forms)
    - [00:02 -+- ModelFormSubmission](#0002----modelformsubmission)
    - [00:24 -+- OrderDetail](#0024----orderdetail)
    - [01:19 -+- JSON](#0119----json)

## ---- SELECT * FROM Project ----

### Project.abstract

    GOAL_ : Create a simple yet beautifully intuitive way to fill out a PDF form online  

### Project.cache(2019-04)

    TASK_043 : Preview the generated PDF on orderdetail.html  
    TASK√043 : Add billing_info + box qty fields to Django model  
    TASK√044 : Make the Django forms CRISPY AF  
    TASK_044 : Ask if billing address is the same, if so, fill in automatically  
    TASK√044 : Set up template inheritance  

    CUE_043.00 : Set up script to automatically post parts of this coding journal to blog app  
    CUE_01 : Save the output PDF into a django/postgres table  

--------ø--------

## ---- SELECT * FROM Session(2019-04-19) ----

### Session.abstract

    GOAL√01 : Rewrite the entire project in the new workflow  
    GOAL_02 : Display the generated PDF after form submission  

### Session.cache

    TASK_ : Figure out a way to have the navbar change the "active" page  

    IDEA_01 : Write CLI tool that sets up the basic Django template with a couple of commands  

    CUE_01 : Start learning Django REST Framework  
    CUE_02 : Read up on REST = Representational State Transfer  

---

## Session.sojourn

--------ø--------

### 21:48 -+- Session.init

Now that I have a reasonable Python development environment again, feeling good and going to start going through django for beginners in earnest.

---

### 22:56 -+- OnForm_PDF

Ok I feel warmed up enough to start on the real dealio, OnForm.

    $ cd ~/workshop/onform

Now to install some dependencies:

    $ pip install black
    /Users/Tobias/.pyenv/shims/black

    $ pip install pylint
    /Users/Tobias/.pyenv/shims/pip

    $ pip install ipython
    /Users/Tobias/.pyenv/shims/ipython

    $ pip install psycopg2-binary
    Successfully installed psycopg2-binary-2.8.2

    $ pip install django
    Successfully installed django-2.2 pytz-2019.1 sqlparse-0.3.0

    $ pip install django-crispy-forms
    $ pip install django-extensions

Ok that's good for now.

--ø--

Time to get django up and running around a bit. Naming the project `OnForm_PDF` because I want to be able to easily distinguish between the project and the app.

    $ django-admin startproject onform_pdf

--ø--

#### Congifuring Postgres

Initialized new server called `onform`.

    postgres=# CREATE DATABASE onform;
    CREATE DATABASE
    postgres=# \c onform
    You are now connected to database "onform" as user "******".

    onform-# CREATE USER **** WITH SUPERUSER PASSWORD '****';
    > CREATE USER

Connected to pgAdmin with the following settings:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "onform",
            "USER": "****",
            "PASSWORD": "****",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

Then migrated now that Postgres connected succyessfully.

    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
        Applying contenttypes.0001_initial... OK
        ...
        Applying sessions.0001_initial... OK

Solid.

    IDEA_01 : Write CLI tool that sets up the basic Django template with a couple of commands  

---

### 23:33 -+- OnForm the Application

Stoked that I set everything up correctly such that black autoformatted everything. I didn't even notice it happening.

    $ python manage.py startapp onform

> onform_pdf/settings.py

    INSTALLED_APPS = [
        ...
        "onform.apps.OnformConfig",
    ]

---

### 01:04 -+- Django request/response cycle

    “URL -> View -> Model (typically) -> Template”

I was going to start small, but then just decided to send it with the complete app as it is, and then some.

---

### 01:22 -+- Static and Templates

    # templates / static files and directories...
    $ cd onform

    $ mkdir -p templates/onform
    $ touch templates/onform/base.html
    $ touch templates/onform/orderform.html

    $ mkdir -p static/onform
    ...
    # more creation / rsyncing (everything and the rsync?)

Decided to organize the static assets in a more neat / scalable manner.

    $ tree
    .
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── static
    │   └── onform
    │       ├── assets
    │       │   ├── jeffco_icon_only_fullColor.png
    │       │   └── jeffco_icon_only_oneColor.png
    │       ├── css
    │       │   ├── main.css
    │       │   ├── main.css.map
    │       │   ├── main.scss
    │       │   ├── orderdetail.css
    │       │   ├── orderdetail.css.map
    │       │   └── orderdetail.scss
    │       ├── js
    │       │   ├── on_order.js
    │       │   ├── orderform.js
    │       │   ├── orders.js
    │       │   ├── pdf-lib.js
    │       │   ├── pdf-lib.min.js
    │       │   └── pdf_gen.js
    │       └── pdf
    │           └── pdf_template.pdf
    ├── templates
    │   └── onform
    │       ├── base.html
    │       ├── onorder.html
    │       ├── orderdetail.html
    │       ├── orderform.html
    │       └── orders.html
    ├── tests.py
    ├── urls.py
    └── views.py

    9 directories, 29 files

Cleaned up the static directory by putting everything into more specific directories. Also used template inheritance. This is the first time I've had 2 blocks per page: 1 for the content and 1 for the scripts.

    {% block onform_js %}
    <script src="../../static/onform/js/pdf-lib.js"></script>
    <script src="../../static/onform/js/pdf_gen.js"></script>
    {% endblock onform_js %}

Here's another paragraph from the book that I thought was a nice explanation / reminder:

    “It’s worth repeating this pattern since you’ll see it over and over again in Django development: Templates, Views, and URLs. The order in which you create them doesn’t much matter since all three are required and work closely together. The URLs control the initial route, the entry point into a page, such as /about, the views contain the logic or the “what”, and the template has the HTML. For web pages that rely on a database model, it is the view that does much of the work to decide what data is available to the template.”

---

### 10:28 -+- Cont'd From Onform Docs

    TASK_01 : Sync up the two documents once entry is complete  

---

### 10:29 -+- Templating

As in the book, I'll be setting up a project-wide templates directory instead of having it in the specific app. I did the same for a project-wide static directory.

    TEMPLATES = [
        {
            ...
            "DIRS": [os.path.join(BASE_DIR, 'templates')],
            ...
        }
    ]

    ...

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), "/var/www/static/"]

After moving the template and static files, the project looks a little something like this:

    $ tree
    .
    ├── manage.py
    ├── onform
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── static
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── onform_pdf
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-37.pyc
        │   ├── settings.cpython-37.pyc
        │   ├── urls.cpython-37.pyc
        │   └── wsgi.cpython-37.pyc
        ├── settings.py
        ├── static
        │   └── onform
        │       ├── assets
        │       │   ├── jeffco_icon_only_fullColor.png
        │       │   └── jeffco_icon_only_oneColor.png
        │       ├── css
        │       │   ├── main.css
        │       │   ├── main.css.map
        │       │   ├── main.scss
        │       │   ├── orderdetail.css
        │       │   ├── orderdetail.css.map
        │       │   └── orderdetail.scss
        │       ├── js
        │       │   ├── on_order.js
        │       │   ├── orderform.js
        │       │   ├── orders.js
        │       │   ├── pdf-lib.js
        │       │   ├── pdf-lib.min.js
        │       │   └── render_pdf.js
        │       └── pdf
        │           └── pdf_template.pdf
        ├── templates
        │   ├── base.html
        │   ├── onorder.html
        │   ├── orderdetail.html
        │   ├── orderform.html
        │   └── orders.html
        ├── urls.py
        └── wsgi.py

    12 directories, 38 files

---

## A Model PDF

> onform/models.py

    from django.db import models
    from django.utils import timezone


    class Order(models.Model):
        order_id = models.AutoField(primary_key=True)
        order_school = models.CharField(max_length=140)
        order_address = models.CharField(max_length=140)
        order_city = models.CharField(max_length=80)
        order_state = models.CharField(max_length=2)
        order_zip = models.CharField(max_length=5)
        order_phone = models.CharField(max_length=10)

        box_qty1 = models.IntegerField(blank=True)
        box_qty2 = models.IntegerField(blank=True)
        box_qty3 = models.IntegerField(blank=True)
        box_qty4 = models.IntegerField(blank=True)

        order_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.order_id


    class Billing(models.Model):
        order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
        bill_name = models.CharField(max_length=70)
        bill_school = models.CharField(max_length=140)
        bill_address = models.CharField(max_length=140)
        bill_city = models.CharField(max_length=80)
        bill_state = models.CharField(max_length=2)
        bill_zip = models.CharField(max_length=5)
        bill_phone = models.CharField(max_length=10)
        bill_fax = models.CharField(max_length=10)
        bill_email = models.EmailField()

        def __str__(self):
            return self.bill_name

Time to make some serious migratory action...

    $ python manage.py makemigrations
    Migrations for 'onform':
        onform/migrations/0001_initial.py
            - Create model Order
            - Create model Billing

    $ python manage.py sqlmigrate onform 0001
    BEGIN;
    --
    -- Create model Order
    --
    CREATE TABLE "onform_order" ("order_id" serial NOT NULL PRIMARY KEY, "order_school" varchar(140) NOT NULL, "order_address" varchar(140) NOT NULL, ... "box_qty4" integer NOT NULL, "order_date" timestamp with time zone NOT NULL);
    --
    -- Create model Billing
    --
    CREATE TABLE "onform_billing" ("id" serial NOT NULL PRIMARY KEY, "bill_name" varchar(70) NOT NULL, ... "order_id_id" integer NOT NULL);
    ALTER TABLE "onform_billing" ADD CONSTRAINT
    ...
    CREATE INDEX "onform_billing_order_id_id_2fd3acd2" ON "onform_billing" ("order_id_id");
    COMMIT;

Looks good after some minor finagling. Time to make like trees and migrate.

    $ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, onform, sessions
    Running migrations:
        Applying onform.0001_initial... OK

Bang Bomb Booooom!

Looking at the new tables on pgAdmin I see that the ForeignKey automatically inserts "id" on the end, so right now it reads as "order_id_id". Minor gripe but I want to fix it.

    $ python manage.py makemigrations
    Did you rename billing.order_id to billing.order (a ForeignKey)? [y/N] y
    Migrations for 'onform':
        onform/migrations/0002_auto_20190419_1800.py
            - Rename field order_id on billing to order

    $ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, onform, sessions
    Running migrations:
        Applying onform.0002_auto_20190419_1800... OK

Solid. Reminds me of my days working at IQMS but much more fun. Part of me wishes I had started learning this back then so I could've learned more from how their databases are designed. Oh well. At least I made it here!

Wow...the server actually started up without any more errors! I was not expecting it to work first try after the migrations.

---

## Getting It Werkin

Just because the server ran without error does not mean there won't be any errors with the site. For example, the one I got is below, which I'm not sure the reason because if you see the template directory it tried, it should be there...oh I just thought of it. The templates / static should be in the project_root, but I put them in the admin "app".

    Template does not exist at:
    orderform.html

    ## Template-loader postmortem
    Django tried loading these templates, in this order:

    Using engine django:

    django.template.loaders.filesystem.Loader: /Users/Tobias/workshop/onform/onform_pdf/templates/orderform.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /Users/Tobias/.pyenv/versions/onform/lib/python3.7/site-packages/django/contrib/admin/templates/orderform.html (Source does not exist)
    django.template.loaders.app_directories.Loader: /Users/Tobias/.pyenv/versions/onform/lib/python3.7/site-packages/django/contrib/auth/templates/orderform.html (Source does not exist)

After moving the templates and static directories, it gave me another error saying `templates/templates/base.html` does not exist. I fixed the "extends" line on each, as seen below, and we are golden as a pony, boiii!

    {% extends 'templates/base.html' %}
    # do not need the /templates/ segment
    {% extends 'base.html' %}

I didn't even have to fix the image link, as it showed up straight away.

--ø--

This time I'm going to try inputting the initial data via the form.

I might reconsider my decision to put the billing info in a separate model, but I'll try it out this way for now.

--ø--

Going to create the admin user now so I don't forget later on.

    $ python manage.py createsuperuser
    Username (leave blank to use 'tobias'): onform
    Email address: ooonform@inform.info
    Password:
    Password (again):
    Superuser created successfully.

Make the onform app editable through admin site:

    from django.contrib import admin

    from .models import Order, Billing

    admin.site.register(Order)
    admin.site.register(Billing)

---

## Mo(re)del

Now that I'm thinking about the models a bit more, I'm thinking I could improve their design quite a bit just by making it more of a relation between a table that holds the contact / billing info and one that holds the orders. 

This would make more sense. The relation would be one (contact) to many (orders).

However, I think it is good to keep the billing and contact info separate.

That looks better, I think...

    class Contact(models.Model):
        id = models.AutoField(primary_key=True)
        school = models.CharField(max_length=140)
        address = models.CharField(max_length=140)
        city = models.CharField(max_length=80)
        state_code = models.CharField(max_length=2)
        zip_code = models.CharField(max_length=5)
        phone = models.CharField(max_length=10)

        def __str__(self):
            return self.school


    class Billing(models.Model):
        id = models.AutoField(primary_key=True)
        contacts = models.ManyToManyField(Contact)

        name = models.CharField(max_length=70)
        school = models.CharField(max_length=140)
        address = models.CharField(max_length=140)
        city = models.CharField(max_length=80)
        state = models.CharField(max_length=2)
        zip = models.CharField(max_length=5)
        phone = models.CharField(max_length=10)
        fax = models.CharField(max_length=10, blank=True)
        email = models.EmailField()

        def __str__(self):
            return self.bill_name


    class Order(models.Model):
        id = models.AutoField(primary_key=True)
        contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

        box_qty1 = models.IntegerField(blank=True)
        box_qty2 = models.IntegerField(blank=True)
        box_qty3 = models.IntegerField(blank=True)
        box_qty4 = models.IntegerField(blank=True)

        order_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.order_date

And it's time to make the migration again.

    $ python manage.py makemigrations
    You are trying to add a non-nullable field 'contact' to order without a default; we can't do that (the database needs something to populate existing rows).

    Please select a fix:
    1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    2) Quit, and let me add a default in models.py

    Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
    Type 'exit' to exit this prompt
    >>> 1

    Migrations for 'onform':
    onform/migrations/0003_auto_20190419_1940.py
        - Create model Contact
        - Rename field bill_address on billing to address
        ...
        - Add field contact to order

I put in 1, because I figure if need be I can set contact.id to be the default jeffco address. But as it stated at the top, this is only to populate existing rows.

I was going to put the results of sqlmigrate but they are sooooooper long.

    $ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, onform, sessions
    Running migrations:
        Applying onform.0003_auto_20190419_1940... OK

---

### Class-Based Views

Implemented my very first ClassBasedView:

    from django.views.generic import TemplateView, DetailView
    from django.views import View

    from .models import Order, Billing
    from .forms import OrderForm, BillingForm


    class OrderFormView(TemplateView):
        template_name = "orderform.html"

--ø--

    TASK_ : Figure out a way to have the navbar change the "active" page  

---ø--

## Render PDF

    TASK_ : Try to find the code that renders the Django Documentation as PDF  
    TASK_ : Reinstall Node.js via nvm  
    TASK_ : Install pdf.js  
    TASK_ : Integrate pdf.js into app  

---

## Tests

Finally I get to learn about implementing tests! I mean I've done a little but my experience with them is very minimal.

> onform/tests.py

    from django.test import TestCase

    class SimpleTests(TestCase):
        def test_orderform_status_code(self):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)

        def test_orderdetail_status_code(self):
            response = self.client.get("/orderdetail/")
            self.assertEqual(response.status_code, 200)

    $ python manage.py test
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    F.
    ======================================================================
    FAIL: test_orderdetail_status_code (onform.tests.SimpleTests)
    ----------------------------------------------------------------------
    ...

The reason the test failed is because I haven't implemented the orderdetail page yet.

---

## (Crispy) Forms

Edited the forms to match the new models.

> onform/forms.py

    from django.forms import ModelForm
    from .models import Contact, Billing, Order


    class ContactForm(ModelForm):
        class Meta:
            model = Contact
            fields = "__all__"


    class BillingForm(ModelForm):
        class Meta:
            model = Billing
            fields = "__all__"


    class OrderForm(ModelForm):
        class Meta:
            model = Order
            fields = "__all__"

> settings.py

    INSTALLED_APPS = [
        ...
        "crispy_forms",
        "onform.apps.OnformConfig",
    ]

    CRISPY_TEMPLATE_PACK = "bootstrap4"

OKAY...now that I'm dealing with the view side of things, to make it easier and quicker on me right now I'm going to make one big model / form.

I don't really need it separated out right now except for personal aesthetic or whatever.

> onform/models.py

    Migrations for 'onform':
    onform/migrations/0004_auto_20190419_2017.py
        - Remove field contact from order
        - Add field bill_address to order
        ...
        - Delete model Contact

    $ python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, onform, sessions
    Running migrations:
        Applying onform.0004_auto_20190419_2017... OK

> onform/forms.py

    class OrderForm(ModelForm):
        class Meta:
            model = Order
            fields = "__all__"

> onform/urls.py

    from django.urls import path

    from . import views

    app_name = "onform"
    urlpatterns = [
        # Home Page - Envelope Order form
        path("", views.orderform, name="orderform"),
        # View all subitted orders
        path("orders/", views.Orders.as_view(), name="orders"),
        # View individual order detail TODO: display as PDF
        path(
            "orders/<int:envelopeorder_id>/",
            views.OrderDetail.as_view(),
            name="orderdetail",
        ),
    ]

> onform/models.py

    from django.db import models
    from django.utils import timezone


    class Order(models.Model):
        contact_school = models.CharField(max_length=140)
        contact_address = models.CharField(max_length=140)
        contact_city = models.CharField(max_length=80)
        contact_state_code = models.CharField(max_length=2)
        contact_zip_code = models.CharField(max_length=5)
        contact_phone = models.CharField(max_length=10)

        box_qty1 = models.IntegerField(blank=True)
        box_qty2 = models.IntegerField(blank=True)
        box_qty3 = models.IntegerField(blank=True)
        box_qty4 = models.IntegerField(blank=True)

        bill_name = models.CharField(max_length=70)
        bill_school = models.CharField(max_length=140)
        bill_address = models.CharField(max_length=140)
        bill_city = models.CharField(max_length=80)
        bill_state = models.CharField(max_length=2)
        bill_zip = models.CharField(max_length=5)
        bill_phone = models.CharField(max_length=10)
        bill_fax = models.CharField(max_length=10, blank=True)
        bill_email = models.EmailField()

        order_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.bill_name

---

### 00:02 -+- ModelFormSubmission

I worked my pirate booty off this afternoon and got a design / layout going that is literal light-years ahead of what I had before.  

The one thing I'm stuck on right now is saving to the database via the form. I didn't want to write an SQL INSERT statement, but figure it's a good way of troubleshooting. The reason I've done it before is because I've run into errors where I can't access the database unless there is an existing record. So I guess I'll do it.

Another reason to do it is it gives me a record to use in testing out the orderdetail view / template.

> onform_pdf(root)/01-Docs/SQL/initial_insert.psql

    INSERT INTO onform_order (
        id,
        school,
        ...
        order_date
    )

    VALUES (
        '1',
        'El Dorado High School',
        ...
        '2019-03-28'
    )

    INSERT 0 1
    Query returned successfully in 61 msec.

Alrighty then, we have our initial record thanks to the initial inser†.

--ø--

I just found [this section on populating the database with test / initial data](https://docs.djangoproject.com/en/2.2/howto/initial-data/) and I definitely want to set this up so I don't have to write out custom SQL every time.

---

### 00:24 -+- OrderDetail

Sweet! The page loaded with the correct data first try!

However, the styling is all funked up for some reason. Not sure why as orderdetail.html is in the same directory as orderform.html.

Get out your pistols—it's troubleshootin' time!

I saw in the debug log that it was adding the extra bits of the url onto the string it used to look for the static files.

    [20/Apr/2019 06:35:22] "GET /static/css/main.css HTTP/1.1" 304 0
    Not Found: /orders/static/js/render_pdf.js
    [20/Apr/2019 06:35:22] "GET /orders/static/js/render_pdf.js HTTP/1.1" 404 2393
    Not Found: /orders/static/js/pdf-lib.js

Figured it was something to do with how I set up the static files directory / url. Found this snippet in the django docs that would explain why it's not working:

    {% load static %}
    <img src="{% static "my_app/example.jpg" %}" alt="My image">

I had hardcoded in the img src like so:

    <img src="../static/assets/..." id="logo-mono">

Fixed all the instances of my mistake...and...viola!

Lookin pretty good.

--ø--

This is definitely something I'll be needing to [read up on more when I start to deploy](https://docs.djangoproject.com/en/2.2/howto/static-files/deployment/) this bad boi.

---

### 01:19 -+- JSON

Last thing I'm going to work on tonight is [converting (serializing) my Django model data](https://docs.djangoproject.com/en/2.2/topics/serialization/#id2) into [JSON](https://docs.python.org/3/library/json.html#module-json), which I can then pass into my javascript in order to render the pdf with all the data embedded.

I also have been meaning to start perusing Django REST Framework and REST frameworks in general. I think this will be a good way to get started.

However, I do want to finish a version of this app that I feel comfortable putting into production before learning more new stuff'n'things.

I found [a tutorial on serializing django model data](https://www.django-rest-framework.org/tutorial/1-serialization/) on the DRF site.

I've downloaded a few good books from aqiliq already and one of them is the one on [Building APIs with DRF](http://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/introduction.html).

    CUE_01 : Start learning Django REST Framework  

And because I really haven't started learning about REST in general yet...

    CUE_02 : Read up on REST = Representational State Transfer  

It seems like Class Based Views will be something to learn in order to really understand DRF.

--ø--

Not going to get too far tonight but still going to get started.

> onform/serializers.py

    from django.core.serializers import serialize

    data = serialize("json", Order)

    with open("order_inform.json", "w") as out:
        json_serializer.serialize(Order.objects.get(pk=1), stream=out)

--ø--

I'm going to make a commit to Git before I do anything else because I have the two main pages of the app working.

..well not completely working yet. The form hasn't been able to save to the database for some reason.

Hasta fuego, amigos!
# 2019-03-25 | #022

\#100DaysofCode

- [2019-03-25 | #022](#2019-03-25--022)
  - [Today's Menu](#todays-menu)
    - [Main Course](#main-course)
    - [CUE_](#cue)
    - [Extras](#extras)
  - [Session Log](#session-log)
    - [15:21 -+- Session Init](#1521----session-init)
    - [15:26 -+- Admin](#1526----admin)
    - [15:31 -+- Shell Models](#1531----shell-models)
    - [15:47 -+- Admin Again](#1547----admin-again)
    - [16:01 -+- Shell Again](#1601----shell-again)
    - [22:19 -+- Session Finité](#2219----session-finit%C3%A9)

---

## Today's Menu

### Main Course

    GOAL_ : Get a working prototype going for the online PDF form  
        --∫--
    TASK√01 : Python - just write something to a PDF - Hell o'Whireld!
    TASK_02 : Python - take input + place it in correct location on PDF
    TASK_03 : Write HTML forms (probably [Django forms](https://docs.djangoproject.com/en/2.1/topics/forms/)) to gather all input data
    TASK_04 : Python - save input data to database
    TASK_05 : Python - write input data to PDF (also using some CSS, JS and/or HTML)
    TASK_06 : Python - email finished PDF out to relevant parties
    TASK_07 : JavaScript - display the filled out PDF (not necessary for prototype)

--------∫--------

### CUE_  

    TASK_02 : Python - take input + place it in correct location on PDF

--------∫--------

### Extras

---

## Session Log

### 15:21 -+- Session Init

Changed the name of the model to FormData.  
Gotta follow those conventions.

### 15:26 -+- Admin

Created superuser:

    $ python manage.py createsuperuser
    > shhhhhh

### 15:31 -+- Shell Models

Changed some things in models.py:

    $ python manage.py makemigrations
    > Migrations for 'pdform':
        pdform/migrations/0004_auto_20190328_2240.py
        - Rename field requester on formdata to request_by
        - Rename field date_requested on formdata to request_date
        - Rename field type on formdata to request_type

    $ python manage.py migrate
    > python manage.py migrate
        Operations to perform:
        Apply all migrations: admin, auth, contenttypes, pdform, sessions
        Running migrations:
        Applying pdform.0004_auto_20190328_2240... OK

And even more...

    $ python manage.py makemigrations
    > Migrations for 'pdform':
        pdform/migrations/0005_auto_20190328_2301.py
            - Alter field phone on formdata
            - Alter field zip_code on formdata

Using the Python shell to test out database models.  
(Here's where iPython comes in):

    In [1]: from pdform.models import FormData

    In [2]: from django.contrib.auth.models import User

    In [3]: FormData.objects.all()
    Out[3]: <QuerySet []>

### 15:47 -+- Admin Again

I keep receiving an error when I try to access the admin area of the app.  
Spent too much time already digging around trying to find the error.

So apparently it was happening because I was using the VSCode debugger to run the dev server and it was logging something at a level which it shouldn't. Easy as that.

Aaaaand, we're in!

### 16:01 -+- Shell Again

    $ python manage.py shell

    In [1]: from pdform.models import FormData

    In [2]: from django.contrib.auth.models import User

    In [3]: User.objects.all()
    Out[3]: <QuerySet [<User: pyradev>]>

    In [4]: user = User.objects.all().first()

    In [5]: user.id
    Out[5]: 1

I was having trouble with the database / models earlier, so I [wrote some SQL](sql_statements.psql) to manually insert a couple of records as seen below.

    In [6]: FormData.objects.all()
    Out[6]: <QuerySet [<FormData: FormData object (1)>, <FormData: FormData object (2)>]>

Accessing the data within the record:

    In [7]: data1 = FormData.objects.first()

    In [8]: data1.request_date
    Out[8]: datetime.datetime(2019, 3, 28, 6, 0, tzinfo=<UTC>)

    In [9]: data1.request_type
    Out[9]: 'envelope'

    In [10]: data1.request_by
    Out[10]: <User: pyradev>

    In [11]: data1.request_by.email
    Out[11]: 'dev@pyramidprint.graphics'

    In [12]: exit()

### 22:19 -+- Session Finité

Ok nooooowwww...  

Hoping I can finally get down to the meat of the app—the actual forms.

Next time, on Planet Form!

Hasta Onfuego, Amigo!

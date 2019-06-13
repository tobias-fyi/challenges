# 2019-05-19 | #100DaysofCode

    GOAL-05-19 ~ Finish JeffCo Email functionality  

## Day 077/100 | 139/365

- [2019-05-19 | #100DaysofCode](#2019-05-19--100daysofcode)
  - [Day 077/100 | 139/365](#day-077100--139365)

---- Tasks ----

    LVL1-139 : Write PDF from within OnForm Django application  
    LVL1-139 : Figure out how to pull data from database for PDF  

    LVL2-139 : Add success message to confirm that PDF was generated and sent  
    LVL2-139 : Create EnviroVar for destination filepath  
    LVL2-139 : Fix the Form Labels  
    LVL2-139 : Button / field to email another copy of PDF  

---- Notes ----

    CUE-139 : Industrial Fasteners Online Order Form  

---- Resources ----

- I found [this answer on StackOverflow](https://stackoverflow.com/questions/53826653/django-access-the-single-model-object-passed-into-detailview-for-manipulation-o) that deals with reportlab
- A little [more research](https://docs.djangoproject.com/en/2.2/ref/class-based-views/mixins-single-object/) has told me that I need to override the generic class `get_object()` method
- Here's a useful line from the [Django docs](https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-display/#detailview):
  - While this view is executing, self.object will contain the object that the view is operating upon.
  - Based on that, I can use self.object. Here is what I came up with based on the [Django docs section](https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/#performing-extra-work) on "performing extra work in DetailView"
- I found some useful info on what I should research to get the [success message functionality](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/) working

---- Selects ----

- Coding Camisade
  - Khan Academy [course on algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
  - [Flashbake](https://craphound.com/news/2009/02/13/flashbake-free-version-control-for-writers-using-git/) (Git for writing)
  - CSS Viewport Units
    - [CSS Tricks Article](https://css-tricks.com/fun-viewport-units/)
    - [Sitepoint](https://www.sitepoint.com/css-viewport-units-quick-start/)
- [Destroy All Software](https://www.destroyallsoftware.com/screencasts)
- [Monica Personal CRM](https://www.monicahq.com/)
- Soundtrack
  - [Atlantis: The Lost Empire OST](https://www.youtube.com/playlist?list=PLmheWFkK-ELRSIJ8aG8PCZ4HSqciD4W9_)
  - My set from [Desert Party 2019](https://www.mixcloud.com/tobiasfyi/playlists/desert-party-2019/)
  - [Breakbot @ Salle Wagram for Cercle](https://youtu.be/PY6WIpCD1L4)
    - The [tracklist](https://www.1001tracklists.com/tracklist/14hrf1lt/breakbot-chateauform-salle-wagram-france-cercle-2018-10-01.html)

---- Sojourn ----

### 21:38 ~ Warmup Wakerife

Wakerife: Wakeful; indisposed to sleep.

Back at it in the studio after what seems like ages. Didn't get to get down on some coding yesterday evening and all day today for a variety of reasons. Going to do some W3RK tonight.

To start things off, I'm going to write a script that Capitalizes directories.

I had started making something similar based off of Corey Schafer's file renaming tutorial. It's cool going back to old scripts I wrote when I was just starting out. It is when I can really see how much I've improved.

I'm trying out a slightly different method than what I did before when I wrote it along with Corey's video. This time I used `os.scandir()` instead of `os.listdir()`. I'm also trying out the whole double underscore name / main dealio...

```python
def rename():
    import os

    work_dir = os.getcwd()

    with os.scandir(work_dir) as dirs:
        for d in dirs:
            if not d.name.startswith(".") and d.is_dir():
                old_name = d.name
                print(old_name)
                new_name = old_name.capitalize()
                print(new_name)

                # os.rename(old_name, new_name)

if __name__ == "__main__":
    rename()
```

I would like to turn this into a CLI tool, most likely using Click...actually what am I saying? Of course it will be with Click.

For now, however, I'll just copy it into the target directory and run it from there.

I copied it into my downloads directory and tried it out. I wanted to test it out by simply printing the old and new names before committing to renaming the directories...

    ╭─ Fineyedesign » tobiasfyi » ~/Downloads                           19.05.19 ∫ 22:22:45
    ╰─ python dirs_capitalize.py
    Music
    Music
    Development
    Development
    Books
    Books
    software
    Software
    visual
    Visual
    documents
    Documents

I'm gonna go for it.

Sweet. Time to get to le Djängo

----∫----

### 22:27 -+- Cont'd In OnForm Journal

---

## 2019-05-19 | OnForm

## ---- SELECT * FROM OnForm(2019-05-19) ----

### OnForm.abstract

    GOAL-05-19 : Finish JeffCo Email functionality  

    TASK√142 : Copy entry to fyi journal  

### OnForm.cache

- Soundtrack
  - [Atlantis: The Lost Empire OST](https://www.youtube.com/playlist?list=PLmheWFkK-ELRSIJ8aG8PCZ4HSqciD4W9_)
  - My set from [Desert Party 2019](https://www.mixcloud.com/tobiasfyi/playlists/desert-party-2019/)
  - [Breakbot @ Salle Wagram for Cercle](https://youtu.be/PY6WIpCD1L4)
    - The [tracklist](https://www.1001tracklists.com/tracklist/14hrf1lt/breakbot-chateauform-salle-wagram-france-cercle-2018-10-01.html)
- Coding Camisade
  - Khan Academy [course on algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)
  - [Flashbake](https://craphound.com/news/2009/02/13/flashbake-free-version-control-for-writers-using-git/) (Git for writing)
  - CSS Viewport Units
    - [CSS Tricks Article](https://css-tricks.com/fun-viewport-units/)
    - [Sitepoint](https://www.sitepoint.com/css-viewport-units-quick-start/)
  - [Classy Views and stuff](http://ccbv.co.uk/projects/Django/2.2/django.views.generic.detail/DetailView/)
  - [Destroy All Software](https://www.destroyallsoftware.com/screencasts)
  - [Monica Personal CRM](https://www.monicahq.com/)

---

### 22:30 ~ Django Deipnosophy

Deipnosophy: Learned dinner conversation.

This time I'm not going to forget to start up the Postgres server before trying to run / catch it. I just want to confirm that the JSON file used in settings.py has the correct information. I believe that the information is actually still the information on the server...

----ƒ----

Confirming that login information is correct by logging into the db via pgAdmin.

...yep the information in the JSON file is incorrect for my local environment. I updated the password. Time to try this again....Nope. Same error. I'm going to take a step backward and try to run the server without the new stuff in the detailview.

First attempt failed because I had an old URL left in there for when I was going to put the PDF render logic in a separate URL from the detail view. Commented that out as well and tried again...

What a wonderful sight!

    ╭─ onform » tobiasfyi » ..nform/onform_pdf »  renderer ● ?       19.05.19 ∫ 22:46:57
    ╰─ python manage.py runserver
    ...
    System check identified no issues (0 silenced).
    May 19, 2019 - 22:47:42
    Django version 2.2, using settings 'onform_pdf.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Looks like everything is workin just fyyyyiiiine...

I tried uncommenting only the top part where I assign the variables. i.e. `order_school = Order.school`. I also changed the capitalization on Order. That errored out. Changed it back and trying again...

Ok that did not error out. I wonder if I can print one of these to the console.

That actually was very useful!

    /Users/Tobias/workshop/onform/onform_pdf/onform/views.py changed, reloading.
    ...
    <django.db.models.query_utils.DeferredAttribute object at 0x1090ac5f8>
    ...

So it looks like I am not actually accessing the data itself. Quick Google search of DeferredAttribute...

---

### 23:05 ~ Query Quangocracy

I found the DeferredAttribute class in the Django source code:

```python
class DeferredAttribute:
    """A wrapper for a deferred-loading field. When the value is read from this object the 
    first time, the query is executed."""
...
```

I wonder if I still need to extract the value from the object.

---

### 23:51 ~ Query Quartering

I was correct in my statement that I still needed to extract the values from the object. I added the `.values()` expression / method and got a promising result.

    order_school = Order.objects.values("school")
    ===
    <QuerySet [{'school': 'Junior Senior High School'}, {'school': 'Cool School'}, {'school': 'El Dorado High School'}, {'school': 'This School'}]>

However, this still retrieves all of the rows in the database.

    order_school = Order.objects.get(pk=pk).values()
    ===
    NameError: name 'pk' is not defined

It errored out when I tried passing in the pk. Now I need to figure out how to get the pk of the current order...

I found [this answer on StackOverflow](https://stackoverflow.com/questions/53826653/django-access-the-single-model-object-passed-into-detailview-for-manipulation-o) that actually deals with reportlab as well. Could be useful.

```python
def get_object(self, queryset=None):
    obj = super(ProductView, self).get_object(queryset=queryset)
    self.generate_pdf(obj)
    return obj

def generate_pdf(self, obj):
    from reportlab.pdfgen import canvas
    p = canvas.Canvas(response)
    name = obj.product_name
    p.drawString(100, 100, name )
    p.showPage()
    p.save()
    print(p)
```

A little [more research](https://docs.djangoproject.com/en/2.2/ref/class-based-views/mixins-single-object/) has told me that I need to override the generic class `get_object()` method.

Here's a useful line from the [Django docs](https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-display/#detailview):

    class django.views.generic.detail.DetailView¶
        While this view is executing, self.object will contain the object that the view is operating upon.

Based on that, I can use self.object. Here is what I came up with based on the [Django docs section](https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/#performing-extra-work) on "performing extra work in DetailView":

```python
def get_object(self):
    order = super().get_object()
    print(order.school)
    return order
```

Let's see what happens...nothing happened. Going to do some more forceful finagling.

So I implemented the generate_pdf example above...

```python
def get_object(self, queryset=None):
    if queryset is None:
        queryset = self.get_queryset()
    obj = super(OrderDetailView, self).get_object(queryset=queryset)
    self.generate_pdf(obj)
    return obj

def generate_pdf(self, obj):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from PyPDF2 import PdfFileReader, PdfFileWriter
    import io
    import os

    school = obj.school
    print(school)
```

However, nothing prints out. That tells me that it's not actually running.

---

### 01:17 ~ Spinning Sarmentum

I found some useful info on what I should research to get the [success message functionality](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/) working...

I am still at the same exact place as when I started...

    <django.db.models.query_utils.DeferredAttribute object at 0x11110b630>

Though I guess I did manage to access the dictionary containing all of the fields. That is maybe where I should be looking. But I'm feeling like there's something rather fundamental that I'm missing here...

    address = order_address.values()
    ===
    AttributeError: 'DeferredAttribute' object has no attribute 'values'

---

### 01:45 ~ Class Cimelia

I feel like my lack of deep knowledge into the deeper deepness of classes and object-oriented programming in general is really showing.

I'll talk to Philip tomorrow and try to figure this out.

Buenos noches, amigos!

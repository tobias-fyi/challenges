# 2019-04-10 | #038

\#100DaysofCode

---

## Today's Menu

### Main Course

    GOAL_38 : First prototype of tobias.fyi  

#### Abstract

*Info not specific to this session.*  
i.e. project-wide tasks + reminders + notes.

    TASK_meta : Set up project-wide templates  
    TASK_meta : Add functionality to import CSV with django-import-export  
    TASK_meta : Look into building blog / portfolio section with Django CMS integration  

- Project-wide templates in [this tutorial on RealPython](https://realpython.com/get-started-with-django-1/)
- List of [useful Django packages](https://vsupalov.com/favorite-django-packages-2019/)
  - [django-import-export](https://django-import-export.readthedocs.io/en/latest/)

--------ƒ--------

### SELECT * FROM session

#### Soundtrack

- pass

#### Extras


---

## Session Log

--------ƒ--------

### Session.init

I went ahead and created the superuser to be able to log into the admin site, as I had foregone that previously.

    $ python manage.py createsuperuser

And once I get my models up and running I'll need to register them in order to view them through the admin site.

> tobiasfyi/admin.py

    admin.site.register(Model)

---

### 23:28 -+- MoreModels

As stated in the previous session.log (with an update), the model relationship for this simple prototype will be as follows:

Project > (ForeignKey / one-to-many) > Activity > (Foreignkey / one-to-many) > Entry

Decided to keep it simple by using only ForeignKeys. I thought for some reason that this would be the primary key of the "one" in the relationship, which means I didn't think through it all that thoroughly.

Also, I do want each Project to be able to be associated with more than one activity, but not the other way around.

    from django.db import models
    from django.utils import timezone


    class Project(models.Model):
        name = models.CharField(max_length=48)

        def __str__(self):
            return self.name


    class Activity(models.Model):
        name = models.CharField(max_length=48)
        project = models.ForeignKey(Project, on_delete=models.PROTECT)

        def __str__(self):
            return self.name


    class Entry(models.Model):
        time_in = models.DateTimeField(default=timezone.now)
        activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
        entry = models.TextField()
        time_out = models.DateTimeField(blank=True)
        duration = models.DurationField(default=960, blank=True)
        timestamp = models.DateTimeField(default=timezone.now, editable=False)

        def __str__(self):
            return self.time_in

Now time to make them migrations.

    $ python manage.py makemigrations
    Migrations for 'sajourn':
    sajourn/migrations/0002_auto_20190411_0000.py
        - Create model Activity
        - Create model Entry
        - Create model Project
        - Delete model SajournalEntry
        - Add field project to activity

---

### 00:42 -+- Recursive Relationships

I didn't end up applying the migration yet because I just had an interesting thought:

    CUE_01 : Create a new model specifically for the time info associated with each entry  

This would potentially allow me to work with the timestamps in a more flexible way. I'm just trying to think of good ways to do that arithmetic automatically—basically have ways to make each entry take as little time as possible.

The time_in / time_out / duration could be auto-generated from either the time_in or the time_out. I'm hoping it won't be too hard to reference another record in the same table, because the time_in could auto-fill with the time_out of the previous record.

This led me to another idea, which I'm pretty sure that I've had before but probably never put down on keys:

When a new entry is submitted (with the required time_out stamp), the system automatically generates a new record with the time_in field filled in with the time_out of the record that was just submitted.

    IDEA_01 : The Rolling UI - one area of the app has a continuous UI that has the functionality described above—next record is auto-generated and the user is taken to the next entry screen immediately.  

I'm thinking that having the timestamp as a separate model would be a good way to start building this. The Timestamp record would be a "child" of the Entry.

Ahaaa I think that this is how I can do it (from the [Django docs](https://docs.djangoproject.com/en/2.2/ref/models/fields/#foreignkey)):

    To create a recursive relationship – an object that has a many-to-one relationship with itself – use models.ForeignKey('self', on_delete=models.CASCADE).

I'd be hesitant to set on_delete=models.CASCADE on a recursive relationship like that. Would that not be potentially catastrophic? i.e. if the very first record was deleted and cascaded deletion *all the way down*.

----ƒ----

I want to continue my thought from earlier and dig deeper into how this separate EntryTime model would make working with the time records more flexible (and hopefully / potentially more powerful). I had imagined that the app would have a way to nest Entry records within a larger period of time yet still have specific timestamps for each of those child timestamps. 

For example, on a day when I'm working at a client's office for a four-hour period, I will have child activities during that time such as going to the bathroom, eating a snack, or taking some supplements. I don't want to have to create a new parent record for each one of those—i.e. I'd like to have the parent record's association cascade down the hierarchy so I would be able to see, by looking only at one of the child records, that I was doing that sub-activity while doing work for the client.

I will continue these thoughts in tomorrow's session.

---

### 01:24 -+- to_field

Some changes I made that are mostly unrelated to the above train of thought:

1. Set the ForeignKey.to_field on each of the child models, which reqired me to...
2. Set unique=True on the to_field for the parent models

Here is an example of that change:

    class Activity(models.Model):
        name = models.CharField(max_length=48, unique=True)
        project = models.ForeignKey(
            Project, on_delete=models.PROTECT, to_field=Project.name
        )

        def __str__(self):
            return self.name

---

### 01:38 -+- Session.bye

Got a little excited about finally getting into some valuable and fascinating ideas regarding the architecture of the project and let the time go by a little bit...

...*just a little bit*.

I'd like to try the migration once before hitting the pillow. That means I'll have to figure out the recursion later.

Meh...getting some errors from the way I set up the datetime arithmetic. Guess it'll hafta wait.

Hasta luego, amiga!
# 2019-04-21 | #100DaysofCode

## Day 049 / 100

- [2019-04-21 | #100DaysofCode](#2019-04-21--100daysofcode)
  - [Day 049 / 100](#day-049--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.journal(2019-04-21)](#sessionjournal2019-04-21)
    - [Loxocache](#loxocache)
    - [22:35 -+- Session.init](#2235----sessioninit)
    - [22:40 -+- Classy Views](#2240----classy-views)
    - [22:44 -+- Saving Private Info](#2244----saving-private-info)
    - [23:26 -+- Saving Private Info, Pt 2](#2326----saving-private-info-pt-2)
    - [23:55 -+- Testing for Peace](#2355----testing-for-peace)
    - [01:36 -+- DoneZO](#0136----donezo)

---

## SELECT * FROM Project

### Project.abstract

    GOAL__ : Create a simple way to fill out a PDF form online

### Project.loxocache(2019-04)

    TASK_047 : Figure out a way to have the navbar change the "active" page  
    TASK_044 : Ask if billing address is the same, if so, fill in automatically  
    TASK_047 : Figure out a way to have the navbar change the "active" page  
    TASK_048 : Write to the database via the form  
    TASK√048 : Write to the database via the admin page  
    TASK_048 : Add checkbox / functionality for same address as above  
    TASK_048 : Fix black so it autoformats  

    CUE_043 : Set up script to automatically post parts of this coding journal to blog app  
    CUE_043 : Save the output PDF into a django/postgres table  
    CUE_047 : Start learning Django REST Framework  
    CUE_047 : Read up on REST = Representational State Transfer  

    IDEA_01 : Write CLI tool that sets up the basic Django template with a couple of commands  

--------ø--------

## SELECT * FROM Session

### Session.abstract

    GOAL_049 : Display the generated PDF after form submission  

#### Session.cache

- pass

---

## Session.journal(2019-04-21)

### Loxocache

    TASK√049 : Implement ClassBasedViews for all current views  
    TASK_049 : Implement tests  

--------ø--------

### 22:35 -+- Session.init

First thing to do this session is get all of the CBV (ClassBasedViews) working.

    TASK√049 : Implement ClassBasedViews for all current views  

---

### 22:40 -+- Classy Views

After a little adjustment I got them all to work, including the DetailView, which I was a little worried about after not being able to figure it out before. Now I see how convenient these generic views are, I didn't have to write all of that post / reverse / etc code. Literally two lines in each view. Nice...

    class OrderFormView(CreateView):
        template_name = "orderform.html"
        form_class = OrderForm


    class OrderDetailView(DetailView):
        model = Order
        template_name = "orderdetail.html"


    class OrdersView(ListView):
        model = Order
        template_name = "orders.html"
        context_object_name = "orders"

Ok...I guess the last one has three. Huge increase, I know. A whole 50% more code!

---

### 22:44 -+- Saving Private Info

I still need to get that form written to the DB. So far the CBV I wrote doesn't do so, but I'm about to figure out why!

Alright I've successfully written the CreateView such that the form fields displayed on the orderform page are coming from the view and not the form I created previously (though I still want to use all the labels and such I wrote into the form). However, it still will not write to the dang databass.

Not enough bass...and now the OrderFormView has three lines! Adding way too much code...

    class OrderFormView(CreateView):
        model = Order
        template_name = "orderform.html"
        fields = "__all__"

Ok I logged in as the admin and attempted to write a new order to the database. The first time I tried, django threw me an error saying that there is already a record with id=1. I went into pgAdmin and changed the current one to id=0, after which I was able to save a new record.

    TASK√048 : Write to the database via the admin page  

---

### 23:26 -+- Saving Private Info, Pt 2

    TASK_048 : Write to the database via the form  

I'm wondering now if that was the reason why the form wasn't saving the data to the database. It wasn't giving me an error, but maybe it wouldn't for that particular action...unless I'm doing what I'm supposed to be and implementing tests. I'll go back and do that after I get it working...?

    TASK_049 : Implement tests  

Hmm...I guess not because I'm still just getting thrown back to the same page and no data has been written to the database.

Man I've tried so many different things to get it to redirect me to the correct page—orderdetail.html—but nothing seems to work and nothing is writing to the database. There aren't any errors either so not much for me to go off of.

Well I found something, though I don't really know if I can do anything useful with it. I saw that when I'm in the admin site and I navigate around I get this error (after a bunch of tracebacks):

    ConnectionResetError: [Errno 54] Connection reset by peer

Ah ok I think that was because I had two tabs open—one of the admin and one of the orderform page.

---

### 23:55 -+- Testing for Peace

Ok I still can't figure it out so I'm going to try creating some tests to see if I can automate this discovery process.

Ok after a ton of writing I ran my first test of the content of the order, which came back ok.

Now after writing the tests for the views, I'm running into one failure with the DetailView. It's saying that the page is not there, which I corroborated by trying to navigate to that URL and receiving a 404 error.

Duh, I was trying to get to /orders/1/, forgetting that I'd changed the id of the initial record to 0 in order to update with a new record or two.

Trying again...nope still getting the error. It works on my end, but the tests create their own temporary database to write to so the tests wouldn't see my records anyways.

But I'm definitely seeing firsthand how useful tests are. Now I don't have to enter in the data every time I want to test it out. Thank goshdaaggit for that!

I also found that I shouldn't put a date in because it has a default.

----ø----

I'm seeing the same thing that I was running into...the order is not being created for whatever reason, so there is no orderdetail for that order.

Why isn't it being created?

Tried making a new migration in case I accidentally changed the model, but it said that there were no changes detected (whew..).

    $ python manage.py makemigrations onform
    No changes detected in app 'onform'

What's weird is it's *only* throwing an error at the response.status_code, because there is an earlier test that gets the absolute URL for that exact URL and it doesn't throw any error.

    def test_post_detail_view(self):
        response = self.client.get("/orders/1/")
        no_response = self.client.get("/orders/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Ed U. Cator")
        self.assertTemplateUsed(response, "orderdetail.html")

---

### 01:36 -+- DoneZO

Ok well I've been spinning my wheels here for too long. I'll come back to this tomorrow with a (hopefully) fresh mind. Damn you, you database interface!

JK I <3 U!

Buenos nachos, amigos
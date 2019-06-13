# 2019-05-27 | #100DaysofCode

    GOAL-05-27 ~ Start building Iterum / Learn web scraping with Python  

## Day 085/100 | 147/365

- [2019-05-27 | #100DaysofCode](#2019-05-27--100daysofcode)
  - [Day 085/100 | 147/365](#day-085100--147365)
    - [13:41 ~ I'm Bringing Ubique Back](#1341--im-bringing-ubique-back)
    - [14:12 ~ Starting Seriatim](#1412--starting-seriatim)
    - [14:46 ~ Secundum Simplification](#1446--secundum-simplification)
    - [15:21 ~ Quasi Real](#1521--quasi-real)
    - [16:04 ~ Vim Videlicet](#1604--vim-videlicet)
    - [22:36 ~ Productivity At Night](#2236--productivity-at-night)
    - [22:49 ~ Organizational Productivity](#2249--organizational-productivity)

---- Tasks ----


---- Notes ----


---- Resources ----

- [vim tutorial / article](https://danielmiessler.com/study/vim/)
  - Here's [the GitHub repo for his .vim directory](https://github.com/danielmiessler/vim)
- [virtualenvwrapper documentation](https://virtualenvwrapper.readthedocs.io/en/latest/)

---- Selects ----


---- Sojourn ----

---

### 13:41 ~ I'm Bringing Ubique Back

Added another try..except to catch the case when an unknown tag is returned.

```python
try:
    bad_tag = bs_object.noneTag.anotherNone
except AttributeError as e:
    print("Tag was not found")
else:
    if bad_tag == None:
        print("Tag was not found")
    else:
        print(bad_tag)
```

Next up, it's time to make things a little more organized and reusable.

> web_scraping/scrapebs3.py

```python
def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs_obj = BeautifulSoup(html.read(), features="html.parser")
        title = bs_obj.body.h1
    except AttributeError as e:
        return None
    return title
```

When I run it, I get a more useful result compared to what happened before, when I had to look through the `html` object in order to find out that there actually was no `<h1>` tag on the page.

---

### 14:12 ~ Starting Seriatim

I managed to write a script that pulls the table of words from a Phrontistery page. Next, I'll need to access the contents of each row, and add those to some sort of dictionary. I will probably try setting the data structure up as a dictionary because I could set the word as the key and the definition as the value.

I tried a few different things to extract the table data from the table object. The best result I got was with a loop over the `.descendants` generator...

```python
for row in table.descendants:
    print(row)
```

This ended up, after all the recursion was done, with...

    <tr><td>vulgo
    <td>commonly; popularly
    </td></td></tr>
    <td>vulgo
    <td>commonly; popularly
    </td></td>
    vulgo

    <td>commonly; popularly
    </td>
    commonly; popularly

I can see that I got the word `vulgo` and the definition `commonly; popularly` after all of it. But I'm still unclear on how to access those for each row.

Ok I was able to whittle it down to the text only...

    print(table.tr.td.get_text())
    ====
    ╭─ iterum » tobiasfyi » ..rum/web_scraping                   19.05.27 ∫ 14:29:41
    ╰─ python get_table.py
    alternatim
    alternately
    ana
    in equal quantities
    ...
    videlicet
    to wit; namely
    vulgo
    commonly; popularly

One rather ugly way I could do this is to set the odd indexes of this to the keys and the even to the values. I'm going to try some other, more intelligent methods, before resorting to that. I bet there's a clever way of doing it that I'm not seeing right now. I mean I did just get started with scraping.

---

### 14:46 ~ Secundum Simplification

Instead of making a new request to the web page every time I run the script, I just copied over the table from the page source to use that as practice. I also copied over the entire page source to use as more real-world practice.

Aaaahaha the entire page is based off of a table. That's why I'm getting all of these crazy ending tabledata tags...

For some reason vscode just doesn't autoformat the html after about row 473. interesting...in the interest of learning the basics, I'm only going to use the extracted table html for now...baby steps.

---

### 15:21 ~ Quasi Real

I added the standard html template and inserted the table into the body to make the example a little more realistic.

Now that I'm using a file, I had to change to code a little to open and access the contents.

---

### 16:04 ~ Vim Videlicet

Started messing around with Vim in order to add some text into the messages on the JeffCo order form. I can see how it would be a really great thing to learn. I want to at least learn how to be comfortable and somewhat efficient using it, though I'm not going to spend too much time doing that right now unless I find a great reason to do so.

I referenced [this tutorial / article](https://danielmiessler.com/study/vim/) to start learning what I'm doing. Here's [the GitHub repo for his .vim directory](https://github.com/danielmiessler/vim).

---

### 22:36 ~ Productivity At Night

Wow it's been hard to get started on something. I've been futzing for the past half hour at least.

I think it's mainly due to me not knowing exactly what I want to work on. I feel like I should work on Motif or AptDraft but for some reason they're just not pulling me especially hard.

I need to get warmed up with something, that's what I need to do.

Or I just need to choose something to work on...

---

### 22:49 ~ Organizational Productivity

Organizing the journal from today is a nice little exercise.

I'm feeling like AptDraft is going to be where I head tonight...though Motif is right there, just hanging.

Ok...flippitty floppotty is on the property. Motif time.

However, Motif does not necessarily mean only WordPress. It would be fun to play around with some other ideas as well. For example, I could use the Motif store as a basis to learn React or practice with Django.

Feels rather good to organize things a little bit; get my mind in order. I'm removing the neuraldraft virtualenv in order to move the project directory to sketchbox. I have a feeling if I try to just move things around and not delete/recreate the venv, things might get funked up.

Well I just found something pretty neat in the [virtualenvwrapper documentation](https://virtualenvwrapper.readthedocs.io/en/latest/):

    postmkvirtualenv is run when a new environment is created, letting you automatically install commonly-used tools.

That's nice to know. There are also pre-removal and post-removal scripts that run as well.

----∫----

After navigating into the neuraldraft directory I found that it only has an old db-data directory inside. That's it.

    ╭─ motif » tobiasfyi » ~/workshop                                        19.05.27 ∫ 23:06:19
    ╰─ rmvirtualenv neuraldraft
    Removing neuraldraft...
    Did not find environment /Users/Tobias/.vega/neuraldraft to remove.

    ╭─ motif » tobiasfyi » ~/workshop                                        19.05.27 ∫ 23:06:30
    ╰─ rmvirtualenv sketchbook/neuraldraft
    Removing sketchbook/neuraldraft...

I also removed the old CS50Flask and badjango project directories. I'll leave sketchbox in there for now.

I want to have a place to hold the saleor project files so I can reference them easily. I think using Saleor effectively is a little above my current experience level, but I love how organized and aesthetic it is and want to be able to draw inspiration and code from it as needed. I guess I could just leave it in the motif project dir for now.

    ╭─ tobiasfyi » ~/.vega/sketchbox                                                             19.05.27 ∫ 23:17:57
    ╰─ rmvirtualenv sketchbox/CS50Flask
    Removing sketchbox/CS50Flask...

I'm cleaning out my closet.

Buenos cleaning, amigos!

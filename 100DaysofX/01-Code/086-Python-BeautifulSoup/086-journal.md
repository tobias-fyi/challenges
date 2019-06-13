# 2019-05-28 | #100DaysofCode

    GOAL-05-28 ~ Improve the Python Web Scraper  

## Day 086/100 | 148/365

- [2019-05-28 | #100DaysofCode](#2019-05-28--100daysofcode)
  - [Day 086/100 | 148/365](#day-086100--148365)
    - [00:09 ~ It's All a Practice](#0009--its-all-a-practice)
    - [00:42 ~ Password Proletariat](#0042--password-proletariat)
    - [00:56 ~ Resource Radiciform](#0056--resource-radiciform)
    - [01:36 ~ Split Definite](#0136--split-definite)
    - [01:58 ~ Multiple Page Mischief](#0158--multiple-page-mischief)
    - [02:41 ~ Better Luck Next Time - But Really](#0241--better-luck-next-time---but-really)

---- Tasks ----


---- Notes ----


---- Resources ----

- Corey Schafer's Python [Tips and Tricks video](https://youtu.be/C-gEQdGVXbk)

---- Selects ----


---- Sojourn ----

### 00:09 ~ It's All a Practice

Decided to practice some Python. Starting out with Corey's Python [Tips and Tricks video](https://youtu.be/C-gEQdGVXbk).

OOoooooOOh and I just thought of something that I should definitely work on—smartass.life.

Over the past month or so I haven't been doing a great job with my journaling, at least on the data side of things in airtable. I have lots of journaling inside of my coding session journals, but I don't have that in the form I would like. i.e. It's not in a dataset that can be easily accessed.

On top of the journaling functionality, writing a script to pull data from my coding journals and formatting it to fit into the database would be a very good thing for me to do. I think this will help reinvigorate my journaling practice.

It's all a practice.

----∫----

I'm going to finish Corey's video first. I created the file within the OOP dir because the example I'm going through at time of creation has to do with classes.

> ../08-Knowledge_Base/Python/OOP/tips_tricks.py

Took me a little while because I didn't realize that the string being passed into the `.setattr()` function is the *actual* key or value.

```python
class Word:
    pass

word = Word()
term = "igniform"  # first key
defin = "having the shape or form of fire"  # first value

setattr(word, term, defin)

print(term)
print(word.igniform)
```

    ╭─ Fineyedesign » tobiasfyi » ..ython/Python_OOP »  master ● ?                     19.05.28 ∫ 00:27:07
    ╰─ python tips_tricks.py
    igniform
    having the shape or form of fire

Pretty neat. This can also be accessed with the `.getattr()` function:

```python
setattr(word, term, defin)
keyword = getattr(word, term)
print(keyword)
# having the shape or form of fire
```

If the data is in the form of a dictionary, which it will be in the case of this word database (at least when working with it in Python), a loop can be used to set the attributes of the class instance...

```python
word_info = {"term": "igniform", "definition": "having the shape or form of fire"}

for key, value in word_info.items():
    setattr(word, key, value)

print(word.term)
print(word.definition)
```

    ╭─ Fineyedesign » tobiasfyi » ..ython/Python_OOP »  master ● ?                              19.05.28 ∫ 00:32:58
    ╰─ python tips_tricks-2.py
    igniform
    having the shape or form of fire

Plus the values can be accessed with a loop...

```python
for key in word_info.keys():
    print(getattr(word, key))
# igniform
# having the shape or form of fire
```

---

### 00:42 ~ Password Proletariat

The getpass library allows passwords to be gathered via `input()` without the password showing up on the screen while being typed. Instead it shows a little lock icon.

```python
username = input("Username: ")
password = input("Password: ") # the password will be visible
print("Entering the Matrix...")
```

Now with `getpass()`...

```python
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

print("Entering the Matrix...")
```

    ╭─ Fineyedesign » tobiasfyi » ..ython/Python_OOP »  master ● ?                              19.05.28 ∫ 00:46:09
    ╰─ python passy.py
    Username: tobias
    Password:
    Entering the Matrix...

---

### 00:56 ~ Resource Radiciform

I can't believe I didn't think to see if there were any good BeautifulSoup tutorials. [Of course Corey has one](https://youtu.be/ng2o98k983k)...I think I'd even seen it before and didn't think of looking.

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:04:42
    ╰─ pip install requests
    ...
    Installing collected packages: chardet, idna, certifi, urllib3, requests

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:08:03
    ╰─ pip install lxml
    ...
    Successfully installed lxml-4.3.3

Started over a bit with a simple printing of the table. This time, however, it's prettyafied!

```python
with open("html/latin.html") as hf:
    soup = BeautifulSoup(hf, "lxml")

print(soup.prettify())
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:09:30
    ╰─ python wordsoup-1.py
    <!DOCTYPE html>
    ...
    <title>
    Word List: Latin Adverbs and Prepositions in English
    </title>
    <link href="wordlist_latin_files/phron.css" rel="stylesheet"/>
    </head>
    <body>
    <table class="words">
    <col width="25%"/>
    <tr>
        <th>
        Word
        </th>
        <th>
        Definition
    ...

That definitely looks better than before—pretty, even. Now for some tag gathering...

```python
match = soup.title
print(match)
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:09:52
    ╰─ python wordsoup-1.py
    <title>Word List: Latin Adverbs and Prepositions in English</title>

...or to get the text (not using `get_text()`):

```python
match = soup.title.text
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:13:05
    ╰─ python wordsoup-1.py
    Word List: Latin Adverbs and Prepositions in English

I think I see the issue I was having earlier with getting the table data. I was going about the conversion into a list the wrong way...

```python
table = soup.find("table", class_="words")
rows = table.findAll("tr")
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:25:17
    ╰─ python wordsoup-1.py
    [<tr>
    <th>
                    Word
                </th><th>
                    Definition
            </th></tr>, <tr>
    <td>alternatim
                </td><td>alternately
            </td></tr>, <tr>
    <td>ana
                </td><td>in equal quantities
            </td></tr>]

---

### 01:36 ~ Split Definite

I came up with a method that works for what I want. It's not all that pretty but oh well...

Ayyyye it actually worked pretty darn well, and the code isn't half bad...ok maybe isn't 90% bad. But it still works! Doesn't matter, had sex / wrote code.

```python
for row in rows:
    row_text = row.get_text()
    row_split = row_text.split()
    wordlist[row_split[0]] = " ".join(row_split[1:])
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:42:52
    ╰─ python wordsoup-1.py
    {'Word': 'Definition',
    'alternatim': 'alternately',
    'ana': 'in equal quantities',
    'bis': 'twice; in two places',
    ...

Niiiiice...now I'm going to try it with the actual webpage...aaaaand...SOLID. Got it on the first try without having to change anything except the source. I wonder if the requests module plus the lxml html parser made the html more manageable, or if the code is just going about it the right way this time...

```python
from bs4 import BeautifulSoup
import requests
import pprint

source = requests.get("http://phrontistery.info/latin.html").text
soup = BeautifulSoup(source, "lxml")
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:47:09
    ╰─ python wordsoup-1.py
    {'Word': 'Definition',
    ...
    'guttatim': 'drop by drop',
    'ibidem': 'in the same place',
    'idem': 'the same word as mentioned before',
    'imprimis': 'in the first place',
    ...
    'quatenus': 'in the capacity of; in so far as',
    'quoad': 'with respect to; as regards',
    'quondam': 'former; sometime; formerly',
    'scilicet': 'to wit; namely',
    'secundum': 'according to',
    ...
    'vice': 'in place of; rather than',
    'videlicet': 'to wit; namely',
    'vulgo': 'commonly; popularly'}

I realized I didn't need the two separate lines in the loop...

```python
for row in rows:
    row_data = row.get_text().split()
    wordlist[row_data[0]] = " ".join(row_data[1:])
```

...and I also just realized that I hadn't been running the new script. In the prompts above I only call the -1 file, not the new one, -2...whoops. Well I didn't get any errors with the new one...forgot to comment out the initial full-page prettify printout...

And boom! No more tiny quandaries!

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 01:56:06
    ╰─ python wordsoup-2.py
    {'Word': 'Definition',
    'alternatim': 'alternately',
    'ana': 'in equal quantities',
    'bis': 'twice; in two places',
    ...

---

### 01:58 ~ Multiple Page Mischief

Now if I can simply loop through all of the pages on the site that have a similar list, I can get all of the data I need! Radical. It would be cool to have the words tagged by what list they came from. Like I mentioned last night, I need to find creative and fun ways of relating this data to other objects and data.

So I am looking for the lists in the nav bar that contain the links to the other pages from which I want to pull data. To start, those will be "Dictionary of Obscure Words" and "Glossaries". I uncommented back out the full-page pretty to find them...

```html
<li class="separator"></li>
<li><a class="arrow" href="ihlstart.html">Dictionary of Obscure Words</a>
<div class="drop decor4_2" style="width: 500px;">
<div class="left">
<b>INTERNATIONAL HOUSE OF LOGORRHEA</b>
<div>
<a href="ihlstart.html">Main Menu</a>
<br/>
...
<div>
<a href="a.html">A</a>
<br/>
<a href="b.html">B</a>
...
<a class="arrow" href="glossaries.html">Glossaries</a>
<div class="drop decor4_2" style="width: 600px;">
<div class="left">
<b>TOPICAL WORD LISTS</b>
<div>
<a href="genitive.html">Adjectives of Relation</a>
<br/>
<a href="bearing.html">Bearing and Carrying</a>
...
```

I'm going to try really quick to get those lists, then it's off to bed for me. I want to be able to work on this tomorrow as well!

So these lists have a few different classes and such by which I can identify and retrieve them. I could get their parent div / list by class, then access the list by using a child generator or something like that.

I think my best bet to start the search would be the top of the navbar section:

```html
<ul class="menuTemplate4 decor4_1" license="2c1p4">
<li><a class="arrow" href="index.html">About</a>
<div class="drop decor4_2" style="width: 400px;">
<div class="left">
<b>THE PHRONTISTERY</b>
<div>
<a href="index.html">Home</a>
<br/>
<a href="news.html">Updates and News</a>
```

That unordered list looks promising, though I guess I can just use the `<div class="drop decor4_2"` part, which is also right above the other ones I'm looking for. Apparently they all have `<div class="left">` as well. That'll do...that'll do.

As Corey is doing, I'm grabbing the correct data from only one first. Then when I know how to get to it I can figure out how to get all of them...

```python
nav_lists = soup.find("div", class_="left").a
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 02:17:10
    ╰─ python wordsoup-3.py
    <a href="index.html">Home</a>

Then I can get the actual value of the href attribute by treating it like a dictionary:

```python
nav_lists = soup.find("div", class_="left").a["href"]
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.05.28 ∫ 02:17:50
    ╰─ python wordsoup-3.py
    index.html

However, I think it would be useful to set up a dictionary in a similar manner to how I did it for the table data. This way I can have the title of the link and the href in one object. Ok I think I know how I'm going to get the whole list. It has to do with a loop...crazy right?

Nope, that didn't quite work. I got a couple of different errors for different reasons. I know I'm close, but just don't know exactly what the list object returned by `.findAll()` looks like.

Ahaa I was just looping over the wrong bit of code.

---

### 02:41 ~ Better Luck Next Time - But Really

I am just about there, but didn't manage to get it tonight. It's late and I started getting tired a while ago. Stoked to pick this up tomorrow though!

G'night mi amigo!

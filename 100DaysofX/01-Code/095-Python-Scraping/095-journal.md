# 2019-06-06 | #100DaysofCode

    GOAL-06-06 ~ Scrape dictionary from the Phrontistery  

## Day 095/100 | 157/365

- [2019-06-06 | #100DaysofCode](#2019-06-06--100daysofcode)
  - [Day 095/100 | 157/365](#day-095100--157365)
    - [13:21 ~ No More Canterbury Lustration](#1321--no-more-canterbury-lustration)
      - [KB++157 ~ Defining nested data structures within loops](#kb157--defining-nested-data-structures-within-loops)
    - [14:26 ~ Too Soon Teloteropathy](#1426--too-soon-teloteropathy)
    - [16:30 ~ Comma Separated Vecordy](#1630--comma-separated-vecordy)
    - [18:39 ~ Action and Recaption](#1839--action-and-recaption)
    - [19:31 ~ The Full Monty Mandamus](#1931--the-full-monty-mandamus)
    - [21:41 ~ tobias.fyi Tessellation](#2141--tobiasfyi-tessellation)
    - [22:03 ~ More and Macarism](#2203--more-and-macarism)
    - [22:43 ~ Resistance is Furciferous](#2243--resistance-is-furciferous)

---- Tasks ----

    TASK-095 ~ Scrape dictionary data of words on Phrontistery  

---- Notes ----

    KB++157 ~ Defining nested data structures within loops  

---- Resources ----

- [ReportLab Documentation](https://www.reportlab.com/documentation/)
- [beautifulsoup4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children)
- [Corey Schafer's video](https://youtu.be/9N6a-VLBa2I?t=695)
- [Airtable API](https://github.com/Airtable/airtable.js)

---- Selects ----

- [The Phrontistery: Dictionary of Lost / Rare Words](http://phrontistery.info/index.html)

---- Sojourn ----

### 13:21 ~ No More Canterbury Lustration

Canterbury: stand with divisions for holding books or music.
Lustration: ritual washing; ablution.

Boom! No more Cant Lustration! I got it to work!

    Remember the Cant...

I found a way to do it that I think is rather clever, though I imagine it's a common way of defining data structures like this. Instead of defining a structure beforehand, I simply create an empty list, and nest the dictionaries within those as items in the list. This way I can keep each layer of the loop / each page distinct from one another.

#### KB++157 ~ Defining nested data structures within loops  

This reminds of how ReportLab uses those flowables (not 100% on that being their name, but I think it's correct) as a way of building PDF pages. Each "flowable" contains a grouping of content which is then appended to the "elements" list that ends up making the page.

```python
dict_data = []  # to be structured as above

for i in range(len(nav_names)):
    for title, href in nav_names[i].items():
        link = base_url + href + ".html"

        # Requests the pages from Phrontistery
        source = requests.get(link).text
        soup = BeautifulSoup(source, "lxml")

        table = soup.find("table", class_="words")
        rows = table.findAll("tr")

        # Set up dictionary containing all content of one page
        page_content = {"title": title, "link": link, "words": []}

        # Add terms + definitions to page_content dict
        for row in rows:
            row_split = row.get_text().split()
            page_words = {"term": row_split[0], "definition": " ".join(row_split[1:])}
            page_content["words"].append(page_words)

        # Add the page's content to the overarching dict
        dict_data.append(page_content)

pprint.pprint(dict_data)
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping            19.06.06 ∫ 13:20:43
    ╰─ python def_scrape-2.py
    [{'link': 'http://phrontistery.info/wisdom.html',
      'title': 'Words of Wisdom',
      'words': [{'definition': 'Definition', 'term': 'Word'},
                {'definition': 'knowledge of the nature of humanity; human wisdom',
                'term': 'anthroposophy'},
                ...
                {'definition': 'knowledge or learning concerning animals',
                'term': 'zoosophy'}]}]

I guess this tells me that dictionaries automatically sort by alphabetical order?...

I define title first, and as it prints above, it shows as alphabetical. That could also be a result of the pprint function I'm using to display the dict.

---- ∫ ----

I also just noticed in the above results that the first line of the words list is the "Word" and "Definition" in the table header. Will probably want to remove that otherwise I'd have to go back and do it later.

Ok I got it without doing anything really complex...

```python
...
# Add terms + definitions to page_content dict
for row in rows:
    row_split = row.get_text().split()
    page_words = {"term": row_split[0], "definition": " ".join(row_split[1:])}
    page_content["words"].append(page_words)

# Remove table header
page_content["words"].pop(0)

# Add the page's content to the overarching dict
dict_data.append(page_content)
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping            19.06.06 ∫ 13:52:37
    ╰─ python def_scrape-2.py
    [{'link': 'http://phrontistery.info/wisdom.html',
    'title': 'Words of Wisdom',
    'words': [{'definition': 'knowledge of the nature of humanity; human wisdom',
                'term': 'anthroposophy'},
                {'definition': 'knowledge of palm-reading', 'term': 'chirosophy'},
                {'definition': 'knowledge of the cosmos', 'term': 'cosmosophy'},
                ...
                {'definition': 'knowledge or learning concerning animals',
                'term': 'zoosophy'}]}]

---

### 14:26 ~ Too Soon Teloteropathy

I spoke too soon that the script was working correctly, because it's not quite there yet. I noticed when I dumped it to JSON that for many of the pages I'm scraping, the first word of the definition is joined to the term. Gotta fix that.

    ...
    {
    "term": "lexigraphyart",
    "definition": "of definition of words"
    }, {
    "term": "lexigraphysystem",
    "definition": "of writing in which each sign represents a word"
    }, {
    "term": "lexiphanicbombastic;",
    "definition": "sesquipedalian; using many long words"
    }, {
    "term": "loan-wordword",
    "definition": "borrowed from another language"
    }, {
    "term": "loganamnosisobsession",
    "definition": "with trying to recall forgotten words"
    },
    ...

Damnit, WordWord!. It obviously has something to do with this particular block:

```python
for row in rows:
    row_split = row.get_text().split()
    print(row_split)
    page_words = {"term": row_split[0], "definition": " ".join(row_split[1:])}
    page_content["words"].append(page_words)
```

I know what I need to do now, but not exactly sure how to do it. I know Corey went over a lot of these concepts in [his beautifulsoup tutorial](https://youtu.be/ng2o98k983k). Going to put that on while I do some graphic work to find out what I should do...

...Actually, before I do that, I just thought of the method I can use to do what I want...or at least most of it. I know how to get the `<td>` tags out, then I'll need to do a bit more research on converting those to text. I know that all of the beautiful soup methods are there for a reason, it's just a matter of using the library enough to get to a use-case for each. This time, on The Fineyedesign show...

Sibling tags! And/or the `.children` iterator! Fun shtuff all around!

```python
for row in rows:
    row_term = row.td  # retrieves term
```

I was going to go straight into using the sibling tag, because of the first two lines of the row loop above and the resulting tag output (gave me the first td tag from each row, aka the term). Therefore, I am fairly confident that I can use one of the sibling functions to access the next tag on the same level.

However, while scrolling through the [beautifulsoup4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children), I happened to see the children generator, and thought I'd give that a go...with great succyess!

```python
for row in rows:
    for td in row.children:
        print(td)  # includes the <td>tag</td>
```

I didn't even get to the sibling section before I got what I wanted...

```python
for row in rows:
    for td in row.children:
        print(td.string)  # retrieves the string
```

        ╭─ iterum » tobiasfyi » ..rum/web_scraping              19.06.06 ∫ 15:08:38
        ╰─ python def_scrape-2.py
        ...
        abecedism
        word created from the initials of words in a phrase

        ablaut
        variation in root vowel of words to change meaning
        ...
        verbile
        one whose mental processes are stimulated by words

        verbomania
        craze for words

        wordbound
        unable to find expression in words

And that's just groovy right there! However, I do want to try out the sibling method of accessing the next `<td>` tag.

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                             19.06.06 ∫ 15:44:00
    ╰─ python def_scrape-2.py
    Traceback (most recent call last):
    File "def_scrape-2.py", line 120, in <module>
        row_def = row.td.next_sibling  # retrieves definitions
    AttributeError: 'NoneType' object has no attribute 'next_sibling'

Well...at least I tried. I like the generator version of it more anyways. However, it might still be nice to have access to another method of doing this, because it may take a few extra lines to be able to extract each of the separate children and make sure they are the correct ones.

When I take out the sibling part of that, I get the following result:

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                             19.06.06 ∫ 15:44:02
    ╰─ python def_scrape-2.py
    None
    <td>abecedism</td>
    <td>ablaut</td>
    <td>acronym</td>
    <td>acrophonic</td>
    ...

And that makes me wonder if it was that first row that caused the NoneType error. Yup! I was correct...

```python
for row in rows:
    if row.td:
        row_term = row.td  # retrieves term
        row_def = row.td.next_sibling  # retrieves definitions
        print(row_term, ":", row_def)
```

That results in what I want, but still surrounded by the tags. Time to strip those bad boiz down to their skivvys.

```python
for row in rows:
    if row.td:
        row_term = row.td.string  # retrieves term
        row_def = row.td.next_sibling.string  # retrieves definitions
        print(row_term, "-", row_def)
```

When I use the string method, however, there are some leftover newline tags and such. Not sure how to get rid of those, but I'm about to find out! I tried using the str() function to convert to string, but to no avail.

```python
row_term = str(row.td.string)
row_def = str(row.td.next_sibling.string)
```

...oh. All I had to do was call `.text` on it, which is something I've done before. Duh...

...but see? I told you I'd figure it out!

```python
for row in rows:
    if row.td:
        row_term = row.td.text
        row_def = row.td.next_sibling.text
```

...except that I didn't...there are still newline tags on the end of the definitions.

    {
    "term": "portmanteau",
    "definition": "word formed by blending two existing words\r\n"
    },
    {
    "term": "proclisis",
    "definition": "pronunciation of word dependent on following word\r\n"
    },
    {
    "term": "provection",
    "definition": "transfer of last letter of one word to first of next\r\n"
    },
    {
    "term": "pundigrion",
    "definition": "play on words; pun\r\n"
    },

I guess I could just brute force it and literally strip off "/r/n" from the end of them...or not...

```python
for row in rows:
    if row.td:
        row_term = row.td.text
        row_def = row.td.next_sibling.text
        row_def = row_def.rstrip(r"\r\n")
        print(row_term, "-", row_def)

        page_words = {"term": row_term, "definition": row_def}
        pprint.pprint(page_words)
        page_content["words"].append(page_words)
```

Results in this output:

    verbile - one whose mental processes are stimulated by words

    {'definition': 'one whose mental processes are stimulated by words\r\n',
    'term': 'verbile'}
    verbomania - craze for words

    {'definition': 'craze for words\r\n', 'term': 'verbomania'}
    wordbound - unable to find expression in words

    {'definition': 'unable to find expression in words\r\n', 'term': 'wordbound'}

Which tells me that for whatever reason, those additional characters are being printed only in the second print statement. And that print statement happens to be both a dictionary and using the pprint module. Let's do some testing to see if those have anything to do with it...first I'm going to use a simple print statement.

    telestich - poem where final letters of each line spell a word

    {'term': 'telestich', 'definition': 'poem where final letters of each line spell a word\r\n'}
    tetragrammaton - sacred word or acronym of four letters

    {'term': 'tetragrammaton', 'definition': 'sacred word or acronym of four letters\r\n'}
    tmesis - separation of word into parts by an intervening word

    {'term': 'tmesis', 'definition': 'separation of word into parts by an intervening word\r\n'}

Nope. The same result. I wonder if it's to do with the fact that it's a dictionary then...that's what seems to be the cause. If I access only the "definition" item in the dictionary, this is the result.

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                             19.06.06 ∫ 16:20:57
    ╰─ python def_scrape-2.py
    word created from the initials of words in a phrase

    variation in root vowel of words to change meaning
    ...

Even using the `repr()` function, those damn extra characters are still there.

Holy shit...so obvious...yet not. 

I was just attempting to strip the wrong characters—any characters, really. I got it to work by not passing anything into the `.rstrip()` method...

```python
...
    ...
        for row in rows:
            if row.td:
                row_term = row.td.text
                row_def = row.td.next_sibling.text
                row_def = row_def.rstrip()

                page_words = {"term": row_term, "definition": row_def}
                page_content["words"].append(page_words)

        page_content["words"].pop(0)

        dict_data.append(page_content)

data_string = json.dumps(dict_data, indent=2)
print(data_string)
```

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                             19.06.06 ∫ 16:28:04
    ╰─ python def_scrape-2.py
    [
    {
        "title": "Words about Words",
        "link": "http://phrontistery.info/words.html",
        "words": [
        {
            "term": "ablaut",
            "definition": "variation in root vowel of words to change meaning"
        },
        {
            "term": "acronym",
            "definition": "word formed from initial letters of another word"
        },
        {
            "term": "acrophonic",

Oh baby that's nice. Sooooo nice and shmexy.

---

### 16:30 ~ Comma Separated Vecordy

Vecordy: madness, folly.

Whewwww I got it! All that's left is to add the code that allows for saving the information as JSON and CSV, then running the script on the rest of the pages.

I'm going to come back to CSV if I need it. For now, JSON will do. Here's the CSV code I've written for it so far, for future reference...

```python
# Open csv file for writing + define headers
csv_file = open("phrontest1.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["term", "definition", "title", "link"])
```

Flippitty fluurrrrppurty floppitty floop! Time for me to change my mind all up on over you!

---- ∫ ----

Decided to go for it and it worked out great! Along with opening the file as I showed above, which takes place before the loops get up and going. Then in the depths of the loop, I write each row with the relevant data. After the loops are all done, then the file gets closed (because no context manager was used). I might change that so there is a context manager...

However, I believe that would mean that I would be running all of the loops from inside that context. I could create functions for all of this in order to make it legit...I will later.

```python
for i in range(len(nav_names)):
    for title, href in nav_names[i].items():
        ...
        # Add terms + definitions to page_content dict
        for row in rows:
            if row.td:
        ...
            # Write the row to the csv file
            csv_writer.writerow(
                [
                    page_words["term"],
                    page_words["definition"],
                    page_content["title"],
                    page_content["link"],
                ]
            )
        ...
    ...
...
csv_file.close()
...
```

Oh boiiiii I'm getting close to letting this bad boy loose on all of the sites that I defined earlier. I'm going to do that once I get home.

I tested out saving one page to JSON and it seemed to have worked out fine. One thing I do want to figure out, however, is having the key be set up like how "states" are in [Corey Schafer's video](https://youtu.be/9N6a-VLBa2I?t=695).

Time to get groovin on this at home!

---

### 18:39 ~ Action and Recaption

Recaption: reprisal; taking back that which is unlawfully obtained.

Ok I'm about to go for it! Just in case the server doesn't like a bunch of requests methodically going through the pages of the site (though I doubt it has anything in place to stop such a thing), I added a `time.sleep(2)` call after each page is complete.

Time to find out if it works! I mean it's only text, so it's not like it will be a lot of wasted data / space if it messes up. But I feel like I should test it out on a smaller subset of the entire page array before unleashing it on the whole.

I'm going to do that. I'll start with the first half-ish of the alphabet: "A" through "O".

Well...off to a start!

...I forgot to turn the array of pages into a list of dictionaries.

    nav_names = [
        {"A": "a"},
        ...
        {"O": "o"},
    ]

Ok...let's do this! Turned on my music, so now I'm ready to rollllll....

...lol...

...at least I got through one...and it worked correctly. Forgot another tiny little thing...I changed the import to datetime and forgot I was still using the time module.

    ╭─ iterum » tobiasfyi » ..rum/web_scraping                              19.06.06 ∫ 19:01:42
    ╰─ python def_scrape-2.py
    Starting page A...
    Completed page A in 0:00:00.402676...
    Traceback (most recent call last):
    File "def_scrape-2.py", line 167, in <module>
        time.sleep(2)
    NameError: name 'time' is not defined

Ok...NOW I'm really, really very, Barry ready.

---- ∫ ----

And awaaaaay we gooooooo! It seemed to have worked. It at least went through all of the pages without throwing any errors, so I'm assuming it worked. Let's take a look!

Browsed through the json file really quick and that looked like it worked great.

Ok I've debated a little bit about whether to start over from the top and do all of it, or to start from where I left off. I decided to start over from the top so it's all nice and neat and tidy. Plus if something can't handle that, I'd like to know where the limit is.

I also wrote a little function to do the countdown...

```python
def countdown(seconds):
    s = int(seconds)
    while s > 0:
        print(f"{s}")
        time.sleep(1)
        s -= 1
    print("Happy New Year!")
```

---

### 19:31 ~ The Full Monty Mandamus

Mandamus: writ instructing that an action should be performed.

It made it all the way to the eighth to last page before throwing an error. The error happened because that page doesn't use a table to organize the data. I'll have to deal with that one separately.

    {"Signs, Symbols, and Accents": "sign"},

Removed that + added some cool little dealios and hitting it off again!

---- ∫ ----

Eet vvvuuuurrrrkkkeeeeddddddd!

    ...
    Starting page Words about Words...
    Completed page Words about Words in 0:00:00.146801...
    Next page in...
    3
    2
    1
    🕺 !Happy New Year! 💃
    Starting page Words of Wisdom...
    Completed page Words of Wisdom in 0:00:00.143481...
    Next page in...
    3
    2
    1
    🕺 !Happy New Year! 💃
    And...
    ...
    💣 BOOM!💥
    ...
    NO...
    MORE...
    CHINESE...
    LAUNDRY!
    😎

No more Chinese Laundry! Time to take a look and see how many rows I got.

In total I scraped 24,851 records from the site. What I just realized is that some of the words are repeated once (in the alphabetical glossary and the topical glossaries). That will be an interesting thing to research. This is exciting!

---

### 21:41 ~ tobias.fyi Tessellation

Tessellation: fitting together exactly; leaving no spaces.

I decided that I need to get all organized and cleaned up with regards to my journal, both for the Challenge and SmartAss. I'm going to spend an hour doing that...

Right...*now!*

Actually wait...not quite yet. Going to finish eating and wash the dishes first.

---

### 22:03 ~ More and Macarism

Macarize: to declare to be happy or blessed.

Decided to keep the tasty journey going with some ice cream and strawberries. I had to eat the strawberries before they went bad. They were right on the edge. Wouldn't want them to go to waste!

It would be pretty sweet to get [connected to the Airtable API](https://github.com/Airtable/airtable.js) from within Node / React / Django. Though if I'm going to go that far, I might as well just come up with my own schemas.

---- ∫ ----

Interesting advice / opinion from Philip today when I inquired about GraphQL. He did not speak highly of it at all and also said that Saleor looked cringey (at least the front page). He mentioned that the reason GraphQL exists in the first place is because of bad API design on the Facebook back end. If they had done things correctly the first time, they wouldn't have needed it at all.

That makes sense, though I'm still surprised because a ton of people have been touting how awesome it is. I'm glad that I asked for a number of reasons. Most importantly, this means I have one less thing on which to disperse my energy and attention. Creating a solid REST APIs with Flask or Django will be my next big phase, which I am just starting by learning the basics of React. I'm excited to get into connecting React with Django or Flask.

Mostly Django, but Flask is cool too. I've just been digging the Django workflow much more than the Flask one. Obviously, I'll have to connect an API with Flask when I finish working on AptDraft.

---

### 22:43 ~ Resistance is Furciferous

Furciferous: bearing a forked appendage; rascally.

Waking up this morning before sunrise was awesome! The combination of waking up + sunrise + cold shower + L-Tyrosine was on point and something I want to keep going. That means I only have another hour or so of work before it's bed time. At the latest.

Buenos resistamos, amigos!

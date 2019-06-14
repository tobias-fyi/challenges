# 2019-06-05 | #100DaysofCode

    GOAL-06-05 ~ Productivity + Building cool stuff  

## Day 094/100 | 156/365

- [2019-06-05 | #100DaysofCode](#2019-06-05--100daysofcode)
  - [Day 094/100 | 156/365](#day-094100--156365)
    - [05:57 -+- Fineyedesign.init](#0557----fineyedesigninit)
    - [07:17 ~ Daedal Datatype Decision](#0717--daedal-datatype-decision)
    - [08:55 ~ Time and Space Sagene](#0855--time-and-space-sagene)
    - [10:01 ~ Farouche JSON Formatter](#1001--farouche-json-formatter)
    - [11:43 ~ Veduta Visualization](#1143--veduta-visualization)
    - [12:17 ~ Lautitious Lunchtime](#1217--lautitious-lunchtime)

---- Notes ----

    CUE-156 : Check out SoundFly + Pickup Music + Sound Gym  
    IDEA-156 : (re)Capture those lost hours  

---- Selects ----

- [HttpBin](https://httpbin.org/)
- [Introducing Mercury OS](https://uxdesign.cc/introducing-mercury-os-f4de45a04289).
- Obligatory Corey Schafer tuts
  - [Image Manipulation with Pillow](https://youtu.be/6Qs3wObeWwc)
  - [Requests](https://youtu.be/tb8gHvYlCFs)
  - [Web Scraping with Requests-HTML](https://youtu.be/a6fIbtFB46g)
  - [Duck Typing and EAFP](https://youtu.be/x3v9zMX1s4s)

---- Sojourn ----

### 05:57 -+- Fineyedesign.init

Starting things off early today, as I've been wanting to get into the habit of.

Warming up with a little web scraping. I forgot that I'd already successfully parsed the table to the point of getting all of the terms and definitions into a dictionary. I did it for a single page, and now the goal is to programmatically run the script through multiple pages and grab all of them.

Instead of using code to get the links, I just wrote them out. The main reason for that is the fact that the links don't really have any unique characteristics or IDs. I think it would've taken longer to write the code to grab the links than it did to simply write them out. If the list of links were hundreds of items long then that would've been different. However, with the multi-cursor function, I can make quick work of things like this where repeated patterns abound.

---

### 07:17 ~ Daedal Datatype Decision

Daedal: formed with art; displaying inventive skill.

Now, I've come to another decision that creates a great learning opportunity for me. In order to create this API, I will need to be able to return JSON. The question is all about data types:

- Should I create a dictionary right off the bat that is structured like JSON?
- Should the data be structured as Python likes it best, then converted to CSV
- How should the data come out of this?

I think it would be a good exercise for me to test out different data types to see which one would be the best for my goals / needs.

The obvious choice that jumps out to me immediately is to have a Pythonic dictionary within the Python script. At the end of the Python script the dictionary is written to a csv, which can then be imported into whatever else. By "whatever else" I'm mostly thinking of other Python scripts and Postgres database tables. I'm not sure how easy it is to read in csv data using javascript.

The reason this came up is I was testing out what the dictionary would look like if I were to structure it like a JSON array...

```python
full_dict = {
    "title": "A",
    "link": "http://phrontistery.info/a.html",
    "words": {
        "term": "aardvolf",
        "definition": "South African carnivorous fox-like quadruped",
    },
}
```

...and once I wrote the above, I realized that it could be a ton simpler if the props weren't named. I'm not sure how easy the following is to convert to JSON, which is why the question came up...

```python
full_dict = {
    "A": [
        "http://phrontistery.info/a.html",
        {"aardvolf": "South African carnivorous fox-like quadruped"},
    ],
}
```

---

### 08:55 ~ Time and Space Sagene

Sagene: fishing-net; network.

Now that I've had time to mull it over a little bit, the latter example I provided above only improves the line-count by 2—from 8 lines to 6 lines. Furthermore, it does not really save any complexity. Quite the contrary, most people would think, I would think...

With larger bits of data, having the field names means the data contained is more straightforward and labeled, instead of whoever / whatever is digesting it being expected to intuit the data fields.

Also, probably good for me to practice a bit with JSON.

---

### 10:01 ~ Farouche JSON Formatter

Farouche: wild; unpolished.

After a little bit of editing, I ran this through a JSON formatter and it said that it is valid JSON

```json
{
    "title": "A",
    "link": "http://phrontistery.info/a.html",
    "words": {
        "term": "aardvolf",
        "definition": "South African carnivorous fox-like quadruped"
    }
}
```

---

### 11:43 ~ Veduta Visualization

Veduta: panoramic view of a town.

Visualizing / writing out the data structure helps me understand and define it more effectively. Here's what I have thus far.

```python
dict_data = [
    {
        "title": "A",
        "link": "http://phrontistery.info/a.html",
        "words": [
            {"term": "aardvolf", "definition": "South African carnivorous fox-like quadruped"},
            {...},
            {"term": "azymous", "definition": "unleavened"},
        ],
    },
    {
        "title": "B",
        "link": "http://phrontistery.info/b.html",
        "words": {"term": "babeldom", "definition": "a confused sound of voices"},
        {...},
        "words": {"term": "bywoner", "definition": "agricultural labourer"},
    },
    {...},
]
```

The basic pattern is lists of dictionaries. I had some error come up regarding a `KeyError: 0` issue.  
I decided to break things down to be sure that I am doing things correctly.  
This is after converting the `nav_names` dict to a list of dicts.

```python
nav_names = [{"A": "a"}, {"Words of Wisdom": "wisdom"}]
...
for i in range(len(nav_names)):
    print(i)
    for title, href in nav_names[i].items():
        print(title)
        dict_data[i]["title"] = title
        print(dict_data[i]["title"])
```

Hmm...maybe if I define the structure beforehand, as I did in this example—I uncommented the dict_data structure—it behaves differently? I tried leaving the definition of dict_data uncommented and ran the script to see if that is different. This is the result with the structure pre-defined:

    ╭─ iterum » tobiasfyi » ..rum/web_scraping            19.06.05 ∫ 12:07:12
    ╰─ python def_scrape-2.py
    [{'link': 'http://phrontistery.info/a.html',
      'title': 'A',
      'words': {'definition': '', 'term': 'azymousunleavened'}},
    {'link': 'http://phrontistery.info/wisdom.html',
      'title': 'Words of Wisdom',
      'words': {'definition': 'knowledge or learning concerning animals',
                'term': 'zoosophy'}}]

So it worked perfectly! Now I'm going to try it again with the structure definition commented out...

...aaaaaaand that made me realize that I hadn't defined dict_data as a list of dicts, it was simply a dict. That would definitely cause a problem. I tried setting it both as a list and a list with an empty dict as well. Both resulted in an error...

    ╭─ iterum » tobiasfyi » ..rum/web_scraping            19.06.05 ∫ 12:13:44
    ╰─ python def_scrape-2.py
    Traceback (most recent call last):
      File "def_scrape-2.py", line 110, in <module>
        dict_data[i]["title"] = title
    IndexError: list index out of range

I guess I'm going with pre-defining the structure...

```python
nav_names = [{"A": "a"}, {"Words of Wisdom": "wisdom"}]

dict_data = [
    {
        "title": "A",
        "link": "http://phrontistery.info/a.html",
        "words": [
            {"term": "aardvolf", "definition": "South African carnivorous fox-like quadruped"}
        ],
    }
]
```

---

### 12:17 ~ Lautitious Lunchtime

Except that I got the same error. I wasn't getting it before because I wasn't trying to define a new index. I'll need to figure out how to be sure that the structure is defined beyond what is defined above. I'll get to that when I return from lunch.

Man, that's ugly right there...and it doesn't work.

    dict_data = [{"": "", "": "", "words": [{}]}]

Looks like I don't know data structures as well as I would like. That means I get to learn!

Buenos learning, Amigo!

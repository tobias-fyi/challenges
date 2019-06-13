# 2019-05-09 | #100DaysofCode

## Day 067 / 100

- [2019-05-09 | #100DaysofCode](#2019-05-09--100daysofcode)
  - [Day 067 / 100](#day-067--100)
  - [SELECT * FROM Project](#select--from-project)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-05)](#projectloxocache2019-05)
  - [SELECT * FROM Session](#select--from-session)
    - [Session.abstract](#sessionabstract)
      - [Session.cache](#sessioncache)
  - [Session.sojourn(2019-05-09)](#sessionsojourn2019-05-09)
    - [Loxocache](#loxocache)
    - [14:15 ~ Session.init](#1415--sessioninit)
    - [14:25 ~ ClickIt or LickIt](#1425--clickit-or-lickit)
    - [15:43 ~ Testing It Out](#1543--testing-it-out)
    - [16:32 ~ Tried and UnTrue](#1632--tried-and-untrue)

---

## SELECT * FROM Project

### Project.abstract

    GOAL-fyinit : CLI tool for intuitive productivity  

    TASK-fyinit : Allow creation of various types of entries (not just Challenges)  
    TASK-fyinit : Function to insert characters into multiple lines i.e. each line with quotes  
    TASK-fyinit : Tag collection  
    TASK-fyinit : Allow different date to be set (not just current day) - maybe by prompting for time delta  

### Project.loxocache(2019-05)

- Click
  - [GitHub repo](https://github.com/pallets/click)
  - [Page on The Pallets Project](https://palletsprojects.com/p/click/)
  - [Documentation](https://click.palletsprojects.com/en/7.x/)

--------å--------

## SELECT * FROM Session

### Session.abstract

    GOAL-067 : workon the fyinit CLI tool to add more general usefulness  

    IDEA-067 : Random {•}.generator | {color, number, string, name}  
    IDEA-067 : Name generator based on my ideabox wordname list  

#### Session.cache

- Music
  - Once again listening to [Lee Burridge at Robot Heart 2018](https://soundcloud.com/robot-heart)
- Usefulness
  - [Multi-Account Containers extension](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/) works amazingly well (on Firefox)
  - [jsPDF](https://github.com/MrRio/jsPDF) - potentially useful for displaying PDFs
  - [Zsh manual](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html)

---

## Session.sojourn(2019-05-09)

### Loxocache

--------å--------

### 14:15 ~ Session.init

Took a little time to recolorize some of my TODO Tree tags. I made the switch yesterday to using dashes instead of underlines to separate the tag from the content. Makes selection of the segments easier.

Excited to work on fyinit again today! It's been too long since I've done anything more than cosmetic changes.

The Pallets Project is the creator / maintainer of Click. Other projects by them include:

- Flask
- Jinja
- ItsDangerous (helpers to pass data into and out of untrusted envs safely)
- MarkupSafe
- Werkzeug (comprehensive WSGI utility library)

---

### 14:25 ~ ClickIt or LickIt

First thing I want to do is add the functionality to allow me to create a more general markdown entry.

Updated the markdown template file (the one I haven't used in the actual script yet).
I don't know if I even really need a template, however, as the snippets I have act as a more flexible templating method.

I wonder if there's a built-in method for reading lines of a file into a list.  
I bet there is, and I think I've actually used it before.

I moved the utility functions (justify_center, table_printer, prompter) out of the main click command.  
This way they are globally-scoped and available to other click commands if needed.  

Not sure why I haven't thought to do this yet...  
There are plenty of terminal commands that I use very frequently, some of which are quite lengthy.

    $ rsync -ah --info=progress2 --append-verify /some-dir/ /some-other-dir/
    > that's a lot of typing every time I want to use it - though I am getting rather fast at it

Better thing to do would be to create aliases for these commands.  
I'm going to start with my typical rsync command and go from there.
Here's the [zsh documentation](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html), for reference.

> ~/.zshrc

    alias rsyn="rsync -ah --info=progress2 --append-verify"

Makes it much quicker! [This article](https://blog.sebastian-daschner.com/entries/zsh-aliases) goes over having the command expand when space bar is pressed.  
That would be very useful but I don't want to get into it right now.

    ╭─ tobiasfyi » .._Base/10_Threads »  master ● ?
    ╰─ rsyn 20_Python/ ~/workshop/Fineyedesign/01-Docs/01-Journals/30-KB/Python
            50.23K 100%    4.31MB/s    0:00:00 (xfr#16, to-chk=0/22)

---

### 15:43 ~ Testing It Out

Install it in order to test out my changes (not much yet)...

    ╭─ Fineyedesign » tobiasfyi » ..hop/Fineyedesign »  master ● ? ↑1          19.05.11 ∫ 15:28:42
    ╰─ pip install -e 08-Projects/fyinit/
    Obtaining file:///Users/Tobias/workshop/Fineyedesign/08-Projects/fyinit
    Requirement already satisfied: Click in /Users/Tobias/.vega/Fineyedesign/lib/python3.7/site-packages (from fyinit==0.2) (7.0)
    Installing collected packages: fyinit
        Running setup.py develop for fyinit
    Successfully installed fyinit

I'm actually going to put the utility functions back into the click command. Makes things easier for now until I clean everything up.

Well...now that I think about it, I don't have to put them back.  
I thought that a variable used in one of the functions wouldn't be available, but it will be when the function is called.

Cool...

---

### 16:32 ~ Tried and UnTrue

I've been stuck on a bug for the last 30 mins or so.  
Everything works fine except for when I try to navigate to certain directories in the `dir_picker` function.  
I'm going to call it for this session, but I'll figure it out next time.

The next thing I was going to try was take out the try/except statement to see if that gives me any good debug info.

Hasta debuego, amigo.
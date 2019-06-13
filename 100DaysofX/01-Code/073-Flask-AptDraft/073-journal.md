# 2019-05-15 | #100DaysofCode

    GOAL-05-15 ~ Get the basic skeleton of AptDraft up and running  

## Day 073/100 | 134/365

- [2019-05-15 | #100DaysofCode](#2019-05-15--100daysofcode)
  - [Day 073/100 | 134/365](#day-073100--134365)
    - [06:39 -+- Session.init](#0639----sessioninit)
    - [07:26 ~ Optional Optimization](#0726--optional-optimization)
    - [07:59 ~ Cali Coding](#0759--cali-coding)
    - [10:04 ~ Collaborative Cacographic Caconym](#1004--collaborative-cacographic-caconym)

---- Tasks ----

    LVL1-136 : Design a simple branding package for AptDraft  
    LVL1-136 : Create basic templates for all pages  
    LVL1-136 : Connect to the Postgres database  
    LVL1-136 : Create user table + login functionality  
    LVL1-136 : User registration  

    LVL2-136 : Connect to the GoodReads API  
    LVL2-136 : Create reading journal table + journal page functionality  

---- Sojourn ----

### 06:39 -+- Session.init

On the plane atm. Decided I'm not going to be sleeping so will get some work done.

---

### 07:26 ~ Optional Optimization

Decided to set an alias and an environment variable for Fineyedesign (and probably other projects as I go) to make navigation a little quicker.

To start out I simply made it a three-letter command to navigate to the project home and a one-letter one to get the project name...

    # ================ Navigation ================ #
    export P="Fineyedesign"
    alias cdp="cd ~/workshop/Fineyedesign"

Decided to test out fyinit with my addition / re-addition of the code to open the correct workspace, and found another bug—when navigating up directories, the old paths are still in the dictionary and so any choice of path will result in the one previously chosen.

I need a way to remove the entry from the dictionary if navigating up. Or I could find another way to store the paths entirely.

---

### 07:59 ~ Cali Coding

Landed 30 mins ago or so. Philip isn't answering so I'm just hanging out writing some code.

Added one line of code to `fyinit` and fixed the bug...

    elif root == "..":
        prefix -= 1
        os.chdir(nav_target[prefix])
        nav_target.pop(prefix + 1) # new

There's likely a better way of doing this, but that works for now.

---

### 10:04 ~ Collaborative [Cacographic Caconym](http://phrontistery.info/c.html)

Made it into Phil's office around 09:30. Interesting little place nestled in amongst some "edgy" lofts. Definitely not what I was expecting, though it made me go down the mental pathway / practice of not setting any prior expectations.

There is not really anything good that can come out of them.

----ƒ----

There are a few things that I can be doing right now. Top of the list is AptDraft.

Hastamos go-for-launch, amigos!

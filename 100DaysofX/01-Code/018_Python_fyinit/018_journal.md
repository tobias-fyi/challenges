# 2019-03-21 | #018

\#100DaysofCode

- [2019-03-21 | #018](#2019-03-21--018)
  - [MENU_Today](#menutoday)
    - [Main Course](#main-course)
    - [Extras](#extras)
    - [22:42 -+- SessInit](#2242----sessinit)
    - [23:15 -+- Defaults](#2315----defaults)
    - [23:23 -+- Template](#2323----template)
    - [23:45 -+- Eos](#2345----eos)

---

## MENU_Today

### Main Course

    GOAL_ : Build INIT script as CLI Tool using Click
    ---º---
    TASK√01 : Set the defaults for input / output files

### Extras

Soundtrack: [Lost Desert at Robot Heart 2018](https://soundcloud.com/robot-heart/lost-desert-robot-heart-burning-man-2018)

### 22:42 -+- SessInit

Getting it going once again.  
First thing I want to do is be able to set defaults for both the file being read and the one being written / created.

### 23:15 -+- Defaults

Whew that took way too long, though I did get a little sidetracked along the way.  
I'm pretty tired so my mind isn't at peak capacity right now.

Now I can just use the one word to copy the contents of the template into the journal.

    $ fyinit
    > code journal.md

In the example in the docs, the click.File class isn't passed mode="rb", only "rb". I think that's part of what confused me.

What I'm thinking I should try to get done right now is simply have another part of the script that updates the template with the current date / journal #, which is then written into the new file.

Or I could do this by searching the chunk before it's written, and if it contains the keywords {date} and {j_num}, replace them with the current date and journal #.

### 23:23 -+- Template

    TASK≈02 : Replace the keywords {date} and {j_num} in the template with current data

### 23:45 -+- Eos

I went down a bit of a rabbit hole trying to figure out the decoding / encoding of strings to bytes and all that—just so I could run a regex sub (search and replace) on the chunk. Couldn't quite figure it out, but I know I'm close. My mind just isn't quite there right now.

That means it's about that time...

Hasta Bananas, Amigo.
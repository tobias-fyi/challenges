# 2019-03-19 | #016

\#100DaysofCode

- [2019-03-19 | #016](#2019-03-19--016)
  - [MENU_Today](#menutoday)
    - [Main Course](#main-course)
    - [Extras](#extras)
    - [17:27 -+- SessInit](#1727----sessinit)
    - [17:27 -+- Nested Commands](#1727----nested-commands)
    - [17:37 -+- Read Write](#1737----read-write)
    - [18:24 -+- AttributeError](#1824----attributeerror)
    - [18:32 -+- Eos](#1832----eos)

---

## MENU_Today

### Main Course

    GOAL_ : Begin learning Unit Testing by utilizing the Python Unit Testing module  
    GOAL_ : Build INIT script as CLI Tool using Click
    ---º---
    TASK_ : Output from the script to a markdown file

### Extras

[Flask on Kubernetes](https://www.testdriven.io/blog/running-flask-on-kubernetes/)

### 17:27 -+- SessInit

Going to be switching from Pytest to unittest as it is in the standard library.
Maybe I'll just try a little of both since Pytest is already installed. Maybe.

    KB_ : rsync -ah will create directories / paths if they do not exist  

Decided to work on the soon-to-be CLI tool within each day's directory rather than work only from the Projects/fyinit directory. As I mentioned, I will try to keep that one up to date with the latest code written during a specific session.

I thought about it a little bit just now, and decided to swap the active codebase to the Projects/ directory, then copy it to corresponding daily dir after each session.

Ok cool.

### 17:27 -+- Nested Commands

Changed the snippet ^^

Trying out Click's nested commands again because I broke it last night.
While watching the video I managed to do the grouping without cli.add_command, but I won't worry about that right now.

### 17:37 -+- Read Write

Created the markdown template into the project folder for the script to read from.
Also, doesn't seem like I really *need* command groups yet, so taking it out for now.

Right now, just trying to copy the template file into a new file. Later, I'll deal with the logic of naming / replacing content with the result of variables.

Hmm...just read in the Click documentation that there is a progress bar built in.  
Nice..

### 18:24 -+- AttributeError

Ayyyye I got it to work with some help from the inout example from the documentation.
This takes an argument as the input and output. 

Next, try it out with the defaults.

I keep getting this error, which I'm assuming is caused by how Click opens / reads files:

    AttributeError: 'bytes' object has no attribute 'read'

### 18:32 -+- Eos

Well I couldn't figure it out but I will next time. For now, the script works as long as the input and output files are specified.

    $ fyinit md_template.md journal.md
    >

End of Session
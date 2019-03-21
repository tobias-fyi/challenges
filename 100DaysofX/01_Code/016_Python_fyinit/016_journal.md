# 2019-03-19 | #016

\#100DaysofCode

- [2019-03-19 | #016](#2019-03-19--016)
  - [MENU_Today](#menutoday)
    - [Main Course](#main-course)
    - [Extras](#extras)
    - [Hello World --+-- 21:02](#hello-world------2102)
    - [stdout --+-- 21:19](#stdout------2119)
    - [Snippet --+-- 22:32](#snippet------2232)
    - [Flags -+- 23:04](#flags----2304)
    - [User Input -+- 23:11](#user-input----2311)
    - [End -+- 23:18](#end----2318)

---

## MENU_Today

### Main Course

    TASK√016 : Write a simple Click application to write user input to file

    GOAL_ : Rewrite INIT script to use Markdown
    GOAL_ : Build INIT script as CLI Tool using Click

### Extras

Resource: [Awesome screencast](https://www.youtube.com/watch?v=kNke39OZ2k0) explaining the basics of Click

### Hello World --+-- 21:02

Back at it and excited to start building this script into a real CLI tool.  
Went through a simple 'Hello World' exercise to get comfortable.

    $ fyinit --string Toby --repeat 3
    > Hello, Toby.
    > Hello, Toby.
    > Hello, Toby.

### stdout --+-- 21:19

Now sending stout to file.  
Successfully wrote the output to a file.  
The program is basically done now.  

Changed the Black line length to the same as flake8 because obvious reasons...

Oh boy this is starting to get exciting because I'm seeing some examples in the documentation for opening database connections. That reminded me of why I'm ultimately building this tool—obviously I want to be able to initialize sessions quickly, but I also want to be able to have the journals be written into a database automatically. I'm starting to work on my first real project which is a combination of journal / personal CRM. So this is starting to get very applicable and I've barely even begun to dig into it.

### Snippet --+-- 22:32

A note from the documentation—:

    To help you decide between options and arguments, the recommendation is to use arguments exclusively for things like going to subcommands or input filenames / URLs, and have everything else be an option instead.

Had a thought earlier:

- I currently have a snippet set up to create a timestamp as a header
- This puts a link in the ToC at the top to each entry
- However, I was thinking it'd be useful to have the time + subject
- Going to create a new snippet for now, to have the option to do both

Here are the snippets in markdown.code-snippts:

    {
        "time_stamp": {
            "prefix": "time-stamp",
            "body": [
                "### --------$CURRENT_HOUR:$CURRENT_MINUTE--------",
                "",
            ],
            "description": "Markdown timestamp entry."
        },
        "sub_stamp": {
            "prefix": "sub-stamp",
            "body": [
                "### ${1:Subject} -+- $CURRENT_HOUR:$CURRENT_MINUTE",
                "",
            ],
            "description": "Markdown timestamp + subject entry."
        },
    }

We'll see if I end up using it that much, as I could just write in the subject without using the snippet.

### Flags -+- 23:04

Used the new snippet! Ain't that just the coolest.

Added a flag to the text for extra verbosenessicity.

    $ fyinit --verbose say
    > Now with extra verbosity.
    > Hello, World.

### User Input -+- 23:11

As a final exercise I want to simply take a user input string and write that to a file.

Ok I trimmed it back a bit to only have the string option and it inserts that into the fstring which is then written to the file.  
Got that working. Now I want to have it prompt for the string instead of passing it in as a parameter.

Cool managed to get that working in a very simple way.  
Doesn't look too pretty but I already have some ideas for how to make it quite noice.

    $ fyinit -c "Here is some super interesting content, amigo." spam.txt
    > Name:
    $ Tobes
    > nano spam.txt
        My name is Tobes.
        ----+----
        Content:
        Here is some super interesting content, amigo.

### End -+- 23:18

For tomorrow:

- Edit snippet so the headlines / ToC looks cleaner and more consistent
- There was something else but I forgot—means it's time for bed

Hasta Buenos, Amigos.

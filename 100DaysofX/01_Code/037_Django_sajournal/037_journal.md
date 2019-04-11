# 2019-04-09 | #037

\#100DaysofCode

- [2019-04-09 | #037](#2019-04-09--037)
  - [Today's Menu](#todays-menu)
    - [Main Course](#main-course)
    - [SELECT * FROM Session](#select--from-session)
      - [Soundtrack](#soundtrack)
      - [Extras](#extras)
  - [Session.log](#sessionlog)
    - [00:18 -+- Session.init](#0018----sessioninit)
    - [00:33 -+- django-model-utils](#0033----django-model-utils)
    - [00:37 -+- Template Extendor](#0037----template-extendor)
    - [00:48 -+- Utilitades del Djangos Modelos](#0048----utilitades-del-djangos-modelos)
    - [01:22 -+- Session.save()](#0122----sessionsave)

---

## Today's Menu

### Main Course

    GOAL_ : First prototype of Smartass Journal app / Project tobias.fyi  

--------∫--------

### SELECT * FROM Session

#### Soundtrack

- pass

#### Extras

- See the size of a directory / tree using `du -sh directory/` command or other permutations of `du`.
- [Adobe Color](https://color.adobe.com/create)

---

## Session.log

--------∫--------

### 00:18 -+- Session.init

Yeah I know...

...once again it's technically not April 9 anymore, but who cares?

----∫----

Decided to finally look up methods for finding the size of directories via the command line.

I wanted to find out the size of the directories in which I'd been putting all of the iterations of a straight-up fillable PDF I designed and built today. There are many iterations, and thought it would be a good idea to check the size before committing to git / pushing to GitHub. I'm not sure what the repository size restrictions are for free accounts, but I don't want huge files cluttering things up regardless.

    $ du -sh /PDFillable/
    9.6M    PDFillable

Nice to know! Here's some highlights from the man page, edited for brevity...or not.

    $ man du

    DU(1)                     BSD General Commands Manual                    DU(1)
    NAME
        du -- display disk usage statistics
    SYNOPSIS
        du [-H | -L | -P] [-a | -s | -d depth] [-c] [-h | -k | -m | -g] [-x] [-I mask] [file ...]
    DESCRIPTION
        The du utility displays the file system block usage for each file argument and for 
        each directory in the file hierarchy rooted in each directory argument.  If no file 
        is specified, the block usage of the hierarchy rooted in the current directory is 
        displayed.

    The options are as follows:
    -a          Display an entry for each file in a file hierarchy.
    -c          Display a grand total.
    -d depth    Display an entry for all files and directories depth directories deep.
    -H          Symbolic links on the command line are followed, symbolic links in file 
                hierarchies are not followed.
    -h          "Human-readable" output.  Use unit suffixes: Byte, Kilobyte, Megabyte, 
                Gigabyte, Terabyte and Petabyte.
    -I mask     Ignore files and directories matching the specified mask.
    -g          Display block counts in 1073741824-byte (1-Gbyte) blocks.
    -k          Display block counts in 1024-byte (1-Kbyte) blocks.
    -L          Symbolic links on the command line and in file hierarchies are followed.
    -m          Display block counts in 1048576-byte (1-Mbyte) blocks.
    -P          No symbolic links are followed.  This is the default.
    -r          Generate messages about directories that cannot be read, files that cannot be 
                opened, and so on.  This is the default case.  This option exists solely for 
                conformance with X/Open Portability Guide Issue 4 (``XPG4'').
    -s      Display an entry for each specified file.  (Equivalent to -d 0)
    -x      File system mount points are not traversed.

Trying out some other options:

    $ du -ash PDFillable/
    2.0M    PDFillable/2019-04-09-3-pdform_fillable_smargin.indd
    140K    PDFillable/pyramid-pdform-fillable.pdf
    652K    PDFillable/2019-04-09-pyramid-pdform.pdf
    2.1M    PDFillable/2019-04-09-3-pdform_fillable.indd
    140K    PDFillable/pyramid-pdform-fillable-1.pdf
    612K    PDFillable/2019-04-09-pyramid-pdform-5.pdf
    608K    PDFillable/2019-04-09-pyramid-pdform-fillable-2.pdf
    676K    PDFillable/2019-04-09-pyramid-pdform-4.pdf
    680K    PDFillable/2019-04-09-pyramid-pdform-3.pdf
    2.1M    PDFillable/2019-04-09-4-pdform_fillable.indd
    9.6M    PDFillable

So I think if I haven't added .indd to my .gitignore, that will help out. Also going to be sure that .ai and .psd are in there as well.

> Challenges/.gitignore

    # Creative files
    *.indd
    *.ai
    *.psd

    $ git commit -m "Added creative files"
    And boom goes the dynamite.

---

### 00:33 -+- django-model-utils

Dug into some django packages and found one that would've helped out a lot with my session last night. Rather than having to look up how to calculate the duration and whatnot, it looks like *django-model-utils* has tools for this already built.

I actually first saw the package while reading Two Scoops of Django.

\#burnspiracy2019

The one I'm particularly interested in is the TimestampField.

However, in true flippy-floppy fashion, I'm going to work on a different part of the project.

The question then is, given that I've worked on the sajourn app on a new branch, should I merge that before starting the next app? I know I can create them concurrently and have multiple branches going...but do I want to deal with that?

I would be good to learn, no doubt.

    $ git checkout sajourn
    check that ish out.

Did I say that I'm a flipp-floppy some—probably most—of the time? Because that's just how I am.

Changed my mind again—decided to finish up the first prototype of sojourn before going onto the next app

And that means...django-model-utils!


But first, let's extend some templates, shall me?

---

### 00:37 -+- Template Extendor

> sajourn/templates/base.html

I want to include the whole navbar in base.html, which means there will be something of a code block to change which navbar link is active depending on the page.

I'll figure that part out later. For now, I just put the entire body inside the {% block content %} in base.html. That also has the nice sife-effect of everything being indented correctly. e.g. if I included only the top \<body\> tag in base.html or vice versa, the indentation just looks a little weird because that tag is never closed / opened within the context of that one file.

---

### 00:48 -+- Utilitades del Djangos Modelos

    $ conda install -c conda-forge django-model-utils
    django-model-utils-3 | 18 KB

Created main.scss to start using some smart(ass) stylings. Opened up a new terminal to have sass autogenerate main.css.

    $ sass --watch main.scss main.css
    Compiled main.scss to main.css.
    Sass is watching for changes. Press Ctrl-C to stop.

Spent a little while getting some good colors from [Adobe Color](https://color.adobe.com/create). Awesome site.

----∫----

Now, back to the show...

Unfortunately, there really is no good documentation for django-model-utils.

I don't want to spin my wheels on figuring this out now. However, I do intend to try it out sometime soon. I also want to give some of the packages in [this list](https://vsupalov.com/favorite-django-packages-2019/) a go.

Here are a few that, at first glance, could be useful for this project:

- django-taggit
- django-filter
- django-tables2
- django-sql-explorer
- django-crispy-forms
- django-extensions
  - shell_plus
  - reset_db
  - runserver_plus
- djang-debug-toolbar

Instead of spending time on the model utils ahora, I'm going to spend this time writing a couple more models in an attempt at making the smartass journal behave at least somewhat like the app I currently use to do this type of thing.

That means I need to add some model relationship goodies. Some decisions must be made with regards to using one-to-one, one-to-many, or many-to-many.

Starting out, the relationships will be as follows:

Project > one-to-one > Activity > (many-to-many) > Entry

I forgot that I need to register the model in tobiasfyi_project/admin.py. Also went ahead and created the superuser to be able to log into the admin site.

---

### 01:22 -+- Session.save()

And there you have it!

Although I didn't write a whole lot of code this time, I'm still learning a lot. Every time I start a new project I dig into different aspects of the prototyping process. I love that.

Es todo una práctica, mi amigo.

Never stop practicing.
Never stop exploring.
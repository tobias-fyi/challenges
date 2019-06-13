# 2019-03-18 | #015

\#100DaysofCode

- [2019-03-18 | #015](#2019-03-18--015)
  - [MENU_Today](#menutoday)
    - [Main Course](#main-course)
    - [Extras](#extras)
    - [--------14:25--------](#1425)
    - [--------14:31--------](#1431)
    - [--------14:33--------](#1433)
    - [--------14:49--------](#1449)
    - [--------15:03--------](#1503)
    - [--------15:23--------](#1523)
    - [--------15:25--------](#1525)
    - [--------15:35--------](#1535)
    - [--------15:47--------](#1547)
    - [--------15:55--------](#1555)

---

## MENU_Today

### Main Course

    GOAL_ : Rewrite INIT script to use Markdown
    GOAL_ : Build INIT script as CLI Tool using Click

### Extras

Soundtrack: [Horizon Zero Dawn OST](https://youtu.be/p_5bzTSGIVw)

### --------14:25--------

New Format,  *who dis*?

I recently decided to start using markdown for my coding journals.  
However, I haven't had time yet to rewrite the INIT script to create .md instead of .txt.

So let's do it.

First, gotta jerry-rig something to raise my desk chair so I can rest my knees.
I haven't had any way of sitting at this workstation for the past month or two, but I feel like it's time. Or maybe that's just my body telling me I need to go on daily runs again (first run in weeks this morning).

### --------14:31--------

I knew those extra speakers would be good for something.
Ok now let's get after it.

As you can probably see, this journal is already using the markdown format.
That's because I created a sort of template while taking notes during my workday yesterday.

One idea I had while doing this is to have a file that acts as the template, which the script reads / copies into the new entry.

Updated the Goals section to reflect my newly defined goals for this session and the next iteration of the script.

### --------14:33--------

Given the above goals, I'm thinking I should create a new virtual environment for the program.  
The Click [Documentation](https://click.palletsprojects.com/en/7.x/quickstart/) says to use virtualenv, so I hope it still works with a conda environment.  
Trying out the Python [code-formatting package Black](https://black.readthedocs.io/en/stable/index.html) for the first time as well.  
One more to test out because it's relevant is [Python-Markdown](https://python-markdown.github.io/)

I believe that's all I need for this environment. Time to conda create that shit. 

    $ conda create -n fyinit python=3.7 click black markdown
    > PackagesNotFoundError:

Hmm...well I guess not. Conda doesn't have it in their package index.  
...  
[With a little research](https://anaconda.org/conda-forge/black) I see I just have to install it using conda forge. I'll install it into the env once it's created and activate.
Ok, fine I'll update first...

    $ conda update -n base -c defaults conda
    > environment location: /anaconda3
        added / updated specs:
            - conda

I just thought of another package I'd like to try out: something to create a progress bar.  
I remember hearing of a recipe on Talk Python to Me to create one just with a few lines of code, but I'm going to do some research.  

Holy shit there are a ton of progress bar packages. I think I've seen or heard of the tqdm package so I'll go with that. Thanks, Reddit!  
...  
Pretty neat little package.  

    tqdm means "progress" in Arabic (taqadum, تقدّم) and is an abbreviation for “I love you so much” in Spanish (te quiero demasiado).

### --------14:49--------

Ok time to finally create the environment...  
But wait! There's more!

I have to install this via conda-forge as well.

    $ conda create -n fyinit python=3.7 click markdown
    > Preparing transaction: done
    > Verifying transaction: done
    > Executing transaction: done

^^ Sometimes monospace makes the design parts of my brain very happy.

    $ conda activate fyinit
    > /anaconda3/envs/fyinit/bin/python

Not sure if it really matters, but I like putting that path in the shebang line for scripts so they run with the version of Python that's installed in the environment.

Remembered another one I want to install in the environment: iPython.  
If you've never used it, you should give it a go. It makes the Python console niiiice.

    $ conda install ipython
    >

Hokey Doke—now to install tqdm:

    $ conda install -c conda-forge tqdm
    >

The output included something about that certain packages will be "superceded by a higher-priority channel". Hopefully nothing is broken. Regardless I'll learn something.  
...and now to install black:

    $ conda install -c conda-forge black
    >

### --------15:03--------

Boom!  
There we have a fresh new virtual environment thanks to Conda.

I'll weight that time as 0.5 because it's not technically writing code, but was useful for me to learn and go through the process again.

Created new directory for this project—decided to go with a new dir in this repo for on-going projects. This way I don't have to copy over the code each time...
...  
I don't *have* to...but I still might because it's a challenge and whatnot.

    $ cd /Challenges/100DaysofX/01_Code/
    $ mkdir Projects
    $ cd $_
    $ pwd
    > /Challenges/100DaysofX/01_Code/Projects

In the spirit of trying out new things, I'm going to use flake8 as the Python linter instead of the usual pylint.  

    $ conda install flake8
    >

Set that up + new Python path in settings.

    "settings": {
        "python.pythonPath": "/anaconda3/envs/fyinit/bin/python",
        "python.linting.pylintEnabled": false,
        "python.linting.flake8Enabled": true,
        "python.formatting.provider": "black",
        "python.formatting.blackPath": "/anaconda3/envs/fyinit/bin/black",
        "python.formatting.blackArgs": [
            "--line-length=90"
        ],
        "editor.formatOnSave": true,
        "files.exclude": {
            "**/.git": true,
            "**/.svn": true,
            "**/.hg": true,
            "**/CVS": true,
            "**/.DS_Store": true,
        },
        "editor.wordWrap": "on",
        "markdown.extension.showExplorer": true
    }

Installed the pytest package for unit testing. First time for that as well!

    $ conda install pytest

    "settings": {
        "python.unitTest.pyTestEnabled": true,
        "python.unitTest.pyTestPath": "/anaconda3/envs/fyinit/bin/pytest",
    }

### --------15:23--------

Okaaaaay now I think I'm ready to go...  
Like I mentioned earlier, I'll count that time as 0.5, which leaves me with about 30 mins left for this session.

Will copy the current code for this script into the projects directory, work on it there, then copy it into the directory for each day that I work on it.

    /Projects/fyinit/fyinit.py

### --------15:25--------

Already seeing some changes due to using black. Nothing big yet, though.

Reading / watching up on how to use Click.

First, create a "proper python package":

    $ cd Projects/fyinit/
    $ touch setup.py
    $ code $_
    >

### --------15:35--------

Well...found my answer about the shebang line in the Click Documentation

    When writing command line utilities, it’s recommended to write them as modules that are distributed with setuptools instead of using Unix shebangs.

Going to set up a test to make sure everything is working.

### --------15:47--------

Testing out Click:

    $ pip install --editable .
    > Installing collected packages: fyinit
    > Running setup.py develop for fyinit
    > Successfully installed fyinit
    > /anaconda3/envs/fyinit/bin/fyinit

And there she is! My very first Python package. How cuuuuuute!  
Time to test her out using the test example in the documentation:

    $ fyinit
    > fyi initilization...

She works!  
This is exciting.

### --------15:55--------

Going to call it for this session.

Hasta Bañanas, Amigo!
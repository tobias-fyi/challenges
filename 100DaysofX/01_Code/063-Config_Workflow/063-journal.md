# 2019-05-05 | #100DaysofCode

## Day 063 / 100

---

## SELECT * FROM Project

### Project.abstract

    GOAL__: Utilize useful bash / terminal functionality to level up my efficiency  

### Project.loxocache(2019-05)

- pass

--------∫--------

## SELECT * FROM Session

### Session.abstract

    GOAL_063 : grep  

#### Session.cache

- Mayan Warrior [mixes](https://soundcloud.com/mayanwarriorofficial) / [videos](https://vimeo.com/mayanwarrior)
  - [Monolink](https://soundcloud.com/mayanwarriorofficial/monolink-live-mayanwarrior-bm2018)
  - [Anton Tumas](https://soundcloud.com/mayanwarriorofficial/anton-tumas-mayan-warrior-burning-man-2018)
  - [Kris Berle](https://soundcloud.com/mayanwarriorofficial/kris-berle-mayan-warrior-burning-man-2018)

---

## Session.sojourn(2019-05-05)

### Loxocache

    TASK√128 : Create new virtual environment / project dir for Challenges  
    TASK√128 : Update Challenges workspace settings  
    TASK√128 : Fix the integrated terminal in my Fineyedesign code-workspace  

    IDEA_128 : Add day of the year to prompt - e.g. 128/365  
    IDEA_128 : Click CLI function to format terminal output  
    IDEA_128 : Set envirovars for each workspace to use in snippets  
    IDEA_128 : Environment Variable Blog / Site - envirovar.com


--------∫--------

### 08:58 ~ Grep

At some point over the last few days I realized that I could be much more efficient with my terminal navigation if I knew how to use a few of the more appropriate tools. Namely, I want to be comfortable using the grep command to search files, and I want to have a working knowledge of how to use the text editor VIM.

Glad to see that [Corey Schafer has a tutorial](https://youtu.be/VGgTmxXp7xQ) on using Grep.

    KB+ : GREP = Global Regular Expression Print  

---

### 09:14 ~ Some Minor Greps

Before I get going on grep, I have a couple of things I'd like to try and figure out.

    TASK√128 : Create new virtual environment / project dir for Challenges  
    TASK√128 : Fix the integrated terminal in my Fineyedesign code-workspace  

    IDEA_128 : Add day of the year to prompt - e.g. 128/365  

I moved the current `Challenges` directory to the desktop, then ran the command to create a new project...

    $ mkproject Challenges
    WARNING: the pyenv script is deprecated in favour of `python3.7 -m venv`
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/Challenges/bin/predeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/Challenges/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/Challenges/bin/preactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/Challenges/bin/postactivate
    virtualenvwrapper.user_scripts creating /Users/Tobias/.vega/Challenges/bin/get_env_details
    Creating /Users/Tobias/workshop/Challenges
    Setting project for Challenges to /Users/Tobias/workshop/Challenges

Then I moved the important contents into the new directory...

    ╭─ Challenges » tobiasfyi » ~/workshop/Challenges       19.05.08 ∫ 09:32:41
    ╰─ mv ~/Desktop/Challenges/* .

Realized that the above command didn't move .git or .gitignore, so moved those separately...

    ╭─ tobiasfyi » ~/Desktop/Challenges »  master ●        19.05.08 ∫ 09:33:10
    ╰─ mv .git ~/workshop/Challenges

    ╭─ tobiasfyi » ~/Desktop/Challenges                     19.05.08 ∫ 09:33:25
    ╰─ mv .gitignore ~/workshop/Challenges

Sweet! Now I can use the `workon` command to work on Challenges. Man I really love this workflow...

    ╭─ tobiasfyi » ~/workshop/Fineyedesign »  master ?         19.05.08 ∫ 09:34:25
    ╰─ workon Challenges

Then I made sure that git is working correctly...

    ╭─ Challenges » tobiasfyi » ~/workshop/Challenges »  master ●  19.05.08 ∫ 09:34:50
    ╰─ git add -A

    ╭─ Challenges » tobiasfyi » ~/workshop/Challenges »  master ✚  19.05.08 ∫ 09:34:57
    ╰─ git commit -m "New project dir / venv created + contents moved accordingly"

    ╭─ Challenges » tobiasfyi » ~/workshop/Challenges »  master ↑1 19.05.08 ∫ 09:35:24
    ╰─ git push origin master
    Enumerating objects: 3, done.
    ...
    To github.com:tobias-fyi/challenges.git
    eacd8c4..65bcbe0  master -> master

I also decided to switch the font in vscode to Inconsolata for Powerline so that the symbols in my terminal show up correctly when copied over...

> .vscode/settings.json

    "terminal.integrated.fontFamily": "Inconsolata for Powerline",
    "terminal.integrated.fontSize": 18,

Nice to switch it up a bit. Keeps my mind fresh / on me toesies.

---

### 09:45 ~ Finishments

    TASK√128 : Create new virtual environment / project dir for Challenges  

Just need to update the workspace settings for `Challenges` and I'll be groovy on this TASK.

I'm actually going to delete the old workspace file and create a new one, just in case that fixes the issue with the virtual environment.

...this font is real nice =) such an unexpected / nice fresh of breathe air.

Oooooh I have a good search query to use as `grep` practice—I want to find the last time I updated pip because I had to again and am wondering if I need to change something so new venvs will automatically install the latest version.

    ╭─ Challenges » tobiasfyi » ..enges/100DaysofX/01_Code »  master ?     19.05.08 ∫ 09:55:28
    ...

I just decided I'd like to have less of the path in the prompt. In the example above the path makes the prompt a bit too long for my taste. Fixing that now...

> ~/.zshrc

My current setup for that segment:

    POWERLEVEL9K_SHORTEN_DIR_LENGTH=24
    POWERLEVEL9K_SHORTEN_DELIMITER=".."
    POWERLEVEL9K_SHORTEN_STRATEGY="truncate_absolute_chars"

I know this can get as unwieldy as the previous setup, but I'll try it out for a bit to see.

    POWERLEVEL9K_SHORTEN_DIR_LENGTH=1
    POWERLEVEL9K_SHORTEN_DELIMITER=".."
    POWERLEVEL9K_SHORTEN_STRATEGY="truncate_to_first_and_last"

Which results in the following prompt...a bit nicer, to be sure...

    ╭─ Challenges » tobiasfyi » ~/../../../01_Code »  master ?          19.05.08 ∫ 10:05:34
    ╰─

Now for the final polish...

    TASK√128 : Update Challenges workspace settings  

    "settings": {
        "python.pythonPath": "/Users/Tobias/.vega/Challenges/bin/python",
        "python.linting.pylintEnabled": true,
        "python.linting.pylintPath": "/Users/Tobias/.vega/Challenges/bin/pylint",
        "python.linting.pylintArgs": [
            "--load-plugins",
            "pylint_django,pylint_flask",
        ],
        "editor.formatOnSave": true,
        "files.exclude": {
            "**/.git": true,
            "**/.svn": true,
            "**/.hg": true,
            "**/CVS": true,
            "**/.DS_Store": true,
        },
        "python.formatting.provider": "black",
        "python.formatting.blackPath": "/Users/Tobias/.vega/Challenges/bin/black",
        "python.formatting.blackArgs": [
            "--line-length=79",
        ]
    }

That's much better.

---

### 10:12 ~ SumChaecks

Now for the big moment...did this also fix the venv issue with the integrated vscode terminal?

Aaaaaaaand...it did!

Boom! No more Chinese laundry!

    TASK√128 : Fix the integrated terminal in my Fineyedesign code-workspace  

Actually...I'm not sure that it did. Nope. I feel like it is a bug in vscode, not something I'm doing.

I even

---

### 10:20 ~ In The Grep of the Moment

Time to search through my journal entries to see where I last mentioned the pip upgrade command...

    ╭─ Fineyedesign » tobiasfyi » ~/../../../../../2019-05 »  master ?         19.05.08 ∫ 10:26:00
    ╰─ grep -r -C 2 "pip install --upgrade pip" *
    19-05-02-edexxx_thurs.md-Kept receiving the prompt to update pip, so I did so (outside and inside the virtual environment).
    19-05-02-edexxx_thurs.md-
    19-05-02-edexxx_thurs.md:    $ pip install --upgrade pip
    19-05-02-edexxx_thurs.md-    Successfully installed pip-19.1
    19-05-02-edexxx_thurs.md-
    --

----ƒ----

Had an idea earlier that I forgot to write down—it would be super sweeeeeeet to be able to type in a command in the terminal and have the terminal output in my clipboard to be formatted nicely. I.e. I want the right side of the prompt to be aligned to the right and everything tabbed out correctly so I can simply paste and move on.

    IDEA_128 : Click CLI function to format terminal output  

----ƒ----

### VSCode EnviroVars

Just had another idea as well...this one regarding vscode snippets and env variables. I wonder if I can set environment variables for each workspace that can set variables to be used inside of the snippets. E.g. for the sym-stamp `----ƒ----` the snippet looks like...

    "symbol_stamp": {
        "prefix": "sym-stamp",
        "body": [
            "----${1:symbol}----",
        ]
    },

Doing it this way is fine. But I still have to manually input the project symbol every time I use it. If I were able to set a project envirovar...

damnit...that's another good URL that I can't afford right now...

    IDEA_128 : Environment Variable Blog / Site - envirovar.com

Anyways...if I could set envirovars for each workspace, I could potentially put the symbol into the snippet automatically. That'd be quite nice.

    IDEA_128 : Set envirovars for each workspace to use in snippets  

Looking through [the vscode docs](https://code.visualstudio.com/docs/editor/variables-reference#_environment-variables) on the subject, I found some useful info...

#### Predefined variables

The following predefined variables are supported:

    ${workspaceFolder}         - the path of the folder opened in VS Code
    ${workspaceFolderBasename} - the name of the folder opened in VS Code without any slashes (/)
    ${file}                    - the current opened file
    ${relativeFile}            - the current opened file relative to workspaceFolder
    ${fileBasename}            - the current opened file's basename
    ${fileBasenameNoExtension} - the current opened file's basename with no file extension
    ${fileDirname}             - the current opened file's dirname
    ${fileExtname}             - the current opened file's extension
    ${cwd}                     - the task runner's current working directory on startup
    ${lineNumber}              - the current selected line number in the active file
    ${selectedText}            - the current selected text in the active file
    ${execPath}                - the path to the running VS Code executable

${CoolFont}                - How do I get the italics?

![coolFontSearch](assets/coolFont.png)

#### Environment variables

You can also reference environment variables through the ${env:Name} syntax (for example, ${env:PATH}).

    {
        "type": "node",
        "request": "launch",
        "name": "Launch Program",
        "program": "${workspaceFolder}/app.js",
        "cwd": "${workspaceFolder}",
        "args": [ "${env:USERNAME}" ]
    }

Looks like I can access envirovars by using the ${env:Name} syntax. So I just need to figure out how to set envirovars for each project.

At the top of the docs page in question, they mention that...`variable substitution is supported inside key and value strings in launch.json and tasks.json files using ${variableName} syntax.`

So maybe if I include `${symbol}` in launch.json...?

[Found this section](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file) of the docs that talks about a variable definitions file.

    An environment variable definitions file is a simple text file containing key-value pairs in the form of environment_variable=value, with # used for comments.

    Multiline values are not supported, but values can refer to any other environment variable that's already defined in the system or earlier in the file. For more information, see Variable substitution.

I'm going to try creating a enviro.env file in the project directory and see if it is picked up.

> Challenges/enviro.env

    # -------- Project EnviroVars -------- #
    project_symbol="ƒ"

#### Snippets

[Variables](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_variables) section of the vscode snippets documentation.

With $name or ${name:default} you can insert the value of a variable. When a variable isn’t set, its default or the empty string is inserted. When a variable is unknown (that is, its name isn’t defined) the name of the variable is inserted and it is transformed into a placeholder.

The following variables can be used:

    TM_SELECTED_TEXT The currently selected text or the empty string
    TM_CURRENT_LINE The contents of the current line
    TM_CURRENT_WORD The contents of the word under cursor or the empty string
    TM_LINE_INDEX The zero-index based line number
    TM_LINE_NUMBER The one-index based line number
    TM_FILENAME The filename of the current document
    TM_FILENAME_BASE The filename of the current document without its extensions
    TM_DIRECTORY The directory of the current document
    TM_FILEPATH The full file path of the current document
    CLIPBOARD The contents of your clipboard
    WORKSPACE_NAME The name of the opened workspace or folder

I don't see anything about using envirovars in snippets but I'm giving it a go anyways.

Nope that didn't work.

---

### 11:28 ~ (On/Up)Ward

Oh well, I don't want to spend any more time on this at the current momento. If I want to revisit it, I'll come back to it.

I'll have to deal with an extra few seconds / keystrokes every time I use it...for now.

![sympetts](assets/smyppets.gif)

----ƒ----

Hasta Luigi, Amigo!
# 2019-06-07 | #100DaysofCode

    GOAL-06-07 ~ Add header-creation functionality to Stradder  

## Day 096/100 | 158/365

- [2019-06-07 | #100DaysofCode](#2019-06-07--100daysofcode)
  - [Day 096/100 | 158/365](#day-096100--158365)
    - [17:21 ~ A Short(ish) Demurrage](#1721--a-shortish-demurrage)

---- Resources ----

- [Click Docs](https://click.palletsprojects.com/en/7.x/)

---- Sojourn ----

### 17:21 ~ A Short(ish) Demurrage

Demurrage: delay of vessel's departure or loading with cargo.

Got caught up for an hour or more adding functionality to the stradder tool when I was in the middle of working on a client's website...whoops.

Worth it though, as now I can easily turn this...

    rename_files.py
    Renames files according to defined format
    within target directory

...into this (with only a few strokes of the sweet, slick, steamy keys of this hard, thick keyboard)...

    # =============================== rename_files.py ================================ #
    # ================== Renames files according to defined format =================== #
    # =========================== within target directory ============================ #

WOW! AMAZING! HOW DID HE DO IT!

I'm not going to just tell everyone my secrets...

...here are some snippets of the code, however. You better enjoy the heck out of reading these.

```python
@click.command()
def cli():
    """Inserts string before and after each line of text in clipboard,
    with option to center content, 8-bit header-style."""

    text = pyperclip.paste()

    # ========| ... 1,000,000 lines of code later ... |======== #

    lines = text.split("\n")

    for i in range(len(lines)):
        if strip_confirm != "n":
            lines[i] = lines[i].strip()

        lines[i] = str(str_before) + lines[i] + str(str_after)

    text = "\n".join(lines)

    pyperclip.copy(text)
```

I spent too much time on writing that code that I didn't get around to actually writing the `rename_files.py` script which originally led me in this direction. So that will have to wait. 

It would be a good addition to the stradder tool, once I add some options and such. I don't want it to grow any bigger until I break it up into multiple commands / arguments / options.

Hasta *anyways*...., amigos!

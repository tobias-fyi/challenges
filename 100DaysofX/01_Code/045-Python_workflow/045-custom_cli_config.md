# Command Line Configuration and Customization

A place to hold all of my CLI configs and config instructions.

Updated 19-04-17

    $ code ~/.zshrc
    
    # --------------------------------------- #
    # -------- Prompt Customizations -------- #
    # --------------------------------------- #

    # ---- Layout ---- #
    POWERLEVEL9K_PROMPT_ON_NEWLINE=true
    POWERLEVEL9K_PROMPT_ADD_NEWLINE=true

    # -------- Left Segments -------- #

    POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv context dir vcs)
    POWERLEVEL9K_LEFT_SEGMENT_SEPARATOR='»'
    POWERLEVEL9K_LEFT_SUBSEGMENT_SEPARATOR='»'
    POWERLEVEL9K_LEFT_SEGMENT_SEPARATOR_FOREGROUND="131"

    POWERLEVEL9K_CONTEXT_TEMPLATE='%m'
    VIRTUAL_ENV_DISABLE_PROMPT=1

    # -- Formatting -- #
    POWERLEVEL9K_SHORTEN_DIR_LENGTH=24
    POWERLEVEL9K_SHORTEN_DELIMITER=".."
    POWERLEVEL9K_SHORTEN_STRATEGY="truncate_absolute_chars"
    POWERLEVEL9K_DIR_PATH_HIGHLIGHT_BOLD=true
    POWERLEVEL9K_DIR_PATH_HIGHLIGHT_FOREGROUND="138"

    # -- Colors -- #
    POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="131"
    POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND='131'
    POWERLEVEL9K_DIR_HOME_FOREGROUND='131'
    POWERLEVEL9K_CONTEXT_DEFAULT_FOREGROUND="131"

    POWERLEVEL9K_DIR_DEFAULT_BACKGROUND="none"
    POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND='none'
    POWERLEVEL9K_DIR_HOME_BACKGROUND='none'
    POWERLEVEL9K_CONTEXT_DEFAULT_BACKGROUND="none"

    POWERLEVEL9K_VCS_CLEAN_FOREGROUND='131'
    POWERLEVEL9K_VCS_CLEAN_BACKGROUND='none'
    POWERLEVEL9K_VCS_UNTRACKED_FOREGROUND='131'
    POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='none'
    POWERLEVEL9K_VCS_MODIFIED_FOREGROUND='124'
    POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='none'

    POWERLEVEL9K_VIRTUALENV_BACKGROUND="none"
    POWERLEVEL9K_VIRTUALENV_FOREGROUND="096"

    # -------- Right Segments -------- #

    POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status history time)
    POWERLEVEL9K_RIGHT_SEGMENT_SEPARATOR='«'
    POWERLEVEL9K_RIGHT_SUBSEGMENT_SEPARATOR='«'
    POWERLEVEL9K_RIGHT_SEGMENT_SEPARATOR_FOREGROUND="131"

    # -- Formatting -- #
    POWERLEVEL9K_TIME_FORMAT="%D{%y.%m.%d ∫ %H:%M:%S}"

    # -- Colors -- #

    POWERLEVEL9K_TIME_FOREGROUND="131"
    POWERLEVEL9K_HISTORY_FOREGROUND="131"

    POWERLEVEL9K_TIME_BACKGROUND="none"
    POWERLEVEL9K_STATUS_DEFAULT_BACKGROUND="none"
    POWERLEVEL9K_STATUS_OK_BACKGROUND="none"
    POWERLEVEL9K_STATUS_ERROR_BACKGROUND="none"
    POWERLEVEL9K_HISTORY_BACKGROUND="none"

---

## Other Options to Explore

- [Powerlevel9k Wiki](https://github.com/bhilburn/powerlevel9k/wiki).
- [Prompt Segments](https://github.com/bhilburn/powerlevel9k#available-prompt-segments)
- todo
- [custom_command](https://github.com/bhilburn/powerlevel9k#custom_command)

### Python

POWERLEVEL9K_PYTHON_ICON
POWERLEVEL9K_PYENV_PROMPT_ALWAYS_SHOW

- virtualenv
  - Your Python VirtualEnv
- anaconda
  - Your active Anaconda environment.
- pyenv
  - Your active python version as reported by the first word of pyenv version. Note that the segment is not displayed if that word is system i.e. the segment is inactive if you are using system python

POWERLEVEL9K_SHORTEN_STRATEGY="truncate_with_package_name"
POWERLEVEL9K_DIR_PACKAGE_FILES=(package.json composer.json)

- Would be sweet to set up a custom name for each project
- Or, I could set up the project symbols / icons in this json file and have that be read in
  - I really want to do this anyways - maybe use a custom_command?

---

## Icons

Can use the `get_icon_names` command to get a list of all of the icon variables.

POWERLEVEL9K_ROOT_ICON: ⚡

POWERLEVEL9K_LEFT_SEGMENT_SEPARATOR=$'\uE0B1'  
POWERLEVEL9K_RIGHT_SEGMENT_SEPARATOR=$'\uE0B3'

---

## Colors

023 - 045 are cool greens and blues.

POWERLEVEL9K_TIME_FOREGROUND='red'
POWERLEVEL9K_TIME_BACKGROUND='blue'
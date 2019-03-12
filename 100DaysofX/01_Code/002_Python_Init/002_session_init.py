#! /anaconda3/envs/tobias_fyi/bin/python

# 100DaysofCode - Day 2
# 002_session_init.py
# create directory + journal for daily session

import os
import sys
import datetime
import subprocess
import time


def justify_center(content, width):
    '''Centers string with dashes - width chars wide'''

    text = content
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].center(width, '-')
    text = '\n'.join(lines)
    return text


def table_printer(array, title, left_width, right_width):
    '''Formats list - table of contents style'''

    print(f'{title}'.center(left_width + right_width, '-'))

    for k, v in enumerate(array):
        print(str(k).ljust(left_width, '.') + str(v).rjust(right_width))


# set up all the time + date variables
c_time = time.strftime("%H:%M", time.localtime(time.time()))
today = datetime.date.today()
c_year = str(today.year)
c_month = str(today.month).zfill(2)
c_day = str(today.day).zfill(2)
c_date = str(today)

# chars to strip off of title
strip_chars = '`~!@#$%^&*()+=,.\\|/<>?;:\'"[]{}'

# Relevant dir / file information
p_name = ''
p_sym = 'º'
j_num = ''
csg = ''

# visual separators - horizontal lines
sep_lg = justify_center(p_sym, 79)
sep_med = justify_center(p_sym, 33)
sep_sm = justify_center(p_sym, 17)

p_paths = {
    'p_all': '/Users/Tobias/Documents/Projects/Challenges/'
}  # dict to hold paths

term_commands = {
    'code': ['code'],
    'code_ws': ['code'],
}  # dict to hold terminal commands

# list challenge directories
os.chdir(p_paths['p_all'])
p_list = os.listdir(os.getcwd())
p_list.sort()
for proj in p_list:
    if os.path.isfile(os.path.join(p_paths['p_all'], proj)):
        # removes files from list - .DS_STORE, README, etc.
        p_list.remove(proj)

print(sep_med)
justify_center(p_sym, 33)
table_printer(p_list, 'Choose your challenge', 8, 25)
print(sep_med)

try:  # find selected directory + add path to dict for later
    p_index = int(input())
    p_root = p_list[p_index]
    p_paths['p_root'] = os.path.join(p_paths['p_all'], p_root)
    os.chdir(p_paths['p_root'])
    p_path = os.getcwd()
except FileNotFoundError:
    print()
    print('Project not found...')
    print(sep)

# construct challenge name out of dir name
# TODO: if 100DaysofX is chosen - construct using 2 dir levels
# TODO: use dates instead of user input to determine day #
print('Enter day #:')
print(sep_sm)
j_num = input().zfill(3)
print(sep_med)

# TODO: nav to specific challenge directory
# TODO: check for existing dir + creates one if not - nav into it
# TODO: prompts for session goal and any tasks
# TODO: creates journal entry with challenge + day# + date + goal
# TODO: open that journal entry in VSCode

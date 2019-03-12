#! /anaconda3/envs/tobias_fyi/bin/python

# 100DaysofCode - Day 3
# 003_session_init.py
# create directory + journal for daily session

import os
import sys
import datetime
import subprocess
import time


def justify_center(content, width, symbol):
    '''Centers string in symbol - width chars wide'''

    text = content
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].center(width, symbol)
    text = '\n'.join(lines)
    return text


def table_printer(array, title, left_width, right_width):
    '''Formats list - table of contents style'''

    print(f'{title}'.center(left_width + right_width, '-'))

    for k, v in enumerate(array):
        print(str(k).ljust(left_width, '.') + str(v).rjust(right_width))


def dir_picker():
    pass


# set up all the time + date variables
c_time = time.strftime("%H:%M", time.localtime(time.time()))
today = datetime.date.today()
c_year = str(today.year)
c_month = str(today.month).zfill(2)
c_day = str(today.day).zfill(2)
c_date = str(today)

start_date = [2019, 3, 4]
start_date = datetime.date(start_date[0], start_date[1], start_date[2])
day_num = str((today - start_date).days).zfill(3)

# aesthetic informatics
v_width = 33
p_icon = 'º'
s_icon = '-'
spacer = ' '
ps_spacer = f'{s_icon*2}{p_icon}{s_icon*2}'


# visual separators - horizontal lines
sep = justify_center(p_icon, v_width, s_icon)
sep_sm = justify_center(p_icon, 17, s_icon)
sep_space = justify_center(p_icon, v_width, spacer)
sep_ps = justify_center(ps_spacer, v_width, spacer)

p_paths = {
    'p_all': '/Users/Tobias/Documents/Projects/Challenges/'
}  # dict to hold paths

term_commands = {
    'code': ['code'],
    'code_ws': ['code'],
}  # dict to hold terminal commands

# list challenges (directories)
# TODO: convert this into a function
os.chdir(p_paths['p_all'])
p_list = os.listdir(os.getcwd())
p_list.sort()
for proj in p_list:
    if os.path.isfile(os.path.join(p_paths['p_all'], proj)):
        # removes files from list - .DS_STORE, README, etc.
        p_list.remove(proj)

print(sep)
table_printer(p_list, 'Choose your challenge', 8, 25)
print(sep)
print(sep_ps)

try:  # find selected directory + add path to dict for later
    p_index = int(input())
    p_root = p_list[p_index]
    p_paths['p_root'] = os.path.join(p_paths['p_all'], p_root)
    os.chdir(p_paths['p_root'])
    p_path = os.getcwd()
    print()
except FileNotFoundError:
    print()
    print('Challenge not found...')
    print(sep)

print(os.getcwd())

# TODO: convert this into a function

c_list = os.listdir(os.getcwd())
c_list.sort()
for challenge in c_list:
    if os.path.isfile(os.path.join(p_paths['p_root'], challenge)):
        # removes files from list - .DS_STORE, README, etc.
        c_list.remove(challenge)

print(sep)
table_printer(c_list, 'Choose again', 8, 25)
print(sep)
print(sep_ps)

try:  # find selected directory + add path to dict for later
    c_index = int(input())
    c_root = c_list[c_index]
    p_paths['c_root'] = os.path.join(p_paths['p_root'], c_root)
    os.chdir(p_paths['c_root'])
    p_path = os.getcwd()
    print()
except FileNotFoundError:
    print()
    print('Challenge not found...')
    print(sep)

print(os.getcwd())

# TODO: check for existing dir + creates one if not - nav into it
# TODO: prompts for session goal and any tasks
# TODO: creates journal entry with challenge + day# + date + goal
# TODO: open that journal entry in VSCode

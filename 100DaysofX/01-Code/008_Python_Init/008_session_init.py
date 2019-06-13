#! /anaconda3/envs/tobias_fyi/bin/python

# 100DaysofCode - Day 8
# 008_session_init.py
# create directory + journal for daily session

import os
import sys
import datetime
import subprocess
import time


def justify_center(content, width, symbol):
    '''Centers string in symbol - width chars wide.'''

    text = content
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].center(width, symbol)
    text = '\n'.join(lines)
    return text


def table_printer(array, title, left_width, right_width):
    '''Formats list - table of contents style.'''

    print(f'{title}'.center(left_width + right_width, '-'))

    for k, v in enumerate(array):
        print(str(k).ljust(left_width, '.') + str(v).rjust(right_width))


def exit_program():
    print('Exiting program...')
    time.sleep(0.3)
    sys.exit()


def prompter(prompt):
    '''Returns user input from prompt.'''

    print(sep)
    print(f'{prompt.title()} for this session:')
    print(sep)
    print(sep_ps)
    return input().title()


def dir_picker(path, prefix):
    '''Allows user to choose from list of paths in cwd.'''

    os.chdir(path)

    dir_list = os.listdir(os.getcwd())
    dir_list.sort()

    for d in dir_list:
        if os.path.isfile(os.path.join(path, d)):
            # removes files from list - .DS_STORE, README, etc.
            dir_list.remove(d)

    print(sep)
    table_printer(dir_list, 'Choose-a-Dir', 8, 25)
    print(sep)
    print(sep_ps)

    try:  # find selected directory + add path to dict for later
        d_index = int(input())
        d_root = dir_list[d_index]
        p_paths[f'{prefix}_root'] = os.path.join(path, d_root)
        os.chdir(p_paths[f'{prefix}_root'])
        print()
    except FileNotFoundError:
        print()
        print('Dir not found...')
        print(sep)
        exit_program()


# set up all the time + date variables
c_time = time.strftime("%H:%M", time.localtime(time.time()))
today = datetime.date.today()
c_year = str(today.year)
c_month = str(today.month).zfill(2)
c_day = str(today.day).zfill(2)
c_date = str(today)

start_date = datetime.date(2019, 3, 4)
day_num = str((today - start_date).days + 1).zfill(3)

# aesthetic informatics
v_width = 33
p_icon = 'º'
s_icon = '-'
spacer = ' '
ps_spacer = f'{s_icon*2}{p_icon}{s_icon*2}'

# visual separators - horizontal lines - confirm
sep = justify_center(p_icon, v_width, s_icon)
sep_sm = justify_center(p_icon, 17, s_icon)
sep_space = justify_center(p_icon, v_width, spacer)
sep_ps = justify_center(ps_spacer, v_width, spacer)
yes_no = '[y/n]'

p_paths = {
    'p_all': '/Users/Tobias/Documents/Projects/Challenges/'
}  # dict to hold paths

term_commands = {
    'code': ['code'],
    'ws_code': ['code', 'challenges.code-workspace'],
}  # dict to hold terminal commands

os.chdir(p_paths['p_all'])

dir_picker(os.getcwd(), 'chal')
dir_picker(os.getcwd(), 'day')

lang = prompter('language')
subject = prompter('subject')
csg = prompter('goal')

header = f'''100 Days of Code
Day #{day_num}
{c_date}
{sep}
'''
meta = f'''
{justify_center(f'{lang} {subject}', 33, s_icon)}
Session Goals
TASK_{day_num} : {csg}
    CWT_01 :
    CWT_02 :
    CWT_03 :
{sep}
'''
body = f'''
----{c_time}

{sep}
'''

day_dir = f'{day_num}_{lang}_{subject}'
p_paths['day_path'] = os.path.join(os.getcwd(), day_dir)

if os.path.isdir(p_paths['day_path']):
    print('Directory already exists.')
    time.sleep(0.3)
    exit_program()

os.makedirs(day_dir)
time.sleep(0.3)
print('Directory created.')
print(sep_sm)
os.chdir(p_paths['day_path'])

j_name = f'{day_num}_journal.txt'
p_paths['j_path'] = os.path.join(os.getcwd(), j_name)
term_commands['code'].append(p_paths['j_path'])

print(f'Creating journal entry...')
print(sep)
time.sleep(0.3)

with open(f'{j_name}', 'w') as j:
    j.write(justify_center(header, 80, s_icon))
    j.write(meta)
    j.write(body)

time.sleep(0.3)
print('...')
print(sep)
print('Opening workspace...')
print(sep)
time.sleep(0.3)

p_paths['ws_path'] = os.path.join(p_paths['p_all'], '00_Admin')
os.chdir(p_paths['ws_path'])

subprocess.run(term_commands['ws_code'])
subprocess.run(term_commands['code'])

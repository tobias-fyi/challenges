#! /anaconda3/envs/tobias_fyi/bin/python

import os

alnum = {
    'W': '85',
    'X': '89',
    'Y': '95',
    'Z': '99',
}

fill_num = 2
prefix_num = 0

file_paths = {
    'projects': '/Users/Tobias/Documents/Projects/',
    'chal': 'Challenges/100DaysofX/01_Code',
    'day': '011_Python_Dirrename',
    'ex': '011_Project_Ex',
    'vis': '3_visual/1_branding',
}

current = os.path.join(file_paths['projects'],
                       file_paths['chal'],
                       file_paths['day'],
                       file_paths['ex'],
                       file_paths['vis'],)

os.chdir(current)

# rename only files in one directory
# TODO: turn this into function(s)
# TODO: try out using dictionaries as described in 011_journal.txt-16:47
for f in os.listdir():
    if os.path.isdir(os.path.join(current, f)):
        f_split = f.replace('_', ' ').replace('-', ' ').split(' ')

        if len(f_split[0]) > 2:
            f_split.insert(0, )

        if f_split[0].isalpha():
            f_split[0] = alnum[f'{f_split[0]}']

        f_split[0] = f_split[0].zfill(fill_num)

        f_split = [f_split[i].title() for i in range(len(f_split))]

        new_name = '_'.join(f_split)

        print(new_name)

        # TODO: Add functionality to add leading number if doesn't exist

        # os.rename(f, new_name)

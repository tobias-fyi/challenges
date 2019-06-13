#! /anaconda3/envs/tobias_fyi/bin/python

# 100DaysofCode - Day 7
# 007_path_method.py
# test out functionality of os.path.dirname(path)

import os

p_paths = {
    'p_all': '/Users/Tobias/Documents/Projects/Challenges/100DaysofX/'
}

print(os.path.dirname(p_paths['p_all']))

# >> /Users/Tobias/Documents/Projects/Challenges

p_split = p_paths['p_all'].strip('/').split('/')

# returns list of path segments
# >> ['Users', 'Tobias', 'Documents', 'Projects', 'Challenges']

print(p_split)

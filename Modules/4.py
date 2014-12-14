# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月14日14:52:59

"""
Problem 4: Write a program to print directory tree.
The program should take path of a directory as argument
and print all the files in it recursively as a tree.
"""

import os
import sys


def dirtree():
    dir_name = sys.argv[1]
    list_dir(dir_name)


def list_dir(path):
    files = os.listdir(path)
    files.sort()
    f_len = len(files)
    for i in range(f_len):
        f = files[i]
        f_path = os.path.join(path, f)
        level = get_level(f_path)
        if i == f_len - 1:
            s_path = get_last_path(level)
        else:
            s_path = get_path(level)
        print s_path + f
        if os.path.isdir(f_path):
            list_dir(f_path)


def get_level(path):
    level = 0
    for x in path:
        if x == os.path.sep:
            level += 1
    return level


def get_path(level):
    if level == 0:
        path = '|'
    elif level == 1:
        path = '|-- '
    else:
        path = '|   ' * (level - 1) + '|-- '
    return path


def get_last_path(level):
    if level == 0:
        path = '\\'
    elif level == 1:
        path = '\-- '
    else:
        path = '|   ' * (level - 1) + '\-- '
    return path


dirtree()

"""
$ python 4.py /home/zhenqingwang/foo
Output:
foo
|-- a.txt
|-- b.txt
|-- code
|   |-- a.py
|   |-- b.py
|   |-- docs
|   |   |-- a.txt
|   |   \-- b.txt
|   \-- x.py
\-- z.txt
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日10:29:10

"""
Problem 7: Implement a program dirtree.py that takes a directory as argument and
prints all the files in that directory recursively as a tree.
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
Output
类似这样的格式
foo/
|-- a.txt
|-- b.txt
|-- bar/
|   |-- p.txt
|   `-- q.txt
`-- c.txt
"""


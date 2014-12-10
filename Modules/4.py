# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月10日19:07:08

"""
Problem 4: Write a program to print directory tree.
The program should take path of a directory as argument
and print all the files in it recursively as a tree.
"""

# TODO
import os
import sys


def dirtree():
    dir_name = sys.argv[1]
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            print '--'+name
            # print os.path.join(root, name)
        # for name in dirs:
            # print os.path.join(root, name)


dirtree()

"""
$ python 4.py /home/zhenqingwang/git_work/python-practice
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

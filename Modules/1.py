# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月10日18:03:05

"""
Problem 1: Write a program to list all files in the given directory.
"""

import os
import sys


def list_file():
    dir_name = sys.argv[1]
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            print os.path.join(root, name)
        for name in dirs:
            print os.path.join(root, name)

list_file()

"""
$ python 1.py /home/zhenqingwang/git_work/acm
Output:
类似这样的结果
/home/zhenqingwang/git_work/acm/1.py
"""

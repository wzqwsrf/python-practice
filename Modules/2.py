# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月10日18:03:05

"""
Problem 2: Write a program extcount.py to count number of files for each extension in the given directory.
The program should take a directory name as argument and print count and extension for each available file extension.
"""

import os
import sys


def extcount():
    dic = {}
    dir_name = sys.argv[1]
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            name_msg = name.split('.')
            suffix = name_msg[len(name_msg)-1]
            num = dic.get(suffix, 0)
            num += 1
            dic[suffix] = num
    for key, value in dic.items():
        print key, value

extcount()

"""
$ python 2.py /home/zhenqingwang/git_work/acm
Output:
类似这样的结果
py 2
java 1
class 1
sql 1
"""

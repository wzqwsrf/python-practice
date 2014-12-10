# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月10日19:06:36

"""
Problem 3: Write a program to list all the files in the given directory along with their length
and last modification time. The output should contain one line for each file containing filename,
length and modification date separated by tabs.
"""

import os
import sys


def list_file():
    dir_name = sys.argv[1]
    r_list = []
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            file_path = os.path.join(root, name)
            stat = os.stat(file_path)
            length = stat.st_size
            modify_date = stat.st_mtime
            r_list.append(name + ' ' + str(length) + ' ' + str(modify_date))
    for x in r_list:
        print x


list_file()

"""
$ python 3.py /home/zhenqingwang/git_work/acm
Output:
类似这样的结果
Solution.class 614 1415012017.51
Solution.java 521 1415011920.35
2.py 557 1413515992.85
postgresql.sql 652 1413432212.98
1.py 431 1413457484.79
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月21日09:55:40

"""
Problem 12: Write a program mydoc.py to implement the functionality of pydoc.
The program should take the module name as argument and print documentation
for the module and each of the functions defined in that module.
"""

import sys
import inspect


def mydoc():
    module_name = sys.argv[1]
    module_name = __import__(module_name)
    print module_name.__doc__
    f_list = dir(module_name)
    print f_list
    for f in f_list:
        if inspect.isfunction(f) is not False:
            print f

mydoc()

"""
Output
foo.zip
9.py
10.py
"""

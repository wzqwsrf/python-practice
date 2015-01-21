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
    help(module_name)

mydoc()

"""
Output
$ python 12.py os
Help on module os:

DESCRIPTION

os - OS routines for Mac, NT, or Posix depending on what system we're on.
...

FUNCTIONS

getcwd()
    ...
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 16: Write a function extsort to sort a list of files based on extension.
"""

def extsort(slist):
    slist.sort(key = lambda s : s.split('.')[1])
    return slist

print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

"""
Output:
['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
"""

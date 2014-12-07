# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:19:58

"""
Problem 29: Write a function array to create an 2-dimensional array.
The function should take both dimensions as arguments.
Value of each element can be initialized to None:
"""


def array(row, col):
    return [[None for j in range(col)]
            for i in range(row)]

a = array(2, 3)
print a
a[0][0] = 5
print a

"""
Output:
[[None, None, None], [None, None, None]]
[[5, None, None], [None, None, None]]
"""

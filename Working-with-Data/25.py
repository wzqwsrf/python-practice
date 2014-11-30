# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月30日23:35:28

"""
Problem 25: Python provides a built-in function map
that applies a function to each element of a list.
Provide an implementation for map using list comprehensions.
"""


def square(x):
    return x * x


def map(square, list1):
    return [square(x) for x in list1]


print map(square, range(5))

"""
Output:
[0, 1, 4, 9, 16]
"""

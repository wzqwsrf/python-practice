# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:07:59

"""
Problem 26: Python provides a built-in function filter(f, a)
that returns items of the list a for which f(item) returns true.
Provide an implementation for filter using list comprehensions.
"""


def even(x):
    return x % 2 == 0


def filter(f, a):
    e_list = []
    for x in a:
        if f(x):
            e_list.append(x)
    return e_list

print filter(even, range(10))


"""
Output:
[0, 2, 4, 6, 8]
"""

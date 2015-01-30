# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日15:44:31

"""
Problem 11: Write a function vectorize which takes a function f and return a new function,
which takes a list as argument and calls f for every element and returns the result as a list.
"""

def vectorize(f):
    """
    >>> f = vectorize(square)
    >>> f([1, 2, 3])
    [1, 4, 9]
    >>> g = vectorize(len)
    >>> g(["hello", "world"])
    [5, 5]
    >>> g([[1, 2], [2, 3, 4]])
    [2, 3]
    """
    def g(data):
        if isinstance(data, list):
            return [f(x) for x in data]
        if isinstance(data, str):
            return f(data)
    return g

def square(x):
    return x * x

f = vectorize(square)
print f([1, 2, 3])
g = vectorize(len)
print g(["hello", "world"])
print g([[1, 2], [2, 3, 4]])


"""
Output
[1, 4, 9]
[5, 5]
[2, 3]
"""
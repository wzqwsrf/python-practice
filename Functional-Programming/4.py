# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月28日13:06:13

"""
Problem 4: Write a function treemap to map a function over nested list.
"""


def treemap(f, a, b=None, y=None):
    """
        >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
        [1, 4, [9, 16, [25]]]
    """
    a_len = len(a)
    for i in a:
        if isinstance(a[i], list):
            treemap(f, a[i], i)
        else:
            a[y] = f(a[i])
    return a


res = treemap(lambda x: x * x, [1, 2, [3, 4, [5]]])
print res

"""
Output
{'a': 1, 'c': 4, 'b': {'y': 3, 'x': 2}}
"""
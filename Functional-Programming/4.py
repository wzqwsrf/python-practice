# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月28日13:06:13

"""
Problem 4: Write a function treemap to map a function over nested list.
"""


def treemap(f, a, y=None):
    """
        >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
        [1, 4, [9, 16, [25]]]
    """
    if y is None:
        b = a
    else:
        b = a[y]
    b_len = len(b)
    for i in range(b_len):
        if isinstance(b[i], list):
            treemap(f, b, i)
        else:
            b[i] = f(b[i])
    return a


res = treemap(lambda x: x * x, [1, 2, [3, 4, [5]]])
print res

"""
Output
[1, 4, [9, 16, [25]]]
"""

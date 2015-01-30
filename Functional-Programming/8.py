# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日11:12:56

"""
Problem 8: Write a function count_change to count the number of ways to change any given amount.
Available coins are also passed as argument to the function.
"""


def count_change(count, data, base=0, num=0):
    """
    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292
    """
    if count == 0:
        return num+1
    count_change[n,j-1] + f[n-v[j],j]


print count_change(10, [1, 5])
"""
Output
类似这样的格式
foo/
|-- a.txt
|-- b.txt
|-- bar/
|   |-- p.txt
|   `-- q.txt
`-- c.txt
"""


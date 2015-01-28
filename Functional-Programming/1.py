# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月27日13:13:29

"""
Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.
"""


def product(x, y):
    if abs(x) > abs(y):
        product(y, x)
    res = 0
    for i in range(abs(x)):
        res += abs(y)
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return res;
    return -res;


print product(2, 3)
print product(55, -32)
print product(100, -1)

"""
Output
6
-1760
-100
"""
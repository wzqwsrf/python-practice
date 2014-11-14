# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 11: What will be the output of the following program?
"""

x = 2
def f(a):
    x = a * a
    return x

y = f(3)
print x, y

"""
Output: 2 9
"""

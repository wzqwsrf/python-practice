# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 1: What will be the output of the following program?
"""

x = [0, 1, [2]]
x[2][0] = 3
print x
x[2].append(4)
print x
x[2] = 2
print x

"""
Output:
[0, 1, [3]]
[0, 1, [3, 4]]
[0, 1, 2]
"""

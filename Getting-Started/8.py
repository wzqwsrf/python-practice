# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 8: What will be the output of the following program?
"""

x = 1
def f():
    return x
print x
print f()

"""
Output:
1
1
内部函数访问全局变量
"""

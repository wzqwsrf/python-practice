# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 6: What will be the output of the following program.
"""
a, b = 2, 3
c, b = a, c + 1
print a, b, c

"""
Output: NameError: name 'c' is not defined
"""

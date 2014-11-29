# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 7: Python has built-in functions min and max to compute minimum
and maximum of a given list. Provide an implementation for these functions.
What happens when you call your min and max functions with a list of strings?
"""

def min(input_list):
    r_min = input_list[0]
    input_list = input_list[1:]
    for x in input_list:
        if x < r_min:
            r_min = x
    return r_min

def max(input_list):
    r_max = input_list[0]
    input_list = input_list[1:]
    for x in input_list:
        if x > r_max:
            r_max = x
    return r_max

print min([-1, 2, 4, -3, 0])
print min(["aa", "b", "cc"])

print max([-1, 2, 4, -3, 0])
print max(["aa", "b", "cc"])

"""
Output:
-3
"aa"
4
"cc"
"""




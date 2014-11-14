# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 11: Write a function dups to find all duplicates in the list.
"""

def unique(nums):
    n_dict = {}
    for x in nums:
        if n_dict.has_key(x):
            n_dict[x] = n_dict.get(x) + 1
        else:
            n_dict[x] = 1
    r_nums = []
    for x in n_dict.keys():
        if n_dict.get(x) != 1:
            r_nums.append(x)
    return r_nums

print unique([1, 2, 1, 3, 2, 5])

"""
Output:
[1, 2]
"""



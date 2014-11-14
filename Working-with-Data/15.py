# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 15: Reimplement the unique function implemented in the earlier examples using sets.
"""

def unique(nums):
    return set(nums)

print unique([1, 2, 1, 3, 2, 5])

"""
Output:
[1, 2, 3, 5]
"""


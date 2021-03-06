# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 4: Implement a function product, to compute product of a list of numbers.
"""

def product(nums):
    result = 1
    for x in nums:
        result *= x
    return result

print product([1, 2, 3])

"""
Output:
6
"""

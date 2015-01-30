# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 2: Python has a built-in function sum to find sum of all elements of a list.
Provide an implementation for sum.
"""

def sum(nums):
    all_sum = nums[0]
    nums = nums[1:]
    for x in nums:
        all_sum += x
    return all_sum

print sum([1, 2, 3])
print sum([1, 2, 3, 4, 0])

"""
Output:
6
10
"""

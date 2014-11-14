# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 12: Write a function group(list, size) that take a list
and splits into smaller lists of given size.
"""

def group(nums, size):
    r_nums = []
    n_len = len(nums)
    for x in range(0, n_len, size):
        i_nums = nums[x:x + size]
        r_nums.append(i_nums)
    return r_nums

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

"""
Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]
"""

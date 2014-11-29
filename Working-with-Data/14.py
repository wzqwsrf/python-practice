# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 14: Improve the unique function written in previous problems to
take an optional key function as argument and use the return value
of the key function to check for uniqueness.
"""

def unique(nums, key):
    nums.sort(key = key)
    print nums
    n_len = len(nums)
    r_nums = []
    for i in range(n_len):
        if key(nums[i]) in r_nums:
            continue
        r_nums.append(key(nums[i]))
    return r_nums

print unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())

"""
Output:
["java", "python"]
"""

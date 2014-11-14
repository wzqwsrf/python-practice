# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 6: Write a function reverse to reverse a list.
Can you do this without using list slicing?
"""

def reverse(nums):
    rnums = []
    n_len = len(nums) - 1
    for i in range(n_len, -1, -1):
        rnums.append(nums[i])
    return rnums

print reverse([1, 2, 3, 4])
print reverse(reverse([1, 2, 3, 4]))


"""
Output:
[4, 3, 2, 1]
[1, 2, 3, 4]
"""

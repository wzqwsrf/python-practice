# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 13: Write a function lensort to sort a list of strings based on length.
"""

def lensort(nums):
    nums.sort(key=lambda x : len(x))
    return nums

print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])

"""
Output:
['c', 'perl', 'java', 'ruby', 'python', 'haskell']
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 3: What happens when the above sum function is called with a list of strings?
Can you make your sum function work for a list of strings as well.

"""
def sum(nums):
    all_sum = nums[0]
    nums = nums[1:]
    for x in nums:
        all_sum += x
    return all_sum

print sum(["hello", "world"])
print sum(["aa", "bb", "cc"])

"""
Output:
"helloworld"
"aabbcc"
"""

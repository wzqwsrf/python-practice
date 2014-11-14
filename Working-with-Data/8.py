# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
Write a function cumulative_sum to compute cumulative sum of a list.
Does your implementation work for a list of strings?
"""

def cumulative_sum(input_list):
    r_list = []
    n_len = len(input_list)
    r_list.append(input_list[0])
    for i in range(1, n_len):
        num = r_list[i - 1] + input_list[i]
        r_list.append(num)
    return r_list

print cumulative_sum([1, 2, 3, 4])
print cumulative_sum([4, 3, 2, 1])
print cumulative_sum(["a", "b", "c", "d"])
print cumulative_sum(["d", "c", "b", "a"])

"""
Output:
[1, 3, 6, 10]
[4, 7, 9, 10]
["a", "ab", "abc", "abcd"]
["d", "dc", "dcb", "dcba"]
"""

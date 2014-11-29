# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 9: Write a function cumulative_product to compute
cumulative product of a list of numbers.
"""

def cumulative_product(input_list):
    r_list = []
    n_len = len(input_list)
    r_list.append(input_list[0])
    for i in range(1, n_len):
        num = r_list[i - 1] * input_list[i]
        r_list.append(num)
    return r_list

print cumulative_product([1, 2, 3, 4])
print cumulative_product([4, 3, 2, 1])

"""
Output:
[1, 2, 6, 24]
[4, 12, 24, 24]
"""

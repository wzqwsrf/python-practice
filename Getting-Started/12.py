# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 12: Write a function count_digits to find number of digits in the given number.
"""

def count_digits(num):
    num = str(num)
    return len(num)

def count_digits1(num):
    n_len = 0
    while num != 0:
        num = num / 10
        n_len += 1
    return n_len

print count_digits(5)
print count_digits(12345)

print count_digits1(5)
print count_digits1(12345)


"""
Output:
1
5
字符串＋除法
"""


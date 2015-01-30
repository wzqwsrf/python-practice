# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日11:12:56

"""
Problem 8: Write a function count_change to count the number of ways to change any given amount.
Available coins are also passed as argument to the function.
"""


def count_change(count, data):
    """
    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292
    """
    dp = []
    x = 0
    while x <= count:
        dp.append(0)
        x += 1
    dp[0] = 1
    for i in range(len(data)):
        for j in range(data[i], count + 1):
            dp[j] += dp[j - data[i]]
    return dp[count]


print count_change(10, [1, 5])

"""
Output
3
"""


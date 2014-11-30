# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月30日23:30:17

"""
Problem 24: Provide an implementation for zip function using list comprehensions.
"""


def zip(list1, list2):
    return [(list1[i], list2[j]) for i in range(len(list1))
            for j in range(len(list2)) if i == j]


print zip([1, 2, 3], ["a", "b", "c"])

"""
Output:
[(1, "a"), (2, "b"), (3, "c")]
"""

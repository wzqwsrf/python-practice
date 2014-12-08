# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月08日14:32:53

"""
Problem 37: Write a function valuesort to sort values of a dictionary based on the key.
"""


def valuesort(dic):
    r_list = []
    for key, value in sorted(dic.items(), key=lambda x: x[0], reverse=False):
        r_list.append(value)
    return r_list


print valuesort({'x': 1, 'y': 2, 'a': 3})


"""
Output:
[3, 1, 2]
"""

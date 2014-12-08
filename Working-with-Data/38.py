# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月08日14:32:53

"""
Problem 38: Write a function invertdict to interchange keys and values in a dictionary.
For simplicity, assume that all values are unique.
"""


def invertdict(dic):
    r_dic = {}
    for key, value in sorted(dic.items(), key=lambda x: x[0], reverse=False):
        r_dic[value] = key
    return r_dic


print invertdict({'x': 1, 'y': 2, 'a': 3})


"""
Output:
{1: 'x', 2: 'y', 3: 'a'}
"""

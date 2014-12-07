# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:16:05

"""
Problem 28: Write a function enumerate that takes a list and
returns a list of tuples containing (index,item) for each item in the list.
"""


def enumerate(in_list):
    d_len = len(in_list)
    return [(i, in_list[i]) for i in range(d_len)]


print enumerate(["a", "b", "c"])

for index, value in enumerate(["a", "b", "c"]):
    print index, value


"""
Output:
[(0, 'a'), (1, 'b'), (2, 'c')]
"""

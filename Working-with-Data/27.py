# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:12:47

"""
Problem 27: Write a function triplets that takes a number n as argument
and returns a list of triplets such that sum of first two elements of
the triplet equals the third element using numbers below n.
Please note that (a, b, c) and (b, a, c) represent same triplet.
"""


def triplets(n):
    return [(x, y, z)
            for x in range(1, n)
            for y in range(x, n)
            for z in range(y, n)
            if x + y == z]

print triplets(5)


"""
Output:
[(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
"""

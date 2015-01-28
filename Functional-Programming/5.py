# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月28日14:15:02

"""
Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.
"""

import copy

def tree_reverse(a, y=None):
    """
        >>> tree_reverse([[1, 2], [3, [4, 5]], 6])
        [6, [[5, 4], 3], [2, 1]]
    """
    if y is None:
        b = a
    else:
        b = a[y]
    b_len = len(b)
    c = copy.deepcopy(b)
    for i in range(b_len - 1, -1, -1):
        if isinstance(c[i], list):
            tree_reverse(c, i)
        else:
            b[b_len-1-i] = c[i]
    return a


res = tree_reverse([[1, 2], [3, [4, 5]], 6])
print res

"""
Output
[1, 4, [9, 16, [25]]]
"""

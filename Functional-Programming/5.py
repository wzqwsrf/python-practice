# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月29日21:43:58

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
    if not isinstance(b, list):
        return b
    b_len = len(b)
    if b_len % 2 == 0:
        m_len = b_len / 2
    else:
        m_len = b_len / 2 + 1
    c = copy.deepcopy(b)
    for i in range(m_len):
        if isinstance(c[i], list):
            first = tree_reverse(b, i)
        else:
            first = c[i]
        if b_len - 1 - i == i:
            b[i] = first
            continue
        if isinstance(c[b_len - 1 - i], list):
            end = tree_reverse(b, b_len - 1 - i)
        else:
            end = c[b_len - 1 - i]
        b[i] = end
        b[b_len - 1 - i] = first
    return b


res = tree_reverse([[1, 2], [3, [4, 5]], 6])
print res

"""
Output
[6, [[5, 4], 3], [2, 1]]
"""

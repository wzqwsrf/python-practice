# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月27日13:21:17

"""
Problem 2: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
"""


def flatten_dict(b, a=None, result=None):
    """Flattens a nested dict.

        >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
        {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if result is None:
        result = {}
    for k, v in b.items():
        if isinstance(v, dict):
            flatten_dict(v, k, result)
        else:
            if a is None:
                result[k] = v
            else:
                result[a + '.' + k] = v
    return result


res = flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
print res

"""
Output
{'a': 1, 'c': 4, 'b.x': 2, 'b.y': 3}
"""
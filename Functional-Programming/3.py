# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月28日12:45:29

"""
Problem 3: Write a function unflatten_dict to do reverse of flatten_dict.
"""


def unflatten_dict(b, a=None, result=None):
    """
        >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
        {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
    """
    if result is None:
        result = {}
    for k, v in b.items():
        if '.' in k:
            key_msg = k.split('.')
            out_key = k[0]
            in_key = k[2]
            res = {} if out_key not in result else result[out_key]
            res[in_key] = v
            result[out_key] = res
        else:
            result[k] = v

    return result


res = unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
print res

"""
Output
{'a': 1, 'c': 4, 'b': {'y': 3, 'x': 2}}
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日10:29:10

"""
Problem 6: Complete the above implementation of json_encode by handling the case of dictionaries.
"""


def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        return "{" + ",".join((json_encode(k) + ":" + json_encode(v) for k, v in data.items())) + "}"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))


def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s


# print json_encode(True)
# print json_encode('abc')
# print json_encode(0.5)
# print json_encode(1)
# print json_encode([1, 2, 3])
# print json_encode([1, [2, 3], 4])
# print type(json_encode([1, [2, 3], 4]))
print json_encode({'a': '1', 'b': 2})

"""
Output
{"a":"1","b":2}
"""

import os
import sys


def dirtree():
    dir_name = sys.argv[1]
    list_dir(dir_name)


def list_dir(path):
    files = os.listdir(path)
    files.sort()
    f_len = len(files)
    for i in range(f_len):
        f = files[i]
        f_path = os.path.join(path, f)
        level = get_level(f_path)
        if i == f_len - 1:
            s_path = get_last_path(level)
        else:
            s_path = get_path(level)
        print s_path + f
        if os.path.isdir(f_path):
            list_dir(f_path)


def get_level(path):
    level = 0
    for x in path:
        if x == os.path.sep:
            level += 1
    return level


def get_path(level):
    if level == 0:
        path = '|'
    elif level == 1:
        path = '|-- '
    else:
        path = '|   ' * (level - 1) + '|-- '
    return path


def get_last_path(level):
    if level == 0:
        path = '\\'
    elif level == 1:
        path = '\-- '
    else:
        path = '|   ' * (level - 1) + '\-- '
    return path


dirtree()
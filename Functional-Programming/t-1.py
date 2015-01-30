# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日10:29:10

"""
transfer data to json
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
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))


def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s


print json_encode(True)
print json_encode('abc')
print json_encode(0.5)
print json_encode(1)
print json_encode([1, 2, 3])
print json_encode([1, [2, 3], 4])
print type(json_encode([1, [2, 3], 4]))

"""
Output
true
"abc"
0.5
1
[1, 2, 3]
[1, [2, 3], 4]
<type 'str'>
"""
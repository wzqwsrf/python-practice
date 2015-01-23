# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月23日11:47:01

"""
Iterators Test1
"""

if __name__ == '__main__':
    for i in [1, 2, 3, 4]:
        print i,
    print '\n',
    for c in "python":
        print c
    print '\n'
    for k in {"x": 1, "y": 2}:
        print k
    for line in open("a.txt"):
        print line,
    print ",".join(["a", "b", "c"])
    print ",".join({"x": 1, "y": 2})
    print list(xrange(5))
    print list("python")
    print list({"x": 1, "y": 2})

"""

1 2 3 4
p
y
t
h
o
n


y
x
Test file output a,b,c
y,x
[0, 1, 2, 3, 4]
['p', 'y', 't', 'h', 'o', 'n']
['y', 'x']
"""
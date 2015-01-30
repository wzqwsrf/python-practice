# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日14:54:03

"""
trace
"""


def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def trace(f):
    def g(x):
        print f.__name__, x
        value = f(x)
        print 'return', repr(value)
        return value

    return g


fib = trace(fib)
print fib(3)

"""
Output
fib 3
fib 2
fib 1
return 1
fib 0
return 1
return 2
fib 1
return 1
return 3
3
"""
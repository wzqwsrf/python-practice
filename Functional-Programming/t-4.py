# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日14:55:13

"""
trace
"""

def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def trace(f):
    f.indent = 0

    def g(x):
        print '|  ' * f.indent + '|--', f.__name__, x
        f.indent += 1
        value = f(x)
        print '|  ' * f.indent + '|--', 'return', repr(value)
        f.indent -= 1
        return value

    return g


def memoize(f):
    cache = {}

    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return g


fib = trace(fib)
fib = memoize(fib)
print fib(4)

"""
Output
|-- fib 4
|  |-- fib 3
|  |  |-- fib 2
|  |  |  |-- fib 1
|  |  |  |  |-- return 1
|  |  |  |-- fib 0
|  |  |  |  |-- return 1
|  |  |  |-- return 2
|  |  |-- return 3
|  |-- return 5
5
"""
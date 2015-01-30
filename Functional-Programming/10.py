# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日14:55:13

"""
trace
"""

import time


def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def profile(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return g

start = time.time()
print start
fib = profile(fib)
print fib(20)
end = time.time()
print end

"""
Output
时间
10946
时间
"""
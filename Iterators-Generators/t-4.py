# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月23日11:54:04

"""
Iterators Test4
"""


class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)


class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()



if __name__ == '__main__':

    z = zrange(5)
    print list(z)
    print list(z)

"""
Output
0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]

"""

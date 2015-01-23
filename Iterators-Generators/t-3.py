# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月23日11:54:04

"""
Iterators Test3
"""


class yrange:
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

    y = yrange(3)
    print y.next()
    print y.next()
    print y.next()
    # print y.next()
    print list(yrange(5))
    print sum(yrange(5))
    y = yrange(5)
    print list(y)
    print list(y)

"""
Output
0
1
2
[0, 1, 2, 3, 4]
10
[0, 1, 2, 3, 4]
[]

"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月26日17:43:34

"""
Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::
"""


class reverse_iter:
    def __init__(self, n_list):
        self.n = len(n_list)
        self.i = 0
        self.n_list = n_list[::-1]

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return self.n_list[i]
        else:
            raise StopIteration()

it = reverse_iter([1, 2, 3, 4])
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()


"""
Output
4
3
2
1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""